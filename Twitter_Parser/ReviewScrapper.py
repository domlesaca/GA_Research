from bs4 import BeautifulSoup
import urllib.request
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
    # decide whether to scrape 1 url or do a search
    if scrapeType == 1:
        urlScrape()
    else:
        searchHotel()

def searchHotel():
    print("THis function is still a work in progress")
    return

def urlScrape():
    # Open all readmore tabs on the page
    readMore(url)
    #file = urllib.request.urlopen('page_source.html')
    file  = open("page_source.html", 'r').read()
    soup = BeautifulSoup(file, "html.parser")
    # open file
    now = datetime.datetime.now()
    fileName = hotelName+"_Reviews_"+str(now.date())+".txt"
    print(fileName)
    rev = open(fileName, "a")
    # Clear the file in case it already exists
    deleteContent(rev)
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
        rev.write(getReviewDate(review)+"\n")
        text = getReviewtext(review)
        rev.write(text+"\n")
        rev.write("\n")

    #print(soup.prettify())

def readMore(url):
    driver = webdriver.Chrome("selenium/webdriver/chromedriver.exe")
    driver.get(url)
    for elem in driver.find_elements_by_link_text('More'):
        elem.click()
        time.sleep(.5)

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

# def screenshot():
#     DRIVER = webdriver.Chrome('C:\Program Files\Python36\selenium\webdriver\chromedriver')
#     driver = webdriver.Chrome(DRIVER)
#     driver.get(url)
#     screenshot = driver.save_screenshot('my_screenshot.png')
#     driver.quit()

if __name__ == '__main__':
    main()
