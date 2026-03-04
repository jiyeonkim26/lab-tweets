#!/usr/bin/python3

import json
import zipfile
import glob

files = glob.glob("condensed_trump_tweet_data_archive/condensed_*.json")
print(files)

all_tweets = []

for file_path in files:
    with open(file_path, "r", encoding="utf-8") as f:
        each_file = json.load(f)
        for tweet in each_file:
            all_tweets.append(tweet["text"])

print("Total tweets:", len(all_tweets))

keywords = [
    "trump",
    "obama",
    "mexico",
    "russia",
    "fake news",
    "china",
    "hillary",
    "media"
]
counts = {i:0 for i in keywords}

for tweet in all_tweets:
    text = tweet.lower()
    for keyword in keywords:
        if keyword in text:
            counts[keyword] += 1

print(counts)

# for markdown table
format_specifier = '05.2f'
total_tweets = len(all_tweets)
percent_tweets = {key: f"{((value / total_tweets)*100):{format_specifier}}" for (key, value) in counts.items()}
print(percent_tweets)


from py_markdown_table.markdown_table import markdown_table
data = [
    {
        'phrase': 'trump',
        'percent of tweets': '38.35', 
    },
    {
        'phrase': 'obama',
        'percent of tweets': '07.47', 
    },
    {
        'phrase': 'mexico',
        'percent of tweets': '00.55', 
    },
    {
        'phrase': 'russia',
        'percent of tweets': '01.13',
    },
    { 
        'phrase': 'fake news',
        'percent of tweets': '00.92'
        }
]
markdown = markdown_table(data).get_markdown()
print(markdown)

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["trump", "obama", "mexico", "russia", "fake news"])
y = np.array([38.35, 07.47, 00.55, 01.13, 00.92])

plt.bar(x,y)
plt.xlabel("Tweets by Trump")
plt.ylabel("Percent of Tweets")
plt.title("What is Trump Tweeting?")
plt.show()
