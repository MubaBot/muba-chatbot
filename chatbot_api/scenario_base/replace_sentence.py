import sqlite3

# conn = sqlite3.connect('chatbotdb.db')
# cur = conn.cursor()

def combine_restaurtant_loc(rest,loc):
    _loc,__loc=loc+"점",loc+"에"
    return [rest+" "+_loc,_loc+" "+rest,__loc+" "+rest,rest+" "+loc,loc+" "+rest]

def get_cur_loc():
    #TODO 서버에서 현재위치 받아오기
    return "안암"

def replace_restaurant(msg):
    sql="select name,franchisee_loc from restaurant"
    conn = sqlite3.connect('chatbotdb.db')
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    find_rest=[]
    idx=1
    for rest,loc in rows:
        if not loc:
            if rest in msg:
                msg=msg.replace(rest,'[음식점{}]'.format(str(idx)))
                idx+=1
                # loc=get_cur_loc()
                find_rest.append((rest))

        else:
            loc_list=loc.split(',')
            b=0
            for loc in loc_list:

                if loc in msg:
                    for rest_ in combine_restaurtant_loc(rest,loc):
                        if rest_ in msg:
                            msg=msg.replace(rest_,'[음식점{}]'.format(str(idx)))
                            idx+=1
                            find_rest.append("%s %s점" %(rest,loc))
                            b=1
                            break
            if b==0:
                if rest in msg:
                    msg=msg.replace(rest, '[음식점{}]'.format(str(idx)))
                    idx+=1
                    # loc = get_cur_loc()
                    find_rest.append("%s" %(rest))
    conn.close()
    return msg,find_rest

def replace_menu(msg,restaurant_list):
    conn = sqlite3.connect('chatbotdb.db')
    cur = conn.cursor()
    idx=1
    for rest in restaurant_list:
        rest=rest.split(' ')[0]
        sql="select menu from restaurant where name=?"
        cur.execute(sql,[rest])
        menu=cur.fetchall()[0][0]
        if not menu:
            conn.close()
            return msg,[]
        menu_list=menu.split(',')
        menu=sorted(menu_list,key=len)
        find_menu=[]
        for menu in menu_list:
            if menu in msg:
                find_menu.append(menu)
                msg=msg.replace(menu,'[메뉴{}]'.format(str(idx)))
                idx+=1
    conn.close()
    return msg,find_menu

def replace_food(msg):
    conn = sqlite3.connect('chatbotdb.db')
    cur = conn.cursor()
    sql="select name from food"
    cur.execute(sql)
    rows=cur.fetchall()
    idx=1
    food_list=[]
    for food in rows:
        food=food[0]
        if food in msg:
            msg=msg.replace(food,'[음식{}]'.format(str(idx)))
            food_list.append(food)
            idx+=1
    conn.close()
    return msg,food_list
#
# msg,rest=replace_restaurant("교촌치킨 안암점에 허니콤보 치킨 주문할래")
# print(msg,rest)
# msg,menu=replace_menu(msg,rest)
# print(msg,menu)
# msg,food=replace_food(msg)
# print(msg,food)
