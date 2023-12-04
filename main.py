def makeLPSArry(sub: str, size: int) -> list[int]:
    len = 0
    lps = [0] * size
    idx = 1

    while idx < size:
        if sub[idx] == sub[len]:
            len += 1
            lps[idx] = len
            idx += 1

        else:
            if len != 0:
                len = lps[len - 1]
            else:
                lps[idx] = 0
                idx += 1

    return lps


def kmp(text: str, sub: str) -> bool:
    textSize = len(text)
    subSize = len(sub)
    lpsArry = makeLPSArry(sub, subSize)

    i = 0
    j = 0
    while (textSize - i) >= (subSize - j):
        if sub[j] == text[i]:
            i += 1
            j += 1

        if j == subSize:
            j = lpsArry[j-1]
            return True

        elif i < textSize and sub[j] != text[i]:
            if j != 0:
                j = lpsArry[j-1]
            else:
                i += 1

    return False




def main():
    fileName = input('What file would you like to use for input?')
    searchWord = input('What word would you like to search for?').lower()

    file = open(fileName, "r")
    count = 0
    book_cnt = 0
    for i in file:
        book_cnt += 1
        if kmp(i, searchWord):
            count += 1

    percent = round(( float(count) / float(book_cnt) ) * 100, 2)
    print(f"The word {searchWord} appears in {percent}% of book titles")


main()
