import csv

# with open('all.csv', "a", encoding="gbk", newline="") as f:
#     csv_writer = csv.writer(f)
#     csv_writer.writerow(['用户名', '帖子内容', '留言用户名', '留言时间', '留言内容'])
#     f.close()

with open('盲人火炬手/message4.csv') as f:
    f=csv.DictReader(f)
    for row in f:
        user_name=row["用户名"]
        user_name = user_name.replace('[','')
        user_name = user_name.replace(']', '')
        user_name = user_name.replace("'", '')
        # print(user_name)

        content = row["帖子内容"]
        content = content.replace('[', '')
        content = content.replace(']', '')
        content = content.replace("'", '')
        # print(content)

        messager = row["留言用户名"]
        messager = messager.replace('[', '')
        messager = messager.replace(']', '')
        messager = messager.replace("'", '')
        # print(messager)

        me_time=row["留言时间"]
        me_time = me_time.replace('[', '')
        me_time = me_time.replace(']', '')
        me_time = me_time.replace("'", '')
        # print(me_time)

        message = row["留言内容"]
        message = message.replace('[', '')
        message = message.replace(']', '')
        message = message.replace("'", '')
        # print(message)

        with open('all.csv', "a", encoding="gbk", newline="") as k:
            csv_writer = csv.writer(k)
            csv_writer.writerow([[user_name], [content], [messager], [me_time], [message]])
            k.close()