from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
import pandas as pd
from time import time
import logging
import csv
import os
import sys
import multiprocessing



#
# def train():
#     logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
#     begin = time()
#     df_train = pd.read_csv('review_crawler/review.csv')
#     discuss_train = list(df_train['after_treatment'])
#     with open('train_cut.csv', 'w') as f:
#         f_csv = csv.writer(f)
#         for i in discuss_train:
#             f_csv.writerow([str(i)])
#     sentences = word2vec.Text8Corpus('train_cut.csv')
#     model = word2vec.Word2Vec(sentences, sg=0, min_count=15, size=300, seed=1, iter=8, workers=15)
#
#     model.save("word2vec.model")
#     end = time()
#     print('Total processing time: %d seconds' % (end - begin))
#
#
# if __name__ == '__main__':
#     train()

if __name__ == '__main__':
    # print open('/Users/sy/Desktop/pyRoot/wiki_zh_vec/cmd.txt').readlines()
    # sys.exit()

    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s', level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))

    # inp为输入语料, outp1 为输出模型, outp2为原始c版本word2vec的vector格式的模型
    fdir = '/Users/chensx/Desktop/graduation_project/'
    inp = fdir + 'train_cut.csv'
    outp1 = fdir + 'comment_text.model'
    outp2 = fdir + 'comment_text.vector'

    # 训练skip-gram模型
    model = Word2Vec(LineSentence(inp), size=400, window=5, min_count=5,
                     workers=multiprocessing.cpu_count())

    # 保存模型
    model.save(outp1)
    model.wv.save_word2vec_format(outp2, binary=False)