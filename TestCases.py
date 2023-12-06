from KMP import findWordsInTitles
from KMP import kmp
from simpleFind import findWordsSimple
import time
import matplotlib.pyplot as plt
import random
import numpy as np


def speedTest():
    testFiles = ['fictionBooks.txt', 'fictionAntiWarBooks.txt', 'nonFictionAntiWarBooks.txt', 'allAntiWarBooks.txt']
    testWords = ['the', 'vietnam', 'war', 'of', 'empire', 'America', 'a']
    x:list = [0]
    kmpy:list = [0]
    naivey:list = [0]

    for j in testFiles:
        print(f'In {j} ')
        KMPstart = time.time()
        book_cnt = 0
        for i in testWords:
            book_cnt, count, percent = findWordsInTitles(j, i)
            print(f'\tThe word \"{i}\" was found in {count} of {book_cnt} ({percent}%) book titles')
        KMPend = time.time()
        KMPtime = KMPend - KMPstart
        x.append(book_cnt)
        kmpy.append(KMPtime)

        simpleStart =time.time()
        for i in testWords:
            book_cnt, count, percent = findWordsSimple(j, i)
            print(f'\tThe word \"{i}\" was found in {count} of {book_cnt} ({percent}%) book titles')
        simpleEnd = time.time()
        simpleTime = simpleEnd - simpleStart
        naivey.append(simpleTime)

        print(f'KMP speed for {j}: {KMPtime}')
        print(f'Naive search alg speed for {j}: {simpleTime}')
        print(f'Difference (Naive - KMP): {simpleTime - KMPtime}\n')

    x.sort()
    naivey.sort()
    kmpy.sort()
    plt.plot(x, kmpy, label = 'KMP')
    plt.plot(x, naivey, label= 'naive solution')
    plt.xlabel('number of books')
    plt.ylabel('time (in seconds)')
    plt.legend()
    plt.show()


def single_string_test():
    titleLen = []
    KMPTimes = []
    simpleTimes = []
    KMPcount = 0
    for j in range(1000, 10000, 200):
        randString = ''
        for i in range(j):
            randString += chr(random.randint(ord('a'), ord('z')))
        # print(randString + '\n')
        titleLen.append(len(randString))
        KMPStart = time.time()
        KMPfound = kmp(randString, 'aaaa')
        KMPEnd = time.time()
        KMPTime = KMPEnd - KMPStart
        KMPTimes.append(KMPTime)
        if KMPfound:
            KMPcount += 1


    print(f'Found string \'abcd\' {KMPcount} times using KMP')
    titleLen.sort()
    KMPTimes.sort()
    plt.scatter(titleLen, KMPTimes, color='red')
    KMPa, KMPb = np.polyfit(titleLen, KMPTimes, 1)
    plt.plot(titleLen, KMPa*np.array(titleLen)+KMPb, label='KMP time', color='red')
    plt.xlabel('String Length')
    plt.ylabel('Time (in seconds)')
    plt.title('Runtime of Knuth-Morris-Pratt algorithm')
    plt.legend()
    plt.show()




def correctnessTests():
    print('Test 1: no substring\nThere is no appearance of the substring in the Book Titles')
    print('\tInput:')
    print('\tfile to search: \'fictionAntiWarBooks.txt\'')
    print('\tsubstring: \'life\'')
    print('\tExpected output: 0')
    book_cnt, count, percent = findWordsInTitles('fictionAntiWarBooks.txt', 'life')
    print(f'\tActual output: {count}')

    print('\nTest 2: single space\nTesting if a space gets correctly found')
    print('\tInput:')
    print('\tfile to search: \'nonFictionAntiWarBooks.txt\'')
    print('\tsubstring: \' \'')
    print('\tExpected output: 70')
    book_cnt, count, percent = findWordsInTitles('nonFictionAntiWarBooks.txt', ' ')
    print(f'\tActual output: {count}')

    print('\nTest 3: single word\nTesting if a common word is found correctly')
    print('\tInput:')
    print('\tfile to search: \'allAntiWarBooks.txt\'')
    print('\tsubstring: \'new\'')
    print('\tExpected output: 5')
    book_cnt, count, percent = findWordsInTitles('allAntiWarBooks.txt', 'new')
    print(f'\tActual output: {count}')

    print('\nTest 4: captialization\nTesting if capitalization has any affect (it should not)')
    print('\tInput:')
    print('\tfile to search: \'fictionAntiWarBooks.txt\'')
    print('\tsubstring: \'wAr\'')
    print('\tExpected output: 9')
    book_cnt, count, percent = findWordsInTitles('fictionAntiWarBooks.txt', 'wAr')
    print(f'\tActual output: {count}')

    print('\nTest 5: repeated words in one line\n'
          'Testing that the algorithm will only return the number '
          'of lines that a word appears rather than how many times it appears')
    print('\tInput:')
    print('\tfile to search: \'allAntiWarBooks.txt\'')
    print('\tsubstring: \'war\'')
    print('\tExpected output: 34')
    book_cnt, count, percent = findWordsInTitles('allAntiWarBooks.txt', 'war')
    print(f'\tActual output: {count}')

    print('\nTest 6: single, non alphanumeric character'
          '\nTesting that the algorithm works with non alphanumeric characters')
    print('\tInput:')
    print('\tfile to search: \'allAntiWarBooks.txt\'')
    print('\tsubstring: \':"\'')
    print('\tExpected output: 34')
    book_cnt, count, percent = findWordsInTitles('allAntiWarBooks.txt', ':')
    print(f'\tActual output: {count}')

