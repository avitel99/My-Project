#uses a1.txt file
import random

u=list(input('enter text'))
num=int(input('key'))

a=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r','s', 't', 'u', 'v', 'w', 'x', 'y', 'z']
cap=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
s=['$','@','#','%','&']
d=['`', '~', '=', ',', '[', '}', '_', '?', ']']
d1=['(', '-', '/', '+', '!', "'", '{', ';']

for x in range(len(u)):
    if u[x]==' ':
        u[x]=s[random.randint(0,4)]
    elif u[x] in '@#$%&':
        u[x]=' '

    elif u[x] in '1234567890':
        u[x]=(int(u[x])+num)%10

    elif u[x]=='.':
        u[x]=d1[random.randint(0,7)]
    elif u[x] in "(-/+!'{;":
        u[x]='.'

    elif u[x] in "`~=,[}_?]":
        u[x]=d[(d.index(u[x])+num)%9]

    else:
        u[x]=a[(a.index(u[x].lower())+num)%26]

s = open("a1.txt", 'a')
s.write('('+str(num) + ')' + ' ')
for q in range(len(u)):
    s.write(str(u[q]))
s.close()
exit()
