# -*- coding: utf-8 -*-
import codecs
from bs4 import BeautifulSoup
import urllib.request
from konlpy.tag import Twitter
import os, re, json, random
class Markov_response():
    def __init__(self):

        self.dict_file = "chatbot_api/Markov_response/chatbot-data.json"
        self.twitter = Twitter()
        if os.path.exists(self.dict_file):
            self.dic = json.load(open(self.dict_file, "r"))


    def register_dic(self,words):
        # global dic
        if len(words) == 0: return
        tmp = ["@"]
        for i in words:
            word = i[0]
            if word == "" or word == "\r\n" or word == "\n": continue
            tmp.append(word)
            if len(tmp) < 3: continue
            if len(tmp) > 3: tmp = tmp[1:]
            self.set_word3(self.dic, tmp)
            if word == "." or word == "?":
                tmp = ["@"]
                continue
        # json.dump(dic, open(self.dict_file,"w", encoding="utf-8"))

    # 딕셔너리에 글 등록하기
    def set_word3(self,dic, s3):
        w1, w2, w3 = s3
        if not w1 in dic: dic[w1] = {}
        if not w2 in dic[w1]: dic[w1][w2] = {}
        if not w3 in dic[w1][w2]: dic[w1][w2][w3] = 0
        dic[w1][w2][w3] += 1
    def make_sentence(self,head):
        if not head in self.dic: return ""
        ret = []
        if head != "@": ret.append(head)
        top = self.dic[head]
        w1 = self.word_choice(top)
        w2 = self.word_choice(top[w1])
        ret.append(w1)
        ret.append(w2)
        while True:
            if w1 in self.dic and w2 in self.dic[w1]:
                w3 = self.word_choice(self.dic[w1][w2])
            else:
                w3 = ""
            ret.append(w3)
            if w3 == "." or w3 == "？ " or w3 == "": break
            w1, w2 = w2, w3
        ret = "".join(ret)
        # 띄어쓰기
        # params = urllib.parse.urlencode({
        #     "_callback": "",
        #     "q": ret
        # })
        return ret

    def word_choice(self,sel):
        keys = sel.keys()
        return random.choice(list(keys))

    def make_reply(self,text):
        # return "Markov response"
        if not text[-1] in [".", "?"]: text += "."
        # print(self.dic)
        words = Twitter().pos(text)
        # self.register_dic(words)

        for word in words:
            face = word[0]
            if face in self.dic:
                return self.make_sentence(face)
        return self.make_sentence("@")



# print(make_reply('ㅁㅊ'))
# f=open('./namu.txt','rb')
# i=0
# while(1):
#     if i%100000==0:
#         print(i)
#     i+=1
#     s=f.readline().decode()
#     if not s:
#         break
#     make_reply(s)
