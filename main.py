from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import smtplib


# Function that sends a mail when called
def send_mail():
    # Setting up the server
    server = smtplib.SMTP("smtp.gmail.com")

    # Establishing connection by saying ehlo(Extended-Hello)
    server.ehlo()

    # Starting the server
    server.starttls()

    # Establishing connection again
    server.ehlo()

    # Logging in to the email from which the mail should be sent
    server.login("your email id", "password")  # Replace the text with your email ID and password

    # Subject of the mail
    subject = f"Change in price of {product_title}"
    # Body of the mail
    body = f"Hey, take a look at {link}. \n\nThe price has changed from {prev_price} to {cur_price}."

    # Combining both the subject and body as a single message for convenience in future
    msg = f'Subject : {subject}\n\n\n\n{body}'

    # Sending the mail
    server.sendmail("from email id", "to email id", msg)  # Replace the from and to address respectively
    print("Mail has been sent!")

    # Quitting the server
    server.quit()

# changing the options so that selenium runs in the background
option = Options()
option.add_argument("--headless")

# Importing the chrome web driver and setting the option to run it in the background
driver = webdriver.Chrome("chromedriver.exe", chrome_options=option)


# Link of the product (You can change the link to any product in amazon.in)
link = "https://www.amazon.in/New-Apple-iPhone-12-128GB/dp/B08L5TNJHG/ref=sr_1_1_sspa?crid=3QNK6CZPVV849&dchild=1&keywords=iphone+12&qid=1607063305&sprefix=iphon%2Caps%2C317&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzSUswSERaSlgzSVdVJmVuY3J5cHRlZElkPUEwMjQzNTk4MkVDTVhXRUlOVTlIVyZlbmNyeXB0ZWRBZElkPUEwMzI0NDAwMUZXTThSRlVWWEZBUyZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="

# To open up the link provided above
driver.get(link)

# Getting the Product Name
product_title = driver.find_element_by_xpath('//*[@id="productTitle"]').text
print(product_title)

# Getting the current price of the product
prev_price = driver.find_element_by_xpath('//*[@id="priceblock_ourprice"]').text[2:]
print(prev_price)

# while loop is used so that the code will be running for ever
while True:

    #Getting the price of the product again
    product_price = driver.find_element_by_xpath('//*[@id="priceblock_ourprice"]').text

    # Assigning the cur_price so that the rupees symbol wont be an issue in the future
    cur_price = product_price[2:]

    # Checking if there's a change in the price
    if prev_price != cur_price:
        print(cur_price)

        # Calling the send_mail function to send the mail
        send_mail()

        # Assigning the prev_price as cur_price so that the code checks if there's a change in new price
        prev_price = cur_price
