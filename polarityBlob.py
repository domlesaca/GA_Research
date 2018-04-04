from textblob import TextBlob
#https://planspace.org/20150607-textblob_sentiment/

import csv

def getPolarity(text):
    return TextBlob(text).sentiment

def getInterjection(fileName):
    interjections = []
    with open(fileName) as file:
        reader = csv.reader(file)
        for row in reader:
            interjections.append(row)
    return interjections

if __name__ == '__main__':
    text = input('Give sentence to analyze:  ')
    print(getPolarity(text))
