words = ['apple', 'banana', 'mango']
uppercased = [word.upper() for word in words]
print(uppercased)
nums = [1,4,7,10,13,16]
odds = [x for x in nums if x % 2 == 1]
print(odds)
scores = [10, 20, 30, 40]
added = [x + 5 for x in scores]
print(added)