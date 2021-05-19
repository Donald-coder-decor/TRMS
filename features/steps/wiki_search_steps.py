from behave import when, then
from selenium.webdriver.chrome.webdriver import WebDriver

from features.pages.wiki_home import WikiHomePage


# @when('The User types {marcdon} in the search bar')
# def type_into_searchbar(context, username):
#     wiki_home: WikiHomePage = context.wiki_home_page
#     wiki_home.login().send_keys(username)
#
#
# @when('The User clicks the search button')
# def press_search_button(context):
#     wiki_home: WikiHomePage = context.wiki_home_page
#     wiki_home.search_button().click()
#
#
# @then('The title should be {title}')
# def verify_title_page(context, title):
#     driver: WebDriver = context.driver
#     assert driver.title == title
