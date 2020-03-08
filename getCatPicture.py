import os
import re
import time

import requests

cat_picture_list = []


# 获取猫图表情包链接
def getCat(url):
    try:
        header = {
            'Host': 'www.fabiaoqing.com',
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
        }
        response = requests.request('get', url, headers=header).text
        cat_picture_list = re.findall(r' data-original="(http://\S+.jpg)', response)
        for i in cat_picture_list:
            #发现第一次下载的缩略图
            i = i.replace('bmiddle', 'large')
            downCarPicture(i)
    except Exception as e:
        print(e)
        pass

# 传入链接下载图片
def downCarPicture(link):
    picture = requests.get(link)
    file_name = 'Picture//'+link.split('/')[-1]
    print('download...', file_name)
    with open(file_name, 'wb+') as f:
        f.write(picture.content)


# 输入需要几页的猫图
def getLink(num):
    for page in range(1, num + 1):
        print('开始下载第%d页' % page)
        url = f"https://www.fabiaoqing.com/search/search/keyword/%E7%8C%AB%E5%92%AA/type/bq/page/{page}.html"
        getCat(url)
        time.sleep(3)
    print("下载完成~")

if __name__  == '__main__':
    #页面猫的表情最多77页
    if os.path.exists('Picture'):
        getLink(77)
    else:
        os.mkdir("Picture")
        getLink(77)
