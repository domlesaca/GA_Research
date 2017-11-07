from bs4 import BeautifulSoup
import urllib.request

def main():
    url = "https://www.tripadvisor.com/Hotel_Review-g45963-d91703-Reviews-Bellagio_Las_Vegas-Las_Vegas_Nevada.html"
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

if __name__ == '__main__':
    main()
