from flask import Flask
from flask import request,make_response,render_template
import json
from chatbot_api.chat_response import *

app = Flask(__name__)


@app.route('/')
def index():
    response = render_template('dashboard.html', foo=42)
    return response


@app.route('/chatbot/api/get_message')
def get_message():
    msg_txt= request.args.get('text', default = '-', type = str)
    scenario = request.args.get('scenario', default=-1, type=int)
    intent_history = request.args.get('intent_history', default='', type=str).split(',')

    argv=request.args.get('argv')
    argv = json.loads(argv)
    print(msg_txt,scenario,intent_history,argv)
    # print(msg_txt,data_dic,intent)
    # if(argv):
    #     argv=json.loads(argv)
    # else:
    #     argv={}
    # res_txt = predict(np.array(inference_embed(msg_txt)).flatten())
    # print(muba_response(msg_txt, scenario, intent_history, argv))
    muba_msg, func, cur_scenario, intent_history,argv=muba_response(msg_txt,int(scenario),intent_history,argv)
    argv=json.dumps(argv)
    #print("@"*100)
    #print(res_txt)
    ret=json.dumps({'msg':muba_msg,'func':func,'argv':argv,'scenario':cur_scenario,'intent_history':','.join(intent_history)})
    print(ret)
    return ret


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
