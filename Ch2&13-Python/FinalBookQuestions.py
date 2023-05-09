# Question 1 - Write a program to return the count of each word in the provided Sentence

def count_eachWord(sentence):
    # Split the sentence into words
    words = sentence.split()

    # Create a dictionary to store the count of each word
    word_count = {}

    # Loop through each word in the list
    for word in words:
        # If the word is already in the dictionary, increment its count
        if word in word_count:
            word_count[word] += 1
        # If the word is not in the dictionary, add it with a count of 1
        else:
            word_count[word] = 1

    # Return the dictionary of word counts
    return word_count


print(count_eachWord("This is a sample sentence to test the word count program"))


# Question 2 - Write a program to count each character in a sentence.

def char_count(input_string):
    char_count_dict = {}
    for char in input_string.lower():
        if char not in char_count_dict:
            char_count_dict[char] = 1
        else:
            char_count_dict[char] += 1
    print(char_count_dict)


char_count("Hello, world!")


# Question 3 - Write a program to reverse a string, Write a program to reverse each word in a given sentence,
# Write a program to reverse the complete sentence preserving the space and special characters.


def reverse_string_loop(string):
    reversed_str = ''
    for i in range(len(string) - 1, -1, -1):
        reversed_str += string[i]
    return reversed_str


def reverse_string_slicing(string):
    return string[::-1]


def reverse_string_reversed(string):
    return ''.join(reversed(string))


print(reverse_string_loop("hello world"))
print(reverse_string_slicing("hello world"))
print(reverse_string_reversed("hello world"))


def reverse_words(sentence):
    # Split the sentence into words
    words = sentence.split()

    # Reverse each word and join them back into a sentence
    reversed_words = [word[::-1] for word in words]
    reversed_sentence = ' '.join(reversed_words)

    return reversed_sentence


print(reverse_words("Hello world, && how are you?"))


def reverse_sentence_preservingSpacesAndSpecialCharacters(sentence):
    # convert the input string to a list of characters
    char_list = list(sentence)

    # define two pointers i and j, pointing to the start and end of the list respectively
    i = 0
    j = len(char_list) - 1

    # loop until the pointers meet or cross each other
    while i < j:
        # if the character at index i is not a letter, move the pointer to the right
        if not char_list[i].isalpha():
            i += 1
        # if the character at index j is not a letter, move the pointer to the left
        elif not char_list[j].isalpha():
            j -= 1
        # if both characters at i and j are letters, swap them and move the pointers towards each other
        else:
            char_list[i], char_list[j] = char_list[j], char_list[i]
            i += 1
            j -= 1

    # join the characters in the list back into a string
    return ''.join(char_list)


print(reverse_sentence_preservingSpacesAndSpecialCharacters("hello, world! how are you today?"))


# Question 4 - Write a program to find if a String and number is a Palindrome or not

def is_palindrome_string(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False


def is_palindrome_num(num):
    original_num = num
    reversed_num = 0

    while num != 0:
        reversed_num = num % 10 + (reversed_num * 10)
        num //= 10

    if original_num == reversed_num:
        return True
    else:
        return False


print(is_palindrome_string("tenet"))
print(is_palindrome_num(121))


# Question 5 - Write a program to find the factorial of a number

def factorialNum(num):
    factorial = 1
    if num < 0:
        factorial = "Sorry, factorial does not exist for negative numbers"
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(2, num + 1):
            factorial = factorial * i
    return factorial


print("Factorial of", 12, "is", factorialNum(12))


# Question 6 - Write a program to find if the number is prime or not, if the number is even or odd.

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num / 2) + 1):
        if num % i == 0:
            return False
    return True


def even_odd(num):
    if num % 2 == 0:
        print("even")
    else:
        print("odd")


print(is_prime(59))
even_odd(13)
#
# Question 7 - Write a program to find second largest number in the list, to count number of even and odd numbers in
# the list, sum all numbers in the list, to remove the duplicates, to reverse list.


def find_second_largest(lst):
    largest_num = lst[0]
    second_largest_num = lst[0]
    for num in lst:
        if num > largest_num:
            second_largest_num = largest_num
            largest_num = num
        elif num > second_largest_num and num != largest_num:
            second_largest_num = num
    return second_largest_num


def count_even_odd(lst):
    even_count = 0
    odd_count = 0
    for num in lst:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count


def find_sum(lst):
    total = 0
    for num in lst:
        total += num
    return total


def remove_duplicates(lst):
    # To remove duplicates from the list we can convert the list to set.
    return list(set(lst))


def reverse_list(lst):
    left = 0
    right = len(lst) - 1
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
    return lst


listOfInt = [4, 5, 5, 9, 13, 45, 23, 9, 98, 13, 58]
print(find_second_largest(listOfInt))
print(count_even_odd(listOfInt))
print(find_sum(listOfInt))
print(remove_duplicates(listOfInt))
print(reverse_list(listOfInt))


# Question 8 - Write a program with asterisk (*) before the parameter (*) indicates that it is a variable-length
# argument. It allows the function to accept an arbitrary number of arguments.

def variable_length(size, *toppings, name=None):
    print("Making Pizza of Size " + str(size))
    print(toppings)
    print(size + " " + name + " Pizza is ready with " + ", ".join(toppings))


variable_length("8 inch", "tomoto", "onion", "chicken", name="3 topping pizza")


# Question 9 - Write a program to return longest sub string without repeating and length of the string.

def longest_substring_without_repeating_chars(input_str):
    longest_substring = ""
    longest_substring_len = 0
    char_dict = {}
    for i in range(0, len(input_str)):
        if input_str[i] not in char_dict.keys():
            char_dict[input_str[i]] = i
        else:
            i = char_dict[input_str[i]]
            char_dict.clear()
        if longest_substring_len < len(char_dict):
            longest_substring_len = len(char_dict)
            longest_substring = str(char_dict.keys())
    print(longest_substring + "     " + str(longest_substring_len))
    return longest_substring_len


print(longest_substring_without_repeating_chars("ahghoihglkvjqdiogfhqerwnoig"))


# Question 10 - Write a program to push all of a given number to the end of the list

def push_num_to_end(lst, num):
    count = 0
    for i in range(len(lst)):
        if lst[i] != num:
            temp = lst[count]
            lst[count] = lst[i]
            lst[i] = temp
            count += 1
    return lst


listWithInt = [4, 5, 5, 9, 13, 45, 23, 9, 98, 13, 58]
print(push_num_to_end(listWithInt, 5))


# Question 11 - Write a program to find if two Strings are Anagram or not

def is_anagram(string1, string2):
    # Convert strings to lists of lowercase characters
    list1 = [char.lower() for char in string1]
    list2 = [char.lower() for char in string2]

    # Sort the lists and compare
    if sorted(list1) == sorted(list2):
        print("True")
    else:
        print("False")


is_anagram("Listen", "Silent")


# Question 12 - Write a program to find the intersection of two Stings using set intersection and using for loop and
# using list comprehension

def intersection_string(string1, string2):
    intersection1 = set(string1.lower())
    intersection2 = set(string2.lower())
    common_chars = set()
    print(intersection1.intersection(intersection2))
    for i in range(len(string1.lower())):
        for j in range(len(string2.lower())):
            if string1[i].lower() == string2[j].lower():
                common_chars.add(string1[i].lower())

    common_chars_list = [char for char in string2.lower() if char in string1.lower()]
    print(str(common_chars))
    print(set(common_chars_list))


intersection_string("Hello", "How are you")
