import itertools
import numpy as np

SIZE = 10000
with open('task3_train_segmented.txt', 'r') as f:
    data = [next(f).split() for x in range(SIZE)]

dictionary = set(itertools.chain(*data))


def countError(correct, test):
    testValue, correctValue = 0, 0
    for i in correct:
        correctValue += len(i)**2
    for i in test:
        testValue += len(i)**2

    testValue = testValue**0.5
    correctValue = correctValue**0.5

    return 1 - abs(testValue-correctValue)/correctValue


def MaxMatch(text):
    if text in dictionary:
        return [text]
    success = None
    it = len(text)+1
    while not success:
        it -= 1
        while text[:it] not in dictionary:
            it -= 1
            if it < 0:
                return None
        success = MaxMatch(text[it:])
    return [text[:it]]+success


i = 0
avErr = 0
for x in data:
    i += 1
    # if not i%10:
    #     print(i)
    # print(x)
    new = MaxMatch(''.join(x))
    # print(new)
    error = countError(x, new)
    avErr = ((i-1) * avErr + error) / i
    # if error != 1:
    #     print(f"""{error}\n{new}\n{x}\n\n""")
print(avErr*100, '%')
# print(dictionary)
