from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find(self, *locator):
        """Finds and returns the element with the specified locator."""
        return self.driver.find_element(*locator)

    def click_element(self, *locator):
        """Finds and clicks the element with the specified locator."""
        self.driver.find_element(*locator).click()

    def hover_element(self, *locator):
        """Performs a hover operation on the element with the specified locator."""
        element = self.find(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def get_current_url(self):
        """Returns the URL of the current page."""
        return self.driver.current_url

    def wait_element(self, method, message=""):
        """It waits for the element according to the specified method and returns it when it becomes clickable."""
        return self.wait.until(ec.element_to_be_clickable(method), message)

    def get_text(self, locator):
        """Returns the text inside the element with the specified locator."""
        return self.wait_element(locator).text
