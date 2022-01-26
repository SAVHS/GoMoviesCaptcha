from selenium import webdriver
import time
import os

options = webdriver.ChromeOptions()

#options.add_argument("--incognito")
options.add_argument("log-level=3")
user_data_dir = os.path.abspath("selenium_data")
options.add_argument(f"user-data-dir={user_data_dir}")
driver = webdriver.Chrome(options=options, executable_path='chromedriver.exe')

captcha_xpath = '//*[@id="checkcapchamodelyii-captcha-image"]' 
time.sleep(1)
for i in range(3):
	for j in range(3):
		driver.get("https://gomovies-online.cam/watch-film/encanto/dsHoOcry/NBiEkI2Y-online-for-free.html")
		driver.get("https://gomovies-online.cam/watch-film/hotel-transylvania-transformania/CCdjX5V7/LZupB3PP-online-for-free.html")
	time.sleep(2)
	element = driver.find_element_by_xpath(captcha_xpath).screenshot(f"captcha{i}.png");

