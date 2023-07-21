# Use String Indexing in Python to check if a String is a Palindrome

a_string = 'Was it a car or a cat I saw'

def palindrome(a_string):
    a_string = a_string.lower().replace(' ', '')
    return a_string == a_string[::-1]

print(palindrome(a_string))

# Returns: True