intent_dic={"주문":0,"예약":1,"정보":2,"추천":3}
Default={"장소":"집","날짜":"지금"}
story_slot_entity = {"주문": {"메뉴": None, "장소": Default["장소"], "날짜":Default["날짜"],"음식점":None},#장소 : default-집
                     "예약": {"음식점": None, "날짜": None},
                     "정보": {"음식점": None},
                     "추천":{"장소":None,"메뉴":None}
                     }

import os
with open(os.path.dirname(__file__)+'/food.txt','rb') as f:
    s = f.read().decode()
    menu_list = list(s.split())
print(menu_list)
# menu_list = ['피자', '햄버거', '치킨']
loc_list = ['판교', '야탑', '서현','안암','여기','우리집','일로','집으로']
date_list = ['지금', '내일', '모래',"한시간",]
restaurant_list=["롯데리아","맥날","맥도날드","버거킹","피자헛","엽기떡볶이","엽떡","교촌치킨","내가찜한닭"]
entity_list={"메뉴":menu_list,"장소":loc_list,"날짜":date_list,"음식점":restaurant_list}
noun_attribute={"<메뉴>":['피자','햄버거','치킨'],
                '<장소>':['판교','야탑','서현','안암'],
                '<날짜>':['지금','내일','모레','오늘'],
                }
restaurant_menu={"교촌치킨":["허니콤보","레드콤보","허니 콤보","레드 콤보"]}
