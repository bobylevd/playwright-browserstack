import pytest

from consts import BROWSERSTACK_USERNAME, BROWSERSTACK_ACCESS_KEY


@pytest.fixture
def caps():
    bs_caps = dict()

    bs_caps["browser"] = "chrome"
    bs_caps["browser_version"] = "latest"
    bs_caps["headless"] = "false"

    bs_caps["os"] = "Windows"
    bs_caps["os_version"] = "10"

    bs_caps["name"] = "Parallel Test1"
    bs_caps["build"] = "browserstack-build-1"

    bs_caps["browserstack.username"] = BROWSERSTACK_USERNAME
    bs_caps["browserstack.accessKey"] = BROWSERSTACK_ACCESS_KEY
    bs_caps["browserstack.console"] = "errors"
    bs_caps["browserstack.networkLogs"] = "true"
    bs_caps["browserstack.playwrightVersion"] = "1.latest"

    bs_caps["client.playwrightVersion"] = "1.latest"
    return bs_caps
