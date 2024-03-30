import openai
import time
import json
import requests
import streamlit as st

# secret authentication key
openai.api_key = "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"


# function for connecting with chatGPT
def basicGeneration (prompt):
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=[{"role": "user", "content": prompt}])
    return completion.choices[0].message.content


# function to get the desired coin's universally unique identifier
def find_coin_uuid(coin):
    coin_url = "https://api.coinranking.com/v2/search-suggestions?query="+coin

    headers = {
        "X-RapidAPI-Key": "a6bc36fc95msh0ef03736585c550p109736jsnb603baf0af30",
        "X-RapidAPI-Host": "coinranking1.p.rapidapi.com"
    }
        
    response1 = requests.request("GET", coin_url, headers=headers)

    # Parse the response data as a JSON object
    JSONResult1 = json.loads (response1.text)
    # extracting the uuid field from the JSON response
    for i in JSONResult1["data"]["coins"]: 
        if i["name"] == option:
            return i["uuid"]
        else:
            print("Coin not found.")


# returns coin data
def getCryptoPrice(uuid):

    url = "https://coinranking1.p.rapidapi.com/coin/"+uuid+"/history"

    querystring = {"referenceCurrencyUuid":"yhjMzLPhuIDl","timePeriod":"7d"}

    headers = {
        "X-RapidAPI-Key": "a6bc36fc95msh0ef03736585c550p109736jsnb603baf0af30",
        "X-RapidAPI-Host": "coinranking1.p.rapidapi.com"
    }

    response2 = requests.request("GET", url, headers=headers, params=querystring)
    # Parse the response data as a JSON object
    JSONResult2 = json.loads (response2.text)
    # Extract the "history" field from the JSON response
    history = JSONResult2["data"]["history"]
    # Extract the "price" field from each element in the "history" array and add to a list
    prices = []
    for change in history:
        prices.append(change["price"])
    # Join the list of prices into a comma-separated string pricesList = ','.join(prices)
    priceList = ','.join(prices)
    # Return the comma-separated string of prices
    return priceList


# Designing the User Interface
st.title("ChatGPT Crypto Analyzer") 
st.subheader("Use ChatGPT to keep track of the crypto world")

option = st.selectbox( 'Choose cryptocurrency for analysis',
                    ('Bitcoin', 'Ethereum', 'Bitcoin Cash',
                    'BNB', 'XRP', 'Cardano', 'Solana',
                    'Polkadot', 'Litecoin', 'Avalanche'))

# storing selected coin uuid
coin_uuid = find_coin_uuid(option)

with st.spinner("Getting "+option+" Prices..."):

    # generating data of desired crypto currency
    coin_data = getCryptoPrice(coin_uuid)

with st.spinner("Analyzing "+option+" Prices..."):

    prompt = f"""You are an expert crypto trader with more than 10 years of experience,
            I will provide you with a list of {option} prices for the last 7 days
            can you provide me with a technical analysis
            of {option} based on these prices. here is what I want:
            Price Overview,
            Moving Averages,
            Relative Strength Index (RSI),
            Moving Average Convergence Divergence (MACD),
            Advice and Suggestion,
            Do I buy or sell?
            Please be as detailed as much as you can, and explain in a way any beginner can understand.
            Here is the price list: {coin_data}"""

    # generating response from chatgpt
    analysis = basicGeneration(prompt)
    st.success("Done!")
    time.sleep(1)
    # setting the dimensions of the text area
    st.text_area("Analysis", analysis, height = 500)