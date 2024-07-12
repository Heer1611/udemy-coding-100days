import requests
from twilio.rest import Client

# Configuration
VIRTUAL_TWILIO_NUMBER = ""  # Your virtual Twilio number
VERIFIED_NUMBER = ""  # Your own phone number verified with Twilio

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = ""  # Your Alpha Vantage API key
NEWS_API_KEY = ""  # Your News API key
TWILIO_SID = ""  # Your Twilio account SID
TWILIO_AUTH_TOKEN = ""  # Your Twilio Auth Token

# Step 1: Use Alpha Vantage to get daily stock data
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]

# Get yesterday's closing stock price
yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data["4. close"])
print(f"Yesterday's Closing Price: {yesterday_closing_price}")

# Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = float(day_before_yesterday_data["4. close"])
print(f"Day Before Yesterday's Closing Price: {day_before_yesterday_closing_price}")

# Find the positive difference between yesterday and the day before yesterday
difference = yesterday_closing_price - day_before_yesterday_closing_price
up_down = "🔺" if difference > 0 else "🔻"

# Work out the percentage difference in price
diff_percent =round( (difference / day_before_yesterday_closing_price) * 100,2)
print(f"Percentage Difference: {diff_percent}%")

# Step 2: Get news articles if the percentage difference is greater than 5%
if abs(diff_percent) > 5:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

    # Get the first 3 articles
    three_articles = articles[:3]

    # Step 3: Use Twilio to send a separate message with each article's title and description
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    # Create a new list of the first 3 article's headline and description
    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

    # Send each article as a separate message via Twilio
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=VIRTUAL_TWILIO_NUMBER,
            to=VERIFIED_NUMBER
        )
        print(f"Message sent with SID: {message.sid}")

