import csv
import string
import jieba


with open("review_crawler/review.csv", 'r') as fp:
    sentence_list = fp.readlines()
    for sentence in sentence_list:
        # print(sentence)
        sentence = jieba.cut(sentence, cut_all=False)
        print('/'.join(sentence))

