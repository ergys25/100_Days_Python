import smtplib
import datetime as dt
import random

email = "@gmail.com"
password = ""

now = dt.datetime.now()
hour = now.hour
if hour == 8:
    with open("Day 32\\quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=email, password=password)
    connection.sendmail(from_addr=email, to_addrs="@gmail.com", msg=quote)
    connection.close()
