import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


@pytest.mark.parametrize("item",
                         [
                             "Xbox",
                             "Jewlery",
                             "Playstation",
                             "Books",
                             "Minimoog"
                         ])
@pytest.mark.regressiontest
def test_ebay_simple_search(browser, item):
    browser.get("https://www.ebay.com")
    browser.find_element(By.ID, 'gh-ac').send_keys(item + Keys.ENTER)
    assert item + ' for sale | eBay' == browser.title