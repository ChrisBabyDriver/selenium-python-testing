import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

@pytest.mark.regressiontest
def test_ebay_motors (browser):
    browser.get("https://www.ebay.com/")
    WebDriverWait(browser, 10).until(EC.title_is("Electronics, Cars, Fashion, Collectibles & More | eBay"))
    assert 'Electronics, Cars, Fashion, Collectibles & More | eBay' == browser.title
    browser.find_element(By.LINK_TEXT,'Motors').click()
    assert 'eBay Motors: Auto Parts and Vehicles | eBay' == browser.title
    complete = Select(browser.find_element(By.NAME,'Make'))
    complete.select_by_visible_text('Aston Martin')
    model = Select(browser.find_element(By.NAME,'Model'))
    model.select_by_visible_text('DB11')
    zip = browser.find_element(By.NAME,'_stpos')
    zip.clear()
    zip.send_keys("21209")
    browser.find_element(By.CLASS_NAME, 'motors-finder__find-btn').click()