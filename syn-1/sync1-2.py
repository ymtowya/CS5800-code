

TargetWord = 'test'

def checkWord(guess):
    if guess == TargetWord:
        return 0
    elif guess < TargetWord:
        return -1
    else:
        return 1

def findWord(wordList):
    n = len(wordList)
    left = 0
    right = n - 1
    targetWord = ''
    steps = 0
    while left <= right:
        mid = (left + right) // 2
        tmpres = checkWord(wordList[mid])
        steps += 1
        if tmpres == 0:
            targetWord = wordList[mid]
            break
        elif tmpres < 0:
            left = mid + 1
        else:
            right = mid - 1
    if targetWord == '':
        print("The target word does not exist in dictionary")
    else:
        print("The scret word is : " + targetWord)
    return steps

if __name__ == '__main__':
    words = ['aware', 'but', 'check', 'end', 'figma', 'grow', 'hello', 'interest', 'jump', 'knee', 'lemon', 'melon', 'never', 'play', 'quit']
    for w in words:
        TargetWord = w
        res = findWord(words)
        print("The search took # of steps is : ", res)
        
