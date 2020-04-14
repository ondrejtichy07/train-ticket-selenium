import time
import settings as s
from selenium import webdriver

browser = webdriver.Chrome(executable_path=s.chromedriver_path)
browser.get('https://www.cd.cz')

#first screen cd.cz
browser.find_element_by_id('csbhp-from').send_keys(s.from_station)
browser.find_element_by_id('csbhp-to').send_keys(s.to_station)
browser.find_element_by_css_selector('.cd-btn-green.smallmagnify.flr').click()
time.sleep(1.5)

#second screen cd.cz
browser.find_element_by_css_selector('.buybut.green').click()
time.sleep(1.5)

#third screen cd.cz
browser.find_element_by_xpath('//*[@id="content_left"]/div[2]/div[1]/div[1]/div[2]/button').click()
time.sleep(1.5)

#fourth screen cd.cz
browser.find_element_by_xpath('//*[@id="main"]/section/div[1]/div/button').click()
time.sleep(1.5)

#fifth screen cd.cz
browser.find_element_by_id('cardName').send_keys('Ondřej Tichý')
browser.find_element_by_xpath('//*[@id="main"]/section/div[1]/form/div[2]/ul/li/input').send_keys(s.phone_num)
browser.find_element_by_xpath('//*[@id="main"]/section/div[1]/button').click()
time.sleep(1.5)

#sixth screen cd.cz
browser.find_element_by_id('email').send_keys(s.email)
browser.find_element_by_xpath('//*[@id="paymentInfo"]/div[9]/div[1]/form/label/span[1]').click()
browser.find_element_by_xpath('//*[@id="paymentInfo"]/div[9]/div[2]/form/label/span[1]').click()
browser.find_element_by_xpath('//*[@id="paymentInfo"]/div[13]/button[1]').click()
time.sleep(1.5)

#bank
browser.find_element_by_xpath('//*[@id="cardnumber"]').send_keys(s.card_num)
time.sleep(1.5)
browser.find_element_by_xpath('//*[@id="expiry"]').send_keys(s.exp)
time.sleep(1.5)
browser.find_element_by_xpath('//*[@id="cvc"]').send_keys(s.cvv)
browser.find_element_by_xpath('//*[@id="pay-submit"]').click()

#quit
time.sleep(180)
browser.quit()