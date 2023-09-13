# https://www.acmicpc.net/problem/1919

str1 = [item for item in input()]
str2 = [item for item in input()]

alphabet = [0]*26

for i in range(26):
    if chr(i+97) in str1 and chr(i+97) in str2:
        alphabet[i] = abs(str1.count(chr(i+97)) - str2.count(chr(i+97)))

    elif chr(i+97) in str1 and chr(i+97) not in str2:
        alphabet[i] = str1.count(chr(i+97))

    elif chr(i+97) not in str1 and chr(i+97) in str2:
        alphabet[i] = str2.count(chr(i + 97))

print(sum(alphabet))