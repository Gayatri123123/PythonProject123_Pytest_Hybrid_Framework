import time

import pytest
from selenium import webdriver
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.Magic_Bricks_Home_Page import Loginpage_of_MB
from pageObjects.common_methods import Common_Methods


class Test_01_Magic_Bricks:
    mb_url = ReadConfig.getMBApplicationURL_of_MB()
    



    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_Home_Page(self, setup):
        self.logger.info("************* Test_01_Magic_Bricks Satrted **************")
        self.driver = setup
        self.driver.get(self.mb_url)
        self.driver.maximize_window()
        self.comm = Common_Methods(self.driver)
        self.hp = Loginpage_of_MB(self.driver)
        time.sleep(3)
        self.comm.scroll_down_for_text("About Magicbricks")
        self.comm.highlight_elm("About Magicbricks",'pink')
        self.comm.scroll_up_for_text("love")
        self.comm.highlight_elm("love",'pink')
        self.hp.click_on_post_property()
        self.comm.switch_to_window()
        #self.hp.switch_to_window()
        self.hp.click_on_owner()
        self.comm.switch_to_parent_window()
        self.comm.scroll_down_for_text("About Magicbricks")
        self.logger.info("************* Test_01_Magic_Bricks Ended **************")


       
        

        #time.sleep(4)
       

       

