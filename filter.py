def buildBadArray(file):
    f = open(file, 'r')
    content = f.read()
    content = content.split('\n')
    f.close()

    badDict = {}
    for word in content:
        if len(word.strip(' ')) > 0 and len(word.split(' ')) == 1:
            badDict[word] = ""

    return badDict

def profanity_filter(content, badDict):
    clean_words = []
    for word in content:
        word = word.strip(' ')
        clean = is_clean(word, badDict)
        if clean:
            print('Passed: ' + word)
            clean_words.append(word)
        else:
            print('Failed: ' + word)
    return clean_words

def is_clean(word, badDict):
    for i in range(len(word)):
        for j in range(len(word) -1):
            if word[i:j+2] in badDict:
                return False
    return True

def write_to_txt(content):
    print('\n WRITING TO TEXT FILE...')
    f = open('./passwordDict/cleanedWords.txt', 'w')
    for word in content:
        f.write('\n' + word)
    f.close()
