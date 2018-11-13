from flask import Flask,redirect
from flask import request,make_response,render_template
import json
from chatbot_api.chat_response import *
import sqlite3
from flask import _app_ctx_stack
import os


app = Flask(__name__)
DATABASE = os.getcwd()+'/chatbotdb.db'

def get_db():
    top = _app_ctx_stack.top
    if not hasattr(top, 'sqlite_db'):
        top.sqlite_db = sqlite3.connect(DATABASE)
    return top.sqlite_db

def query_execute(q,arg):
    conn = get_db()
    cur = conn.cursor()
    cur.execute(q,arg)
    conn.commit()
    cur.close()

@app.teardown_appcontext
def close_connection(exception):
    top = _app_ctx_stack.top
    if hasattr(top, 'sqlite_db'):
        top.sqlite_db.close()

@app.route('/chatbot/chatbot')
def chatbot():
    response = render_template('dashboard.html', foo=42)
    return response

@app.route('/')
def index():
    return redirect('/chatbot/db_manage')


@app.route('/chatbot/api/get_message')
def get_message():
    msg_txt= request.args.get('text', default = '-', type = str)
    scenario = request.args.get('scenario', default=-1, type=int)
    intent_history = request.args.get('intent_history', default='', type=str).split(',')

    argv=request.args.get('argv')
    argv = json.loads(argv)
    print('hi'+msg_txt,scenario,intent_history,argv)
    muba_msg, func, cur_scenario, intent_history,argv=muba_response(msg_txt,int(scenario),intent_history,argv)
    argv=json.dumps(argv)
    #print("@"*100)
    #print(res_txt)
    ret=json.dumps({'msg':muba_msg,'func':func,'argv':argv,'scenario':cur_scenario,'intent_history':','.join(intent_history)})
    print(ret)
    return ret

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

@app.route('/chatbot/db_manage')
def db_manage():
    tables = ['scenario', 'muba_response_def', 'user_request_def', 'response_func']
    cur_table = request.args.get('table', default='muba_response_def', type=str)
    intent_list=[]
    if cur_table=='muba_response_def':
        response_def=query_db('select * from muba_response_def')
        for idx,rd in enumerate(response_def):

            x=query_db('select intent_name,func from muba_response_intent where muba_response_intent_id  = ?',[rd[1]],one=True)
            # print(x)
            if len(x)==2:
                response_def[idx]=rd+(x[0],x[1],)
        table_info=response_def
        intent_list=query_db('select muba_response_intent_id,intent_name from muba_response_intent')
    if cur_table=='user_request_def':
        request_def=query_db('select * from user_request_def')
        for idx,rd in enumerate(request_def):

            x=query_db('select intent_name from user_request_intent where user_request_intent_id  = ?',[rd[1]],one=True)
            # print(x)
            if len(x)==1:
                request_def[idx]=rd+(x[0],)
        table_info=request_def
        intent_list = query_db('select user_request_intent_id,intent_name from user_request_intent')
    if cur_table=='scenario':
        user_intent = query_db('select user_request_intent_id,intent_name from user_request_intent')
        muba_intent = query_db('select muba_response_intent_id,intent_name from muba_response_intent')
        scenario=query_db('select * from scenario')
        idx=0
        for id,scene in scenario:
            # print(scene)
            scene=scene.split(',')[1:]
            intent_str_list=[]


            for i,s in enumerate(scene):
                if i%2==1:
                    x=query_db('select intent_name from muba_response_intent where muba_response_intent_id=?',[s],one=True)
                    if x:
                        y=query_db('select sentence from muba_response_def where muba_response_intent_id=?',[s])

                        intent_str_list.append(('muba',x[0],y))
                else:
                    x = query_db('select intent_name from user_request_intent where user_request_intent_id=?', [s],
                                 one=True)
                    if x:

                        y = query_db('select sentence from user_request_def where user_request_intent_id=?', [s])

                        intent_str_list.append(('user', x[0],y))
            scenario[idx]=scenario[idx]+(intent_str_list,)
            idx+=1
        print(scenario)
        table_info=scenario
        response = render_template('manage.html', table_info=table_info, tables=tables, cur_table=cur_table,user_intent=user_intent,muba_intent=muba_intent)
        return response




    response = render_template('manage.html',table_info=table_info,tables=tables,cur_table=cur_table,intent_list=intent_list)
    return response



@app.route('/chatbot/db_manage/item_add',methods=['POST'])
def item_add():
    table_name=request.form['cur_table']
    id=request.form.get('intent_id',type=int)
    sentence=request.form.get('sentence',type=str)
    if id and sentence:
        if table_name=='muba_response_def':
            query_execute('insert into muba_response_def (muba_response_intent_id,sentence) values (?, ?);',[id,sentence])
        if table_name=='user_request_def':
            query_execute('insert into user_request_def (user_request_intent_id,sentence) values (?, ?);',[id,sentence])

    return redirect('/chatbot/db_manage?table='+table_name)

@app.route('/chatbot/db_manage/item_delete')
def item_delete():
    table_name=request.args.get('table')
    id=request.args.get('id')
    if table_name=='muba_response_def' and id:
        print('hihi')
        query_execute('delete from muba_response_def where sentence_id=(?)',[id])
    elif table_name=='user_request_def' and id:
        query_execute('delete from user_request_def where sentence_id=?', [id])

    return redirect('/chatbot/db_manage?table='+table_name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
