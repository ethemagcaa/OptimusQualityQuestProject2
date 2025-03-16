from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class SearchResultsPage(BasePage):
    PRODUCT_TITLES = (By.XPATH, "//h2[contains(., 'Samsung')]")
    SECOND_PAGE_BUTTON = (By.XPATH, "//a[contains(@class, 's-pagination-button') and contains(text(), '2')]")
    THIRD_PRODUCT = (By.XPATH, "(//h2[contains(@class, 'a-size-base-plus')])[3]")

    def verify_results(self):
        """Confirms that 'Samsung' products are listed on the page."""
        elements = self.driver.find_elements(*self.PRODUCT_TITLES)
        return len(
            elements) > 0  # Returns True if the length of the list elements is greater than 0, that is, if at least one element was found.

    def go_to_second_page(self):
        """It moves to page 2 of the search results and waits."""
        self.click_element(*self.SECOND_PAGE_BUTTON)
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located(self.THIRD_PRODUCT)
        )  # Wait for page 2 to load

    def is_on_second_page(self):
        """Verifies if you are currently on page 2."""
        return "ref=sr_pg_2" in self.driver.current_url  # Check if ref=sr_pg_2 is in the URL

    def go_to_third_product(self):
        """3. Waits before clicking on the product and then clicks."""
        WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(self.THIRD_PRODUCT)
        )  # 3. Wait for the product to be clickable
        self.click_element(*self.THIRD_PRODUCT)
