import pytest
from selenium import webdriver
from pytest_metadata.plugin import metadata_key


#To RUN Particularly on Chrome browser
@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    return driver


#To Run on any browser
@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver=webdriver.Chrome()
        print("lanching chrome browser")
    elif browser=='edge':
        driver=webdriver.Edge()
        print("lanching firefox browser")
    else:
        driver=webdriver.Chrome()
    #driver = webdriver.Edge()
    return driver
def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
    


#=================Pytest HTML Report==============

#it is hook for adding Environment info to HTML Report
###pytest html report

#for nopcommerce
def pytest_configure(config):
    config.stash[metadata_key]["Project Name"] = 'nop commerce'
    config.stash[metadata_key]["Module Name"] = 'Customer'
    config.stash[metadata_key]["Tester"] = "Gayatri"

'''
  
#for Magic Bricks
def pytest_configure(config):
    config.stash[metadata_key]["Project Name"] = 'Magic Bricks'
    config.stash[metadata_key]["Module Name"] = 'Home Page of Magic Bricks'
    config.stash[metadata_key]["Tester"] = "Gayatri"
    
#for Talent_Page
def pytest_configure(config):
    config.stash[metadata_key]["Project Name"] = 'Talent Page'
    config.stash[metadata_key]["Module Name"] = 'Emp Data'
    config.stash[metadata_key]["Tester"] = "Gayatri"
    
'''

'''
def pytest_config_modifyreport(config):
    # Add a key to the report
    config_report['Project Name'] = 'non commerce'
    config_report['Module Name'] = 'Customer'
    config_report['Tester'] = 'Gayatri'
   #json_report['foo'] = 'bar'
'''

#@pytest.hookimpl(optionalhook=True)
'''def pytest_configure(config):
    config._metadata = {
        'Tester': 'Gayatri Reddy',
        'Project Name': 'Project123'

    }
'''
    #config_metadata["Project Name"] = "non commerce"
    #config.stash[metadata_key]['Module Name'] = 'Customer'
    #config.stash[metadata_key]['Tester'] = 'Gayatri'

'''

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
'''





