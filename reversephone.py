import itertools
import enchant

def reversephone(phonenum, wordsplit):
    d = enchant.Dict('en_US')
    cutphone = ''
    letterdict = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
    if '-' in phonenum or '.' in phonenum:
        cutphone = ''.join(phonenum[-8:].split(phonenum[-5]))
    else:
        cutphone = phonenum[-7:]

    try:
        if wordsplit == '7-0':
            for i in itertools.product(list(letterdict[cutphone[0]]),list(letterdict[cutphone[1]]),list(letterdict[cutphone[2]]),list(letterdict[cutphone[3]]),list(letterdict[cutphone[4]]),list(letterdict[cutphone[5]]),list(letterdict[cutphone[6]]),):
                word = ''.join(i)
                if d.check(word):
                    print(f'{phonenum[:3]}-{word.upper()}')

        elif wordsplit == '3-4':
            firstwordlist = []
            secondwordlist = []
            for i in itertools.product(list(letterdict[cutphone[0]]),list(letterdict[cutphone[1]]),list(letterdict[cutphone[2]])):
                word = ''.join(i)
                if d.check(word):
                    firstwordlist.append(word)
            for i in itertools.product(list(letterdict[cutphone[3]]),list(letterdict[cutphone[4]]),list(letterdict[cutphone[5]]),list(letterdict[cutphone[6]])):
                word = ''.join(i)
                if d.check(word):
                    secondwordlist.append(word)
            for i in itertools.product(firstwordlist,secondwordlist):
                word = ''.join(i)
                print(f'{phonenum[:3]}-{word.upper()}')

        elif wordsplit == '4-3':
            firstwordlist = []
            secondwordlist = []
            for i in itertools.product(list(letterdict[cutphone[0]]),list(letterdict[cutphone[1]]),list(letterdict[cutphone[2]]),list(letterdict[cutphone[3]])):
                word = ''.join(i)
                if d.check(word):
                    firstwordlist.append(word)
            for i in itertools.product(list(letterdict[cutphone[4]]),list(letterdict[cutphone[5]]),list(letterdict[cutphone[6]])):
                word = ''.join(i)
                if d.check(word):
                    secondwordlist.append(word)
            for i in itertools.product(firstwordlist,secondwordlist):
                word = ''.join(i)
                print(f'{phonenum[:3]}-{word.upper()}')

        elif wordsplit == '2-5':
            firstwordlist = []
            secondwordlist = []
            for i in itertools.product(list(letterdict[cutphone[0]]),list(letterdict[cutphone[1]])):
                word = ''.join(i)
                if d.check(word):
                    firstwordlist.append(word)
            for i in itertools.product(list(letterdict[cutphone[2]]),list(letterdict[cutphone[3]]),list(letterdict[cutphone[4]]),list(letterdict[cutphone[5]]),list(letterdict[cutphone[6]])):
                word = ''.join(i)
                if d.check(word):
                    secondwordlist.append(word)
            for i in itertools.product(firstwordlist,secondwordlist):
                word = ''.join(i)
                print(f'{phonenum[:3]}-{word.upper()}')

        elif wordsplit == '5-2':
            firstwordlist = []
            secondwordlist = []
            for i in itertools.product(list(letterdict[cutphone[0]]),list(letterdict[cutphone[1]]),list(letterdict[cutphone[2]]),list(letterdict[cutphone[3]]),list(letterdict[cutphone[4]])):
                word = ''.join(i)
                if d.check(word):
                    firstwordlist.append(word)
            for i in itertools.product(list(letterdict[cutphone[5]]),list(letterdict[cutphone[6]])):
                word = ''.join(i)
                if d.check(word):
                    secondwordlist.append(word)
            for i in itertools.product(firstwordlist,secondwordlist):
                word = ''.join(i)
                print(f'{phonenum[:3]}-{word.upper()}')

        elif wordsplit == '6-1':
            firstwordlist = []
            secondwordlist = []
            for i in itertools.product(list(letterdict[cutphone[0]]),list(letterdict[cutphone[1]]),list(letterdict[cutphone[2]]),list(letterdict[cutphone[3]]),list(letterdict[cutphone[4]]),list(letterdict[cutphone[5]])):
                word = ''.join(i)
                if d.check(word):
                    firstwordlist.append(word)
            for i in itertools.product(list(letterdict[cutphone[6]])):
                word = ''.join(i)
                if d.check(word):
                    secondwordlist.append(word)
            for i in itertools.product(firstwordlist,secondwordlist):
                word = ''.join(i)
                print(f'{phonenum[:3]}-{word.upper()}')

        elif wordsplit == '1-6':
            firstwordlist = []
            secondwordlist = []
            for i in itertools.product(list(letterdict[cutphone[0]])):
                word = ''.join(i)
                if d.check(word):
                    firstwordlist.append(word)
            for i in itertools.product(list(letterdict[cutphone[1]]),list(letterdict[cutphone[2]]),list(letterdict[cutphone[3]]),list(letterdict[cutphone[4]]),list(letterdict[cutphone[5]]),list(letterdict[cutphone[6]])):
                word = ''.join(i)
                if d.check(word):
                    secondwordlist.append(word)
            for i in itertools.product(firstwordlist,secondwordlist):
                word = ''.join(i)
                print(f'{phonenum[:3]}-{word.upper()}')

    except:
        print('Something is wrong with the provided number. Make sure it is in one of these formats:\n\n111-222-3333\n111.222.3333\n1112223333\n\nDo not include letters or special characters and only include 10 digits\nTHE NUMBERS 0 AND 1 DO NOT WORK\n')

    wordsplits = ['7-0','3-4','4-3','2-5','5-2','6-1','1-6']

    if wordsplit not in wordsplits:
        print("""
                That is not a suitable split. Instead try one of these:

                '7-0'  for one seven letter word
                '3-4'  for a three letter word followed by a four letter word
                '4-3'  for a four letter word followed by a three letter word
                '2-5'  for a two letter word followed by a five letter word
                '5-2'  for a five letter word followed by a two letter word
                '6-1'  for any six letter word followed by a single letter
                '1-6'  for any single letter followed by a six letter word
              """)

reversephone('123.883.6745','7-')

# GITHUB
# WEBSITE --> https://blog.pythonanywhere.com/169/
