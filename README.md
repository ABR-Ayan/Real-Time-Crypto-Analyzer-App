# Real-Time-Crypto-Analyzer-App

This Streamlit application utilizes OpenAI's ChatGPT model to provide technical analysis for selected cryptocurrencies based on their price data from the last 7 days.

# Functionality
Cryptocurrency Selection: Choose a cryptocurrency from the dropdown list to analyze. Options include Bitcoin, Ethereum, Bitcoin Cash, BNB, XRP, Cardano, Solana, Polkadot, Litecoin, and Avalanche.

Analysis Generation: Upon selecting a cryptocurrency, the application fetches the price data for the chosen cryptocurrency and generates a technical analysis request for ChatGPT.

ChatGPT Response: ChatGPT generates a detailed technical analysis based on the provided price data. The analysis includes a price overview, moving averages, Relative Strength Index (RSI), Moving Average Convergence Divergence (MACD), and advice/suggestions on whether to buy or sell.

# Usage
To run the application, make sure you have Python installed along with the required dependencies specified in requirements.txt. Then execute the following command:

streamlit run chatgpt_crypto_analyzer.py

The application will open in your default web browser, allowing you to interact with it.

# Dependencies
OpenAI's ChatGPT
Streamlit
Requests
JSON

# Disclaimer
This application is for educational and demonstration purposes only. The cryptocurrency market is highly volatile, and any investment decisions should be made after thorough research and consideration of risks. The technical analysis provided by ChatGPT does not constitute financial advice.
