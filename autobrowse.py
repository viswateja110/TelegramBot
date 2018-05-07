from selenium import webdriver
import time
browser = webdriver.Chrome(
    'C:\\Users\\venga\\Downloads\\chromedriver_win32\\chromedriver.exe')
browser.get('https://web.whatsapp.com/')
name = raw_input('enter the user name: ')
name = name.replace('\r', '')
msg = raw_input('enter msg: ')
msg = msg.replace('\r', '')
cnt = int(input('enter count:'))
raw_input('press any key to proceed after scanning qr')

# user = browser.find_element_by_xpath(
#   '//*[@id="pane-side"]/div/div/div/div[15]/div/div/div[2]/div[1]/div[1]/span')
user = browser.find_elements_by_xpath('//span[@title=\"'+name+'\"]')[0]
print user
user.click()

msgBox = browser.find_element_by_class_name('_2bXVy')

for i in range(cnt):
    msgBox.send_keys(msg+str(i))
    btn = browser.find_element_by_class_name('_2lkdt')
    btn.click()
