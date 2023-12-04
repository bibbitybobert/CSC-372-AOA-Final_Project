def simpleFind(line:str, substr:str) -> bool:
    subLen = len(substr)
    lineLen = len(line)

    for i in range(lineLen - subLen + 1):
        j = 0

        while (j < subLen):
            if line[i+j] != substr[j]:
                break
            j+=1

        if j == subLen:
            return True
        return False


def findWordsSimple(fileName:str, searchWord:str) -> (int, int, float):
    file = open(fileName, "r")
    count = 0
    book_cnt = 0
    for i in file:
        book_cnt += 1
        if simpleFind(i.lower(), searchWord.lower()):
            count+= 1

    percent = round((float(count) / float(book_cnt)) * 100, 2)
    return book_cnt, count, percent
