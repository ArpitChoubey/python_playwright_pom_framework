import pytest
from playwright.sync_api import expect, Page

from LoginPage  import LoginPage
from Homepage1 import HomePage
from CartPage import CartPage


@pytest.mark.parametrize("username, password, product_name", [
    ("arpit", "test@123", "Samsung galaxy s6"),
])
def test_user_can_login_and_add_product_to_cart(
        page: Page, username, password, product_name):

    page.goto("https://www.demoblaze.com/index.html")

    # Login
    login_page = LoginPage(page)
    login_page.click_login_link()
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login_button()

    # HomePage
    home_page = HomePage(page)
    home_page.add_product_to_cart(product_name)
    home_page.goto_cart()

    # CartPage
    cart_page = CartPage(page)

    product = cart_page.check_product_in_cart(product_name)

    expect(product).to_be_visible()