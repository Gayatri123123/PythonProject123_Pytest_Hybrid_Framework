import logging
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Loginpage_of_MB:
    

    def __init__(self,driver):
        self.driver=driver

    '''
    def notification_window(self):
        option1 = EdgeOptions()
        option1.use_chromium = True
        option1.add_arguments("--disable-notifications")
        self.driver = webdriver.Edge(options=option1)
    '''

    def drop_down_of_BSH(self,num):

        common_xpath =self.driver.find_element(By.XPATH,'//*[@id="commercialIndex"]/header/section[2]/div/ul/li['+num+']/a').click()
        logging.info("Clicked on %s",str(num))

    def click_DashBoard(self):
        ele=self.driver.find_element(By.XPATH,'/html/body/header/section[2]/div/ul/li[3]/div/div/div[1]/ul/li[2]/a')
        ele.click()
    #//*[@id="commercialIndex"]/header/section[2]/div/ul/li[3]/div/div/div[1]/ul/li[2]/a

    def find_ur_workspace(self,text):
        ele=self.driver.find_element(By.XPATH,'//*[@id="tab'+text+'"]')
        ele.click()
        self.driver.find_element(By.XPATH,'//*[@id="keyword"]').send_keys("abc")

    def click_on_post_property(self):
        self.driver.find_element(By.XPATH,'//*[@id="commercialIndex"]/header/section[1]/div/div[2]/div[3]/a').click()
        time.sleep(5)
        logging.info("Clicked on Post Property")

    def click_on_owner(self):
        self.driver.find_element(By.XPATH,'//*[@id="details-container"]/div[2]/div[2]/div[1]/label').click()
        time.sleep(3)
        logging.info("Clicked on Owner")









    
        
