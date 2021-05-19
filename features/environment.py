from multiprocessing import context
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from features.pages.wiki_home import WikiHomePage


# All setup and teardown functions must go in this file.
# These functions must be named using behave's conventions
#from features.steps.wiki_lang_steps import driver


def before_all(context):
    # options = Options()
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')

    driver: WebDriver = webdriver.Chrome(
        "C:/Users/adoko/Documents/2104-python-java-wvu/chromedriver.exe")

    wiki_home_page = WikiHomePage(driver)

    context.driver = driver
    context.wiki_home_page = wiki_home_page
    print("started")


def after_all(context):
    context.driver.quit()
    print("ended")
# try:
#     # 'C:/Users/adoko/Desktop/2104-python-java-wvu/chromedriver.exe', chrome_options=options)
#     driver.get("file:///C:/Users/adoko/Documents/Java%20Raveture%20notes/Project%20One/projectOneFrontEnd/index.html")
#     sleep(2)
#     #wiki_home_page.login().click()
#     assert "Welcome to Tuition Reimbursement Service Management  App @revature" == driver.title
# except AssertionError:
#     print("Login page not found")
# else:
#     print("Test Passed- No assertion failed")
# finally:
#     sleep(3)
    #driver.close()
