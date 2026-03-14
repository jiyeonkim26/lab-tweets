#!/usr/bin/python3

import csv

file_name = 'tweets_01-08-2021.csv'

keywords = [
    "trump",
    "obama",
    "mexico",
    "russia",
    "fake news",
    "china",
    "hillary",
    "media",
    "rigged"
]

counts = {i:0 for i in keywords}

all_tweets = []

with open(file_name, 'r', newline='', encoding= 'utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter= ',')
    for row in reader:
        for tweet in row:
            all_tweets.append(tweet)

total_tweets = len(all_tweets)
print('total tweets:', total_tweets)

for tweet in all_tweets:
    text = tweet.lower()
    for keyword in keywords:
        if keyword in text:
            counts[keyword] += 1

print(counts)

# for markdown table
percent_tweets = {key: (value / total_tweets) * 100 for (key, value) in counts.items()}
for keyword in sorted(keywords):
    print(f"| {keyword:>17} | {percent_tweets[keyword]:05.2f} |")

key_list = list(percent_tweets.keys())
percent_list = list(percent_tweets.values())

list_percent_tweets = list(percent_tweets.items())
print(list_percent_tweets)

print("| phrase            | percent of tweets |")
print("| ----------------- | ----------------- |")

for keyword in sorted(keywords):
    print(f"| {keyword:>17} | {percent_tweets[keyword]:<18}|")


import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = {'keyword': key_list, 'percent': percent_list}
df = pd.DataFrame(data)
df_sorted = df.sort_values('percent', ascending=True)

plt.bar(df_sorted['keyword'], df_sorted['percent'])
plt.xlabel("Tweets by Trump")
plt.ylabel("Percent of Tweets")
plt.title("What is Trump Tweeting?")
plt.show()
