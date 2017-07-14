#coding: utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from lxml import etree
# import requests
import time
import sys
import os

driver = webdriver.PhantomJS('/home/bixiang/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')
driver.get("https://bbs.byr.cn/index")
time.sleep(1)
elem = driver.find_element_by_name("id")
elem.send_keys("*********")
elem = driver.find_element_by_name("passwd")
elem.send_keys("**********")
time.sleep(1)
login = driver.find_element_by_id("b_login")
ActionChains(driver).click(login).perform()
time.sleep(5)

# https://bbs.byr.cn/#!board/JobInfo
driver.get("https://bbs.byr.cn/#!article/JobInfo/post")
time.sleep(1)

subject = driver.find_element_by_id("post_subject")
subject.send_keys(u'''中国科学院软件研究所招聘数据挖掘工程师''')

content = driver.find_element_by_id("post_content")
content.send_keys(u'''任职条件：
全职：
1.至少两年相关工作经验；
2.有机器学习、数据挖掘实际项目工作经验者优先；
3.熟练运用Mysql、Oracle或mongodb等数据库操作；
4.至少熟悉一门脚本语言；
5.熟练运用C/C++或Java者优先；
6.有信用评价系统相关算法经验者优先。
7.有个人技术博客者优先

实习生：
1.博士生、硕士生或大三已保研本科生；
2.硕士生实习需获导师同意；
3.至少实习3个月，每周最少4天。

岗位职责：
负责海量文本数据的处理分析； 
负责金融及风控方向数据挖掘实际项目算法研究；
​负责NLP方向算法研究与实现；''')

submit = driver.find_element_by_css_selector("input.button")
ActionChains(driver).click(submit).perform()

driver.close()
