from gensim.models import word2vec
import jieba
import pandas as pd
import os
import csv

def train():
    df_train = pd.read_csv('review_crawler/review.csv')
    discuss_train = list(df_train['after_treatment'])
    # with open('train_cut.csv', 'a') as f:
    #     f_csv = csv.writer(f)
    #     for i in discuss_train:
    #         f_csv.writerow([str(i)])
    sentences = word2vec.Text8Corpus('review_crawler/train_cut.csv')
    model = word2vec.Word2Vec(sentences, size=200)

    model.save("word2vec.model")
    # y = model.most_similar(u"苹果", topn=20)
    # for a in y:
    #     print(a)

if __name__ == '__main__':
    train()