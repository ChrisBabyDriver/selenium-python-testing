import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

@pytest.mark.regressiontest
def test_ebay_car_search(browser):
    browser.get("https://www.ebay.com/")
    WebDriverWait(browser, 10).until(EC.title_is("Electronics, Cars, Fashion, Collectibles & More | eBay"))
    assert 'Electronics, Cars, Fashion, Collectibles & More | eBay' == browser.title
    browser.find_element(By.NAME, '_nkw').send_keys("Lexus")
    element = WebDriverWait(browser,15).until(EC.presence_of_element_located((By.XPATH, '//a[@aria-label="lexus rx350 in Auto Parts & Accessories"]')))
    browser.find_element(By.NAME, '_nkw').click()
    element.click()
    WebDriverWait(browser, 10).until(EC.title_is("Lexus Rx350 in Parts & Accessories for sale | eBay"))
    assert 'Lexus Rx350 in Parts & Accessories for sale | eBay' == browser.title





