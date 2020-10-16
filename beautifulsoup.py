import bs4
import requests
import io
response=requests.get('http://nghiahsgs.com/')
html_doc=response.text
file=open('code.html','a',encoding='utf-8')
file.write(html_doc)
soup=bs4.BeautifulSoup(html_doc,'html.parser')
eles=soup.select('style')
for ele in eles:
    print(ele.get_text())