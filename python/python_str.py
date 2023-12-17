# 1. write a python program to remove given character from string

x = ("marolix")
y = "o"
op = x.replace(y,"")
print(op)

print("-------------------------------------------------------------------------------")

# 2. python program of count the given character in string  
str = "maroliix"
char = "i"
count = 0
for i in range(len(str)):
    if(str[i]==char):
        count = count+1
print(count)

print("-----------------------------------------------------------------------------------")

# 3. python program check if two string are Anagrams

str1 = "listen"
str2 = "silent"

if sorted(str1) == sorted(str2):
    print("the string are Anagrams")
else:
    print("the string are not in Anagrams")

print("-----------------------------------------------------------------------------------")

# 4. python program to check the string in palidrom

str1 = "radar"
word_lower = str1.lower()
reverse = word_lower[::-1]

if str1 == reverse:
    print("it's a palindrome")
else:
    print("it's not a palindrome")

print("-----------------------------------------------------------------------------------")

# 5. check if a given character is a vowel or constant

char = "a"
char_lower = char.lower()       # Convert the character to lowercase for case-insensitive comparison
is_aplpha = char_lower.isalpha()

if char_lower in 'aeiou':
    print(f"the character '{char}' is a vowel")
else:
    print(f"the character '{char}' is a constant")

print("-----------------------------------------------------------------------------------")

# 6. check if a given character is a digit

char = "5"
word = char.isdigit()
print(word)

print("-----------------------------------------------------------------------------------")

# 7. Replace spaces with a given character

str1 = "hey this is good"
change = "-"
result = str1.replace(" ",change)
print(result)

print("-----------------------------------------------------------------------------------")

# 8. convert lowercase character to uppercase in a string

stri = "hello"
word = stri.upper()
print(word)

print("-----------------------------------------------------------------------------------")

# 9. convert lowercase vowels to uppercase string

stri = "hello marolix"
vowels = "aeious"
word = ""

for char in stri:
    if char in vowels:
        word += char.upper()
    else:
        word += char
print(word)

print("-----------------------------------------------------------------------------------")

# 10. Delete vowels in given string

strg = "hello marolix"
vowels= "aeious"
result = ""

for char in strg:
    if char not in vowels:
        result += char
print(result)

print("-----------------------------------------------------------------------------------")

# 11. Counting the occurance of vowels and consonants in a string

string1 = "hello marolix"
vowels = "aeious"
consonant = "bdcfghjklsqrtyzxmnv"
vowels_count = 0
consonant_count = 0

for char in string1:
    if char in vowels:
        vowels_count += 1
    elif char in consonant:
        consonant_count += 1
        
print(f"vowels: {vowels_count},consonant: {consonant_count}")

print("-----------------------------------------------------------------------------------")

# 12. count Alphabets,Digits,SpecialCahracters

ads = "venkat@123"
alphabet = 0
digits = 0
spl_character = 0

for char in ads:
    if char.isalpha():
        alphabet += 1
    elif char.isdigit():
        digits += 1
    else:
        spl_character += 1

print("the alphabet of count time is",alphabet)
print("the digit of the count is: ",digits)
print("the special character of the count is :",spl_character)

print("-----------------------------------------------------------------------------------")

# 13. Remove repeated character from string

character = "establishment assistent"
unique_charc = ""

for char in character:
    if char not in unique_charc:
        unique_charc += char
print(unique_charc)

print("-----------------------------------------------------------------------------------")

# 14. separate the characters in given string

original = "hello python"
charac = ' '.join(original)
print(charac)

print("-----------------------------------------------------------------------------------")

# 15. Remove blank space from a string

string1 = "hello world"
words = string1.replace(" ","")
print(words)
print("-----------------------------------------------------------------------------------")

# 16.concatenate two strings using the join() method

str1 = "hello"
str2 = "marolix"
concate=''.join([str1,str2])
print(concate)

print("-----------------------------------------------------------------------------------")

# 17. conateneate two strings without using join() method

st1 = "hello"
st2 = "world"
concatne = st1+st2
print(concatne)

print("-----------------------------------------------------------------------------------")

# 18. copy one string to another string 
str1 = "hello venkat"
copied = str1
print(copied)

print("-----------------------------------------------------------------------------------")

# 19. sort character of a string in ascending order

string1 = "programing"
sort = ''.join(sorted(string1))
print(sort)

print("-----------------------------------------------------------------------------------")

# 20. sort charatcer of a string in decending order

sting2 = "marolix"
sorts = ''.join(sorted(sting2,reverse=True))
print(sorts)

print("-----------------------------------------------------------------------------------")

# 21.calculate the sum of integers in a string

num = ("123445")
sum_of_num = 0

for char in num:
    if char.isdigit:
        sum_of_num += int(char)
print(sum_of_num)

print("-----------------------------------------------------------------------------------")

# 22.print all non-repeating character in a string

strings = "programming"
non_repeating = []

for char in strings:
    if strings.count(char) == 1:
        non_repeating.append(char)
        
result = ''.join(non_repeating)
print(result)