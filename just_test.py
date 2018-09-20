import codecs
from konlpy.tag import Twitter

tagger = Twitter()
class SentenceReader:

    def __init__(self, filepath):
        self.filepath = filepath

    def __iter__(self):
        for line in codecs.open(self.filepath, encoding='utf-8'):
            yield line.split(' ')

import gensim
sentences = [["my", "name", "is", "jamie"], ["jamie", "is", "cute"]]
# model = gensim.models.Word2Vec(sentences)
sentences_vocab = SentenceReader('raw_sentences.txt')
sentences_train = SentenceReader('raw_sentences.txt')
print(sentences_train)
model = gensim.models.Word2Vec()
# model = gensim.models.Word2Vec(sentences_vocab, min_count=1)
sentences = ['I love ice-cream', 'he loves ice-cream', 'you love ice cream']
model.build_vocab(sentences)
model.train(sentences)
# from sklearn.manifold import TSNE
# import pandas as pd
# import matplotlib
# import matplotlib.pyplot as plt
#
#
# font_name = matplotlib.font_manager.FontProperties(
#                 fname="/usr/share/fonts/truetype/nanum/NanumGothic.ttf"  # 한글 폰트 위치를 넣어주세요
#             ).get_name()
# vocab = model.wv.index2word
# matplotlib.rc('font', family=font_name)
# tsne = TSNE(n_components=2)
# X_tsne = tsne.fit_transform(X) #t-분포 확률적 임베딩(t-SNE)은 데이터의 차원 축소에 사용
# df = pd.concat([pd.DataFrame(X_tsne),
#                 pd.Series(vocab)],
#                axis=1)
#
# df.columns = ['x', 'y', 'word']
# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)
# print(df)
# ax.scatter(df['x'], df['y'])
# ax.set_xlim(df['x'].max(), df['x'].min())
# ax.set_ylim(df['y'].max(), df['y'].min())
# for i, txt in enumerate(df['word']):
#     ax.annotate(txt, (df['x'].iloc[i], df['y'].iloc[i]))
# plt.show()

# from pandas import Series, DataFrame
#
# daeshin = {'open':  [11650, 11100, 11200, 11100, 11000],
#            'high':  [12100, 11800, 11200, 11100, 11150],
#            'low' :  [11600, 11050, 10900, 10950, 10900],
#            'close': [11900, 11600, 11000, 11100, 11050]}
#
# daeshin_day = DataFrame(daeshin)
# print(daeshin_day)