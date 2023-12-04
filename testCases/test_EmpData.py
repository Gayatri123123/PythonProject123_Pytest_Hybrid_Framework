import time
import pytest
from pageObjects.EmpData import MyConnect
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen


class Test_005_EMP:
    talent_url = ReadConfig.getApplicationURL_of_Talent()


    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_Emp_Data(self, setup):
        self.logger.info("************Test_001_Validatinding Started Emp Details***************")
        self.driver = setup
        self.driver.get(self.talent_url)
        self.driver.maximize_window()
        time.sleep(10)

        self.data = MyConnect(self.driver)
        time.sleep(30)
        self.data.click_on_cross_btn()

        self.data.scrolldown_till_myconnect()
        self.data.click_on_MyConnect()
        self.data.switch_to_child_window()
        time.sleep(10)
        self.data.click_on_EMP_Data()
        self.data.click_on_Acess_UR_Data()
        self.data.switch_to_child1_window()
        self.data.click_on_Favorites()
        self.data.click_on_Org_Favorties()
        time.sleep(10)
        self.data.maximise_window()

        #self.data.click_on_Payslip()

        #self.data.switch_to_parent_window()
        #self.data.EMPData()
        #self.data.AcessURData()
        #self.data.Personalise()
        self.logger.info("************Test_001_Validation Ended For Emp Details***************")

