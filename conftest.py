import pytest

from tests.pages.LoginPage import LoginPage

SUPPORTED_BROWSERS_LIST = [
    "chrome",
    "firefox",
    "safari",
    "headless-chrome",
    "headless-firefox",
    "headless-safari",
]

def pytest_addoption(parser):
    parser.addoption(
        "--use-browser",
        action="store",
        default="headless-firefox",
        help="Define the browser to be executed. Current supported versions: " + ", ".join(SUPPORTED_BROWSERS_LIST)
    )


@pytest.fixture(scope="function")
def start_by_login_page(request):
    """Fixture that starts the WebDriver by accessing the Login page"""
    selected_browser = request.config.getoption("--use-browser")
    login_page = LoginPage(driver=selected_browser)
    yield login_page
    
    login_page.close_driver()

