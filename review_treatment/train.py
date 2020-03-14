from gensim.models import word2vec
import pandas as pd
import csv


def train():
    df_train = pd.read_csv('../review_crawler/review.csv')
    discuss_train = list(df_train['after_treatment'])
    with open('../train_cut.csv', 'a') as f:
        f_csv = csv.writer(f)
        for i in discuss_train:
            f_csv.writerow([str(i)])
    sentences = word2vec.Text8Corpus('train_cut.csv')
    model = word2vec.Word2Vec(sentences, size=200)

    model.save("word2vec.model")


if __name__ == '__main__':
    train()