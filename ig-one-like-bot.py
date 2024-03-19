# Drake Sorkhab, March 2024

import time # For a pause with time.sleep()
import getpass # For a hidden password input through getpass.getpass()

# Selenium tools
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

# This function will find an element then spam-click it until it is successfully clicked once
def spammer(driver,xpath):
	element = None
	while not element:
		try:
			element = driver.find_element("xpath",xpath)
		except:
			pass

	while True:
		try:
			element.click()
			break
		except:
			pass

# This function will find an element then spam-click it until it is successfully clicked once AND doesn't stop till it's no longer clickable 
def spammer_till_gone(driver,xpath):

	element = None
	while not element:
		try:
			element = driver.find_element("xpath",xpath)
		except:
			pass

	while True:
		try:
			element.click()
			break
		except:
			pass
	while True:
		try:
			element.click()
		except:
			break

# This function will find an element then enter keys into it (text entry)
def spam_keys(driver,xpath,keys):
	element = None
	while not element:
		try:
			element = driver.find_element("xpath",xpath)
		except:
			pass
	element.send_keys(keys)



# This function opens up a Chrome tab and attempts to submit a survey with the parameters as the survey options
def execute_browser_tasks(username, password):

	if len(password) < 6:
		exit("Password must be 6+ characters.")
	
	# Make the browser headless and set the URL
	options = webdriver.ChromeOptions() ; options.headless = True ; url = "https://www.instagram.com/"

	# Initialise the driver used by Selenium
	driver = webdriver.Chrome()
	
	# Load the webpage
	driver.get(url)

	# Log in with username, password, and "Log in" button click
	spam_keys(driver, r"""//*[@id="loginForm"]/div/div[1]/div/label/input""" , username)
	spam_keys(driver, r"""//*[@id="loginForm"]/div/div[2]/div/label/input""" , password)
	spammer_till_gone(driver,r"""//*[@id="loginForm"]/div/div[3]/button/div""")

	# Get rid of "Save info" message
	spammer(driver, r"""/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/section/div/button""")

	# Get rid of "Notifications" message
	spammer(driver, r"""/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]""")

	time.sleep(100)


	





execute_browser_tasks("drake_sorkhav",getpass.getpass())
	