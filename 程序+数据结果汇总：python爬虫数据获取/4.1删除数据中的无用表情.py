import csv

with open('all_de_emo.csv', "a", encoding="gbk", newline="") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['用户名', '帖子内容', '留言用户名', '留言时间', '留言内容'])
    f.close()

with open('all_re.csv') as f:
    f=csv.DictReader(f)
# print（f.loc[df['id'] == 1]）
    for row in f :
        if row["留言内容"] !="['']":
            # print(row)
            user_name=row["用户名"]
            content=row["帖子内容"]
            messager=row["留言用户名"]
            me_time=row["留言时间"]
            message=row["留言内容"]

            user_name = user_name.replace('[','')
            content = content.replace('[','')
            messager = messager.replace('[','')
            me_time = me_time.replace('[','')
            message = message.replace('[','')

            user_name = user_name.replace(']', '')
            content = content.replace(']', '')
            messager = messager.replace(']', '')
            me_time = me_time.replace(']', '')
            message = message.replace(']', '')

            user_name = user_name.replace("'", '')
            content = content.replace("'", '')
            messager = messager.replace("'", '')
            me_time = me_time.replace("'", '')
            message = message.replace("'", '')

            with open('all_de_emo.csv', "a", encoding="gbk", newline="") as f:
                csv_writer = csv.writer(f)
                csv_writer.writerow([[user_name], [content], [messager], [me_time], [message]])
            f.close()
