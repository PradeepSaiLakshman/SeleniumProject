# import pytest
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# def driver():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.implicitly_wait(5)
#     yield driver
#     driver.quit()

# def test_login_with_valid_credentials(driver):
#     driver.get("https://demo.nopcommerce.com/")
    
#     assert "nopCommerce demo store" in driver.title
    
#     driver.find_element(By.XPATH,"//a[contains(text(),'Log in')]").click()
    
#     returning_customer = driver.find_element(By.XPATH,"//h2[text()='Returning Customer']").text
#     assert returning_customer == 'Returning Customer'
    
#     driver.find_element(By.ID,"Email").send_keys("demo@example.com")
#     driver.find_element(By.ID, "Password").send_keys("demo123")
    
#     driver.find_element(By.XPATH,"//button[text()='Log in']").click()
    
#     my_account = driver.find_element(By.XPATH,"//a[contains(text(),'Log out')]").text
#     assert "Log out" in my_account
    
#     driver.find_element(By.XPATH,"//a[contains(text(),'Log out')]").click()
#     login_link = driver.find_element(By.XPATH,"//a[contains(text(),'Log in')]").text
#     time.sleep(3)
#     assert "Log in" in login_link
    
    

















