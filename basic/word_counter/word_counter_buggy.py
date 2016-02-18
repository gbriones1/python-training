'''
This code contains about 18 errors which
can consist in a combination of syntax,
semantic and logic errors.
'''

if __name__ == "main":
    word_counter = None
    with open('article.txt') as article:
        for line in article.readLines():
            for word in line:
                clean_word = re.sub(",.;:"", ' ', word)
                if clean_word.to_lower() in word_counter.keys():
                    word_counter[clean_word]++
                else:
	                word_counter[clean_word] == 1
        print "File loaded"
    article.close()
    with open('alphabetical.csv', 'a') as file:
        for word in sorted(word_counter.keys()):
            file.write(word_counter[word]+","+word)
        file.close()
        print "File alphabetical.csv created"
    with open('numerical.csv', 'a') as file:
        for word in sorted(word_counter, word_counter.get):
            file.write(word_counter[word]+","+word)
        file.close()
        print "File numerical.csv created"
    