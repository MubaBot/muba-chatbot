from chatbot_api.entity import *

def is_restaurant(msg):
    for rest in restaurant_list:
        if msg==rest:
            return True
    return False

def is_menu(msg):
    for menu in menu_list:
        if msg==menu:
            return True
    return False

def find_restaurant(msg):
    for rest in restaurant_list:
        if rest in msg:
            return rest
    return -1

def find_menu(msg):
    for menu in menu_list:
        if menu in msg:
            return menu
    return -1
