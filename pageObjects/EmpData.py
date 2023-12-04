import logging
import time
from selenium.webdriver.common.by import By


class MyConnect:


    def __init__(self,driver):
        self.driver=driver

    def click_on_cross_btn(self):
        self.driver.find_element(By.XPATH,'//*[@id="splashscreen-container"]/span/button').click()
        #self.driver.find_element(By.CSS_SELECTOR,'')

    def scrolldown_till_myconnect(self):
        self.driver.execute_script("window.scrollBy(0, 500)")
        time.sleep(4)

    def maximise_window(self):
        self.driver.maximize_window()

    def click_on_MyConnect(self):
        self.driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/main/div[6]/div[1]/div[1]/div[4]/div/div[1]/ul/li[5]/a").click()
        time.sleep(6)

    def switch_to_child_window(self):
        child = self.driver.window_handles[1]
        self.driver.switch_to.window(child)
        value_pageTitle = self.driver.title
        logging.info("The page title is %s",value_pageTitle)


    def switch_to_parent_window(self):
        parent = self.driver.window_handles[0]
        self.driver.switch_to.window(parent)
        value_pageTitle = self.driver.title
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


    def click_on_Payslip(self):

        self.driver.find_element(By.XPATH,"//*[text()='Pay Slip']").click()
        time.sleep(3)

    def click_on_EMP_Data(self):
        self.driver.find_element(By.XPATH,'//*[@id="home"]/div/main/div/div/div/div[2]/div/section[2]/div/div[2]/div/div[1]/div/div/a/div[2]/h3').click()
        time.sleep(4)

    def click_on_Acess_UR_Data(self):
        self.driver.find_element(By.XPATH,'//*[text()="Access Your Personal Data (ESS)"]').click()
        time.sleep(4)


    def click_on_Favorites(self):
        self.driver.find_element(By.XPATH,'//*[@id="buttonFavorites_HyperLink"]/span').click()
        time.sleep(4)

    def click_on_Org_Favorties(self):
        self.driver.find_element(By.XPATH,'//*[@id="SubMenuContainer_buttonFavorites_HyperLink0_item_1"]/td[3]/div').click()
        value_pageTitle = self.driver.title
        logging.info("The page title is %s",value_pageTitle)
