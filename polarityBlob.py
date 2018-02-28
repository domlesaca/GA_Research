from textblob import TextBlob
#https://planspace.org/20150607-textblob_sentiment/

def getPolarity(text):
    return TextBlob(text).sentiment

if __name__ == '__main__':
    text = input('Give sentence to analyze:  ')
    print(getPolarity(text))
