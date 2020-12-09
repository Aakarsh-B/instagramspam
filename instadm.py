from selenium import webdriver
import time

#navigating to instagram
driver = webdriver.Chrome()
driver.get('https://instagram.com')
time.sleep(3)


#logging in
username = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
username.send_keys('YOUR-USERNAME')
time.sleep(3)
password = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
password.send_keys('YOUR-PASSWORD')
time.sleep(3)
login = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')
login.click()
time.sleep(10)


#going to the dm of the desired person
driver.get('URL-OF-THE-PERSON-YOU-WANT-TO-SPAM')
time.sleep(7)
poorguy = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/div/button')
poorguy.click()
time.sleep(5)
notnow = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
notnow.click()

i=0
n=50 #increase this number to spam more times!

while i<n:
    i+=1
    chatbox = driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
    chatbox.send_keys('THE TEXT/MESSAGE YOU WISH TO SPAM')
    sendbtn = driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button')
    sendbtn.click()
driver.close()