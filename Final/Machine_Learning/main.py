import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# def get_mean_volume(symbol):
#     """Return the mean volume for stock indicated by symbol."""

#     df = pd.read_csv("stocks/{}.csv".format(symbol))
#     return df['Volume'].mean()


# def get_max_close(symbol):
#     """Return the maximum closing value for stock indicated by symbol. """

#     df = pd.read_csv("stocks/{}.csv".format(symbol))
#     return df['Close'].max()


def test_run():
    start_date = '2010-01-22'
    end_date = '2010-01-26'
    dates = pd.date_range(start_date, end_date)

    # Create an empty dataframe
    df1 = pd.DataFrame(index=dates)
    # Read SPY data into temporary dataframe
    dfSPY = pd.read_csv("stocks/SPY.csv", index_col="Date",
                        parse_dates=True, usecols=["Date", "Close"], na_values=['nan'])
    # Join the two dataframes
    df1 = df1.join(dfSPY)
    df1.dropna(inplace=True)
    print(df1)


if __name__ == "__main__":
    test_run()
