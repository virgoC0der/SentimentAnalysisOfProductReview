import csv
import re
import jieba
import jieba.analyse
import pandas as pd


def filter_emoji(desstr, restr=' '):
    # 过滤emoji
    try:
        co = re.compile(u'[\U00010000-\U0010ffff]')
    except re.error:
        co = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
    return co.sub(restr, desstr)


def stopwords_list():
    stopwords = [line.strip() for line in
                 open('/Users/chensx/Downloads/stopwords/哈工大停用词表.txt', encoding='utf-8').readlines()]
    return stopwords


def sep_words():
    sentence_after_list = []
    stopwords = stopwords_list()
    jieba.load_userdict("/Users/chensx/Desktop/大学/毕业设计文献/THUOCL/THUOCL_it.txt")
    jieba.suggest_freq("下单", True)
    jieba.suggest_freq("WiFi", True)
    with open("review_crawler/review.csv", 'r') as fp:
        sentence_list = fp.readlines()
        sentence_list = sentence_list[1:]
        for sentence in sentence_list:
            sentence = sentence.rstrip('\n')
            sentence = filter_emoji(sentence)
            sentence_after = jieba.cut(sentence, cut_all=False)
            outstr = ''
            for word in sentence_after:
                if word not in stopwords:
                    outstr += word
                    outstr += ' '
            sentence_after_list.append(outstr.rstrip())

    data = pd.read_csv('review_crawler/review.csv')
    data = pd.DataFrame(data)
    data['after_treatment'] = sentence_after_list
    data.to_csv('review_crawler/review.csv')


if __name__ == '__main__':
    sep_words()
