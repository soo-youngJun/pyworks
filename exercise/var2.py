# ** 키워드 매개 변수 -> 딕셔너리 구조

def ranking(**kwargs):
    print(kwargs)

ranking(first='kang', second='han', third='elsa')