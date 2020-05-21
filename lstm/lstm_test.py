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
        print(string, 'neutral')
    else:
        print(string, ' negative')


def lstm_predict():
    model = load_model()
    path = "../data/"
    file_list = ['neg.csv', 'neutral.csv', 'pos.csv']
    wrong_list = []
    wrong_ans = 0
    amount = 0
    for file in file_list:
        review_csv = pd.read_csv(path+file, encoding='utf-8')
        length = len(review_csv)
        head = 0.8*length
        review_list = review_csv['text'][int(0.8*length):]
        amount += length

        for review in review_list:
            data = input_transform(review)
            data.reshape(1,-1)
            result = model.predict_classes(data)
            if result[0] == 1:
                if file == 'pos.csv':
                    print (review,' positive')
                else:
                    wrong_ans += 1
                    wrong_list.append(review)
            elif result[0] == 0:
                if file == 'neutral.csv':
                    print (review,' neutral')
                else:
                    wrong_ans += 1
                    wrong_list.append(review)
            else:
                if file == 'neg.csv':
                    print (review,' negative')
                else:
                    wrong_ans += 1
                    wrong_list.append(review)

    print(wrong_list)
    accuracy = (amount-wrong_ans)/amount
    print("accuracy: %f" % (accuracy))


if __name__=='__main__':
    # lstm_predict()
    string = "一般般，人很多，饭菜咸"
    lstm_predict_single(string)
