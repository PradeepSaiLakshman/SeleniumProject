from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class RegisterPage(BasePage):

    gender_male = (By.ID, "gender-male")
    first_name = (By.ID, "FirstName")
    last_name = (By.ID, "LastName")
    email = (By.ID, "Email")
    company = (By.ID, "Company")
    password = (By.ID, "Password")
    confirm_password = (By.NAME,"ConfirmPassword")
    register_button = (By.ID, "register-button")
    success_message = (By.XPATH,"//div[contains(text(),'Your registration completed')]")
    error_message = (By.XPATH,"//li[contains(text(), 'The specified email already exists')]")

    def register(self, fname, lname, email, company, pwd):
        self.click(self.gender_male)
        self.type(self.first_name, fname)
        self.type(self.last_name, lname)
        self.type(self.email, email)
        self.type(self.company, company)
        self.type(self.password, pwd)
        self.type(self.confirm_password, pwd)
        self.click(self.register_button)

    def get_success_message(self):
        return self.get_text(self.success_message)
    
    def get_error_messages(self):
        return self.get_text(self.error_message)







