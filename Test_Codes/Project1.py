from selenium import webdriver
from selenium.webdriver.common.by import By
from Test_Data import data
import pytest
import time

class Test_Sumukh:
    url = "https://opensource-demo.orangehrmlive.com"
    
    # Booting Method for running the Python Tests
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox()
        yield
        self.driver.close()

    #TC_Login_01 : Successful Employee Login to OrangeHRM Page
    
    def test_TC_Login_01(self, booting_function):
        self.driver.maximize_window()#Maximising the browser window
        time.sleep(data.Sumukh_Data.smallWait) #Wait time for Maximising Screen
        self.driver.get(self.url)
        time.sleep(data.Sumukh_Data.smallWait)
        self.driver.find_element(by=By.NAME, value=data.Sumukh_Selectors.input_box_username).send_keys(data.Sumukh_Data.username)
        self.driver.find_element(by=By.NAME, value=data.Sumukh_Selectors.input_box_password).send_keys(data.Sumukh_Data.password)
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.login_xpath).click()
        assert self.driver.title == 'OrangeHRM'
        print("SUCCESS # Logged In Succesfully")

    #TC_Login_02 : Invalid Employee Login to OrangeHRM Page

    def test_TC_Login_02(self, booting_function):
        self.driver.maximize_window() #Maximising the browser window
        time.sleep(data.Sumukh_Data.smallWait) #Wait time for Maximising Screen        
        self.driver.get(self.url)
        time.sleep(data.Sumukh_Data.smallWait)
        self.driver.find_element(by=By.NAME, value=data.Sumukh_Selectors.input_box_username).send_keys(data.Sumukh_Data.username)
        self.driver.find_element(by=By.NAME, value=data.Sumukh_Selectors.input_box_password).send_keys(data.Sumukh_Data.invalidpassword)
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.login_xpath).click()
        time.sleep(data.Sumukh_Data.mediumWait)
        assert self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.invalid_login_xpath)
        print("SUCCESS # Invalid Credentials Message is displayed on the screen")



    #TC_PIM_01 : Add a new emplyee in the PIM Module

    def test_TC_Login_03(self, booting_function):
        self.driver.maximize_window()#Maximising the browser window
        time.sleep(data.Sumukh_Data.smallWait) #Wait time for Maximising Screen
        self.driver.get(self.url)
        time.sleep(data.Sumukh_Data.smallWait)
        self.driver.find_element(by=By.NAME, value=data.Sumukh_Selectors.input_box_username).send_keys(data.Sumukh_Data.username)
        self.driver.find_element(by=By.NAME, value=data.Sumukh_Selectors.input_box_password).send_keys(data.Sumukh_Data.password)
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.login_xpath).click()
        time.sleep(data.Sumukh_Data.mediumWait)
        print("Login is successful")
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.PIM_xpath).click()
        print("Click on PIM was successful")
        time.sleep(data.Sumukh_Data.mediumWait )
        self.driver.find_element(by=By.LINK_TEXT, value=data.Sumukh_Selectors.tab_add_employee).click()
        time.sleep(data.Sumukh_Data.mediumWait)
        print("Click on Add Employee was successful")
        self.driver.find_element(by=By.NAME, value=data.Sumukh_Selectors.input_box_firstname).send_keys(data.Sumukh_Data.firstName) #Fill First Name
        time.sleep(data.Sumukh_Data.smallWait)
        self.driver.find_element(by=By.NAME, value=data.Sumukh_Selectors.input_box_lastname).send_keys(data.Sumukh_Data.lastName) #Fill Last Name
        time.sleep(data.Sumukh_Data.smallWait)
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.save_xpath).click() #Click on Save.
        time.sleep(data.Sumukh_Data.longWait)
        print("Click on Save was successful")
        New_Name1 = self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.newName_xpath).text
        assert New_Name1 == data.Sumukh_Data.fullName #Asserting the Name of the Employee being displayed after creation.
        print("SUCCESS # A New Employee is added into the PIM Module")
    
    #TC_PIM_02 : Edit an existing emplyee in the PIM Module

    def test_TC_Login_04(self, booting_function):
        self.driver.maximize_window()#Maximising the browser window
        time.sleep(data.Sumukh_Data.smallWait) #Wait time for Maximising Screen
        self.driver.get(self.url)
        time.sleep(data.Sumukh_Data.smallWait)
        self.driver.find_element(by=By.NAME, value=data.Sumukh_Selectors.input_box_username).send_keys(data.Sumukh_Data.username)
        self.driver.find_element(by=By.NAME, value=data.Sumukh_Selectors.input_box_password).send_keys(data.Sumukh_Data.password)
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.login_xpath).click()
        time.sleep(data.Sumukh_Data.mediumWait)
        print("Login is successful")
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.PIM_xpath).click()
        print("Click on PIM was successful")
        time.sleep(data.Sumukh_Data.mediumWait)
        #Enter First Name and click on Search
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.firstName_xpath).send_keys(data.Sumukh_Data.firstName)
        time.sleep(data.Sumukh_Data.smallWait)
        print("Click on Search")
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.search_xpath).click()
        time.sleep(data.Sumukh_Data.mediumWait)
        #Click on the first row check box
        print("Click on the first checkbox")
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.firstCheckBox_xpath).click()
        time.sleep(data.Sumukh_Data.smallWait)
        #Click on Edit icon
        print("Click on the Edit Icon")
        self.driver.find_element(by=By.XPATH, value= data.Sumukh_Selectors.edit_xpath).click()
        time.sleep(data.Sumukh_Data.mediumWait)
        #Edit First Name
        self.driver.find_element(by=By.NAME, value=data.Sumukh_Selectors.input_box_firstname).send_keys(data.Sumukh_Data.newName)
        time.sleep(data.Sumukh_Data.smallWait)
        #Click on Save
        self.driver.find_element(by=By.XPATH, value= data.Sumukh_Selectors.editSave_xpath).click() #Click on Save.
        print("Successfully Saved the new Name to the Employee")
        time.sleep(data.Sumukh_Data.longWait)
        self.driver.refresh() #Refreshing the page so the new name loads
        time.sleep(data.Sumukh_Data.mediumWait)
        print("Asserting the new name is not equal to old name")
        new_NAME = self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.newName_xpath).text
        assert new_NAME != data.Sumukh_Data.fullName
        print("SUCCESS # Employee Details Modified")

    #TC_PIM_03 : Delete an existing emplyee in the PIM Module

    def test_TC_Login_05(self, booting_function):
        self.driver.maximize_window()#Maximising the browser window
        time.sleep(data.Sumukh_Data.smallWait) #Wait time for Maximising Screen
        self.driver.get(self.url)
        time.sleep(data.Sumukh_Data.smallWait)
        self.driver.find_element(by=By.NAME, value=data.Sumukh_Selectors.input_box_username).send_keys(data.Sumukh_Data.username)
        self.driver.find_element(by=By.NAME, value=data.Sumukh_Selectors.input_box_password).send_keys(data.Sumukh_Data.password)
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.login_xpath).click()
        time.sleep(data.Sumukh_Data.mediumWait)
        print("Login is successful")
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.PIM_xpath).click()
        print("Click on PIM was successful")
        time.sleep(data.Sumukh_Data.mediumWait)
        #Enter First Name and click on Search
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.firstName_xpath).send_keys(data.Sumukh_Data.firstName)
        time.sleep(data.Sumukh_Data.smallWait)
        print("Click on Search")
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.search_xpath).click()
        time.sleep(data.Sumukh_Data.smallWait)
        #Click on the first row check box
        print("Click on the first checkbox")
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.firstCheckBox_xpath).click()
        time.sleep(data.Sumukh_Data.smallWait)
        #Click on Delete icon
        print("Click on the Delete Icon")
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.delete_xpath).click()
        time.sleep(data.Sumukh_Data.mediumWait)
        print("Confirm deleting the patient details")
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.confirmDelete_xpath).click()
        time.sleep(data.Sumukh_Data.longWait)       
        print("Asserting No Data found of a perticular employee message")     
        assert self.driver.find_element(by=By.XPATH, value= data.Sumukh_Selectors.dataNA_xpath)
        print("SUCCESS # Employee details deleted")