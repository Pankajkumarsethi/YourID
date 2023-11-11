from selenium.webdriver.common.by import By


class LoginPage:
    """Create loging page object class under 'PageObjects package'"""

    link_signin_xpath = "//a[text()='Sign In']"
    textbox_username_xpath = "//input[@id='loginUserName']"
    textbox_password_xpath = "//input[@ng-model='$parent.viewData.login.password']"
    button_login_xpath = "//button[@ng-click='login(loginForm)']"
    link_logout_xpath = "//span[text()='Log out']"

    def __init__(self, driver):
        self.driver = driver

    # def SetDriver(self, driver):
    #     self.driver = driver

    def clickSignin(self):
        self.driver.find_element(By.XPATH, self.link_signin_xpath).click()

    def setUserName(self, username):
        # self.driver.find_element(By.XPATH, self.textbox_username_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(username)

    def setPassWord(self, password):
        # self.driver.find_element(By.XPATH, self.textbox_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT, self.link_logout_xpath).click()
