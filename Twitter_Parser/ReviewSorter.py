import ReviewScrapper
import datetime
import csv

termCounts = {}
hotelMatches = {}
hotelTermMatches = {}

def searchWord(keyWord, fileName, hotelName):
    file = open("reviews/"+fileName, 'r')
    sortedName = "sorted/Sorted_"+fileName
    with open(sortedName, 'a') as newFile:
        for review in file.readlines():
            if keyWord in review:
                newFile.write(review)
                termCounts[term] += 1
                hotelMatches[hotelName] += 1
                hotelTermMatches[hotelName][keyWord] += 1
    file.close()

def scrapeSite(url, hotelName, keyWords, pages):
    # file of reviews we want to search
    now = datetime.datetime.now()
    fileName = hotelName+"_Reviews_"+str(now.date())+".txt"
    file = open("reviews/"+fileName, 'a')
    ReviewScrapper.deleteContent(file)
    file.close()
    for i in range(0, pages):
        urlText = url[0]+str(url[1]+i*5)+url[2]
        ReviewScrapper.urlScrape(urlText, hotelName)
    for keyWord in keyWords:
        searchWord(keyWord, fileName, hotelName)

if __name__ == '__main__':
    pages = 2
    terms = []
    # Get terms from file
    termFile = open("terms.txt", 'r')
    #remove new line characters from terms
    for line in termFile:
        term = line.replace("\n", "")
        terms.append(term)
        termCounts[term] = 0

    urls = [("https://www.tripadvisor.com/Hotel_Review-g309280-d301435-Reviews-or", 0, "-Luna_Lodge-Carate_Corcovado_National_Park_Osa_Peninsula_Province_of_Puntarenas.html"),
            ("https://www.tripadvisor.com/Hotel_Review-g6003263-d293477-Reviews-or", 0, "-Hotel_Punta_Islita_Autograph_Collection-Punta_Islita_Province_of_Guanacaste.html"),
            ("https://www.tripadvisor.com/Hotel_Review-g2705972-d293118-Reviews-or", 0, "-Lapa_Rios_Ecolodge_Osa_Peninsula-Cabo_Matapalo_Osa_Peninsula_Province_of_Puntarenas.html"),
            ("https://www.tripadvisor.com/Hotel_Review-g1237032-d300371-Reviews-or", 0, "-Finca_Rosa_Blanca_Coffee_Plantation_Resort-Santa_Barbara_Province_of_Heredia.html"),
            ("https://www.tripadvisor.com/Hotel_Review-g9771272-d669920-Reviews-or", 0, "-Pacuare_Lodge-Pacuare_River_Province_of_Limon.html")]
    hotelNames = ["Luna_Lodge", "Punta_Islita", "Lapa_Rios", "Finca_Rosa", "Pacuare_Lodge"]
    hotelMatches = {"Luna_Lodge": 0, "Punta_Islita": 0, "Lapa_Rios": 0, "Finca_Rosa": 0, "Pacuare_Lodge": 0}

    # Keeps track of table of number of matches for each term for each hotel
    for hotel in hotelNames:
        searchTerms = {}
        for t in terms:
            searchTerms[t] = 0
        hotelTermMatches[hotel] = searchTerms

    # run for each term
    for i in range(0, len(urls)):
        scrapeSite(urls[i], hotelNames[i], terms, pages)

    with open("stats.csv", 'w') as csvFile:
        ReviewScrapper.deleteContent(csvFile)
        fieldNames = ['hotel_name']+terms
        writer = csv.DictWriter(csvFile, fieldnames=fieldNames)

        writer.writeheader()
        row = {}
        for hotel in hotelNames:
            row['hotel_name'] = hotel
            for term in terms:
                row[term] = hotelTermMatches[hotel][term]
            writer.writerow(row)

    print(termCounts)
    print(hotelMatches)

