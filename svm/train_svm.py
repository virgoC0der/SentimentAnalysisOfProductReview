from sklearn.model_selection import train_test_split
from gensim.models.word2vec import Word2Vec
import numpy as np
import pandas as pd
import jieba
from sklearn.externals import joblib
from sklearn.svm import SVC
import sys

# reload(sys)
# sys.setdefaultencoding('utf8')


# 加载文件，导入数据,分词
def loadfile():
    neg=pd.read_csv('../data/neg.csv',header=None,index_col=None)
    pos=pd.read_csv('../data/pos.csv',header=None,index_col=None,error_bad_lines=False)
    neu=pd.read_csv('../data/neutral.csv', header=None, index_col=None)

    cw = lambda x: list(jieba.cut(x))
    pos['words'] = pos[0].apply(cw)
    neg['words'] = neg[0].apply(cw)
    neu['words'] = neu[0].apply(cw)

    # print pos['words']
    # use 1 for positive sentiment, 0 for negative
    y = np.concatenate((np.ones(len(pos),dtype=int), np.zeros(len(neu), dtype=int), -1*np.ones(len(neg),dtype=int)))

    x_train, x_test, y_train, y_test = train_test_split(np.concatenate((pos['words'], neu['words'], neg['words'])), y, test_size=0.2)

    np.save('data/y_train.npy', y_train)
    np.save('data/y_test.npy', y_test)
    return x_train, x_test


# 对每个句子的所有词向量取均值
def buildWordVector(text, size, imdb_w2v):
    vec = np.zeros(size).reshape((1, size))
    count = 0.
    for word in text:
        try:
            vec += imdb_w2v[word].reshape((1, size))
            count += 1.
        except KeyError:
            continue
    if count != 0:
        vec /= count
    return vec


# 计算词向量
def get_train_vecs(x_train, x_test):
    n_dim = 300
    # Initialize model and build vocab
    imdb_w2v = Word2Vec(size=n_dim, min_count=10)
    imdb_w2v.build_vocab(x_train)

    # Train the model over train_reviews (this may take several minutes)
    imdb_w2v.train(x_train, total_examples=imdb_w2v.corpus_count, epochs=imdb_w2v.epochs)

    train_vecs = np.concatenate([buildWordVector(z, n_dim, imdb_w2v) for z in x_train])
    # train_vecs = scale(train_vecs)

    np.save('data/train_vecs.npy', train_vecs)
    print(train_vecs.shape)
    # Train word2vec on test tweets
    imdb_w2v.train(x_test, total_examples=imdb_w2v.corpus_count, epochs=imdb_w2v.epochs)
    imdb_w2v.save('model/w2v_model.pkl')
    # Build test tweet vectors then scale
    test_vecs = np.concatenate([buildWordVector(z, n_dim, imdb_w2v) for z in x_test])
    # test_vecs = scale(test_vecs)
    np.save('data/test_vecs.npy', test_vecs)
    print(test_vecs.shape)


def get_data():
    train_vecs = np.load('data/train_vecs.npy')
    y_train = np.load('data/y_train.npy')
    test_vecs = np.load('data/test_vecs.npy')
    y_test = np.load('data/y_test.npy')
    return train_vecs, y_train, test_vecs, y_test


##训练svm模型
def svm_train(train_vecs, y_train, test_vecs, y_test):
    clf = SVC(kernel='rbf', verbose=True)
    clf.fit(train_vecs, y_train)
    joblib.dump(clf, 'model/model.pkl')
    print(clf.score(test_vecs, y_test))


##得到待预测单个句子的词向量
def get_predict_vecs(words):
    n_dim = 300
    imdb_w2v = Word2Vec.load('model/w2v_model.pkl')
    # imdb_w2v.train(words)
    train_vecs = buildWordVector(words, n_dim, imdb_w2v)
    # print train_vecs.shape
    return train_vecs


####对单个句子进行情感判断
def svm_predict(string):
    words = jieba.lcut(string)
    words_vecs = get_predict_vecs(words)
    clf = joblib.load('model/model.pkl')

    result = clf.predict(words_vecs)
    print(result)

    if int(result[0]) == 1:
        print(string, ' positive')
    elif int(result[0]) == -1:
        print(string, ' negative')
    elif int(result[0]) == 0:
        print(string, ' neutral')


if __name__ == '__main__':
    # #导入文件，处理保存为向量
    #    x_train,x_test=loadfile() #得到句子分词后的结果，并把类别标签保存为y_train。npy,y_test.npy
    #    get_train_vecs(x_train,x_test) #计算词向量并保存为train_vecs.npy,test_vecs.npy
    #    train_vecs,y_train,test_vecs,y_test=get_data()#导入训练数据和测试数据
    #    svm_train(train_vecs,y_train,test_vecs,y_test)#训练svm并保存模型

    #对输入句子情感进行判断
    # string = '一般般吧'
    string='牛逼的手机，从3米高的地方摔下去都没坏，质量非常好'
    svm_predict(string)