from libs.db.dbconn import getconn

def select_emp():
    conn = getconn()
    cur = conn.cursor()
    sql = "select * from employee"
    cur.execute(sql)
    rs = cur.fetchall()   # 데이터 목록 반환(리스트형)
    for i in rs:
        print(i)
    conn.close()

def select_one():
    conn = getconn()
    cur = conn.cursor()
    sql = "select * from employee where emp_id=?"
    cur.execute(sql, ('e103',))   # 튜플 1개인 경우 마지막 ,(콤마) 필요
    rs = cur.fetchone()   # 데이터 목록 반환(리스트형)
    print(rs)
    conn.close()

def insert_emp():
    conn = getconn()
    cur = conn.cursor()
    '''
    try:
        id = input("아이디를 입력하세요.")
        name = input("이름을 입력하세요.")
        age = int(input("나이를 입력하세요."))
        salary = int(input("연봉을 입력하세요."))
    except:
        print("입력오류로 저장되지 않습니다.")
        conn.commit()
    '''
    sql = "insert into employee(emp_id, name, age, salary) values (?, ?, ?, ?)"
    cur.execute(sql, ('e104', '김산', 22, 5000))
    conn.commit()
    conn.close()

def update_emp():
    conn = getconn()
    cur = conn.cursor()
    sql = "update employee set salary=? where emp_id=?"
    cur.execute(sql, (25000, 'e102'))
    conn.commit()
    conn.close()

def delete_emp():
    conn = getconn()
    cur = conn.cursor()
    sql = "delete from employee where emp_id=?"
    cur.execute(sql, ('e102',))
    conn.commit()
    conn.close()

if __name__=="__main__":
    insert_emp()
    #update_emp()
    delete_emp()
    select_emp()
    #select_one()
