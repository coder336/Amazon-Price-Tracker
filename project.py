import requests

from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.in/Redmi-Note-Pro-Interstellar-Snapdragon/dp/B077PWBC78/ref=sr_1_1?dchild=1&keywords=redmi+9+pro&qid=1625844433&sr=8-1'
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

def check_price():
    page=requests.get(URL, headers = headers)
    soup=BeautifulSoup(page.content,'html.parser')
    title=soup.find(id="productTitle").get_text()
    print(title.strip())
    price=soup.find(id="priceblock_ourprice").get_text()
    p=int(price[2:4]+price[5:8])
    print(p)
    if(p<=13000):
        send_mail()
    else:
        print("Mail Not Sent! Price is High")
    
def send_mail():
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('','')
    subject="Price fell down"
    body="Check the link: https://www.amazon.in/Redmi-Note-Pro-Interstellar-Snapdragon/dp/B077PWBC78/ref=sr_1_1?dchild=1&keywords=redmi+9+pro&qid=1625844433&sr=8-1"
    msg=f"Subject: {subject}\n\n{body}"
    server.sendmail("chandler1837@gmail.com","subha113475@gmail.com",msg)
    print("Mail Sent")
    server.quit()

#while True:
check_price()
#time.sleep(60*60*24)
