'''
def getpage():
    try:
        x = int(input("게시글 총 건수:"))
        y = int(input("한 페이지에 보여줄 게시글수:"))
        if x % y == 0:
            print(abs(x/y) + "페이지가 필요합니다.")
        else:
            print((x/y)+1, "페이지가 필요합니다.")
    except ValueError as e:
        print(e)

getpage()
'''

def getpage(x, y):
    if x % y == 0:
        return x // y
    else:
        return x // y + 1

print(getpage(5, 10))
print(getpage(10, 10))
print(getpage(15, 10))
print(getpage(20, 10))
print(getpage(25, 10))