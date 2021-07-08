import sqlite3

def getconn():
    conn = sqlite3.connect("c:/pydb/webdb.db")
    return conn

def select_book():
    conn = getconn()
    cur = conn.cursor()
    sql = "select * from t_book"
    cur.execute(sql)
    rs = cur.fetchall()
    for i in rs:
        print(i)
    conn.close()

def insert_book():
    conn = getconn()
    cur = conn.cursor()
    sql = "insert into t_book (title, publisher, page) values (? ,?, ?)"
    cur.execute(sql, ('천개의 파랑', '천선란', 300))
    conn.commit()
    conn.close()

def select_one():
    conn = getconn()
    cur = conn.cursor()
    sql = "select * from t_book where book_no=?"
    cur.execute(sql, (3,))
    rs = cur.fetchone()
    print(rs)
    conn.close()

def update_book():
    conn = getconn()
    cur = conn.cursor()
    sql = "update t_book set page=? where book_no=?"
    cur.execute(sql, (400, 2))
    conn.commit()
    conn.close()

def delete_book():
    conn = getconn()
    cur = conn.cursor()
    sql = "delete from t_book where book_no=?"
    cur.execute(sql, (1,))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    #insert_book()
    #update_book()
    #delete_book()
    #select_book()
    select_one()