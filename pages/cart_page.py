from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CartPage(BasePage):
    CART_PRODUCT_TITLE = (By.CSS_SELECTOR, "span.sc-product-title")
    DELETE_BUTTON = (By.CSS_SELECTOR, "input[aria-label*='Sil']")
    CART_COUNT = (By.ID, "nav-cart-count")

    def verify_product_in_cart(self):
        """Checks whether the correct product is in the cart."""
        return self.find(*self.CART_PRODUCT_TITLE).is_displayed()

    def delete_product(self):
        """Deletes the product from the cart."""
        self.click_element(*self.DELETE_BUTTON)

    def verify_cart_is_empty(self):
        """Verifies that the cart is empty."""
        return self.get_text(self.CART_COUNT) == "0"
