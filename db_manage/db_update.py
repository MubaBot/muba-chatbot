import sqlite3, json
def add_scenario(scenario_json):
    conn = sqlite3.connect('chatbotdb.db')
    cur = conn.cursor()
    '''
    example
    {
        "scenario": [
            {
                "who": "muba",
                "intent": "인사"
            },
            {
                "who": "user",
                "intent": "음식이름"
            },
            {
                "who": "muba",
                "intent": "특정 음식 음식점 보여주기"
            },
            {
                "who": "user",
                "intent": "음식점이름"
            },
            {
                "who": "muba",
                "intent": "음식점 메뉴 보여주기"
            },
            {
                "who": "user",
                "intent": "메뉴주문"
            },
            {
                "who": "muba",
                "intent": "주문확인"
            }
        ],
    }
    '''
    try:
        scene_list=scenario_json['scenario']
    except:
        return '[error] request_error'
    scenario_intent_idx_list=[]
    for idx,scene in enumerate(scene_list):
        if scene["who"]=="user":
            sql = "select user_request_intent_id from user_request_intent where intent_name=?"
        if scene["who"]=="muba":
            sql = "select muba_response_intent_id from muba_response_intent where intent_name=?"
        cur.execute(sql, [scene["intent"]])
        rows = cur.fetchall()
        if len(rows)==0:
            return "[error] %s intent isn't exit" %scene["intent"]
        # scenario_json["scenario"][idx]["intent_id"]=rows[0][0]
        scenario_intent_idx_list.append(str(rows[0][0]))


    scenario=json.dumps(scenario_json)
    scenario=','.join(scenario_intent_idx_list)
    sql = "insert into scenario (scenario) values (?)"

    cur.execute(sql, [scenario])
    conn.commit()
    conn.close()
    return "success"
def add_user_request_intent(table,intent):
    conn = sqlite3.connect('chatbotdb.db')
    cur = conn.cursor()

    sql = "insert into user_request_intent (intent_name) values (?)"

    cur.execute(sql, [intent])
    conn.commit()
    conn.close()
def add_muba_response_intent(intent):
    conn = sqlite3.connect('chatbotdb.db')
    cur = conn.cursor()

    sql = "insert into muba_response_intent (intent_name) values (?)"

    cur.execute(sql, [intent])
    conn.commit()
    conn.close()

def add_user_request_def(intent,sentence):
    conn = sqlite3.connect('chatbotdb.db')
    cur = conn.cursor()

    sql_insert = "insert into user_request_def (user_request_intent_id,sentence) values (?,?)"
    sql = "select user_request_intent_id from user_request_intent where intent_name=?"

    cur.execute(sql, [intent])
    rows = cur.fetchall()
    intent_id = (rows[0][0])

    cur.execute(sql_insert, (intent_id,sentence))
    conn.commit()
    conn.close()


def add_muba_reqsponse_def(intent, sentence):
    conn = sqlite3.connect('chatbotdb.db')
    cur = conn.cursor()

    sql_insert = "insert into muba_response_def (muba_response_intent_id,sentence) values (?,?)"
    sql = "select muba_response_intent_id from muba_response_intent where intent_name=?"

    cur.execute(sql, [intent])
    rows = cur.fetchall()
    intent_id = (rows[0][0])

    cur.execute(sql_insert, (intent_id, sentence))
    conn.commit()
    conn.close()
