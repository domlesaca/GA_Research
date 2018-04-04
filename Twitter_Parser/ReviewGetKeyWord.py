

def searchWord(keyWord, fileName):
    file = open(fileName, 'r')
    matches = []
    for review in file.readlines():
        if keyWord in review:
            matches.append(review)
    file.close()
    return matches

if __name__ == '__main__':
    fileName = input("Which file do you want to search? ")
    key = input("Keyword: ")
    matches = searchWord(key, fileName)
    print(len(matches), "Matches")
    for match in matches:
        print(match)
