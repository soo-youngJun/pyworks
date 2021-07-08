import os
'''
os.chdir("c:/")
dir = os.popen('dir')
print(dir)
print(dir.read())
'''

# 디렉터리 이름 - 리스트 반환

dirnames =os.listdir('c:/pyworks/exercise')
print(dirnames[-1])    # 리스트로 출력

for dirnames in dirnames:
    print(dirnames)    # 요소 값 출력
