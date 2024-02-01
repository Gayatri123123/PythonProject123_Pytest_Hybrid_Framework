import time
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class Search_Customer:

    def __init__(self, driver):
        self.driver = driver

    def set_email(self,email):
        ele=self.driver.find_element(By.XPATH,'//*[@id="SearchEmail"]')
        ele.clear()
        ele.send_keys(email)
        logging.info("Enterd email")

    def set_first_name(self):
        ele=self.driver.find_element(By.XPATH,"//*[@id='SearchFirstName']")
        ele.click()
        ele.send_keys("Virat")
        logging.info("Enterd first name")


    def set_last_name(self):
        ele=self.driver.find_element(By.XPATH,'//*[@id="SearchLastName"]')
        ele.click()
        ele.send_keys("Kohli")
        logging.info("Enterd last name")

    def click_on_search_btn(self):
        ele=self.driver.find_element(By.XPATH,'//*[@id="search-customers"]').click()
        logging.info("Clicked on Search Button")

    def get_table_info(self):
        self.driver.find_element(By.XPATH,'//*[@id="customers-grid"]//tbody/tr')

    def get_no_of_rows(self):
        return  len(self.driver.find_elements(By.XPATH,'//*[@id="customers-grid"]//tbody/tr'))

    def get_no_of_columns(self):
        return  len(self.driver.find_elements(By.XPATH,'//*[@id="customers-grid"]//tbody/tr'))

    def get_customer_details(self):
        self.driver.find_element(By.XPATH,'//*[@id="customers-grid"]/tbody/tr/td[2]').text
       # //*[@id="customers-grid"]/tbody/tr/td[2]



    def search_customer_by_email(self,email):
        flag=False
        a=self.get_customer_details()
        for r in range(1,self.get_no_of_rows()+1):
            table=self.get_table_info()
            email_id = table.find_element(By.XPATH,'//*[@id="customers-grid"]/tbody/tr[2]/td[2]').text
            if email_id == email:
                flag = True
                break
        return flag

    def search_customer_by_name(self,name):
        flag=False
        for r in range(1,self.get_no_of_rows()+1):
            table=self.get_table_info()
            Name = table.find_element(By.XPATH,'//*[@id="customers-grid"]/tbody/tr[2]/td[2]').text
            if Name == name:
                flag = True
                break
        return flag

    #//table[@id='customers-grid']//tbody/tr
