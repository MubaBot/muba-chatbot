from konlpy.tag import Mecab
from entity_def import *




def getentity(strbuf):
    #일단 명사만 추출
    #TODO 학습모델로 바꿔야함 https://github.com/alfredfrancis/ai-chatbot-framework/blob/master/app/nlu/entity_extractor.py
    mecab = Mecab('/usr/local/lib/mecab/dic/mecab-ko-dic')
    M=mecab.pos(strbuf)
    tagged_text = ''
    for pos_tags in M:
        if (pos_tags[1] in ['NNG', 'MAG', 'NNP', 'SL'] and len(pos_tags[0]) > 1):
            feature_value = pos_tags[0]
            tagged_text = tagged_text + pos_tags[0] + ' '
    return tagged_text
print(getentity('교촌치킨 시킬거야'))
def clear_slot(intent_idx):
    for intent_str, idx in intent_dic.items():
        if idx == intent_idx:
            intent=intent_str
            break
    for key in story_slot_entity[intent].keys():
        story_slot_entity[intent][key]=None
    return

def ismenu(msg):
    mecab = Mecab('/usr/local/lib/mecab/dic/mecab-ko-dic')
    M = mecab.pos(msg)
    menu=[]
    for pos_tag in M:
        if (pos_tag[1] in ['NNG', 'NNP', 'SL', 'MAG']):  # 명사, 영어만 사용
            if pos_tag[0] in menu_list:  # 메뉴 List 에서 검색
                menu.append(pos_tag[0])
    return menu
def remove_menu(intent_idx):
    for intent_str, idx in intent_dic.items():
        if idx == intent_idx:
            intent=intent_str
            break
    slot_value = story_slot_entity.get(intent)
    for menu in entity_list["메뉴"]:
        slot_value["메뉴"].remove(menu)
    return


def getentity_slot(intent_idx, strbuf):
    mecab = Mecab('/usr/local/lib/mecab/dic/mecab-ko-dic')
    for intent_str, idx in intent_dic.items():
        if idx == intent_idx:
            intent=intent_str
            break
    slot_value = story_slot_entity.get(intent)
    added=0
    M = mecab.pos(strbuf)
    ## 조사를 안쓰는 경우 피자 같은 단어를 명사로 해석안함.. -> 꼼수로 단어단위로 잘라서 해결 + mecab에 고유명사 추가해야함
    # print(M)
    for pos_tag in M:
        if (pos_tag[1] in ['NNG', 'NNP', 'SL', 'MAG']):  # 명사, 영어만 사용
            for key in slot_value:

                if pos_tag[0] in entity_list[key]:  # 메뉴 List 에서 검색
                    added = 1
                    if slot_value[key] is None:
                        slot_value[key] = [pos_tag[0]]
                    else:
                        slot_value[key].append(pos_tag[0])

    M=strbuf.split(' ')
    for pos_tag in M:
        for key in slot_value:
            if pos_tag[0] in entity_list[key]:  # 메뉴 List 에서 검색
                added = 1
                if slot_value[key] is None:
                    slot_value[key] = [pos_tag[0]]
                else:
                    slot_value[key].append(pos_tag[0])

    return added,slot_value

def set_noun2slot(msg):
    slot_value={}
    attr_key = noun_attribute.keys()
    for key in attr_key:
        for noun in noun_attribute[key]:
            if noun in msg:
                msg=msg.replace(noun,key)
                if key in slot_value:
                    slot_value[key]+=[noun]
                else:
                    slot_value[key]=[noun]

    return msg,slot_value
print(set_noun2slot('안암에 피자 시켜줘'))
def set_slot2noun(msg,slot_value):
    attr_key = list(noun_attribute.keys())
    for key in attr_key:
        if key in msg:
            msg=msg.replace(key,slot_value[key].pop(0))
    return msg

def set_noun_list(data_list):
    attr_key=list(noun_attribute.keys())
    for i,val in enumerate(data_list):
        for key in attr_key:
            if val in noun_attribute[key]:
                data_list[i]=key
    return data_list





# print(getentity_slot("주문","판교에 피자를 시켜줘"))

#"판교에 피자 시켜줘 "= [('판교', 'NNG'), ('에', 'JKB'), ('피', 'VV'), ('자', 'EC'), ('시켜', 'VV+EC'), ('줘', 'VX+EC')]
