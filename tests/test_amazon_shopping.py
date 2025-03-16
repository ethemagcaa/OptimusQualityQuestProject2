from tests.base_test import BaseTest
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


class TestAmazonShopping(BaseTest):
    def test_amazon_shopping(self):
        """Amazon tests the entire shopping process from start to finish."""

        # 1️⃣ Home page verification
        home_page = HomePage(self.driver)
        assert home_page.is_homepage_displayed(), "Home page not loaded!"

        # 2️⃣ Product search
        home_page.search_product("samsung")

        # 3️⃣ Verify search results
        search_results_page = SearchResultsPage(self.driver)
        assert search_results_page.verify_results(), "Product results are not visible!"

        # 4️⃣ Go to page 2
        search_results_page.go_to_second_page()

        # ✅ Verify you are on page 2
        assert search_results_page.is_on_second_page(), "Failed to move to page 2!"

        # 5️⃣ 3. Go to the product and enter the detail page
        search_results_page.go_to_third_product()

        # ✅ Check if we are on the product detail page
        product_page = ProductPage(self.driver)
        assert product_page.is_product_page_displayed(), "Failed to navigate to product page!"

        # 6️⃣ Add product to cart
        product_page.add_product_to_cart()

        # 7️⃣ Go to Cart
        product_page.go_to_cart()

        # ✅ Verify that the product has been added to the cart
        assert product_page.verify_product_added(), "The product was not added to the cart!"

        # 8️⃣✅ Go to cart and verify product
        cart_page = CartPage(self.driver)
        assert cart_page.verify_product_in_cart(), "No products found in the cart!"

        # 9️⃣ Delete product from cart
        cart_page.delete_product()

        # ✅ Verify that the cart is empty
        cart_page.verify_cart_is_empty()
        assert cart_page.verify_cart_is_empty(), "Cart is still full, item could not be deleted"

        # 🔟 Return to home page
        home_page.return_to_homepage()

        # ✅ Verify that you are on the home page
        assert home_page.is_homepage_displayed(), "Could not return to home page!"
