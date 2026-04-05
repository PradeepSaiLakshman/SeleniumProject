import pytest
from selenium.webdriver.common.by import By
from pages.register_page import RegisterPage

@pytest.mark.order(1)
@pytest.mark.smoke
@pytest.mark.positive
def test_register_user(driver):
    driver.get("https://demo.nopcommerce.com/")
    driver.find_element(By.XPATH, "//a[contains(text(),'Register')]").click()
    register_page = RegisterPage(driver)
    register_page.register("demo1", "example", "demo3@example.com", "Cognizant", "demo123")
    assert "Your registration completed" in register_page.get_success_message()

@pytest.mark.order(2)
@pytest.mark.regression
@pytest.mark.negative
def test_register_existing_email(driver):
    driver.get("https://demo.nopcommerce.com/")
    driver.find_element(By.XPATH,"//a[contains(text(),'Register')]").click()
    register_page = RegisterPage(driver)
    register_page.register("demo1", "example", "demo3@example.com", "Cognizant", "demo123")
    assert "exists" in register_page.get_error_messages()










