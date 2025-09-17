import unittest

import pytest
from pages.login_page import LoginPage
from utils.driver_setup import get_driver


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = get_driver()
        self.login_page = LoginPage(self.driver)
        self.login_page.open_page()

    def test_valid_login(self):
        self.login_page.login("standard_user", "secret_sauce")
        self.assertIn("inventory.html", self.driver.current_url)

    def test_invalid_username(self):
        self.login_page.login("wrong_user", "secret_sauce")
        error = self.login_page.get_error_message()
        self.assertIn("Username and password do not match", error)

    def test_invalid_password(self):
        self.login_page.login("standard_user", "wrong_pass")
        error = self.login_page.get_error_message()
        self.assertIn("Username and password do not match", error)

    def test_empty_fields(self):
        self.login_page.login("", "")
        error = self.login_page.get_error_message()
        self.assertIn("Username is required", error)

    def tearDown(self):
        self.driver.quit()

# PyTest hook for screenshots on failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = getattr(item.instance, "driver", None)
        if driver:
            screenshot_path = f"screenshots/{item.name}.png"
            driver.save_screenshot(screenshot_path)
            if "pytest_html" in item.config.pluginmanager.list_name_plugin():
                extra = getattr(rep, "extra", [])
                extra.append(item.config.pluginmanager.getplugin("html").extras.image(screenshot_path))
                rep.extra = extra

if __name__ == "__main__":
    unittest.main()
