from bs4 import BeautifulSoup
import urllib.request
from selenium import webdriver

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
    return

def urlScrape():
    file = urllib.request.urlopen(url)
    soup = BeautifulSoup(file, "html.parser")
    # open file
    rev = open("reviews.txt", "a")
    thnk = open("thanks.txt", "a")

    # find reviews in file
    reveiws = soup.find_all("div", class_="entry")
    for reveiw in reveiws:
        x = reveiw.text
        # parse thank yous
        if x[0:4] == "Dear":
            thnk.write(x+"\n")
        else:
            rev.write(x+"\n")
        print(x)

    #print(soup.prettify())

# def screenshot():
#     DRIVER = webdriver.Chrome('C:\Program Files\Python36\selenium\webdriver\chromedriver')
#     driver = webdriver.Chrome(DRIVER)
#     driver.get(url)
#     screenshot = driver.save_screenshot('my_screenshot.png')
#     driver.quit()

if __name__ == '__main__':
    main()
