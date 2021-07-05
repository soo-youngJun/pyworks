# 자료 삽입 코드

from libs.db.dbconn import getconn

def insert_data():
    conn = getconn()
    cur = conn.cursor()
    # 자료 추가 - SQL
    cur.execute("insert into member values (103, '황진이', 25)")
    cur.execute("insert into member values (104, '성춘향', 22)")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    insert_data()