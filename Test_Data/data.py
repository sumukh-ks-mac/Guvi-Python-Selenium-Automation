# This file consists of Test Information like username, password, XPATH etc

# Python Class for Username ,  Password ,  Names and Wait Time (Sleep-Time).
class Sumukh_Data:
    username = "Admin"
    password = "admin123"
    invalidpassword = "Invalid Password"
    firstName = "PIN"
    lastName = "BALL"
    fullName = "PIN BALL"
    newName = "Nobel"
    smallWait = 5
    mediumWait = 10
    longWait = 20


# Python Class for Selenium Selectors
class Sumukh_Selectors:
    input_box_username = "username"
    input_box_password = "password"
    input_box_firstname = "firstName"
    input_box_lastname = "lastName"
    tab_add_employee = "Add Employee"
    login_xpath = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
    save_xpath = '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]'
    newName_xpath = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[1]/div[1]/h6'
    invalid_login_xpath = '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p'
    PIM_xpath = '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a'
    firstName_xpath = '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input'
    search_xpath = '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]'
    firstCheckBox_xpath = '/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[1]/div/div/label/span/i'
    edit_xpath = '/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[9]/div/button[2]/i'
    save_xpath = '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]'
    delete_xpath = '/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[9]/div/button[1]/i'
    confirmDelete_xpath = '/html/body/div/div[3]/div/div/div/div[3]/button[2]'
    dataNA_xpath = '/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span'
    editSave_xpath = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button'