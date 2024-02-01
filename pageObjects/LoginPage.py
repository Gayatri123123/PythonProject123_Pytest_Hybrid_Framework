import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui

class Loginpage:
    #textbox_username_xpath = "email"
    #textbox_username_id = "Email"
    #textbox_password_class = "password"
    #button_login_class = "button-1 login-button"
    link_logout_linktext = "Logout"

    def __init__(self,driver):
        self.driver=driver

    '''def highlight_elm(self):
        #self.driver.execute_script("arguments[0].style.border='3px solid red'",element)
        ele = self.driver.find_element(By.XPATH, "//*[text()='Welcome, please sign in!']")
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",ele,"background:yellow; color:Red; border:4px dotted solid yellow;")
        time.sleep(5)'''
    def highlight_elm(self,text):
        #self.driver.execute_script("arguments[0].style.border='3px solid red'",element)
        ele = self.driver.find_element(By.XPATH, "//*[contains(text(),'"+text+"')]")
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",ele,"background:yellow; color:Red; border:4px dotted solid yellow;")

        #self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",ele,"background:'"+bcg_color+"'; color:'"+color+"'; border:4px dotted solid yellow;")
        time.sleep(5)


    #remove_highlight_element
    def remove_highlight_element(self,text):
        
        ele = self.driver.find_element(By.XPATH, "//*[contains(text(),'"+text+"')]")
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",ele,"background:''; color:''; border:'';")

        #self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",ele,"background:'"+bcg_color+"'; color:'"+color+"'; border:4px dotted solid yellow;")
        time.sleep(5)

    def setUserName(self,username):
       self.driver.find_element(By.XPATH, "//*[@id='Email']").clear()
       self.driver.find_element(By.XPATH,"//*[@id='Email']").send_keys(username)

       #self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",ele,"background:yellow; color:Red; border:4px dotted solid yellow;")

    def setPassword(self,password):
        self.driver.find_element(By.XPATH, "//*[@id='Password']").clear()
        self.driver.find_element(By.XPATH, "//*[@id='Password']").send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button").click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH,'//*[@id="navbarText"]/ul/li[3]/a').click()
        time.sleep(3)









