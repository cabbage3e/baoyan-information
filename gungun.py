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

