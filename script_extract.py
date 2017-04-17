import urllib.request
import re
import MySQLdb
import requests
from bs4 import BeautifulSoup


def get_single_item_data(item_url):
    para=""
    i=0
    source_code=requests.get(item_url)
    plain_text =source_code.text
    soup=BeautifulSoup(plain_text)
    for item_name in soup.find_all('p'):

            para=para+str(item_name.get_text())
    return para

bdd= MySQLdb.connect("127.0.0.1","root","","browser_online",use_unicode=True, charset="utf8")
fir= bdd.cursor()

fir.execute("SELECT link_indefine_link FROM  link_undefine where link_indefine_link not like '%.gif%' or link_indefine_link not like '%.css%' or link_indefine_link not like '%.pdf%' or link_indefine_link not like '%.txt%' or link_indefine_link not like '%.xml%' or link_indefine_link not like '%.jx%' or link_indefine_link not like '%.png%' or link_indefine_link not like '%.jpg%' or link_indefine_link not like '%.jpeg%'  order by link_indefine_id asc limit 1 ")
for url in fir.fetchone():
    url=url

fir.execute("delete  from link_undefine  where link_indefine_link= '"+url+"'")

reg1="[name|property]=[\"'][og:]*?description[\"'] content=[\"']([a-zA-Z0-9À-ÿ _&#?;*\-:\/.!\"',+]*)[\"']"
reg3="<title[a-zA-Z0-9 \"' _.=-]*>(.*?)</title>"
reg11=reg1.encode(encoding='UTF-8')

off_htmlcode=urllib.request.urlopen(url)
off_htmlcode=off_htmlcode.read()

des_htmlcode=re.compile(reg11)
des_htmlcode=re.findall(des_htmlcode, off_htmlcode)

tit_htmlcode= re.compile("<title[a-zA-Z0-9-é \"' _.=-]*>(.*?)</title>", re.IGNORECASE|re.DOTALL)
tit_htmlcode=tit_htmlcode.search(off_htmlcode.decode("utf-8")).group(1)
desc=""
tit=""
for desc in des_htmlcode:
    desc=desc
    tit=tit_htmlcode
print (tit)
fir.execute("delete  from link_define  where link_define_link like '"+url+"'")
bdd.commit()

print(get_single_item_data(url+desc.decode('utf-8')))

fir.execute("INSERT into link_define(link_define_link,link_define_titl, link_define_desc) values(%s, %s, %s)",(url,tit,get_single_item_data(url+desc.decode('utf-8'))))

bdd.commit()

fir.close()
