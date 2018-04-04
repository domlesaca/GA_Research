import spacy

if __name__ == '__main__':
    nlp = spacy.load('en')

    fileName = input("Enter file Path")
    file = open(fileName, 'r')
    for line in file:
        doc = nlp(line)
        nouns = []
        verbs = []
        for token in doc:
            if token.pos_ == 'NOUN' or token.pos_=='PROPN':
                print(token.text, token.pos_)
                nouns.append(token.text)
            if token.pos_ == 'VERB':
                print(token.text, token.pos_)
                verbs.append(token.text)

        print(len(nouns), "Nouns")
        print(len(verbs), "Verbs")
        input('Enter for the next line')
