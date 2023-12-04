import time

import pytest
from selenium import webdriver
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.LoginPage import Loginpage
from pageObjects.SearchCustomer import Search_Customer
from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.common_methods import *


class Test_004_Search_Customer():
    comm_url = ReadConfig.getApplicationURL1_of_comm()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_search_customer_by_email(self,setup):
        self.logger.info("************Test_004 Search Customer by email Started ***************")
        self.driver = setup
        self.driver.get(self.comm_url)
        self.driver.maximize_window()
        self.common = Common_Methods(self.driver)
        self.lp = Loginpage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************ Login Succesful ***************")
        self.logger.info("************Starting Search Customer by email ***************")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickonlinkCustomers_menu()
        self.addcust.clickonlinkCustomers_menuitem()
        self.logger.info("************Searching Customer by email ***************")
        time.sleep(5)
        search_customer = Search_Customer(self.driver)
        time.sleep(2)
        search_customer.set_email("kiyjcycyhjc676008@gmail.com")
        time.sleep(2)
        search_customer.click_on_search_btn()
        time.sleep(5)
        self.common.scroll_down_for_text("nopCommerce version 4.60.0")
        self.common.highlight_elm("kiyjcycyhjc676008@gmail.com",'pink')
        self.common.highlight_elm("Virat Kohli",'pink')
        self.logger.info("************Test_004 Search Customer by email ended ***************")



    @pytest.mark.regression
    def test_search_customer_by_name(self,setup):
        self.logger.info("************Test_004 Search Customer by name Started ***************")
        self.driver = setup
        self.driver.get(self.comm_url)
        self.driver.maximize_window()
        self.lp = Loginpage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************ Login Succesful ***************")
        self.logger.info("************Starting Search Customer by name ***************")
        self.common = Common_Methods(self.driver)
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickonlinkCustomers_menu()
        self.addcust.clickonlinkCustomers_menuitem()
        self.logger.info("************Searching Customer by name ***************")
        time.sleep(5)
        search_customer = Search_Customer(self.driver)
        time.sleep(2)
        search_customer.set_first_name()
        time.sleep(2)
        search_customer.set_last_name()
        time.sleep(2)
        search_customer.click_on_search_btn()
        time.sleep(5)
        self.common.scroll_down_for_text("nopCommerce version 4.60.0")
        self.common.highlight_elm("kiyjcycyhjc676008@gmail.com",'pink')
        time.sleep(2)
        self.common.highlight_elm("Virat Kohli",'pink')
        self.logger.info("************Test_004 Search Customer by name ended ***************")



