

TargetWord = 0

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
    targetWord = -1
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
    if targetWord == -1:
        print("The target word does not exist in dictionary")
    return steps

if __name__ == '__main__':
    counts = 0
    words = range(0, 267751)
    for w in range(0, 267751 // 2):
        TargetWord = w
        res = findWord(words)
        counts += res
    print("The average # of steps is : ", counts / 267751 * 2)
        
