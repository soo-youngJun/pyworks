import glob

# 리스트형으로 반환
data = glob.glob("c:/pyworks/exercise/*.py")
print(data)
print(data[0])

for i in data:
    print(i)
