from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    SEARCH_BOX = (By.XPATH, "//input[@id='twotabsearchtextbox']")
    SEARCH_BUTTON = (By.ID, "nav-search-submit-button")
    AMAZON_LOGO = (By.ID, "nav-logo-sprites")

    def is_homepage_displayed(self):
        """Confirms that the home page has opened."""
        return "amazon.com.tr" in self.get_current_url()

    def search_product(self, product_name):
        """Types the product name in the search box and starts the search."""
        self.find(*self.SEARCH_BOX).send_keys(product_name)
        self.click_element(*self.SEARCH_BUTTON)

    def return_to_homepage(self):
        """Clicking on the Amazon logo returns to the home page."""
        self.click_element(*self.AMAZON_LOGO)
