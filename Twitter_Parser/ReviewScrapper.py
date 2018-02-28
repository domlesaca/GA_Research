from bs4 import BeautifulSoup
import urllib.request
import requests
from selenium import webdriver
import datetime
import time

# Input the url for the specific page you want to scrape
url = "https://www.tripadvisor.com/Hotel_Review-g45963-d91703-Reviews-or5-Bellagio_Las_Vegas-Las_Vegas_Nevada.html"
# Input the name of the hotel you want to search
hotelName = "Bellagio"
# Input one if you want to scrape the URL or 0 if you want to scrape a search for a hotel
scrapeType = 1
#



def main():
    print('hi')

def getPages(url):
    page = requests.get(url)
    time.sleep(1)
    soup = BeautifulSoup(page.content, 'html.parser')
    print(soup)
    tags = soup.find('div', attrs={'class': 'pagination-details'})
    print(tags)
    text = tags.get_text()
    s, dash, e, of, total, rev = text.split(' ')
    total = int(total.replace(',', ''))
    total = int((total - total%5)/5)
    print(total)
    return total

def urlScrape(url, hotelName):
    # Open all readmore tabs on the page
    readMore(url)
    #file = urllib.request.urlopen('page_source.html')
    file  = open("page_source.html", 'r').read()
    soup = BeautifulSoup(file, "html.parser")
    # open file
    now = datetime.datetime.now()
    fileName = "reviews/"+hotelName+"_Reviews_"+str(now.date())+".txt"
    print(fileName)
    rev = open(fileName, "a")
    # Clear the file in case it already exists
    thnk = open("thanks.txt", "a")
    # clear the thanks file to avoid duplicates
    deleteContent(thnk)


    # find reviews on webpage
    reviews = soup.find_all("div", class_="review-container")
    for review in reviews:
        # add star rating to the file
        stars = getStars(review)
        rev.write(str(stars)+"\n")
        # add date the review was made to the file
        reviewDate = getReviewDate(review)
        rev.write(reviewDate+"\n")
        text = getReviewtext(review)
        rev.write(text+"\n")
        rev.write("\n")
    rev.close()
    #print(soup.prettify())

def readMore(url):
    # open chrome
    driver = webdriver.Chrome("selenium/webdriver/chromedriver.exe")
    # go to the selected URL
    driver.get(url)
    # Searches for the spans that allow us to read the full reviews
    taLinks = driver.find_elements_by_class_name('taLnk')
    blueLinks = driver.find_elements_by_class_name("ulBlueLinks")
    intersect = set(taLinks) & set(blueLinks)
    for elem in intersect:
        try:
            # click on the read more links for the comments
            elem.click()
            # give the page a chance to catch up
            time.sleep(.5)
        except:
            # No point to this code, It just avoids exceptions just in case
            x = 1

    # screenshot webassign

    with open('page_source.html', 'w', errors='ignore') as f:
        f.write(driver.page_source)
    driver.close()

# Clears all data in a given file
def deleteContent(pfile):
    pfile.seek(0)
    pfile.truncate()

# Function to get the number of stars rated by a review
def getStars(review):
    if len(review.find_all("span", class_="bubble_50")) > 0:
        return 5
    elif len(review.find_all("span", class_="bubble_40")) > 0:
        return 4
    elif len(review.find_all("span", class_="bubble_30")) > 0:
        return 3
    elif len(review.find_all("span", class_="bubble_20")) > 0:
        return 2
    elif len(review.find_all("span", class_="bubble_10")) > 0:
        return 1
    else:
        return 0

# Function to get the date teh review was posted
def getReviewDate(review):
    # search for the span with the class ratingDate
    date = review.find("span", class_="ratingDate")
    # get the title of the span, this is how the date is stored
    date = date["title"]
    return date

# Function to get the text of a review
def getReviewtext(review):
    text = review.find("div", class_="entry")
    return text.text

if __name__ == '__main__':
    main()
