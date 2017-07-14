#coding: utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from lxml import etree
# import requests
import time
import sys
import os

driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
driver.get("https://bbs.byr.cn/index")
time.sleep(1)
elem = driver.find_element_by_name("id")
elem.send_keys("***********")
elem = driver.find_element_by_name("passwd")
elem.send_keys("***********")
time.sleep(1)
login = driver.find_element_by_id("b_login")
ActionChains(driver).click(login).perform()
time.sleep(5)

# https://bbs.byr.cn/#!board/JobInfo
driver.get("https://bbs.byr.cn/#!article/test/post")
time.sleep(1)

subject = driver.find_element_by_id("post_subject")
subject.send_keys("test_subject")

content = driver.find_element_by_id("post_content")
content.send_keys("test_content")

submit = driver.find_element_by_css_selector("input.button")
ActionChains(driver).click(submit).perform()

