from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "The page url in not login url!"

    def should_be_login_form(self):
        login_email = self.is_element_present(*LoginPageLocators.LOGIN_EMAIL_FIELD)
        login_password = self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD_FIELD)

        assert login_email and login_password, "Login form is not fully presented!"

    def should_be_register_form(self):
        register_email = self.is_element_present(*LoginPageLocators.REGISTER_EMAIL_FIELD)
        register_pass1 = self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD_FIELD)
        register_pass2 = self.is_element_present(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD_FIELD)

        assert register_email and register_pass1 and register_pass2, "Register form is not fully presented!"