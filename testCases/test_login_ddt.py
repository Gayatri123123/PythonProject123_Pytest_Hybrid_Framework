import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import Loginpage
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils


class Test_002_DDT_Login:
    comm_url = ReadConfig.getApplicationURL1_of_comm()
    path=".//TestData/LoginData.xlsx"

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self,setup):
        self.logger.info("************** Test_002_DDT_Login Started***************** ")
        self.driver= setup
        self.driver.get(self.comm_url)
        time.sleep(5)
        self.lp = Loginpage(self.driver)

        self.rows = XLUtils.getRowCount(self.path,'Sheet1')
        print("no of rows in excel:",self.rows)

        list_status = []



        for r in range(2,self.rows+1):
            self.user = XLUtils.readData(self.path,'Sheet1',r,1)
            self.password = XLUtils.readData(self.path,'Sheet1',r,2)
            self.exp = XLUtils.readData(self.path,'Sheet1',r,3)

            self.lp.setUserName(self.user)
            time.sleep(2)
            self.lp.setPassword(self.password)
            time.sleep(2)
            self.lp.clickLogin()
            time.sleep(5)


            act_title=self.driver.title
            exp_title="Dashboard / nopCommerce administration"
            if act_title == exp_title:
               if self.exp=="Pass":
                   self.logger.info("test is passed")
                   self.lp.clickLogout()
                   list_status.append("Pass")
               elif self.exp=="Fail":
                   self.logger.info("test is failed")
                   self.lp.clickLogout()
                   list_status.append("Fail")

            elif act_title!= exp_title:
                if self.exp=="Pass":
                   self.logger.info("test is failed")
                   self.lp.clickLogout()
                   list_status.append("Fail")
                elif self.exp == "Fail":
                   self.logger.info("test is passed")
                   list_status.append("Pass")


        if "Fail" not in list_status:
            self.logger.info("Login ddt test passed")
            self.driver.close()
            assert True

        else:
            self.logger.info("login ddt test failed ")

            self.driver.close()
            assert False

        self.logger.info("************** Test_002_DDT_Login Ended***************** ")










#pytest -s -v -n=2 --html=Reports\report.html testCases/test_login.py --browser edge
#




