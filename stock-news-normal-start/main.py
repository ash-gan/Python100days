import requests
import datetime as dt
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
ACCOUNT_SID = "ACe535d3f0aa798cd3cf6de337fcad8c95"
AUTH_TOKEN = "34728e1e2fc5dd4265af556cefed8ff4"
client = Client(ACCOUNT_SID, AUTH_TOKEN)


STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

parameters = {"function": "TIME_SERIES_DAILY",
              "symbol": STOCK_NAME,
              "outputsize": "full",
              "apikey":"S5F4FSK404HMV764"}

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
#TODO 2. - Get the day before yesterday's closing stock price
#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
resp = requests.get(url=STOCK_ENDPOINT, params=parameters)
resp.raise_for_status()
data = resp.json()
series_daily_data = data["Time Series (Daily)"]
stdt = [value for (key,value) in series_daily_data.items()]
previous_day_closing = stdt[0]["4. close"]
day_before_previous = stdt[1]["4. close"]
per_change = ((float(previous_day_closing) - float(day_before_previous))/float(day_before_previous))*100

## STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
news_url = "https://newsapi.org/v2/everything"
current_date = dt.datetime.now()
news_params = {"q": COMPANY_NAME,
                "from": str(current_date).split(" ")[0],
                "sortBy": "popularity",
               "apiKey": "945b1f022c2040799ba605707da1fe29"}

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

news_resp = requests.get(url=news_url, params=news_params)
news_resp.raise_for_status()
news_data = news_resp.json()
latst_3 = news_data["articles"][:3]
## STEP 3: Use twilio.com/docs/sms/quickstart/python
#to send a separate message with each article's title and description to your phone number.
#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
#TODO 9. - Send each article as a separate message via Twilio.
mess_to = [{"title":item["title"],"description":item["description"]} for item in latst_3]

#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
if per_change > 0:
    ICON = "🔺"
else:
    ICON = "🔻"
for news_message in mess_to:
    text = f"""
            TSLA: {ICON}{abs(per_change)}
            Headline: {news_message["title"]}
            Brief: {news_message["description"]}
     """
    print(text)
    # message = client.messages \
    #              .create(
    #                      body=text,
    #                      from_='+14847302090',
    #                      to='+16462561464'
    #                    )
