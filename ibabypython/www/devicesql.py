from models import Device,next_id
from config import configs #1111
import pymysql
pymysql.install_as_MySQLdb()

import MySQLdb
import time
def connect_mysql(node_id,device_name,device_data):
    uid = next_id()
    #conn=MySQLdb.connect(host='localhost',user='root',passwd='wang1234',db='awesome',port=3306)
    conn=MySQLdb.connect(**configs.db)
    cursor=conn.cursor()
    #sql="""INSERT INTO devices(id,node_id,device_name,device_date,created_at) VALUES (uid,node_id,device_name,device_data,time.time())"""
    value=[uid,node_id,device_name,device_data,time.time()]

    try:
        #cursor.execute(sql)
        cursor.execute('INSERT INTO devices values(%s,%s,%s,%s,%s)',value)
        conn.commit()
    #if set==0:#insert
    #cursor.execute('insert into devices (id,node_id,device_name,device_date,created_at) values (%s,%s,%s,%s,%s)',[])
    #if set == 1:
    except:
        conn.rollback()
    conn.close()

def delete_state():
    conn=MySQLdb.connect(**configs.db)
    cursor=conn.cursor()
    sql="delete from states where line='%d'" %(1)
    try:
        cursor.execute(sql)
        conn.commit()

    except:
        conn.rollback()
    conn.close()
def insert_state(line,device1,device2,device3):
    uid = next_id()
    conn=MySQLdb.connect(**configs.db)
    cursor=conn.cursor()
    value=[uid,1,device1,device2,device3]

    try:

        cursor.execute('INSERT INTO states values(%s,%d,%d,%d,%f)',value)
        conn.commit()
    except:
        conn.rollback()
    conn.close()
def state_now():
    
    conn=MySQLdb.connect(**configs.db)
    cursor=conn.cursor()
    sql="select * from states where line='%d'" %(1)
    try:
        cursor.execute(sql)
        result_states=cursor.fetchone()
        states=[0,0,37,0]
        states[0]=result_states[2]
        states[1]=result_states[3]
        states[2]=result_states[4]
        states[3]=result_states[5]
        return states

    except:
        state=[0,0,36.5,0]
        conn.rollback()
        return state
    conn.close()
    

def update_state(node,device,data):
    conn=MySQLdb.connect(**configs.db)
    cursor=conn.cursor()
    if node=="room" and device=="light":
        sql="update states set room_light=not room_light where line='%d'" %(1)
    elif node =="door" and device=="lock":
        sql="update states set door_lock=not door_lock where line='%d'" %(1)
    elif node =="room" and device=="temp":
        sql="update states set room_temp='%f'"%(data)+"where line='%d'" %(1)
    else:
        sql="update states set message='%f'"%(data)+"where line='%d'" %(1)
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()
    conn.close()




    

