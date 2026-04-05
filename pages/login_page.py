from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    email_input = (By.ID,"Email")
    password_input = (By.ID, "Password")
    login_button = (By.XPATH, "//button[text()='Log in']")
    logout_link = (By.XPATH, "//a[contains(text(),'Log out')]")
    error_message = (By.XPATH, "//div[contains(text(),'unsuccessful')]")

    def login(self, email, password):
        self.type(self.email_input, email)
        self.type(self.password_input, password)
        self.click(self.login_button)
    
    def is_logged_in(self):
        return "Log out" in self.get_text(self.logout_link)
    
    def get_error_message(self):
        return self.get_text(self.error_message)







