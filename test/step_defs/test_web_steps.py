# Import
from pytest_bdd import scenarios, when, then, parsers
from pages.result import GoogleResultPage
from pages.search import GoogleSearchPage
# import for Applitools Visual Verification
from test.automated_visual_verification.conftest import eyes, open_eyes, validate_window, close_eyes


# Scenarios
scenarios('../features/GoogleHomePage.feature', example_converters=dict(phrase=str))


# When Steps
@when(parsers.parse('I click "{text}"'))
def click_link(browser, text):
    xpath = "//a[contains(text(),'%s')]" % text
    link = browser.find_element_by_xpath(xpath)
    link.click()


@when(parsers.parse('I click "{text}" button'))
def click_google_app(browser, text):
    xpath = '//a[@*="%s"]' % text
    link = browser.find_element_by_xpath(xpath)
    link.click()


@when(parsers.parse('I click "{text}" icon'))
def click_icon(browser, text):
    browser.switch_to.frame(browser.find_element_by_xpath('//iframe[@role="presentation"]'))
    xpath = '//span[contains(text(),"%s")]/..' % text
    link = browser.find_element_by_xpath(xpath)
    link.click()
    browser.switch_to.default_content()


@when(parsers.parse('I search for "<phrase>" text'))
def text_search(browser, phrase):
    search_input = GoogleSearchPage(browser)
    search_input.search(phrase)


# Then Steps
@then(parsers.parse('I am redirected to the Google "{phrase}" page'))
def redirect_image(browser, phrase, eyes):
    xpath = "//div[@class='logo-subtext']/span"
    expected_text = phrase.lower()
    element = browser.find_element_by_xpath(xpath)
    assert element.text == expected_text
    validate_window(browser, eyes, tag='Google_Image_page')


@then(parsers.parse('title is correct on the "{phrase}" page'))
@then(parsers.parse('title is correct on the "<phrase>" page'))
def check_title(browser, phrase,):
    result_page = GoogleResultPage(browser)
    assert phrase.lower() in result_page.title().lower()


@then(parsers.parse('I redirected to the "{phrase}" page(Gmail)'))
def redirect_gmail(browser, phrase, eyes):
    xpath = "//*[contains(@class,'header--desktop')]//span[@class='h-c-header__product-logo-text']"
    expected_text = phrase
    element = browser.find_element_by_xpath(xpath)
    assert element.text.lower() == expected_text.lower()
    validate_window(browser, eyes, tag='Gmail_page')


@then(parsers.parse('I redirected to the "{phrase}" page(Sign In)'))
def redirect_sign_in(browser, phrase, eyes):
    xpath = "//*[@id='headingText']"
    expected_text = phrase
    element = browser.find_element_by_xpath(xpath)
    assert element.text.lower() == expected_text.lower()
    validate_window(browser, eyes, tag='SignIn_page')


@then(parsers.parse('I redirected to the "{phrase}" page(How Google Search works)'))
def redirect_google_search(browser, phrase, eyes):
    xpath = '//h2[@class="h-c-headline h-c-headline--two content-animate content-animation"]'
    expected_text = phrase
    element = browser.find_element_by_xpath(xpath)
    assert element.text.lower() == expected_text.lower()
    validate_window(browser, eyes, tag='How_Google_search_works_page')


@then(parsers.parse('the results with "<phrase>" shown'))
def search_results(browser, phrase, eyes):
    xpath = '//div[@class="r"]'
    link_list = browser.find_element_by_xpath(xpath)
    assert len(link_list.find_elements_by_xpath(xpath)) > 0
    xpath = '//input[@name="q"]'
    search_input = browser.find_element_by_xpath(xpath)
    assert search_input.get_attribute('value').lower() == phrase.lower()
    validate_window(browser, eyes, tag='Search_result_page')


@then(parsers.parse('I can see Google "{phrase}"'))
def redirect_account(browser, phrase, eyes):
    xpath = '//span[@class="h-c-header__product-logo-text"]'
    expected_text = phrase
    element = browser.find_element_by_xpath(xpath)
    assert element.text.lower() == expected_text.lower()
    validate_window(browser, eyes, tag='Google_account_page')
