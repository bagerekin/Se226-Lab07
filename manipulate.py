import string

def reverse_string(s):
    return s[::-1]

def capitalize_words(s):
    return s.title()

def remove_punctuation(s):
    return ''.join([c for c in s if c not in string.punctuation])
