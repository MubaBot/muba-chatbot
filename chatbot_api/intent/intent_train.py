from intent_model import Intent_learning,intent_predict
import numpy as np
train_data_list={
                'encode' : ['안녕','안녕하세요','안암에 피자 시켜줘','판교에 오늘 피자 주문해줘','오늘 날짜에 호텔 예약 해줄레','모래 날짜에 판교 여행 정보 알려줘','뭐해'],
                'decode' : ['3','3','0','0','1','2','10000']
             }
train_data_list={
                'encode' : ['안녕','안녕하세요','<장소>에 <메뉴> 시켜줘','<장소>에 <날짜> <메뉴> 주문해줘','<날짜> 날짜에 호텔 예약 해줄래','<날짜> 날짜에 <장소> 여행 정보 알려줘','뭐해'],
                'decode' : ['3','3','0','0','1','2','4']
             }
Intent_l=Intent_learning()
Intent_l.train(train_data_list)
intent_predict('뭐해')