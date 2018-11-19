import sqlite3

# conn = sqlite3.connect('chatbotdb.db')
# cur = conn.cursor()
def find_intent_hard(msg):
    conn = sqlite3.connect('chatbotdb.db')
    cur = conn.cursor()
    sql="select user_request_intent_id,sentence from user_request_def"
    cur.execute(sql)
    rows=cur.fetchall()
    for intent,sent in rows:
        if msg==sent:
            conn.close()
            return str(intent)
    conn.close()
    return None

def intent_scenario_conformity_check(scenario_id,intent_list):
    conn = sqlite3.connect('chatbotdb.db')
    cur = conn.cursor()
    if(scenario_id==-1 or scenario_id==-2):
        conn.close()
        return False
    sql="select scenario from scenario where scenario_id = ?"
    cur.execute(sql,[scenario_id])

    this_scenario=cur.fetchall()[0][0].split(',')
    print(this_scenario)
    if(this_scenario[:len(intent_list)]==intent_list):
        conn.close()
        return True
    else:
        conn.close()
        return False

def find_scenario_base_priv_intent(intent_list):
    print(len(intent_list))
    conn = sqlite3.connect('chatbotdb.db')
    cur = conn.cursor()
    sql = "select scenario_id,scenario from scenario"
    cur.execute(sql)
    scenario_list=cur.fetchall()
    candidate_scenario_idx_list=[]
    for idx,scene in scenario_list:
        scene=scene.split(',')
        if(intent_list==scene[:len(intent_list)]):
            candidate_scenario_idx_list.append(idx)
    conn.close()
    return candidate_scenario_idx_list

def find_intent_soft_base_scenario(msg,scenario_id,loc):
    conn = sqlite3.connect('chatbotdb.db')
    cur = conn.cursor()
    sql = "select scenario from scenario where scenario_id = ?"
    cur.execute(sql, [scenario_id])
    # print(cur.fetchall()[0][0].split(','))
    try:
        this_scenario = cur.fetchall()[0][0].split(',')
    except Exception as ex:
        conn.close()
        return ex
    print(this_scenario)
    if (len(this_scenario)-1)<loc:
        return False
    predict_intent=this_scenario[loc]
    sql="select keyword from user_request_intent_keyword where user_request_intent_id=?"
    cur.execute(sql,[predict_intent])
    rows=cur.fetchall()
    for keyword in rows:
        if keyword[0] in msg:
            conn.close()
            return predict_intent
    conn.close()
    return False

def find_intent_soft(msg,intent_list):
    conn = sqlite3.connect('chatbotdb.db')
    cur = conn.cursor()
    sql = "select keyword,user_request_intent_id from user_request_intent_keyword"
    cur.execute(sql)
    rows=cur.fetchall()
    for keyword,intent in rows:
        if keyword in msg:
            scene=find_scenario_base_priv_intent(intent_list+[str(intent)])
            if scene:
                conn.close()
                return intent,scene[0]
    conn.close()
    return False,False

def make_response_base_scenario(scenario_id,loc,argv):
    conn = sqlite3.connect('chatbotdb.db')
    cur = conn.cursor()
    sql = "select scenario from scenario where scenario_id = ?"
    cur.execute(sql, [scenario_id])
    response_intent = cur.fetchall()[0][0].split(',')[loc]
    sql="select sentence from muba_response_def where muba_response_intent_id=?"#" union select func from muba_response_intent where muba_response_intent_id=?"
    cur.execute(sql,[response_intent])
    rows=cur.fetchall()
    response_sentence=rows[0][0]
    sql="select func from muba_response_intent where muba_response_intent_id=?"
    cur.execute(sql, [response_intent])
    rows = cur.fetchall()
    func=rows[0][0]
    replace_dic={'food':'[음식%d]','restaurant':'[음식점%d]','menu':'[메뉴%d]','user':'[사용자%d]'}
    for key,replace in replace_dic.items():
        if key not in argv.keys():
            continue
        for idx,data in enumerate(argv[key]):
            find_str=replace %(idx+1)
            # print('aaa'+data)
            response_sentence=response_sentence.replace(find_str,data)
    conn.close()
    return response_sentence,func,response_intent

# print(make_response_base_scenario(4,3,{'restaurant':['교촌치킨']}))
# print(find_scenario_base_priv_intent(['1','18','2']))
# print(find_intent_hard("뭐먹지?"))
# print(intent_scenario_conformity_check('4',['1','18','2']))
# print(find_intent_soft_base_scenario('[음식] 시켜줘','7',1))
# print(find_intent_soft('[음식] 시켜줘라!!',['1']))
