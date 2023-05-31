# -*- coding = utf-8 -*-
# @Time : 2023/4/25 21:12
# @Author : 陈保罗
# @File : JavaSE-Spider.py
# @Software : PyCharm


from bs4 import BeautifulSoup
import re
import urllib.request, urllib.error
import xlwt
import sqlite3


def main():
    posturl = "/package-summary.html"  # 列表网址后缀
    # print(baseurl + posturl)
    packagelist = getpacklist(contenturl, baseurl)  # 获取所有包的列表
    # for i in range(0, len(packagelist)):
    #     # print(i, packagelist[i])
    #     getinterfacelist(packagelist[i])
    print(IFlink)




baseurl = "https://docs.oracle.com/javase/8/docs/api/"  # 列表网址前缀
contenturl = "https://docs.oracle.com/javase/8/docs/api/overview-summary.html"  # 目录网址
findtitle = re.compile(r'<span>(.*?)</span>', re.S)
findlink = re.compile(r'<a href="(.*?)">', re.S)
findIFname = re.compile(r'<a href=.*">(.*?)</a>', re.S)
findIFlink = re.compile(r'<a href="(.*?)"', re.S)

IFname = []
IFlink = []


def getpacklist(contenturl, baseurl):
    packagelist = []
    html = askURL(contenturl)
    soup = BeautifulSoup(html, "html.parser")
    for item in soup.find_all('td', class_="colFirst"):
        item = str(item)
        link = baseurl + re.findall(findlink, item)[0]
        packagelist.append(link)
    # print(packagelist)
    return packagelist


def getinterfacelist(packageurl):
    html = askURL(packageurl)
    soup = BeautifulSoup(html, "html.parser")
    for table in soup.find('table', class_="typeSummary"):
        for item in table.find_all('td', class_="colFirst"):
            item = str(item)
            templink = re.findall(findIFlink, item)[0]
            templink = baseurl + templink.replace('../', '')
            IFlink.append(templink)
            tempname = re.findall(findIFname, item)[0]
            IFname.append(tempname)

    return 0

def getIFdata(IFurl):
    html = askURL(IFurl)
    soup = BeautifulSoup(html, "html.parser")

    return 0


def askURL(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
    }
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")  # 解码
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr((e, "reason")):
            print(e.reason)

    return html


if __name__ == '__main__':
    main()
