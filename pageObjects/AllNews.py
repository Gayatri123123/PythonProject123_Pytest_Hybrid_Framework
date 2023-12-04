import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui

class AllNews:


    def __init__(self,driver):
        self.driver=driver

    def highlight_elmforprofile(self,text,bclr,clr):
        #self.driver.execute_script("arguments[0].style.border='3px solid red'",element)
        ele = self.driver.find_element(By.XPATH, "//*[contains(text(),'"+text+"')]")
        #self.driver.execute_script("arguments[0].setAttribute('style',color:'"+clr+"'),
        #self.driver.execute_script("arguments[0].style.color='"+clr+"';",ele)
        self.driver.execute_script("arguments[0].style.border='"+bclr+"'; arguments[0].style.backgroundColor='"+clr+"'",ele)


    def clickonAllNews(self):
        self.driver.find_element(By.XPATH,'//*[@id="megamenu-news"]/a').click()
        time.sleep(3)

    def clickonLandD(self):
        ele = self.driver.find_element(By.XPATH,'//*[@id="in_megamenu-news_megamenu"]/div/div[3]/div/ul/li/a[2]')
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",ele,"background:yellow; color:Red; border:4px dotted solid yellow;")
        ele.click()
        time.sleep(3)
        ele=self.driver.find_element(By.XPATH,'//*[text()="NEWS FROM Learning & Development "]')

        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",ele,"background:yellow; color:Red; border:4px dotted solid yellow;")
