import time
import os
from selenium import webdriver

options = webdriver.ChromeOptions()

#options.add_argument("--incognito")
options.add_argument("log-level=3")
user_data_dir = os.path.abspath("selenium_data")
options.add_argument(f"user-data-dir={user_data_dir}")
driver = webdriver.Chrome(options=options, executable_path="chromedriver.exe")
time.sleep(1)  # Waits for chrome to finish initializing


url_list = [
	"https://gomovies-online.cam/watch-film/hotel-transylvania-transformania/CCdjX5V7/LZupB3PP-online-for-free.html",
	"https://gomovies-online.cam/watch-film/encanto/dsHoOcry/NBiEkI2Y-online-for-free.html",
	"https://gomovies-online.cam/watch-film/the-matrix-resurrections/sBRaSOyh/6vX83o4Q-online-for-free.html",
	"https://gomovies-online.cam/watch-film/dont-look-up/NpCMyts4/F8AfXkOk-online-for-free.html",
	"https://gomovies-online.cam/watch-film/dune-2021/Y22d0PzC/sMhqqCVF-online-for-free.html",
	"https://gomovies-online.cam/watch-film/ghostbusters-afterlife/zYO1mqp7/TRmyHHI0-online-for-free.html",
]

captcha_xpath = "//*[@id=\"checkcapchamodelyii-captcha-image\"]"
for i in range(3):
	for url in url_list:
		driver.get(url)
	time.sleep(2)
	element = driver.find_element_by_xpath(captcha_xpath).screenshot(f"captcha{i}.png")
