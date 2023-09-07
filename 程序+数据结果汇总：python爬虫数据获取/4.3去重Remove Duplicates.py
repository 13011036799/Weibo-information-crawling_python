import shutil
import pandas as pd


frame=pd.read_csv('all.csv',engine='python')
data = frame.drop_duplicates(subset=['用户名','留言用户名','留言内容'], keep='first', inplace=False)
data.to_csv('all_re.csv', encoding='utf8')


# data.drop_duplicates(subset=['A','B'],keep='first',inplace=True)
