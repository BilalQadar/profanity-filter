from filter import buildBadArray, profanity_filter, write_to_txt

if __name__ == "__main__":
    f = open('./passwordDict/commonPasswords.txt', 'r')
    content = f.read()
    content = content.split('\n')
    f.close()

    badDict = buildBadArray('googleBadWords.txt')
    cleanWords = profanity_filter(content, badDict)
    write_to_txt(cleanWords)
    print('Completed')
