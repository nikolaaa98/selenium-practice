# selenium-practice
This is a repo for practice selenium 

# Install dependecny 

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
``

# Run using jenkins

```bash
docker run -d --name jenkins \
  -p 8080:8080 -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  -v "$HOME/Desktop/selenium-practice:/workspace/selenium-practice" \
  jenkins/jenkins:lts
``