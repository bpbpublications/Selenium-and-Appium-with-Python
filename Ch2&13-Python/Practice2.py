def pushNumtoEnd(li, num):
    count = 0
    for i in range(len(li)):
        if li[i] != num:
            temp = li[count]
            li[count] = li[i]
            li[i] = temp
            count += 1
    print(li)


li = [5, 6, 2, 3, 6, 3, 9, 3, 4, 5, 6]
pushNumtoEnd(li, 3)


def noOfWordsInString(strig):
    li = strig.lower().split(" ")
    d = {}
    for strig1 in li:
        if strig1 not in d.keys():
            d[strig1] = 1
        else:
            d[strig1] = d[strig1] + 1
    for keys, values in d.items():
        print(str(keys) + " count is " + str(values))


noOfWordsInString("This this is is a new word in sentence")


def isAnagram(s1, s2):
    li1 = [x for x in s1.lower()]
    li2 = [x for x in s2.lower()]
    if sorted(li1) == sorted(li2):
        print(True)
    else:
        print(False)


isAnagram("Listen", "Silent")


def isStringPalindrome(st):
    if st.lower() == st[::-1].lower():
        print(True)
    else:
        print(False)


isStringPalindrome("Tenet")


def isNumPalindrome(num):
    num1 = num
    temp = 0
    while num != 0:
        temp = (num % 10) + (temp * 10)
        num = num // 10
    if temp == num1:
        print(True)
    else:
        print(False)


isNumPalindrome(1214)


def longestSubStringWithoutRepeating(str1):
    longestSubStr = ""
    longestSubstrLen = 0
    li = [x for x in str1]
    d = {}
    for i in range(len(li)):
        if li[i] not in d:
            d[li[i]] = i
        else:
            i = d[li[i]]
            d.clear()
        if longestSubstrLen < len(d):
            longestSubStr = str(d.keys())
            longestSubstrLen = len(d)
    print(longestSubStr)
    print(longestSubstrLen)


longestSubStringWithoutRepeating("GEEKSFORGEEKS")


def reverseList(string):
    li = [x for x in string.lower()]
    string1 = ""
    l, r = 0, len(li) - 1
    while l < r:
        temp = li[l]
        li[l] = li[r]
        li[r] = temp
        l += 1
        r -= 1

    for x in li:
        string1 += str(x)
    print(string1)


reverseList("dfafadf")


def reveseStringPreservingSpecialCharSpace(string):
    li = [x for x in string.lower()]
    string1 = ""
    l, r = 0, len(li) - 1
    while l < r:
        if not li[l].isalpha():
            l += 1
        elif not li[r].isalpha():
            r -= 1
        else:
            temp = li[l]
            li[l] = li[r]
            li[r] = temp
            l += 1
            r -= 1
    for x in li:
        string1 += str(x)
    print(string1)


reveseStringPreservingSpecialCharSpace("dfaf%^&* fdafaf  adf")


def intersectionString(str1, str2):
    str3 = ""
    s1 = set(str1)
    s2 = set(str2)
    s3 = set()
    print(s1.intersection(s2))
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                s3.add(str1[i])

    intersect = [x for x in str2 if x in str1]
    print(str(s3))
    print(set(intersect))


intersectionString("Hello", "How are you")


def exceptionHandling():
    a = 7
    b = 0
    try:
        print(a / b)
    except ArithmeticError:
        print("Cannot Divide by 0")
    finally:
        print("This will be printed")


exceptionHandling()
