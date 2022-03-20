import time
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


options = webdriver.ChromeOptions()

#options.add_argument("--incognito")
options.add_argument("log-level=3")
user_data_dir = os.path.abspath("selenium_data")
options.add_argument(f"user-data-dir={user_data_dir}")
driver = webdriver.Chrome(options=options, executable_path="chromedriver.exe")
captcha_xpath = "//*[@id=\"checkcapchamodelyii-captcha-image\"]"
time.sleep(1)  # Waits for chrome to finish initializing

url_list = [
	"https://gomovies-online.cam/watch-film/hotel-transylvania-transformania/CCdjX5V7/LZupB3PP-online-for-free.html",
	"https://gomovies-online.cam/watch-film/encanto/dsHoOcry/NBiEkI2Y-online-for-free.html",
	"https://gomovies-online.cam/watch-film/the-matrix-resurrections/sBRaSOyh/6vX83o4Q-online-for-free.html",
	"https://gomovies-online.cam/watch-film/dont-look-up/NpCMyts4/F8AfXkOk-online-for-free.html",
	"https://gomovies-online.cam/watch-film/dune-2021/Y22d0PzC/sMhqqCVF-online-for-free.html",
	"https://gomovies-online.cam/watch-film/ghostbusters-afterlife/zYO1mqp7/TRmyHHI0-online-for-free.html",
]

def wait_until_element(stratagy, locator, timeout=10):
	wait = WebDriverWait(driver, timeout)
	element = wait.until(
		EC.presence_of_element_located(
			(
				stratagy, locator
			)
		)
	)

	return element

def screenshot_captcha():
	try:
		wait_until_element(By.XPATH, captcha_xpath)
		# time.sleep(0.1)
		driver.find_element_by_xpath(captcha_xpath).screenshot(f"captchas/captcha{i+1}.png")
		driver.delete_cookie("advanced-frontendgomovies7")
		driver.refresh()
	except WebDriverException:
		screenshot_captcha()



for url in url_list:
		driver.get(url)

for i in range(2000):
	screenshot_captcha()
