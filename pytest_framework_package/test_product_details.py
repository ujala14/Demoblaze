from POM.product_page import ProductDetail_class
import time

def test_product_detail_page(go_to_homepage):
    product_page = ProductDetail_class(go_to_homepage.driver)

    #  Click first product
    product_page.click_product()
    time.sleep(2)  # wait for page to load
    product_name = product_page.get_text(product_page.PRODUCT_NAME)
    print("Product opened:", product_name)
    assert product_name, "Product detail page did not open"

    #  Verify price is shown
    price = product_page.get_product_price()
    print("Product price:", price)
    assert price.startswith("$"), "Product price is not visible"

    #  Click Add to Cart
    product_page.click_add_to_cart()
    alert = product_page.wait_for_alert()
    alert_text = alert.text
    print("Alert text:", alert_text)
    assert "Product added" in alert_text, "Add to cart alert not shown"
    alert.accept()  # close alert

    #  Verify product image
    image_visible = product_page.is_product_image_visible()
    print("Product image visible:", image_visible)
    assert image_visible, "Product image not visible"

    product_page.screenshot(f"{product_name}_product_detail.png")
