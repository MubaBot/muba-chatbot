from chatbot_api.intent import *
import numpy as np
train_data_list={
                'encode' : ['안녕','안녕하세요','안암에 피자 시켜줘','판교에 오늘 피자 주문해줘','오늘 날짜에 호텔 예약 해줄레','모래 날짜에 판교 여행 정보 알려줘'],
                'decode' : ['3','3','0','0','1','2']
             }
train_data_list={
                'encode' : ['안녕','안녕하세요','안암에 피자 시켜줘','판교에 오늘 피자 주문해줘','오늘 날짜에 호텔 예약 해줄레','모래 날짜에 판교 여행 정보 알려줘','뭐해'],
                'decode' : ['3','3','0','0','1','2','10000']
             }

# Intent_l=Intent_learning()
# Intent_l.train(train_data_list)
intent_predict("안농")