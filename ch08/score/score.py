with open('scorelist.txt', 'w') as f:
    while True:
        try:
            st = input("성적을 저장할까요?(y/n):")
            if st == 'y' or st == 'Y':
                name = input("이름 입력 : ")
                kor = int(input("국어 점수 : "))
                math = int(input("수학 점수 : "))
                #avg = (kor + math) / 2

                f.write(name + ' ')
                f.write(str(kor) + ' ')
                f.write(str(math) + '\n')
                #f.write(str(avg) + '\n')
            elif st == 'n' or st == 'N':
                print("입력을 종료합니다.")
                break
            else:
                print("잘못된 입력입니다. 다시 입력해주세요")
        except ValueError:
            print("잘못된 입력입니다. 다시 입력해주세요")

'''
with open('scorelist.txt', 'r') as f:
    print(f.read())
'''
