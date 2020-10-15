import requests
from bs4 import BeautifulSoup
import smtplib

URL = ' https://www.amazon.com/Sony-Full-Frame-Mirrorless-Interchangeable-Lens-ILCE7M3/dp/B07B43WPVK/ref=sr_1_3?dchild=1&keywords=sony+a7&qid=1598901849&sr=8-3'

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15'}


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()

    print(title)

    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = price[0:5]

    print(price)

    if (price < 1,700.00) :
        send_email()
    elif (price > 1,700.00):
        send_email()



def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 554)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('bazoungoula26@gmail.com', 'xrwkudtjvjmoygje')

    subject = "Hey the price fell down"
    body = " Check the Amazon link https://www.amazon.com/Sony-Full-Frame-Mirrorless-Interchangeable-Lens-ILCE7M3/dp/B07B43WPVK/ref=sr_1_3?dchild=1&keywords=sony+a7&qid=1598901849&sr=8-3 "

    msg = f"Subject:{subject}\n, \n, {body}"

    server.sendmail(
        'bazoungoula26@gmail.com'
        'nsinganimusic@gmail.com',
        msg

    )

    server.quit()
print("Hey email has been sent")










