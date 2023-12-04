from KMP import findWordsInTitles
from simpleFind import findWordsSimple
import time


def speedTest():
    testFiles = ['fictionBooks.txt', 'fictionAntiWarBooks.txt', 'nonFictionAntiWarBooks.txt', 'allAntiWarBooks.txt']
    testWords = ['the', 'vietnam', 'war', 'of', 'empire', 'America', 'a']

    for j in testFiles:
        print(f'In {j} ')
        KMPstart = time.time()
        for i in testWords:
            book_cnt, count, percent = findWordsInTitles(j, i)
            print(f'\tThe word \"{i}\" was found in {count} of {book_cnt} ({percent}%) book titles')
        KMPend = time.time()
        KMPtime = KMPend - KMPstart

        simpleStart =time.time()
        for i in testWords:
            book_cnt, count, percent = findWordsSimple(j, i)
            print(f'\tThe word \"{i}\" was found in {count} of {book_cnt} ({percent}%) book titles')
        simpleEnd = time.time()
        simpleTime = simpleEnd - simpleStart

        print(f'KMP speed for {j}: {KMPtime}')
        print(f'Naive search alg speed for {j}: {simpleTime}')
        print(f'Difference (Naive - KMP): {simpleTime - KMPtime}\n')


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

