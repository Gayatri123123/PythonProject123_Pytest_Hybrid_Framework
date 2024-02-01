import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import logging

class Common_Methods:

        def __init__ (self, driver):
                self.driver = driver

        def highlight_elm(self,text,clr):
                ele = self.driver.find_element(By.XPATH, "//*[contains(text(),'"+text+"')]")
                self.driver.execute_script("arguments[0].style.color='"+clr+"'",ele)
                time.sleep(3)
                logging.info("Verified on %s",str(text))

        def remove_highlight_element(self,text):

                ele = self.driver.find_element(By.XPATH, "//*[contains(text(),'"+text+"')]")
                self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",ele,"background:''; color:''; border:'';")

                #self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",ele,"background:'"+bcg_color+"'; color:'"+color+"'; border:4px dotted solid yellow;")
                time.sleep(5)

        def scroll_down_for_text(self,text_name):
        ###### scrollIntoView()
                ele=self.driver.find_element(By.XPATH,"//*[contains(text(),'"+text_name+"')]")
                self.driver.execute_script("arguments[0].scrollIntoView();",ele)
                time.sleep(5)
                logging.info("Scrolled till %s",text_name)

        ##### window.scroll
                #self.driver.execute_script("window.scrollBy(0, 500)")

        #### By ARROW_DOWN
                #ele.send_keys(Keys.ARROW_DOWN)
                #time.sleep(4)

        ####### Scroll until visibility
                #text = By.XPATH,"//*[contains(text(),'"+text_name+"')]"
                #ele1 = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(text))

        def scroll_up_for_text(self,text_name):
        ###### scrollIntoView()
                ele=self.driver.find_element(By.XPATH,"//*[contains(text(),'"+text_name+"')]")
                self.driver.execute_script("arguments[0].scrollIntoView();",ele)
                time.sleep(3)
                logging.info("Scrolled till %s",text_name)

        #scroll up home
                #self.driver.execute_script("window.scrollTo(0,0);")

        #nt working but it will work try later
                #ele.send_keys(Keys.HOME)

        def click_on_text(self,text_name):
                ###### scrollIntoView()
                ele=self.driver.find_element(By.XPATH,"//*[contains(text(),'"+text_name+"')]")
                time.sleep(3)
                logging.info("Verified on %s",text_name)

#switching next window
        def switch_to_window(self):
                #self.driver.switch_to.new_window('window')
                #self.driver.switch_to.new_window('tab')
                child = self.driver.window_handles[1]
                self.driver.switch_to.window(child)
                time.sleep(2)
                logging.info("switched to another window")

        def switch_to_new_window(self):
                self.driver.switch_to.new_window('window')
        def swich_to_new_tab(self):
                self.driver.switch_to.new_window('tab')

#switch to home window
        def switch_to_parent_window(self):
                parent = self.driver.window_handles[0]
                self.driver.switch_to.window(parent)
                value_pageTitle = self.driver.title
                time.sleep(3)
                logging.info("The page title is %s",value_pageTitle)

        def switch_to_child1_window(self):
                child = self.driver.window_handles[2]
                self.driver.switch_to.window(child)
                value_pageTitle = self.driver.title
                logging.info("The page title is %s",value_pageTitle)

        def switch_to_parent1_window(self):
                parent = self.driver.window_handles[1]
                self.driver.switch_to.window(parent)
                value_pageTitle = self.driver.title
                logging.info("The page title is %s",value_pageTitle)

