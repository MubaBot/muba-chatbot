from openpyxl import *
import string
import sqlite3,os
# PROJ_DIR='C:\\Users\\USER\\Desktop\\vmshared\\chatbot'

wb = Workbook()      # 워크북을 생성한다.
filename='test.xlsx'
wb=load_workbook(filename=filename)
column=string.ascii_uppercase[1:]
def update_user_request_intent():
    #user_request_intent
    conn = sqlite3.connect('chatbotdb.db')
    cur = conn.cursor()

    for col in column:
        d = wb['user_request_def'][col+'2'].value

        if d:
            sql = "insert into user_request_intent (intent_name) values (?)"
            print(type(d))
            cur.execute(sql,[d])
            print(d)
        else:
            break
    conn.commit()
    conn.close()
def update_user_request_def():
    #user_request_def
    conn = sqlite3.connect('chatbotdb.db')
    cur = conn.cursor()
    sql_insert = "insert into user_request_def (user_request_intent_id,sentence) values (?,?)"
    data_list=[]
    for col in column:
        intent=wb['user_request_def'][col+'2'].value
        if not intent:
            break

        sql = "select user_request_intent_id from user_request_intent where intent_name=?"

        cur.execute(sql,[intent])
        rows=cur.fetchall()
        intent_id=(rows[0][0])
        row=3
        while(1):
            d=wb['user_request_def'][col+str(row)].value
            if d:
                data_list.append((intent_id,d))
                # print(d)
                row+=1
            else:
                break
    cur.executemany(sql_insert,data_list)
    conn.commit()
    conn.close()
#muba_response_intent
def update_muba_response_intent():
    #user_request_intent
    conn = sqlite3.connect('chatbotdb.db')
    cur = conn.cursor()

    for col in column:
        d = wb['muba_response_def'][col+'2'].value

        if d:
            sql = "insert into muba_response_intent (intent_name) values (?)"
            print(type(d))
            cur.execute(sql,[d])
            print(d)
        else:
            break
    conn.commit()
    conn.close()
#muba_response_def
def update_muba_response_def():
    # user_request_def
    conn = sqlite3.connect('chatbotdb.db')
    cur = conn.cursor()
    sql_select_check="select from muba_response_def where muba_response_intent_id=? and sentence=?"

    sql_insert = "insert into muba_response_def (muba_response_intent_id,sentence) values (?,?)"
    data_list = []
    for col in column:
        intent = wb['muba_response_def'][col + '2'].value
        if not intent:
            break


        sql = "select muba_response_intent_id from muba_response_intent where intent_name=?"

        cur.execute(sql, [intent])
        rows = cur.fetchall()
        intent_id = (rows[0][0])
        row = 3
        while (1):
            d = wb['muba_response_def'][col + str(row)].value
            if d:
                data_list.append((intent_id, d))
                # print(d)
                row += 1
            else:
                break
    cur.executemany(sql_insert, data_list)
    conn.commit()
    conn.close()

# update_muba_response_intent()
# update_muba_response_def()