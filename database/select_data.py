# member 테이블 전체 검색

from libs.db.dbconn import getconn

def select_data():
    conn = getconn()
    cur = conn.cursor()
    # 자료 조회 - SQL DML (select)
    sql = "select name, age from member"
    cur.execute(sql)
    print("데이터 전체 조회")
    rs = cur.fetchall()  # 꺼내온 자료 객체
    for i in rs:
        print(i)
    # select 할 때는 commit 없음
    conn.close()

if __name__ == "__main__":
    select_data()
