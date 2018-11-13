# -*- coding: utf-8 -*-'
# from .response_def import *


from chatbot_api.Markov_response.test import Markov_response
from chatbot_api.scenario_base.replace_sentence import *
from chatbot_api.scenario_base.find_intent import *
MR = Markov_response()


def muba_response(msg, cur_scenario, priv_intent,argv):
    # 메시지가 음식 이름일때 -> 그 음식을 판매하는 근처의 음식점 보여주기
    orig_msg=msg
    if 'restaurant' in argv.keys():
        restaurant=argv['restaurant']
    else:
        msg,restaurant=replace_restaurant(msg)

    if restaurant:
        if 'restaurant' in argv.keys():
            argv['restaurant']=restaurant+argv['restaurant']
        else:
            argv['restaurant']=restaurant
        msg,menu=replace_menu(msg,restaurant)
        if menu:
            if 'menu' in argv.keys():
                argv['menu'] = menu + argv['menu']
            else:
                argv['menu'] = menu
    msg,food=replace_food(msg)
    if food:
        if 'food' in argv.keys():
            argv['food'] = food + argv['food']
        else:
            argv['food'] = food
    # print(msg,argv)
    # print('scenario'+str(cur_scenario))
    # print('priv_inent',priv_intent)
    intent=find_intent_hard(msg)
    if intent:

        if(intent_scenario_conformity_check(cur_scenario,priv_intent+[intent])):
            # print('ho',cur_scenario,len(priv_intent),argv)
            priv_intent.append(intent)
            muba_msg,func,muba_intent=make_response_base_scenario(cur_scenario,len(priv_intent),argv)
            priv_intent.append(muba_intent)
            return muba_msg,func,cur_scenario,priv_intent,argv
        else:
            scenario_candidate_list=find_scenario_base_priv_intent(priv_intent+[intent])
            # print(scenario_candidate_list)
            # print(priv_intent+[intent])

            if len(scenario_candidate_list)>0:
                cur_scenario=scenario_candidate_list[0]
                priv_intent.append(intent)
                muba_msg, func,muba_intent = make_response_base_scenario(cur_scenario, len(priv_intent),argv)
                priv_intent.append(muba_intent)
                return muba_msg, func, cur_scenario, priv_intent,argv
            else:
                #시나리오에 없는.. 시나리오 -> 새로운 시나리오 시작
                ##TODO bug 처음부터 없는거 들어오면 다 무한루프)
                new_argv={'user':argv['user']}
                # input('>')
                return muba_response(orig_msg,-1,['1',],new_argv)#muba_msg, func, cur_scenario, priv_intent

    else:
        if cur_scenario!=-1:
            intent=find_intent_soft_base_scenario(msg,cur_scenario,len(priv_intent))
            if not intent:
                scenario_candidate_list=find_scenario_base_priv_intent(priv_intent)
                for scenario_candidate in scenario_candidate_list:
                    intent = find_intent_soft_base_scenario(msg,cur_scenario,len(priv_intent))
                    if intent:
                        cur_scenario=scenario_candidate
                        priv_intent.append(intent)
                        muba_msg, func, muba_intent = make_response_base_scenario(cur_scenario, len(priv_intent),argv)
                        priv_intent.append(muba_intent)
                        return muba_msg, func, cur_scenario, priv_intent,argv
                if not intent:
                    muba_msg=MR.make_reply(msg)
                    func=''
                    return muba_msg,func,cur_scenario,priv_intent,argv
        else:
            print(msg,priv_intent)
            intent,scenario=find_intent_soft(msg,priv_intent)

            if not intent:
                muba_msg = MR.make_reply(msg)
                func = ''
                return muba_msg, func, cur_scenario, priv_intent,argv
            else:
                priv_intent.append(intent)
                muba_msg, func, muba_intent = make_response_base_scenario(cur_scenario, len(priv_intent),argv)
                priv_intent.append(muba_intent)
                return muba_msg, func, cur_scenario, priv_intent,argv




