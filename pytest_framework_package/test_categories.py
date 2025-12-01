import pytest
import time
from POM.categories_page import Categories_class

# List of categories to test
categories_list = ["phones", "laptops", "monitors"]

@pytest.mark.parametrize("category_name", categories_list)
def test_category_screenshot(go_to_homepage, category_name):
    # Initialize Categories_class (inherits Homepage_class and utils)
    cat = Categories_class(go_to_homepage.driver)

    # Click the category button
    cat.click_category(category_name)
    time.sleep(2)  # small wait for products to load

    # Get visible products using Homepage_class methods
    cat.get_product_titles()      # List of all product titles
    cat.get_product_images()      # List of all product image URLs
    cat.get_product_prices()      # List of all product prices

    # Take screenshot of the category products
    screenshot_file = cat.screenshot_category(f"{category_name}_category.png")
    print(f"Screenshot saved as: {screenshot_file}")
