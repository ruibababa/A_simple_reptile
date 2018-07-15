from urllib.request import urlopen
import re


def getNovelContent():

    html = urlopen(url="http://www.quanshuwang.com/book/44/44683").read()   # 获取网站源代码。
    html = html.decode("gbk")   # 编译源代码，避免出现乱码。
    urls = re.findall(r'<li><a href="(.*?)" title=".*?">(.*?)</a></li>', html)  # 找到关键数据（正则匹配）。
    for url in urls:

        novel_url = url[0]  # 网址
        novel_title = url[1]    # 每节的章节名
        novel_content = urlopen(url=novel_url).read()   # 读取每章的内容。
        novel_content = novel_content.decode("gbk")       # 编译，避免乱码
        # print(novel_content)
        text = re.findall(r'</script>&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<script type="text/javascript">', novel_content, re.S)
        # 上面的那段代码是找到文章的内容，re.S相当于".",作用是匹配除“\n”以外的任何字符
        content = text[0].replace("&nbsp;&nbsp;&nbsp;&nbsp;", "")  # 清洗数据，把没有必要的数据除掉
        content = content.replace("<br />", "")   # 清洗数据，把没有必要的数据除掉
        with open(r'C:\Users\lenovo\Desktop\文档\web\novel\{}.txt'.format(novel_title), 'w', encoding='gbk') as f:
            f.write(content)

        f.close()       # 写入自己的文档。

getNovelContent()
