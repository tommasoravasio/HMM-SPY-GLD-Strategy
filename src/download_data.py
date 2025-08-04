import yfinance as yf
import pandas as pd
import os

def download_data(tickers, start_date, end_date, filepath):
    """
    Downloads historical stock data for the given tickers and saves it to a CSV file.

    Args:
        tickers (list): A list of stock tickers.
        start_date (str): The start date for the data in 'YYYY-MM-DD' format.
        end_date (str): The end date for the data in 'YYYY-MM-DD' format.
        filepath (str): The path to save the CSV file.
    """
    data = yf.download(tickers, start=start_date, end=end_date, auto_adjust=True)
    data = data[['Close']]
    data.columns = tickers
    data.to_csv(filepath)
    print(f"Data downloaded and saved to {filepath}")

if __name__ == "__main__":
    # Define the tickers and the date range
    TICKERS = ['SPY', 'GLD']
    START_DATE = '2000-01-01'
    END_DATE = pd.to_datetime('today').strftime('%Y-%m-%d')

    # Define the output file path
    OUTPUT_FILEPATH = os.path.join('data', 'spy_gld.csv')

    # Create the data directory if it doesn't exist
    os.makedirs(os.path.dirname(OUTPUT_FILEPATH), exist_ok=True)

    # Download the data
    download_data(TICKERS, START_DATE, END_DATE, OUTPUT_FILEPATH)
