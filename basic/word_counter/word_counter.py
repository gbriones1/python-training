import re

if __name__ == "__main__":
    word_counter = {}
    with open('article.txt', 'r') as article:
        for line in article.readlines():
            for word in line.split():
                clean_word = re.sub('[,.;:)("]|\'s', '', word).lower()
                if clean_word in word_counter.keys():
                    word_counter[clean_word] += 1
                else:
                    word_counter[clean_word] = 1
        print "File loaded"
    article.close()
    with open('alphabetical.csv', 'w') as file:
        for word in sorted(word_counter.keys()):
            file.write(str(word_counter[word])+","+word+"\n")
        file.close()
        print "File alphabetical.csv created"
    with open('numerical.csv', 'w') as file:
        for word in sorted(word_counter, key=word_counter.get, reverse=True):
            file.write(str(word_counter[word])+","+word+"\n")
        file.close()
        print "File numerical.csv created"
    