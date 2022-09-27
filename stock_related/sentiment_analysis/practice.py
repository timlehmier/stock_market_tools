from typing_extensions import dataclass_transform
from textblob import TextBlob
import sys
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import nltk
import re
import string


zm_tweets = pd.read_csv(
    '../stock_market_tools/stock_related/data/df_twitter_ticker_symbols.csv')

df_tweets = pd.DataFrame(zm_tweets, columns=["Date", "User", "Tweet"])
print(df_tweets)
