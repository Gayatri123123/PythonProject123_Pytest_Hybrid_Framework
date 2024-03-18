import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import Loginpage
from pageObjects.common_methods import Common_Methods
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    comm_url = ReadConfig.getApplicationURL1_of_comm()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homePageTitle(self, setup):

        self.logger.info("************Test_001_Login HomePage Started ***************")
        self.driver = setup
        self.driver.get(self.comm_url)
        self.common = Common_Methods(self.driver)
        self.hp = Loginpage(self.driver)
        time.sleep(5)
        self.common.highlight_elm("Welcome",'pink')
        time.sleep(3)
        self.common.remove_highlight_element("Welcome",)
        time.sleep(3)
        act_title=self.driver.title
        if act_title=="Your store. Login":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            assert False
        self.logger.info("************Test_001_Login HomePage Ended ***************")

    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("************Test_001_Login LoginPage Started ***************")
        self.driver= setup
        self.driver.get(self.comm_url)
        self.lp = Loginpage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title
        if act_title=="Dashboard / nopCommerce administration":
            assert True
            time.sleep(5)
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            assert False
        self.logger.info("************Test_001_Login LoginePage Started ***************")

#pytest -s -v -n=2 --html=Reports\report.html testCases/test_login.py --browser edge




