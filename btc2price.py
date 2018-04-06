import time
import smtplib
from contextlib import suppress
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome('C:\\Users\\themi\\Desktop\\chromedriver_win32\\chromedriver.exe')
driver.get('https://www.huobipro.com/coin_coin/exchange/#eth_btc')
time.sleep(2)
previous_price=1
current_price=1
while True:
    time.sleep(2)
    try:
        assert 'BTC' in driver.title
    except:
        print('error: BTC not asserted')
    time.sleep(2)
    try:
        content=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.CLASS_NAME,"ticker_close")))
    except:
        print('error: Content Not Found')
    previous_price=current_price
    #sleep function is forbidden here, because once sleeped for several seconds, the variable 'content' changed, so original content is different form current content, thus error will occur.
    current_price=float(content.text)
    fluctuation=((current_price-previous_price)/previous_price)
    print(fluctuation)
    time.sleep(10)

