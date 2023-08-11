# Code for checking if two strings are anagrams

s1 = input ("\tEnter string1\t\n")
s2 = input ("\tEnter string2\t\n")

def verify( s1, s2):
    if sorted(s1)== sorted(s2):
        print("\nstrings are anagrams\n")
    else:
        print("\t\n Yay !!! Strings are not anagrams \n")

verify (s1, s2)
