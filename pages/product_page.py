from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "input#add-to-cart-button")
    CART_COUNT = (By.ID, "nav-cart-count")
    GO_TO_CART_BUTTON = (By.XPATH, "//a[@data-csa-c-content-id='sw-gtc_CONTENT']")

    def is_product_page_displayed(self):
        """Checks if it is on the product detail page."""
        return "dp" in self.get_current_url()

    def add_product_to_cart(self):
        """Adds the product to the cart."""
        self.wait_element(self.ADD_TO_CART_BUTTON, "The add to cart button is not visible.")
        self.click_element(*self.ADD_TO_CART_BUTTON)

    def go_to_cart(self):
        """Clicks the goto cart button."""
        self.wait_element(self.GO_TO_CART_BUTTON, "Go to cart button is not visible.")
        self.click_element(*self.GO_TO_CART_BUTTON)

    def verify_product_added(self):
        """Checks the number of items in the cart."""
        return self.get_text(self.CART_COUNT) != "0"
