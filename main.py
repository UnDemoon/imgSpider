import urllib.request
import re
import os
import urllib

#   获取网页内容
def get_html(url):
    page = urllib.request.urlopen(url)
    html_a = page.read()
    return html_a.decode('utf-8')

#   下载图片
def get_img(filepath, html):
    reg = r'https://[^\s]*?\_r.jpg'
    imgre = re.compile(reg)  # 转换成一个正则对象
    imglist = imgre.findall(html)  # 表示在整个网页过滤出所有图片的地址，放在imgList中
    x = 0        # 声明一个变量赋值
    path = filepath  # 设置图片的保存地址
    if not os.path.isdir(path):
        os.makedirs(path)  # 判断没有此路径则创建
    imglist = list(set(imglist))
    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl, os.path.join(path, str(x)+'.jpg'))  # 打开imgList,下载图片到本地
        x = x + 1
        print('图片开始下载，注意查看文件夹')
    return imglist

if __name__ == '__main__':
    url = 'https://www.zhihu.com/question/267536123/answer/855562769'
    filepath = './downloads'
    html_b = get_html(url)
    get_img(filepath, html_b)
