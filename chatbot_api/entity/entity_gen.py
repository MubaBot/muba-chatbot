def use_w2v():
    from gensim.models import word2vec
    model=word2vec.Word2Vec.load("namu.model")
    # print(model.most_similar(positive=["한국","지역","부산","이태원"],negative=["아시아","우리나라","외국인"],topn=1000))
    # with open('./food.txt','wb') as f:
    #     f.write('\n'.join(list(map(lambda x:x[0],model.most_similar(positive=["치킨","피자","메뉴"],negative=[],topn=1000)))).encode())
    # print(model.most_similar(positive=["집","동네","여기"],negative=[],topn=1000))
    # '\n'.join(list(map(lambda x:x[0],model.most_similar(positive=["배달","치킨","피자","김치찌개"],negative=["사서","상인"],topn=1000))))

# def wiki_crawl():
#     from bs4 import BeautifulSoup
#     import urllib
#     web_url='https://ko.wiktionary.org/w/index.php?title=%EB%B6%84%EB%A5%98:%ED%95%9C%EA%B5%AD%EC%96%B4_%EC%9D%8C%EC%8B%9D&from=%EA%B0%80'
#     with urllib.request.urlopen(web_url) as response:
#         html = response.read()
#         soup = BeautifulSoup(html, 'html.parser')
#         # print(soup)
#         print(soup.find_all("a"))

def add_food(word):
    with open('./food.txt', 'r+') as f:
        s=f.read()
        food=list(s.split())
    with open('./food.txt','a+') as f:
        if word not in food:
            f.write('\n'+word)

add_food('매운탕')




