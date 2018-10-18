import re
#import operator
#from collections import OrderedDict

# sort a given string. Each word in the String will contain a single number.
# This number is the position the word should have in the result.

# def order(sentence):
#     arrayStr = sentence.split(" ")
#
#     data = {}
#     for str in arrayStr:
#         valKey = map(int, re.findall('\d+', str))
#         #    print valKey
#         data[str] = valKey
#
#     result = []
#
#     d_sorted_by_value = OrderedDict(sorted(data.items(), key=lambda x: x[1]))
#     for k, v in d_sorted_by_value.items():
#         result.append(k)
#
#     return ' '.join(result)

def getNumber(val):
    return re.findall('\d+', val)

def order(sentence):
    arrayStr = sentence.split(" ")
    arrayStr.sort(key=getNumber, reverse=False)
    return ' '.join(arrayStr)