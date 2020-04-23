from gensim.models import Word2Vec
from lstm.train_lstm import create_dictionaries
from keras.models import model_from_yaml
from review_treatment.review_pretreatment import *
import yaml
import numpy as np


def input_transform(string):
    # words=jieba.lcut(string)
    words = sep_string(string)
    print(words)
    words=np.array(words).reshape(1,-1)
    model=Word2Vec.load('../model/Word2vec_model.pkl')
    _,_,combined=create_dictionaries(model,words)
    return combined

def load_model():
    print('loading model......')
    with open('../model/lstm.yml', 'r') as f:
        yaml_string = yaml.load(f)
    model = model_from_yaml(yaml_string)

    print('loading weights......')
    model.load_weights('../model/lstm_three.h5')
    model.compile(loss='binary_crossentropy',
                  optimizer='adam', metrics=['accuracy'])
    return model

def lstm_predict_single(string):
    model = load_model()
    data = input_transform(string)
    data.reshape(1, -1)
    result = model.predict_classes(data)
    if result[0] == 1:
        print(string, ' positive')
    elif result[0] == 0:
        print(string, 'neural')
    else:
        print(string, ' negative')


def lstm_predict():
    model = load_model()
    review_csv = pd.read_csv("../data/res_comment.csv", encoding='utf-8')
    review_list = review_csv['text']
    result_list = review_csv['sentiment']
    wrong_list = []
    wrong_ans = 0
    for i in range(0, 100):
        data = input_transform(review_list[i])
        data.reshape(1,-1)
        result = model.predict_classes(data)
        if result[0] == 1:
            if result_list[i] == 'positive':
                print (review_list[i],' positive')
            else:
                wrong_ans += 1
                wrong_list.append(review_list[i])
        elif result[0] == 0:
            if result_list[i] == 'neural':
                print (review_list[i],' neural')
            else:
                wrong_ans += 1
                wrong_list.append(review_list[i])
        else:
            if result_list[i] == 'negative':
                print (review_list[i],' negative')
            else:
                wrong_ans += 1
                wrong_list.append(review_list[i])

    print(wrong_list)
    accuracy = (100-wrong_ans)/100
    print("accuracy: %f" % (accuracy))

if __name__=='__main__':
    # lstm_predict()
    string = "书的质量还好，但是内容实在没意思。本以为会侧重心理方面的分析😂，但实际上是婚外恋内容。"
    lstm_predict_single(string)