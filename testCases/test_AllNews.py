import random
import string
import time

import pytest
from selenium import webdriver

from pageObjects.AllNews import AllNews
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen


class Test_004_Talent:
    talent_url = ReadConfig.getApplicationURL_of_Talent()


    logger = LogGen.loggen()


    @pytest.mark.regression
    def test_TalentPageTitle(self, setup):
        self.logger.info("************Test_001_Validating ***************")
        self.driver = setup
        self.driver.get(self.talent_url)
        self.driver.maximize_window()

        time.sleep(10)
        act_title=self.driver.title
        if act_title=="India Intranet Homepage | Talent Capgemini":
            assert True
            time.sleep(3)
            #self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_TalentPageTitle.png")
            self.driver.close()
            assert False

        self.news = AllNews(self.driver)

        self.news.highlight_elmforprofile("Welcome","yellow","pink")
        time.sleep(3)
        self.news.clickonAllNews()
        self.news.clickonLandD()


    '''def test_AllNews(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL1)
        self.driver.maximize_window()
        time.sleep(5)
        self.news = TalentPage(self.driver)

        self.news.highlight_elmforprofile()
        time.sleep(3)
        self.news.clickonAllNews()
        self.news.clickonLandD()
        #//*[text()="NEWS FROM Learning & Development "]'''







