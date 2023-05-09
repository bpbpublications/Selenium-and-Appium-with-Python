import random


def fun(sent):
    words = sent.split()
    print(type(words))
    print(len(words))
    dict = {}
    for word in words:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
    for i in sorted(dict.items()):
        print(i)
    return dict


fun("this is the total number of words in the string test")


def fun2(string1):
    revers = "".join(reversed(string1))
    rev = string1[::-1]
    print(revers)
    print(rev)
    list1 = [*string1]
    list2 = [x for x in string1]
    print(type(list1))
    print(list1)
    print(list1.count('i'))
    print(list2.count('a'))
    fruits = ["apple", "orange", "mango", "papaya", "apple"]
    listAsTuple = tuple(fruits)
    listAsString = " ".join(fruits)
    print(fruits.count("apple"))
    print(type(listAsTuple))
    print(listAsString.strip())
    print(random.randint(a=0, b=1))
    print(random.random())


fun2("gauisdbfuainfio")


def fun3(num):
    num1 = num
    temp = 0

    while num != 0:
        temp = num % 10 + (temp * 10)
        num //= 10
        print(num)
    if num1 == temp:
        print(True)
    else:
        print(False)


fun3(12321)


def fun4(num):
    factorial = 1
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(2, num + 1):
            factorial = factorial * i
    print(factorial)


fun4(0)


def fun5(num):
    if num % 2 == 0:
        print("even")
    else:
        print("odd")
    s1 = {1, 2, 3, 4, 5, 6}
    s2 = {5, 6, 7, 8, 9}
    print(s1.intersection(s2))
    print(min(s1))
    print(max(s1))
    list1 = [a for a in range(5)]
    print(list1)
    list2 = [a for a in range(5) if a < 3]
    print(list2)
    print(dict([(i, i * 2) for i in range(5)]))


fun5(9)


def fun6(first, last):
    full_name = first + ' ' + last
    print(full_name.title())


fun6("yogashiva", "mathivanan")


def fun7(size, *toppings, name=None):
    print("Making Pizza of Size" + str(size))
    print(toppings)
    for topping in toppings:
        print(topping, end=" ")
    tea = set(toppings)
    print(type(tea))


fun7("8 inch", "tomoto", "onion", "chicken", name="3 topping pizza")


def fun8(first, last, **user_info):
    profile = {'firstName': first, 'lastName': last}
    for key, value in user_info.items():
        profile[key] = value
    print(profile)


fun8("shiva", "mathi", age=33, mobile=56789, address="123 St")


def fun9(a):
    if a == 1 or a == 0:
        return 1
    else:
        return a * fun9(a - 1)


print(fun9(5))


def second_largest_of_list():
    li1 = [45, 34, 89, 12, 99, 23, 55]
    highest = 0
    secondHighest = 0
    for i in li1:
        if i > highest:
            secondHighest = highest
            highest = i
        elif i > secondHighest:
            secondHighest = i
    print(str(highest) + "    " + str(secondHighest))
    print(sorted(li1)[len(li1) - 2])


second_largest_of_list()


def longestChar(string1):
    d = {}
    for ch in string1:
        if ch not in d.keys():
            d[ch] = 1
        else:
            d[ch] = d[ch] + 1
    print(d)


def longestSubWithoutRepeating(string1):
    longestSubStr = ""
    longestSubLen = 0
    d = {}
    for i in range(0, len(string1)):
        if string1[i] not in d.keys():
            d[string1[i]] = i
        else:
            i = d[string1[i]]
            d.clear()
        if longestSubLen < len(d):
            longestSubLen = len(d)
            longestSubStr = str(d.keys())
    print(longestSubStr + "     " + str(longestSubLen))
    return longestSubLen


longestSubWithoutRepeating("GEEKSFORGEEKS")