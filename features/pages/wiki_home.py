from selenium.webdriver.chrome.webdriver import WebDriver


class WikiHomePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def login(self):
        return self.driver.find_element_by_id('btntlogin')

    def login_password(self):
        return self.driver.find_element_by_id('username')

    def login_username(self):
        return self.driver.find_element_by_id('password')

    def Create_course(self):

        return self.driver.find_element_by_id('create')

    def approve(self):

        return self.driver.find_element_by_id('approved')

    def supervisor_login(self):
        return self.driver.find_element_by_id('btntlogin')

    def Depthead_login(self):
        return self.driver.find_element_by_id('btntlogin')

    def supervisor_login(self):
        return self.driver.find_element_by_id('btntlogin')

    def benco_login(self):
        return self.driver.find_element_by_id('btntlogin')

    def submit_form(self):
        return self.driver.find_element_by_id('submit')



