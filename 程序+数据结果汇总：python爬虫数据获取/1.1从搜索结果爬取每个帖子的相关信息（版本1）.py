import requests
import csv
import time
from selenium import webdriver
from lxml import etree

url='https://s.weibo.com/weibo?q=%E7%9B%B2%E4%BA%BA%E7%82%B9%E7%87%83%E5%86%AC%E6%AE%8B%E5%A5%A5%E4%B8%BB%E7%81%AB%E7%82%AC&page=1'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0',
    'Cookie':'UOR=www.228.com.cn,widget.weibo.com,login.sina.com.cn; SINAGLOBAL=2088087647028.1885.1638210812366; ULV=1648355156837:5:1:1:6266296310407.26.1648355156712:1640994025082; ALF=1684634883; SCF=Ap0cLm9XYH-Xi6nhSBG8IHsQkyF9o2fJevua_1z-xb6dfg39Qmgk-vf1SPDTzhsqe5J8RO7vqd_2CgKcrpWWdtc.; _s_tentry=data.weibo.com; Apache=6266296310407.26.1648355156712; WBtopGlobal_register_version=2022051208; SSOLoginState=1652314568; SUB=_2A25PjDnVDeRhGeFL6lUR9ivJzTqIHXVs-CwdrDV8PUNbmtAKLW3VkW9NQnE_KlKG-nPq-efh73l-5LELsFLavLB9; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFGrOpA7_EbLRRfXYBaX5_45JpX5KMhUgL.FoMfeKM7So-fSoq2dJLoIEXLxKBLBo.L1-qLxK-L1-eLBKnLxKBLBo.L12eLxKqL1h.L1KnLxK.L1hzLBKqt'
    }
# 打开浏览器——目标网址
res=requests.get(url,headers=headers)
res=etree.HTML(res.content)

with open('every_post4.csv', "a", encoding="gbk", newline="") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['用户名', '用户id', '发帖时间', '微博内容', '具体微博网址'])
    f.close()

all_path='/html/body/div[1]/div[2]/div/div[2]/div[1]/div[2]/div'
# 1.用户名、用户id
for i in range(1,4):
    user_name=res.xpath(all_path+'['+str(i)+']'+'/div[2]/div[1]/div[2]/div[1]/div[2]/a/text()')
    # user_name = res.xpath(all_path + '[' + str(i) + ']' + '/div/div[1]/div[2]/div[1]/div[2]/a/text()')
    user_name =str(user_name[0])
    # user_name =user_name.replace('[','')
    # user_name = user_name.replace("'", "")
    # user_name = user_name.replace(']', '')
    print(user_name)

    user_link = res.xpath(all_path +'['+str(i)+']'+ '/div[2]/div[1]/div[2]/div[1]/div[2]/a/@href')
    # user_link = res.xpath(all_path + '[' + str(i) + ']' + '/div/div[1]/div[2]/div[1]/div[2]/a/@href')
    user_link ='https:'+str(user_link[0])
    print(user_link)

    # 获取mid值、用户id,构建每条微博的网址web=https://weibo.com/用户id/mid值
    user_id = str(user_link[18:28])
    mid = res.xpath(all_path + '[' + str(i) + ']' + '/@mid')
    mid = str(mid[0])
    web = 'https://weibo.com/' + user_id + '/' + mid
    print(web)

    post_time=res.xpath(all_path+'['+str(i)+']'+'/div[2]/div[1]/div[2]/p[1]/a[1]/text()')
    # post_time=res.xpath(all_path+'['+str(i)+']'+'/div/div[1]/div[2]/p[1]/a[1]/text()')
    post_time=str(post_time[0])
    post_time=post_time.replace(' ','')
    post_time=post_time.replace(r'\n','')
    print(post_time)

    post_content=res.xpath(all_path+'['+str(i)+']'+'/div[2]/div[1]/div[2]/p[3]/text()')
    # post_content=res.xpath(all_path+'['+str(i)+']'+'/div/div[1]/div[2]/p[3]/text()')
    if post_content == []:
        post_content = res.xpath(all_path + '[' + str(i) + ']' + '/div[2]/div[1]/div[2]/p[2]/text()')
        # post_content = res.xpath(all_path + '[' + str(i) + ']' + '/div/div[1]/div[2]/p[2]/text()')
        for e in post_content:
            post_content = e.encode("gbk", "ignore")
            post_content = str(post_content, encoding='gbk')
            result = ''
            for q in post_content:
                result += q
                result = result.replace(' ', '')
                result = result.replace(r'\n', '')
            print(result)
    else:
        for w in post_content:
            post_content = w.encode("gbk", "ignore")
            post_content = str(post_content, encoding='gbk')
            result = ''
            for p in post_content:
                result += p
                result = result.replace(' ', '')
                result = result.replace(r'\n', '')
            print(result)

    # 储存进csv文件
    with open('every_post4.csv', "a", encoding="gbk", newline="") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow([[user_name],[user_link],[post_time],[result],[web]])
        time.sleep(0.5)
    f.close()

    time.sleep(2)


for j in range(5, 24):
    # user_name=res.xpath(all_path+'['+str(j)+']'+'/div[2]/div[1]/div[2]/div[1]/div[2]/a/text()')
    user_name = res.xpath(all_path + '[' + str(j) + ']' + '/div/div[1]/div[2]/div[1]/div[2]/a/text()')
    user_name = str(user_name[0])
    print(user_name)

    # user_link = res.xpath(all_path +'['+str(j)+']'+ '/div[2]/div[1]/div[2]/div[1]/div[2]/a/@href')
    user_link=res.xpath(all_path+'['+str(j)+']'+'/div/div[1]/div[2]/div[1]/div[2]/a/@href')
    user_link = 'https:' + str(user_link[0])
    print(user_link)
    # time.sleep(2)

    # 获取mid值、用户id,构建每条微博的网址web=https://weibo.com/用户id/mid值
    user_id = str(user_link[18:28])
    mid = res.xpath(all_path + '[' + str(j) + ']' + '/@mid')
    mid = str(mid[0])
    web = 'https://weibo.com/' + user_id + '/' + mid
    print(web)

    # post_time=res.xpath(all_path+'['+str(j)+']'+'/div[2]/div[1]/div[2]/p[1]/a[1]/text()')
    post_time = res.xpath(all_path + '[' + str(j) + ']' + '/div/div[1]/div[2]/p[1]/a[1]/text()')
    post_time = str(post_time[0])
    post_time = post_time.replace(' ', '')
    post_time = post_time.replace(r'\n', '')
    print(post_time)

    # post_content=res.xpath(all_path+'['+str(j)+']'+'/div[2]/div[1]/div[2]/p[3]/text()')
    post_content = res.xpath(all_path + '[' + str(j) + ']' + '/div/div[1]/div[2]/p[3]/text()')
    if post_content == []:
        # post_content = res.xpath(all_path + '[' + str(j) + ']' + '/div[2]/div[1]/div[2]/p[2]/text()')
        post_content = res.xpath(all_path + '[' + str(j) + ']' + '/div/div[1]/div[2]/p[2]/text()')
        for e in post_content:
            post_content = e.encode("gbk", "ignore")
            post_content = str(post_content, encoding='gbk')
            result = ''
            for q in post_content:
                result += q
                result = result.replace(' ', '')
                result = result.replace(r'\n', '')
            print(result)
    else:
        for w in post_content:
            post_content = w.encode("gbk", "ignore")
            post_content = str(post_content, encoding='gbk')
            result = ''
            for p in post_content:
                result += p
                result = result.replace(' ', '')
                result = result.replace(r'\n', '')
            print(result)

    # 储存进csv文件
    with open('every_post4.csv', "a", encoding="gbk", newline="") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow([[user_name], [user_link], [post_time], [result], [web]])
        time.sleep(0.5)
    f.close()

    time.sleep(2)
