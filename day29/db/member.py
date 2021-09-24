# member table 생성 및 관리
from  day28.libs.dbconn import getconn
import sqlite3

def create_table():
    # conn = sqlite3.connect("c:/webdb/webdb.db") # db 연결 객체 생성(import getconn 안할때)
    conn = getconn() # import getconn할때
    cur = conn.cursor() # db 작업객체 생성
    sql = """
        CREATE TABLE member(
            memberId char(5) PRIMARY KEY,
            passwd   char(8) NOT NULL,
            name     TEXT NOT NULL,
            age      INTEGER,
            reg_date DATELINE DEFAULT CURRENT_TIMESTAMP
        )
    """
    cur.execute(sql)
    conn.commit()
    conn.close()

def insert_member():
    # conn = sqlite3.connect("c:/webdb/webdb.db")
    conn = getconn()
    cur = conn.cursor()
    sql = "INSERT INTO member(memberId, passwd, name, age) VALUES (?, ?, ?, ?)"
    cur.execute(sql, ('10003', 'c1234567', '콩쥐', 17))
    conn.commit()
    conn.close()

def select_member():
    conn = getconn()
    cur = conn.cursor()
    sql = "SELECT * FROM member"
    cur.execute(sql)
    rs = cur.fetchall()
    for i in rs:
        print(i)
    conn.close() # select는 commit 필요 X

# 특정한 1개 검색 - 아이디와 비밀번호 가져오기
def select_one():
    conn = getconn()
    cur = conn.cursor()
    sql = "SELECT memberId, passwd FROM member WHERE memberId = ?"
    cur.execute(sql, ('10002', ))  # 1개 매핑 시 , 필수
    rs = cur.fetchone() # 1개의 정보를 반환받음
    print(rs)
    conn.commit()
    conn.close()

def update_member():
    conn = getconn()
    cur = conn.cursor()
    sql = "UPDATE member SET age = ? WHERE memberId = ?"
    cur.execute(sql, (37, '10001'))
    conn.commit()
    conn.close()

def delete_member():
    conn = getconn()
    cur = conn.cursor()
    sql = "DELETE FROM member WHERE memberId = ?"
    cur.execute(sql, ('10002', ))
    conn.commit()
    conn.close()

# create_table()
# insert_member()
# update_member()
delete_member()
# select_one()
select_member()


