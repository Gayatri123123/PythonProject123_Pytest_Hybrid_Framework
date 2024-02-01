import random
import string
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.LoginPage import Loginpage
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.Magic_Bricks_Home_Page import Loginpage_of_MB



class Test_003_AddCustomer:
    comm_url = ReadConfig.getApplicationURL1_of_comm()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self,setup):
        self.logger.info("************Test_003 AddCustomer Started ***************")
        self.driver = setup
        self.driver.get(self.comm_url)
        self.driver.maximize_window()
        self.lp = Loginpage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************ Login Succesful ***************")
        self.logger.info("************Starting Add Customer Test***************")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickonlinkCustomers_menu()
        self.addcust.clickonlinkCustomers_menuitem()
        self.addcust.clickonbtn_AddNew()
        self.logger.info("************Providing customer info ***************")
        self.email = random_generator() + "@gmail.com"
        self.addcust.entertxtEmail(self.email)
        self.addcust.entertxtPassword()
        self.addcust.entertxtFirstName()
        self.addcust.entertxtLastName()
        self.addcust.clickonrdFemale()
        self.addcust.entertxtDOB()
        self.addcust.entertxtCompanyName()
        self.addcust.select_txt_for_NewsLetter()
        time.sleep(3)
        self.addcust.scroll_down_for_text("nopCommerce version 4.60.0")
        time.sleep(5)
        self.addcust.select_manager_for_vendor()
        self.addcust.enter_comments()
        self.addcust.scroll_down_for_text("Customer info")
        self.addcust.click_on_Save_btn()
        self.logger.info("************Test_003 AddCustomer Ended ***************")
        '''
        self.msg = self.driver.find_element(By.TAG_NAME,"body").text

        print(self.msg)
        if 'Customer has been added Successfully. ' in self.msg:
            self.logger.info("************Test_003 AddCustomer Passed ***************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_addCustomer_scr.png")
            self.logger.info("************Test_003 AddCustomer Failed ***************")
            assert False, "Assertion Error: Customer has not been added successfully."
        '''
        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        print(self.msg)


        if 'The new customer has been added successfully.' in self.msg:
            self.logger.info("************Test_003 AddCustomer Passed ***************")
            assert True == True
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_addCustomer_scr.png")
            self.logger.info("************Test_003 AddCustomer Failed ***************")
            assert False, "Assertion Error: Customer has not been added successfully."








def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

