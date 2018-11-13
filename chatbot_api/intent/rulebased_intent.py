# from .rulebased_intent_data import
# -*- coding: utf-8 -*-
intent_dic={"주문":0,"예약":1,"정보":2,"추천":3,"취소":4}
intent2word_set={
    "주문":["배달 부탁해","배달좀","시켜줘","배달해주삼","배달해줘","주문해줘","주문좀","시킬래","시킬","주문할게"],
    "예약":["예약 해줘","예약해줘","예약할게","예약해주세요"],
    "정보":["좀 알려줘","알려주라","정보"],
    "추천":["추천","추천좀","추천해줘","추천해주라","먹고싶다","먹고싶어","먹을래","뭐 먹지","배고파","뭐먹지"],
    "취소":["빼줘","취소해줘","안먹을래","안 먹을래","뺄래","빼주세요","취소해주세요"]
}
tail=["좀","해","해줘","해도","해라","해줘요","해주세요"]

def intent_rulebased_predict(msg):
    for intent in intent_dic.keys():
        for word in intent2word_set[intent]:
            if word in msg:
                return intent_dic[intent]
    return -1
