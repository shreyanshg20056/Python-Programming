# upper(): It is used to upper case all characters of the string
# len(): It is used to measure length of the string
# When we use these functions that gives different output then these functions create a another string 
# lower(): It is used to lower case all characters of the string
# strip(): It is used to remove the character from the entire string that we given.
# rstrip(): It is used to remove the character from the right string that we given.
# lstrip(): It is used to remove the character from the left string that we given.
# replace(): It is used to replace characters or any words inside string
# split(): It splits character that are divided with whitespaces and stored each as element of list.
# capitalize(): It capitals the first character of the string.
# centre(): It aligns the string to the centre as per the parameters given by the user.
# count(): It counts the no. of occurence of that character inthe string.
# endswith(): It checks whether the given character ends the string or not.
# find(): If given chharacter is present in string then it return its index otherwise -1.
# index(): If given chharacter is present in string then it return its index otherwise it return error!!.
# isalnum(): It returns true only if string consist of a-z,A-Z,0-9.Otherwise if it consist a whitespaces and special characters then it return false.
# isalpha(): It returns true only if string consist of a-z,A-Z.Otherwise if it consist a whitespaces,0-9,and special characters then it return false.
# islower(): It return true only if string consist of lower alphabet characters otherwise it returns false.
# isprintable(): It returns true if there is all character that can print in terminal such as these characters which didnt print(\n,\t,etc...). 
# isspace(): It returns true only if the full string consist only whitespaces.
# istitle(): It returns true if every letter of each word is capitalize.
# isupper(): It returns true if all characters are in upper case otherwise it returns false.
# startswith(): It returns true if given character is the character which starts the strings.
# swapcase(): It Swaps upeer case to lower case and lower case to upper case.
# title(): It converts every first character of each words into upper case.
n = "tgfd\n"
s = "!!!! CODING !!!!!"
s1 = "Coding Is Important"
m = "python programming"
w = "    "
print(s.strip("!"))
print(s.rstrip("!"))
print(s.lstrip("!"))
print(s.replace("!","#"))
print(s.split(" "))
print(m.endswith("n"))
print(m.capitalize())
print(len(s.center(50)))
print(s.count("!"))
print(m.find("h"))
print(m.index("t"))
print(m.isalnum())
print(m.isalpha())
print(n.isalnum())
print(n.isalpha())
print(n.islower())
print(s.isprintable())
print(n.isprintable())
print(w.isspace())
print(s1.istitle())
print(s1.isupper())
print(m.startswith("p"))
print(s1.swapcase())
print(m.title())