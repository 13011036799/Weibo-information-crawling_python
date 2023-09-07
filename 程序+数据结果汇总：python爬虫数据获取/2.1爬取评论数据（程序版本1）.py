import emojiswitch
import requests
import csv
import time
from selenium import webdriver
from lxml import etree
import re
from selenium import webdriver
import emoji



with open('message4.csv', "a", encoding="gbk", newline="") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['用户名',  '帖子内容','留言用户名',  '留言时间', '留言内容'])
    f.close()


with open('every_post4.csv') as f:
    f=csv.DictReader(f)
    for row in f:
        web=row["具体微博网址"]
        print(web[2:47])

        driver = webdriver.Chrome()
        driver.implicitly_wait(10)  # 隐式等待，最长等20秒
        driver.get(web[2:47])

        time.sleep(15)

        user_name = driver.find_element_by_xpath(
            '/html/body/div/div[1]/div[2]/div[2]/main/div[1]/div/div[2]/article/div[2]/header/div[1]/div/div[1]/a/span')
        content = driver.find_element_by_xpath(
            '/html/body/div/div[1]/div[2]/div[2]/main/div[1]/div/div[2]/article/div[2]/div/div[1]/div')
        print(user_name.text)
        print(content.text)

        user_name = user_name.text
        content = content.text

        content = content.encode("gbk", "ignore")
        content = str(content, encoding='gbk')

        for g in range(100):
            try:
                for i in range(1):
                    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")  # 将滚动条调整至页面底部循环三次
                    time.sleep(1.5)

                driver.implicitly_wait(5)  # 隐式等待，最长等20秒

                for i in range(1, 120):
                    try:
                        all_path = '/html/body/div/div[1]/div[2]/div[2]/main/div/div/div[2]/div[2]/div[3]/div/div[3]/div/div/div[1]/div/div[1]/div'

                        messager = driver.find_element_by_xpath(all_path + '[' + str(i) + ']' + '/div/div/div/div[1]/div[2]/div[1]/a')
                        me_time= driver.find_element_by_xpath(all_path + '[' + str(i) + ']' +'/div/div/div/div[1]/div[2]/div[2]/div[1]')
                        message= driver.find_element_by_xpath(all_path + '[' + str(i) + ']' +'/div/div/div/div[1]/div[2]/div[1]/span')
                        print(messager.text)
                        print(me_time.text)
                        print(message.text)
                        messager = messager.text
                        me_time = me_time.text
                        message = message.text

                        message = message.encode("gbk", "ignore")
                        message = str(message, encoding='gbk')

                    except:
                        all_path = '/html/body/div/div[1]/div[2]/div[2]/main/div/div/div[2]/div[2]/div[3]/div/div[2]/div/div/div[1]/div/div[1]/div'

                        try:
                            messager = driver.find_element_by_xpath(
                                all_path + '[' + str(i) + ']' + '/div/div/div/div[1]/div[2]/div[1]/a')
                            me_time = driver.find_element_by_xpath(
                                all_path + '[' + str(i) + ']' + '/div/div/div/div[1]/div[2]/div[2]/div[1]')
                            message = driver.find_element_by_xpath(
                                all_path + '[' + str(i) + ']' + '/div/div/div/div[1]/div[2]/div[1]/span')
                            print(messager.text)
                            print(me_time.text)
                            print(message.text)
                            messager = messager.text
                            me_time = me_time.text
                            message = message.text

                            message = emoji.demojize(message)
                            message =emojiswitch.demojize(message,delimiters=("--","--"),lang="zh")

                            message = message.encode("gbk", "ignore")
                            message = str(message, encoding='gbk')

                        except:
                            break

                    # 储存进csv文件
                    with open('message4.csv', "a", encoding="gbk", newline="") as f:
                        csv_writer = csv.writer(f)
                        csv_writer.writerow([[user_name], [content], [messager], [me_time], [message]])
                        time.sleep(0.5)
                    f.close()

            except:
                break

        driver.quit()