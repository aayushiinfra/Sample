# Code for checking if two strings are anagrams

s1 = input ("Enter string1")
s2 = input ("Enter string2")

def verify( s1, s2):
    if sorted(s1)== sorted(s2):
        print("strings are anagrams")
    else:
        print("strings are not anagrams")

verify (s1, s2)
