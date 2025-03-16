import time
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class BaseTest(unittest.TestCase):

    def setUp(self):
        """Launches the browser and navigates to Amazon."""
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.amazon.com.tr/")
        self.accept_cookies()

    def tearDown(self):
        """Closes the browser after the test."""
        self.driver.quit()

    def accept_cookies(self):
        """Turn off Amazon cookie notification."""
        try:
            cookie_accept_button = self.driver.find_element(By.ID, "sp-cc-accept")
            cookie_accept_button.click()
            time.sleep(2)
        except NoSuchElementException:
            pass  # Don't give an error if there is no cookie button
