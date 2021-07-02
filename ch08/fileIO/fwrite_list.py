
f = open('c:/pyfile/2021kbo.txt', 'w')

team = ['기아', '삼성', 'LG', 'NC', '키움', 'KT', 'SSG', '롯데']
'''
for i in team:
    f.write(i + "\n")

'''
# range() 함수

n = len(team)
for i in range(n):
    f.write(team[i] + " ")
f.close()

f = open('c:/pyfile/2021kbo.txt', 'r')
date = f.read()
print(date)
f.close()