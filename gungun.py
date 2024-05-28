# # -*- coding: UTF-8 -*-
# import os
# import time
# import requests
# from bs4 import BeautifulSoup
# from openpyxl import Workbook
#
#
# url = f'http://pc.baoyanwang.com.cn/articles?category=%E4%BF%9D%E7%A0%94%E4%BF%A1%E6%81%AF'
#
# header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
#                         'Chrome/112.0.0.0 Safari/537.36',
#           'cookie': '__yjs_duid=1_b1ac9fc87dce4de5552d7cf0924fb4981686228951567; u=b0281776fd75d3eefeb3562b2a5e6534; '
#                     '__bid_n=1889b14047a51b2b754207; '
#                     'FPTOKEN=qU+ieOMqkW6y6DlsOZ+D/T'
#                     '+SCY6yS3dYvGXKibFoGBijKuUuSbc3ACFDzjlcC18wuDjNLENrw4ktAFAqnl3Akg492Lr4fbvNrkdJ'
#                     '/ZQrluIdklkNDAKYnPrpcbe2H9y7AtX+/b+FCTkSTNv5+qB3OtQQ3BXXsEen72oEoAfK+H6'
#                     '/u6ltZPdyHttJBJiXEDDS3EiUVt+S2w+8ozXENWbNt/AHeCgNUMmdeDinAKCR+nQSGK/twOoTLOU/nxBeSAazg'
#                     '+wu5K8ooRmW00Bk6XAqC4Cb829XR3UinZHRsJxt7q9biKzYQh'
#                     '+Yu5s6EHypKwpA6RPtVAC1axxbxza0l5LJ5hX8IxJXDaQ6srFoEzQ92jM0rmDynp+gT'
#                     '+3qNfEtB2PjkURvmRghGUn8wOcUUKPOqg==|mfg5DyAulnBuIm/fNO5JCrEm9g5yXrV1etiaV0jqQEw=|10'
#                     '|dcfdbf664758c47995de31b90def5ca5; PHPSESSID=18397defd82b1b3ef009662dc77fe210; '
#                     'Hm_lvt_de3f6fd28ec4ac19170f18e2a8777593=1686322028,1686360205; '
#                     'history=cid%3A2455%2Ccid%3A2476%2Ccid%3A5474%2Ccid%3A5475%2Ccid%3A2814%2Cbid%3A3667; '
#                     'Hm_lpvt_de3f6fd28ec4ac19170f18e2a8777593=1686360427'}
#
# response = requests.get(url, headers=header)
#
# time.sleep(0.01)# print(response)
#
# # 获取网页信息#
# soup = BeautifulSoup(response.content, 'lxml')
# soup = BeautifulSoup(response.content, 'html.parser')
# print(soup)# 解析网页数据#
# tr_tags = soup.find('div', class_="md_1009 modelbox tcenter").get_text()
# tr_tags = soup.find_all('div', class_="md_1009 modelbox tcenter")
# print(tr_tags)
#
# # 循环遍历获取tr标签下的td标签文本
# td_tags = soup.select('tr td')
# for i in range(0, len(td_tags), 2):
#     school_name = td_tags[i].get_text()
#     address = td_tags[i + 1].get_text()
#     score = td_tags[i + 2].get_text()
#     time.sleep(0.1)
#     print(f'正在爬取：--{school_name}--{address}--')    # 将数据项转换为一个元组
#     row = (school_name, address)    # 将数据行写入 Excel 表格
#     ws.append(row)
#


# import requests
# from bs4 import BeautifulSoup
# import csv
#
# # 目标URL
# url = "http://pc.baoyanwang.com.cn/articles?category=%E4%BF%9D%E7%A0%94%E4%BF%A1%E6%81%AF"
#
# header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
#                         'Chrome/125.0.0.0 Safari/537.36',
#           'cookie': 'baoyan-token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbGllbnRfaWQiOjY0ODIzLCJyb2xlIjoidXNlciIsImV4cCI6MTcxOTQ3ODYyMSwiaXNzIjoieWFuZ2tldGFuZyJ9.SYhq50Skj_qdstG4NcQo7iqOQ36hw83Kq8jeiMreSgc'}
#
# # 发送HTTP请求
# response = requests.get(url, headers=header)
# response.encoding = 'utf-8'
#
# # 确认请求成功
# if response.status_code == 200:
#     # 解析HTML内容
#     soup = BeautifulSoup(response.content, 'html.parser')
#
#     # 找到翻页元素
#     pagination = soup.find('ul', class_='el-pager')
#     if pagination:
#         # 找到当前活动页面
#         active_page = pagination.find('li', class_='active')
#         current_page = int(active_page.text.strip())
#
#         # 打开CSV文件，准备写入
#         with open('info.csv', mode='w', newline='', encoding='utf-8') as file:
#             writer = csv.writer(file)
#             # 写入CSV文件的表头
#             writer.writerow(['Title', 'Registration Time'])
#
#             # 构建当前页的URL
#             current_url = f"{url}&page={current_page}"
#             # 发送HTTP请求
#             current_response = requests.get(current_url)
#
#             # 确认请求成功
#             if current_response.status_code == 200:
#                 # 解析HTML内容
#                 current_soup = BeautifulSoup(current_response.content, 'html.parser')
#
#                 # 查找所有包含目标信息的<div>标签
#                 articles = current_soup.find_all('div', class_='article')
#
#                 for article in articles:
#                     # 查找目标<a>标签及其标题
#                     title_tag = article.find('a', class_='article-title')
#                     if title_tag:
#                         title = title_tag.text.strip()  # 提取标题
#
#                         # 查找报名时间的<div>标签
#                         time_tag = article.find('div', class_='article-start-time')
#                         if time_tag:
#                             registration_time = time_tag.text.strip().replace("报名时间：", "")  # 提取并清理报名时间文本
#
#                             # 写入CSV文件
#                             writer.writerow([title, registration_time])
#             else:
#                 print(f"Failed to retrieve the webpage {current_url}. Status code: {current_response.status_code}")
#     else:
#         print("Pagination element not found.")
# else:
#     print(f"Failed to retrieve the webpage {url}. Status code: {response.status_code}")
#
# print("Data extraction completed.")

# import requests
# from bs4 import BeautifulSoup
# import csv
#
# # 目标URL
# url = "http://pc.baoyanwang.com.cn/articles?category=%E4%BF%9D%E7%A0%94%E4%BF%A1%E6%81%AF"
# header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
#                         'Chrome/125.0.0.0 Safari/537.36',
#           'cookie': 'baoyan-token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbGllbnRfaWQiOjY0ODIzLCJyb2xlIjoidXNlciIsImV4cCI6MTcxOTQ3ODYyMSwiaXNzIjoieWFuZ2tldGFuZyJ9.SYhq50Skj_qdstG4NcQo7iqOQ36hw83Kq8jeiMreSgc'}
#
# # 发送HTTP请求
# response = requests.get(url, headers=header)
# response.encoding = 'utf-8'
# print(response.text)
#
# # 确认请求成功
# if response.status_code == 200:
#     # 解析HTML内容
#     soup = BeautifulSoup(response.content, 'html.parser')
#
#
#     # 打开CSV文件，准备写入
#     with open('articles.csv', mode='w', newline='', encoding='utf-8') as file:
#         writer = csv.writer(file)
#         # 写入CSV文件的表头
#         writer.writerow(['Title', 'Registration Time'])
#
#         # 查找所有包含目标信息的<div>标签
#         articles = soup.find_all('div', class_='article')
#
#         for article in articles:
#             # 查找目标<a>标签及其标题
#             title_tag = article.find('a', class_='article-title')
#             if title_tag:
#                 title = title_tag.text.strip()  # 提取标题
#
#                 # 查找报名时间的<div>标签
#                 time_tag = article.find('div', class_='article-start-time')
#                 if time_tag:
#                     registration_time = time_tag.text.strip().replace("报名时间：", "")  # 提取并清理报名时间文本
#
#                     # 写入CSV文件
#                     writer.writerow([title, registration_time])
# else:
#     print(f"Failed to retrieve the webpage. Status code: {response.status_code}")



# from bs4 import BeautifulSoup
# import csv
# from selenium import webdriver
#
# def get_page_content():
#     url = "http://pc.baoyanwang.com.cn/articles?category=%E4%BF%9D%E7%A0%94%E4%BF%A1%E6%81%AF"
#     driver_path = "C:\Program Files\Google\Chrome\Application\chromedriver.exe"  # 需要替换为你的 Chrome WebDriver 路径
#     options = webdriver.ChromeOptions()
#     options.add_argument("--headless")  # 无头模式，不打开浏览器界面
#     options.add_argument("--disable-gpu")
#     driver = webdriver.Chrome(executable_path=driver_path, options=options)
#     driver.get(url)
#     page_content = driver.page_source
#     driver.quit()
#     return page_content
#
# # 假设你已经获取了完整的 HTML 内容并存储在变量 html_content 中
# html_content = get_page_content()
#
#
# # 使用 BeautifulSoup 解析 HTML 内容
# soup = BeautifulSoup(html_content, 'html.parser')
#
# # 打开 CSV 文件准备写入数据
# with open('info.csv', 'w', newline='', encoding='utf-8') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['School', 'Department', 'Registration Time', 'Description'])  # 写入 CSV 文件的标题行
#
#     # 查找所有类为 article 的 div 元素
#     articles = soup.find_all('div', class_='article')
#     for article in articles:
#         # 查找目标 <a> 标签及其标题
#         title_tag = article.find('a', class_='article-title')
#         if title_tag:
#             title = title_tag.text.strip()  # 提取标题
#             school, department = title.split("——", 1)  # 使用 "——" 进行分割，最多分割一次
#
#             # 查找报名时间的 <div> 标签
#             time_tag = article.find('div', class_='article-start-time')
#             if time_tag:
#                 registration_time = time_tag.text.strip().replace("报名时间：", "")  # 提取并清理报名时间文本
#                 start_time, end_time = registration_time.split("~")
#
#             # 找到文章描述的 div 标签
#             article_desc_tag = article.find('div', class_='article-desc')
#             if article_desc_tag:
#                 article_desc = article_desc_tag.text.strip()
#                 # 写入 CSV 文件
#                 writer.writerow([school.strip(), department.strip(), start_time, end_time, article_desc])
#
# print("Data written to articles.csv")

from bs4 import BeautifulSoup
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_page_content(url):
    options = webdriver.ChromeOptions() # 需要安装ChromeDriver并配置系统环境变量
    options.add_argument("--headless")  # 无头模式，不打开浏览器界面
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    return driver

def parse_page(driver):
    page_content = driver.page_source
    soup = BeautifulSoup(page_content, 'html.parser')

    # 查找所有类为 article 的 div 元素
    articles = soup.find_all('div', class_='article')
    for article in articles:
        # 查找目标 <a> 标签及其标题
        title_tag = article.find('a', class_='article-title')
        if title_tag:
            title = title_tag.text.strip()  # 提取标题
            if "——" in title:
                school, department = title.split("——", 1)  # 使用 "——" 进行分割，最多分割一次
            else:
                school = title
                department = ""

            # 查找报名时间的 <div> 标签
            time_tag = article.find('div', class_='article-start-time')
            if time_tag:
                registration_time = time_tag.text.strip().replace("报名时间：", "")  # 提取并清理报名时间文本
                start_time, end_time = registration_time.split("~")

            # 找到文章描述的 div 标签
            article_desc_tag = article.find('div', class_='article-desc')
            if article_desc_tag:
                article_desc = article_desc_tag.text.strip()
                # 写入 CSV 文件
                writer.writerow([school.strip(), department.strip(), start_time, end_time, article_desc])

def click_next_page(driver):
    try:
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'btn-next'))
        )
        next_button.click()
        return True
    except:
        return False

# 打开 CSV 文件准备写入数据
with open('info.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['School', 'Department', 'Start Time', 'End Time', 'Description'])  # 写入 CSV 文件的标题行

    # 初始页面
    url = "http://pc.baoyanwang.com.cn/articles?category=%E4%BF%9D%E7%A0%94%E4%BF%A1%E6%81%AF" #保研信息网的网址
    driver = get_page_content(url)
    parse_page(driver)

    # 点击下一页并获取内容，最多点击次数可选（这里是30次）
    for _ in range(30):
        if click_next_page(driver):
            # 等待新页面加载完成
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'article')))
            parse_page(driver)
        else:
            break

    print("Data written to info.csv")

# 关闭浏览器
driver.quit()

