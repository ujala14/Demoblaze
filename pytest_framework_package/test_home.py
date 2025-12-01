import pytest
import time
    
# ===== TEST 1: Navbar =====
def test_navbar_elements(go_to_homepage):
    nav_status = go_to_homepage.navbar_items_status()
    for name, visible in nav_status.items():
        print(f"Navbar element: {name}, Visible: {visible}")
        assert visible, f"Navbar element '{name}' is not visible"

# ===== TEST 2: Categories =====
def test_categories_visible(go_to_homepage):
    categories = go_to_homepage.get_categories_present()
    for name, visible in categories.items():
        print(f"Navbar element: {name}, Visible: {visible}")
        assert visible, f"Category '{name}' is not visible"

# # ===== TEST 3: Product grid (titles, images, prices) =====
def test_product_grid(go_to_homepage):
    titles = go_to_homepage.get_product_titles()
    images = go_to_homepage.get_product_images()
    prices = go_to_homepage.get_product_prices()

    assert len(titles) > 0, "No product titles found"
    assert len(images) == len(titles), "Mismatch in number of images and titles"
    assert len(prices) == len(titles), "Mismatch in number of prices and titles"

    for i in range(len(titles)):
        assert titles[i] != "", f"Product title at index {i} is empty"
        assert images[i] != "", f"Product image at index {i} is missing"
        assert "$" in prices[i], f"Product price at index {i} is invalid: {prices[i]}"

# # ===== TEST 4: Pagination =====
def test_pagination(go_to_homepage):
    before_next_titles = go_to_homepage.get_product_titles()

    # Next button
    assert go_to_homepage.is_next_clickable(), "Next button is not clickable"
    go_to_homepage.click_next_button()
    time.sleep(2)
    after_next_titles = go_to_homepage.get_product_titles()
   
    assert before_next_titles !=  after_next_titles, "Product list did not change after clicking Next"

    # Previous button
    assert go_to_homepage.is_prev_clickable(), "Previous button is not clickable"
    go_to_homepage.click_prev_button()

    back_titles = go_to_homepage.get_product_titles()
    assert back_titles == before_next_titles, "Previous button did not return to original products"


# # ===== TEST 6: Footer =====
def test_footer(go_to_homepage):
    assert go_to_homepage.is_footer_visible(), "Footer is not visible"
