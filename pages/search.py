from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class GoogleSearchPage:
    def __init__(self, browser):
        self.browser = browser

    def search(self, text):
        xpath = '//input[@name="q"]'
        search_input = self.browser.find_element_by_xpath(xpath)
        search_input.send_keys(text + Keys.RETURN)
