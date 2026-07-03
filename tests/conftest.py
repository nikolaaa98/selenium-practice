import os
from datetime import datetime

import pytest

from config.config import Config
from utils.driver_factory import get_driver
from utils.logger import get_logger
from utils.screenshot import take_screenshot

logger = get_logger("conftest")


def pytest_configure(config):
    """
    Configure the HTML report to have a timestamp in its name and to be placed in the reports/ folder.
    """
    os.makedirs(Config.REPORTS_DIR, exist_ok=True)

    # Set the report path only if the user did not pass --html manually
    if not config.option.htmlpath:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_path = os.path.join(Config.REPORTS_DIR, f"report_{timestamp}.html")
        config.option.htmlpath = report_path
        config.option.self_contained_html = True

    logger.info("=" * 70)
    logger.info("STARTING TEST SESSION")
    logger.info(f"HTML report: {config.option.htmlpath}")
    logger.info("=" * 70)


def pytest_sessionfinish(session, exitstatus):
    """Log the end of the test session."""
    logger.info("=" * 70)
    logger.info(f"TEST SESSION FINISHED (exit status: {exitstatus})")
    logger.info("=" * 70)


@pytest.fixture()
def driver(request):
    """
    Create a new WebDriver instance for each test.
    If the test fails, a screenshot is taken and attached to the HTML report.
    """
    test_name = request.node.name
    logger.info(f"--- TEST START: {test_name} ---")

    drv = get_driver()
    # Store the driver on the node so the hook can use it on test failure
    request.node.driver = drv

    yield drv

    logger.info(f"--- TEST END: {test_name} ---")
    drv.quit()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    """
    Hook called after each test phase (setup, call, teardown).
    If the test fails in the 'call' phase, take a screenshot and attach it to the HTML report.
    """
    outcome = yield
    report = outcome.get_result()

    extras = getattr(report, "extras", [])

    if report.when == "call":
        if report.failed:
            logger.error(f"TEST FAILED: {item.name}")
            drv = getattr(item, "driver", None)
            if drv is not None:
                screenshot_path = take_screenshot(drv, item.name)
                if screenshot_path:
                    # Attach the screenshot to the HTML report (pytest-html v4+)
                    try:
                        from pytest_html import extras as html_extras
                        extras.append(html_extras.image(screenshot_path))
                        extras.append(html_extras.url(f"file://{os.path.abspath(screenshot_path)}"))
                    except ImportError:
                        logger.warning("pytest-html is not installed, screenshot not attached to report.")
        elif report.passed:
            logger.info(f"TEST PASSED: {item.name}")

    report.extras = extras
