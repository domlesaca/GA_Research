
def main():
    # word to search
    keyWord = "would"
    # file of reviews we want to search
    fileName = "Bellagio_Reviews_2017-11-07.txt"
    file = open(fileName, 'r')
    sortedName = "Sorted_"+fileName
    newFile = open(sortedName, 'w')
    for review in file.readlines():
        if keyWord in review:
            print(review)
            newFile.write(review)




if __name__ == '__main__':
    main()
