# 1번

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
'''
input1 = int(input("첫번째 숫자를 입력하세요:"))
input2 = int(input("두번째 숫자를 입력하세요:"))

total = input1 + input2
print("두 수의 합은 %d" % total)


# 4번

print("you""need""python")
print("you"+"need"+"python")
print("you", "need", "python")
print("".join(["you", "need", "python"]))
'''

