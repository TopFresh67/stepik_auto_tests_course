from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_LINK_REG), "Login link is not presented"
        assert "login" in self.browser.current_url, "login is not included in current URL"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.SIGNIN_LINK), "Sign In link is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_LINK), "Registration link is not presented"