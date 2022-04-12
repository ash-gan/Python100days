import pandas as pd
import datetime as dt
import random
import smtplib, ssl

letters = [1, 2, 3]
smtp_server = "smtp.gmail.com"
port = 465
sender = "bchange28@gmail.com"
password = "bethechange@1324"
context= ssl.create_default_context()
#----------------- get today's month and day -----------------------------#
d = pd.read_csv("birthdays.csv")
for i, j in d.iterrows():
    month = j["month"]
    day = j["day"]
    if month == dt.datetime.now().month and day == dt.datetime.now().day:
        letter = "letter_"+str(random.choice(letters))+".txt"
        with open(file="./letter_templates/"+letter, mode='r') as fr:
            letter_content = fr.read()
            new_content = letter_content.replace("[NAME]", j["name"])

        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender, password)
            server.sendmail(from_addr=sender, to_addrs=j["email"], msg=f"Subject:Happy Birthday\n\n{new_content}")







