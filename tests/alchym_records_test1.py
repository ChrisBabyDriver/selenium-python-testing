import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = ChromeService(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)
browser.maximize_window()
browser.get("https://alhymrecords.com/")
time.sleep(5)
assert 'Alhym' == browser.title
assert 'https://alhymrecords.com/' == browser.current_url
time.sleep(5)
browser.find_element(By.LINK_TEXT, 'RELEASES').click()
time.sleep(3)
assert 'Releases Grid – Boxed – Alhym' == browser.title
assert 'https://alhymrecords.com/releases-grid-boxed/' == browser.current_url
time.sleep(3)
header=browser.find_element(By.CLASS_NAME, 'ekinox-title')
assert 'RELEASES GRID – BOXED'== header.text
time.sleep(3)
