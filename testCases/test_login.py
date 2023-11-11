from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig as Rc
from utilities.custonmLogger import Logger
from time import sleep


class TestLogin:
    baseURL = Rc.getApplicationURL()
    username = Rc.getUserEmail()
    password = Rc.getPassword()
    logger = Logger.logGen()

    # logger = Il.initLogger()

    def test_login(self, setup):
        self.logger.info("**************YourID loging has been started now")

        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        sleep(5)
        title = self.driver.title
        self.logger.info(title)
        self.driver.save_screenshot(".\\screenShots\\" + "Dashboard.png")
        self.Lp = LoginPage(self.driver)
        self.logger.info(self.Lp.link_signin_xpath)
        sleep(10)
        # self.driver.implicitly_wait(10)
        # self.Lp.SetDriver(self.driver)
        self.Lp.clickSignin()
        self.driver.implicitly_wait(10)
        self.driver.save_screenshot(".\\screenShots\\" + "loginScreen.png")
        # sleep(10)
        self.Lp.setUserName(self.username)
        sleep(5)
        self.Lp.setPassWord(self.password)
        sleep(5)
        self.Lp.clickLogin()
        sleep(10)
        k = self.driver.title
        self.logger.info(k)
        self.Lp.clickLogout()
        sleep(5)
        self.driver.close()
