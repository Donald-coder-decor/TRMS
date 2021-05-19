# from telnetlib import EC
from lib2to3.pgen2 import driver
from time import sleep

from behave import given, when, then

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from features.pages.wiki_home import WikiHomePage



# Employee login
@given(u'The Employee is on the Login Home Page')
def step_impl(context):
    driver: WebDriver = context.driver
    driver.get(
        "file:///C:/Users/adoko/Documents/Java%20Raveture%20notes/Project%20One/projectOneFrontEnd/loginpage.html")
    sleep(5)


@when(u'Employee enters Username as <username>')
def login_usernames(context):
    driver: WebDriver = context.driver
    WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.ID, 'username')))
    driver.find_element_by_id('username').send_keys("marcdon")

    sleep(5)

@when(u'Employee enters Password as <password>')
def login_password(context):
    driver: WebDriver = context.driver
    WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.ID, 'password')))
    driver.find_element_by_id('password').send_keys("1010")

    sleep(5)

@when(u'Employee should click on the login button')
def login(context):
    wiki_home: WikiHomePage = context.wiki_home_page
    wiki_home.login().click()



@given(u'The Employee is on the Login Home Page\'')
def step_impl(context):
    driver: WebDriver = context.driver
    driver.get(
        "file:///C:/Users/adoko/Documents/Java%20Raveture%20notes/Project%20One/projectOneFrontEnd/loginpage.html")
    sleep(5)

#
# @when(u'Employee enters Username as <username>\'')
# def step_impl(context):
#     pass
#
#
# @when(u'Employee enters Password as <password>\'')
# def step_impl(context):
#     pass
#
#
# @then(u'The Employee should be on the  login Page')
# def step_impl(context):
#     pass
#
#
# @given(u'The Employee is on the TRSM Home Page')
# def step_impl(context):
#     pass
#
#
# @when(u'The User types <marcdon>  and password <1010>in the search bar')
# def step_impl(context):
#     pass
#
#
# @when(u'The User clicks the search button')
# def step_impl(context):
#     pass


@then(u'The title should be marcdon - Tuition Reimbursement Service Management  App')
def step_impl(context):
    pass


@then(u'The title should be jude - Tuition Reimbursement Service Management  App')
def step_impl(context):
    pass


@then(u'The title should be Donald - Tuition Reimbursement Service Management  App')
def step_impl(context):
    pass


@then(u'The title should be Ganon - Tuition Reimbursement Service Management  App')
def step_impl(context):
    pass


#   ----------------------- Supervisor login roles------------------------

@given(u'The Supervisor is  ready to login')
def step_impl(context):
    driver: WebDriver = context.driver
    driver.get(
        "file:///C:/Users/adoko/Documents/Java%20Raveture%20notes/Project%20One/projectOneFrontEnd/loginpage.html")
    sleep(5)


@when(u'The Supervisor put in the Username')
def step_impl(context):
    driver: WebDriver = context.driver
    WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.ID, 'username')))
    driver.find_element_by_id('username').send_keys("sup")

    sleep(5)


@when(u'The Supervisor put in the <passsword>')
def step_impl(context):
    driver: WebDriver = context.driver
    WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.ID, 'password')))
    driver.find_element_by_id('password').send_keys("sup")
    print("Login as Supervisor")
    sleep(5)


@when(u'The Supervisor clicks on the Login Button')
def supervisor_login(context):
    wiki_home: WikiHomePage = context.wiki_home_page
    wiki_home.login().click()



@then(u'The Supervisor should be on the Login and his special view Home page')
def step_impl(context):
    driver: WebDriver = context.driver
    driver.get(
        "file:///C:/Users/adoko/Documents/Java%20Raveture%20notes/Project%20One/projectOneFrontEnd/homepage.html")
    sleep(5)


@given(u'The Department Head is  ready to login')
def step_impl(context):
    driver: WebDriver = context.driver
    driver.get(
        "file:///C:/Users/adoko/Documents/Java%20Raveture%20notes/Project%20One/projectOneFrontEnd/loginpage.html")
    sleep(5)


@when(u'The Department Head put in the username')
def step_impl(context):
    driver: WebDriver = context.driver
    WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.ID, 'username')))
    driver.find_element_by_id('username').send_keys("desty123")

    sleep(5)


@when(u'The Department Head put in  <passsword>')
def step_impl(context):
    driver: WebDriver = context.driver
    WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.ID, 'password')))
    driver.find_element_by_id('password').send_keys("desty")

    sleep(5)


@when(u'The Department Head clicks on the Login Button')
def step_impl(context):
    wiki_home: WikiHomePage = context.wiki_home_page
    wiki_home.Depthead_login().click()


@then(u'The Department Head should be on the Login anda Home page')
def step_impl(context):
    driver: WebDriver = context.driver
    driver.get(
        "file:///C:/Users/adoko/Documents/Java%20Raveture%20notes/Project%20One/projectOneFrontEnd/homepage.html")
    sleep(5)


@given(u'The Benco is  ready to login')
def step_impl(context):
    driver: WebDriver = context.driver
    driver.get(
        "file:///C:/Users/adoko/Documents/Java%20Raveture%20notes/Project%20One/projectOneFrontEnd/loginpage.html")
    sleep(5)


@when(u'The Benco put in the username')
def step_impl(context):
    driver: WebDriver = context.driver
    WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.ID, 'username')))
    driver.find_element_by_id('username').send_keys("derick123")

    sleep(5)


@when(u'The Benco put in the <passsword>')
def step_impl(context):
    driver: WebDriver = context.driver
    WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.ID, 'password')))
    driver.find_element_by_id('password').send_keys("derick1")

    sleep(5)


@when(u'The Benco clicks on the Login Button')
def step_impl(context):
    wiki_home: WikiHomePage = context.wiki_home_page
    wiki_home.benco_login().click()


@then(u'The Benco should be on the Login and a Home page')
def step_impl(context):
    driver: WebDriver = context.driver
    driver.get(
        "file:///C:/Users/adoko/Documents/Java%20Raveture%20notes/Project%20One/projectOneFrontEnd/homepage.html")
    sleep(5)


@given('The Employee is on the TRMS Home Page')
def TRMS(context):
    driver: WebDriver = context.driver
    driver.get('file:///C:/Users/adoko/Documents/Java%20Raveture%20notes/Project%20One/projectOneFrontEnd/loginpage.html')





@when(u'Employee types in the location')
def step_impl(context):
    driver: WebDriver = context.driver
    WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.ID, 'location')))
    driver.find_element_by_id('location').send_keys("West Virginia")

    sleep(5)


@when(u'Employee types in the Description')
def step_impl(context):
    driver: WebDriver = context.driver
    WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.ID, 'description')))
    driver.find_element_by_id('description').send_keys("Tuition form")

    sleep(5)

@when(u'Employee types in the grade format')
def step_impl(context):
    driver: WebDriver = context.driver
    WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.ID, 'grade')))
    driver.find_element_by_id('grade').send_keys("A+")

    sleep(5)

@when(u'Employee types in Event type')
def step_impl(context):
    driver: WebDriver = context.driver
    WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.ID, 'event')))
    driver.find_element_by_id('event').send_keys("University Course Event")

    sleep(5)

@when(u'Employee clicks on submit form button')
def step_impl(context):
    wiki_home: WikiHomePage = context.wiki_home_page
    wiki_home.submit_form().click()




# supervisor approval
@when(u'Superivisor is on the approval page')
def step_impl(context):
    driver: WebDriver = context.driver
    driver.get(
        "file:///C:/Users/adoko/Documents/Java%20Raveture%20notes/Project%20One/projectOneFrontEnd/homepage.html")
    sleep(5)



@when(u'Supervisor type in the Employee ID')
def step_impl(context):
    driver: WebDriver = context.driver
    WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.ID, 'emp_id')))
    driver.find_element_by_id('emp_id').send_keys("10")

    sleep(5)


@when(u'Supervisor clicks the Approval button')
def step_impl(context):
    wiki_home: WikiHomePage = context.wiki_home_page
    wiki_home.approve().click()

@then(u'The form is approved')
def step_impl(context):
    driver: WebDriver = context.driver
    driver.get(
        "file:///C:/Users/adoko/Documents/Java%20Raveture%20notes/Project%20One/projectOneFrontEnd/homepage.html")
    sleep(5)


# @when('The Employee clicks on login button')
# def nav_to_login(context):
#     wiki_home_page: WikiHomePage = context.wiki_home_page
#     wiki_home_page.login().click()
#
#
# @then('The Employee should be on the  login Page')
# def verify_on_login(context):
#     driver: WebDriver = context.driver
#     assert driver.title == "Tuition Reimbursement Service Management  App"
#         # End of first scnario
#
# @when('The Employee should type in username and password')
# def type_username_password(context):
#     # Can code either way, one provides IntelliSense
#     # wiki_home_page: WikiHomePage = context.wiki_home_page
#     # wiki_home_page.spanish().click()
#     context.wiki_home_page.spanish().click()
#
#
# @then('The User should be on the Spanish Home Page')
# def verify_on_spanish(context):
#     driver: WebDriver = context.driver
#     assert driver.title == "Wikipedia, la enciclopedia libre"
