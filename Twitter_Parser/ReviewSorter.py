import ReviewScrapper


def main():
    # word to search
    keyWord = "Returned"
    # file of reviews we want to search

    fileName = "Bellagio_Reviews_2017-11-28.txt"
    file = open(fileName, 'r')
    sortedName = "Sorted_"+fileName
    newFile = open(sortedName, 'w')
    for review in file.readlines():
        if keyWord in review:
            newFile.write(review)
    file.close()
    newFile.close()




if __name__ == '__main__':
    ReviewScrapper.urlScrape()
    main()
