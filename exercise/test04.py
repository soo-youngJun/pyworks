# 1번
'''
def is_odd(number):
    if number % 2 == 1:
        return True
    else:
        return False

print(is_odd(8))

# 2번

def avr_number(*args):
    result = 0
    for i in args:
        result += i
        print(i, result)
    return result / len(args)

print(avr_number(1, 2))
print(avr_number(3,2,5,4,1))

# 3번

input1 = int(input("첫번째 숫자를 입력하세요:"))
input2 = int(input("두번째 숫자를 입력하세요:"))

total = input1 + input2
print("두 수의 합은 %d" % total)


# 4번

print("you""need""python")
print("you"+"need"+"python")
print("you", "need", "python")
print("".join(["you", "need", "python"]))


# 5번

f1 = open("test.txt", 'w') # with ~ as로 변경하거나
f1.write("Life is too short")
f1.close()  # close() 필요

f2 = open("test.txt", 'r')
print(f2.read())
f1.close() # close() 필요

# 6번

user_input = input("저장할 내용을 입력하세요: ")
f = open('test.txt', 'a')
f.write(user_input)
f.write("\n")
f.close()
'''

# 7번

f = open('text.txt', 'r')
body = f.read()
f.close()

body = body.replace('java', 'python')

f = open('text.txt', 'w')
f.write(body)
f.close()


