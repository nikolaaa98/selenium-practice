// =============================================================================
//  Selenium Tests – Jenkins Declarative Pipeline
//  Equivalent of .github/workflows/python-app.yml, but for Jenkins.
//
//  Requirements on the Jenkins agent:
//    - Python 3.10+ (`python3` on Linux/macOS, `python` on Windows)
//    - Chrome / Firefox / Edge installed (depending on which browsers you pick)
//    - Jenkins plugins: Pipeline, HTML Publisher, JUnit, Timestamper
//      (optional: AnsiColor, Workspace Cleanup)
// =============================================================================

pipeline {
    // If you have a dedicated agent (e.g. label `selenium` or `linux`), replace with:
    //   agent { label 'selenium' }
    agent any

    parameters {
        booleanParam(name: 'CHROME',   defaultValue: true,  description: 'Run tests on Chrome')
        booleanParam(name: 'FIREFOX',  defaultValue: false, description: 'Run tests on Firefox')
        booleanParam(name: 'EDGE',     defaultValue: false, description: 'Run tests on Microsoft Edge')
        booleanParam(name: 'HEADLESS', defaultValue: true,  description: 'Run browsers in headless mode')
    }
    string(
        name: 'TAGS',
        defaultValue: '',
        description: 'Pytest marker expression (e.g. "smoke", "regression and not slow", "smoke or sanity"). Leave empty to run all tests.'
    )

    options {
        timestamps()
        buildDiscarder(logRotator(numToKeepStr: '20', artifactNumToKeepStr: '10'))
        timeout(time: 30, unit: 'MINUTES')
        disableConcurrentBuilds()
        // ansiColor('xterm')   // uncomment if the AnsiColor plugin is installed
    }

    environment {
        // ----- Configuration consumed by config/config.py -----
        HEADLESS = "${params.HEADLESS}"

        // ----- PUBLIC demo credentials for the-internet.herokuapp.com -----
        //  (safe to commit; for real secrets use Jenkins Credentials with
        //   `withCredentials` in the appropriate stage – see note at the bottom)
        VALID_USERNAME   = 'tomsmith'
        VALID_PASSWORD   = 'SuperSecretPassword!'
        INVALID_USERNAME = 'wrong_user'
        INVALID_PASSWORD = 'wrong_password'
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Set up Python venv & install dependencies') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                            set -e
                            python3 -m venv .venv
                            . .venv/bin/activate
                            python -m pip install --upgrade pip
                            pip install -r requirements.txt
                            pip install pytest-metadata   # required for JUnit XML metadata
                        '''
                    } else {
                        bat '''
                            if not exist .venv python -m venv .venv
                            call .venv\\Scripts\\activate.bat
                            python -m pip install --upgrade pip
                            pip install -r requirements.txt
                            pip install pytest-metadata
                        '''
                    }
                }
            }
        }

        stage('Determine browser list') {
            steps {
                script {
                    def browsers = []
                    if (params.CHROME)  { browsers << 'chrome'  }
                    if (params.FIREFOX) { browsers << 'firefox' }
                    if (params.EDGE)    { browsers << 'edge'    }
                    if (browsers.isEmpty()) {
                        echo 'No browser selected — falling back to Chrome only.'
                        browsers = ['chrome']
                    }
                    env.SELECTED_BROWSERS = browsers.join(',')

                    echo "Browsers to test : ${env.SELECTED_BROWSERS}"
                    echo "Headless mode   : ${params.HEADLESS}"
                }
            }
        }

        stage('Run tests') {
            steps {
                script {
                    def browsers = env.SELECTED_BROWSERS.split(',')
                    def parallelStages = [:]

                    browsers.each { browser ->
                        parallelStages["Tests · ${browser}"] = {
                            runTests(browser)
                        }
                    }

                    parallel parallelStages
                }
            }
        }
    }

    post {
        always {
            // Native Jenkins test trend graph (Test Result trend)
            junit testResults: 'reports/junit-*.xml', allowEmptyResults: true

            // HTML report link on the build sidebar ("Selenium HTML Report")
            publishHTML(target: [
                allowMissing:          true,
                alwaysLinkToLastBuild: true,
                keepAll:               true,
                reportDir:             'reports',
                reportFiles:           '*.html',
                reportName:            'Selenium HTML Report'
            ])

            // Archive reports/, screenshots/ and logs/ as build artifacts
            archiveArtifacts artifacts: 'reports/**, screenshots/**, logs/**',
                             allowEmptyArchive: true,
                             fingerprint: true
        }

        success  { echo 'All tests passed.' }
        failure  { echo 'Build failed — check the artifacts and the HTML report.' }
        unstable { echo 'Some tests failed — check the JUnit results.' }
    }
}


// -----------------------------------------------------------------------------
//  Helper: runs pytest for a single browser (invoked in parallel).
// -----------------------------------------------------------------------------
def runTests(String browser) {
    withEnv(["BROWSER=${browser}"]) {
        if (isUnix()) {
            sh """
                set -e
                . .venv/bin/activate
                pytest \\
                    --html=reports/report-${browser}.html \\
                    --self-contained-html \\
                    --junitxml=reports/junit-${browser}.xml
            """
        } else {
            bat """
                call .venv\\Scripts\\activate.bat
                pytest ^
                    --html=reports/report-${browser}.html ^
                    --self-contained-html ^
                    --junitxml=reports/junit-${browser}.xml
            """
        }
    }
}


// -----------------------------------------------------------------------------
//  OPTIONAL: instead of hard-coding credentials in `environment`, use the
//  Jenkins Credentials Store and wrap the `stage('Run tests')` block with:
//
//  withCredentials([usernamePassword(
//      credentialsId: 'herokuapp-valid-creds',
//      usernameVariable: 'VALID_USERNAME',
//      passwordVariable: 'VALID_PASSWORD'
//  )]) {
//      parallel parallelStages
//  }
// -----------------------------------------------------------------------------
