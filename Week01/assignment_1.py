#安装并使用 requests、bs4 库，爬取猫眼电影的前 10 个电影名称、电影类型和上映时间，
#并以 UTF-8 字符集保存到 csv 格式的文件中。
import requests
from bs4 import BeautifulSoup as bes
import pandas as pd

myurl = 'https://maoyan.com/films?showType=3'
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
cookie = '__mta=175996573.1601115841806.1601130101762.1601130106025.5; uuid_n_v=v1; uuid=64841150FFE211EA93DE532F8E87605B62378236FD7C44339D053BBA80413B31; _csrf=2882796b1f46a46898ced6092b0b411a5008cbf56901b30c704b1fd2353b56d4; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1601115842; _lxsdk_cuid=174c9f0e499c8-0a51c427553373-316b7004-384000-174c9f0e499c8; _lxsdk=64841150FFE211EA93DE532F8E87605B62378236FD7C44339D053BBA80413B31; mojo-uuid=79332338cf7baffd7fa2090816dfea73; mojo-session-id={"id":"53bfb5ad95492aff20ec6655737690cc","time":1601129800198}; mojo-trace-id=6; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1601131627; __mta=175996573.1601115841806.1601130106025.1601131626865.6; _lxsdk_s=174cac587be-f9e-857-569%7C%7C14'
header = {'user-agent':user_agent, 'cookie':cookie}
response = requests.get(myurl,headers=header)
bs_info = bes(response.text, 'html.parser')

result = []
for tags in bs_info.find_all('div', attrs={'class': 'movie-hover-info'},limit=10):
    more_info = tags.select('div.movie-hover-title')
    mname = more_info[0].find('span', attrs={'class': 'name'}).text
    mtype = more_info[1].contents[2].strip()
    mtime = more_info[3].find('span', attrs={'class': 'hover-tag'}).next_sibling.strip()
    result.append({'电影名称':mname, '电影类型':mtype, '上映时间':mtime})

print(result)
movie_info = pd.DataFrame(data = result)
movie_info.to_csv('./movie.csv', encoding='utf8', index=False, header=True)

    # for atag in tags.find_all('span'):
    # print(result)
    # print(mname)
    # print(mtype)
    # print(mtime)
    # print(mname[0].contents[0].text)
    # atag.find('span')[0].select()