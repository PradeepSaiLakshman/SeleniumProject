from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ContactPage(BasePage):
    name_input = (By.ID, "FullName")
    email_input = (By.ID, "Email")
    enquiry_input = (By.ID, "Enquiry")
    submit_button = (By.NAME, "send-email")
    success_message = (By.XPATH, "//div[contains(text(), 'successfully sent')]")

    def submit_enquiry(self, name, email, enquiry):
        self.type(self.name_input, name)
        self.type(self.email_input, email)
        self.type(self.enquiry_input, enquiry)
        self.click(self.submit_button)
    
    def get_success_message(self):
        return self.get_text(self.success_message)



