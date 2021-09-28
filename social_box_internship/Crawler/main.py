from lxml import html
import requests

res = requests.get('https://www.yellowpages.vn')
print(type(res),res)

tree = None
if res.status_code == 200:
    tree = html.fromstring(res.content)
    print(res.content)
if tree is not None:
    category_link = tree.xpath('//div[@style="height:auto; width:160px; margin-top:28px; float:left"]//a/@href')

    print(category_link)