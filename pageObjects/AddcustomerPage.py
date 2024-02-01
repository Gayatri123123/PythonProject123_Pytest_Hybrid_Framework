import time
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select



class AddCustomer:

    linkCustomers_menu = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a"
    linkCustomers_menuitem ="/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a/p"
    btnAddNew = "//*[@class='btn btn-primary']"
    btnPlus = "//*[@class = 'fa toggle-icon fa-plus']"
    txtEmail = "//*[@id='Email']"
    txtPassword = "//*[@id='Password']"
    txtFirstName = "//*[@id='FirstName']"
    txtLastName = "//*[@id='LastName']"
    rdFemale = "//*[@id='Gender_Female']"
    txtDOB = "//*[@id='DateOfBirth']"
    txtCompanyName = "//*[@id='Company']"
    txtNewsLetter = '//*[@id="customer-info"]/div[2]/div[9]/div[2]/div/div[1]/div'
    lst_item = "//li[contains(text(),'Test store 2']"
    txtCustomerRole = '//*[@id="customer-info"]/div[2]/div[10]/div[2]/div/div[1]/div/div'
    lst_item1 = "//li[contains(text(),'Registered']"
    lst_item2 = "//li[contains(text(),'Vendors']"
    drp_vendors = '//*[@id = "VendorId"]'
    txtAdminContent = "//*[@class='form-control']"
    btnSave = "//*[@name='save']"


    def __init__ (self, driver):
        self.driver = driver

    def clickonlinkCustomers_menu(self):
        #self.driver.find_element_by_xpath(self.linkCustomers_menu).click()
        self.driver.find_element(By.XPATH, "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a").click()
        time.sleep(2)
        logging.info("Clicked on Customer Manu")

    def clickonlinkCustomers_menuitem(self):
        self.driver.find_element(By.XPATH, "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a/p").click()
        time.sleep(2)
        logging.info("Clicked on Customer Manu Item")

    def clickonbtn_AddNew(self):
        self.driver.find_element(By.XPATH, "//*[@class = 'btn btn-primary']").click()
        time.sleep(2)
        logging.info("Clicked on Add New")

    def entertxtEmail(self,email):
        ele = self.driver.find_element(By.XPATH,"//*[@id='Email']")
        ele.clear()
        ele.send_keys(email)
        #self.driver.find_element(By.XPATH,"//*[@id='Email']").send_keys("gayatrireddyreddy@gmail.com")
        logging.info("entered Email")

    def entertxtPassword(self):
        self.driver.find_element(By.XPATH,"//*[@id='Password']").send_keys("Gayatri1234$")
        logging.info("entered Password")


    def entertxtFirstName(self):
        self.driver.find_element(By.XPATH,"//*[@id='FirstName']").send_keys("Gayatri")
        logging.info("entered First Name")


    def entertxtLastName(self):
        self.driver.find_element(By.XPATH,"//*[@id='LastName']").send_keys("Reddy")
        logging.info("entered Last Name")


    def clickonrdFemale(self):
        self.driver.find_element(By.XPATH,"//*[@id='Gender_Female']").click()
        logging.info("Selected gender")


    def entertxtDOB(self):
        self.driver.find_element(By.XPATH,"//*[@id='DateOfBirth']").send_keys("25/April/1999")
        logging.info("Entered DOB")

    def entertxtCompanyName(self):
        self.driver.find_element(By.XPATH,"//*[@id='Company']").send_keys("Capgemini")
        time.sleep(5)
        logging.info("Entered Company Name")

    def select_txt_for_NewsLetter(self):
        #elm = self.driver.find_element(By.XPATH,'//*[@id="customer-info"]/div[2]/div[9]/div[2]/div/div[1]/div').click()
        self.driver.find_element(By.XPATH,'//*[@id="customer-info"]/div[2]/div[9]/div[2]/div/div[1]/div').click()
        time.sleep(5)
        #self.driver.find_element(By.XPATH,"//*[contains(text(),'"+text_name+"')]").click()
        self.driver.find_element(By.XPATH,'/html/body/div[5]/div/div[2]/ul/li[1]').click()
        logging.info("Selected News Letter")

        '''
        
        if newsletter == 'Test store 2':
            self.listitem = self.driver.find_element(By.XPATH,"//li[contains(text(),'Test store 2']").click()
        else:
            self.listitem = self.driver.find_element(By.XPATH,"//li[contains(text(),'Your store name']").click()
            
        '''

    def select_manager_for_vendor(self):
        ele=self.driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/form/section/div/div/nop-cards/nop-card/div/div[2]/div[11]/div[2]/select").click()
        ele=self.driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/form/section/div/div/nop-cards/nop-card/div/div[2]/div[11]/div[2]/select/option[2]").click()
        #ele.select_by_value("Vendor 1")
        logging.info("Selected Manager for Vendor")

    def scroll_down_for_text(self,text_name):
        ###### scrollIntoView()
        ele=self.driver.find_element(By.XPATH,"//*[contains(text(),'"+text_name+"')]")
        self.driver.execute_script("arguments[0].scrollIntoView();",ele)
        logging.info("Verified on %s",text_name)

    def enter_comments(self):
        ele=self.driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/form/section/div/div/nop-cards/nop-card/div/div[2]/div[13]/div[2]/textarea")
        ele.send_keys("Details of the user")
        logging.info("Entered Comments")

    def click_on_Save_btn(self):
        ele=self.driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/form/div[1]/div/button[1]").click()
        logging.info("Clicked on Save Button")















