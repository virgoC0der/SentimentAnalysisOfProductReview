# 基于机器学习的商品评论情感分析
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FvirgoC0der%2FSentimentAnalysisOfProductReview.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2FvirgoC0der%2FSentimentAnalysisOfProductReview?ref=badge_shield)


## 从淘宝爬取评论
使用Selenium模拟真实登录行为，并爬取数据。

## 数据清理
如果文本中有“666“，”好好好“等无用词语，去掉评论中的标点符号。

## 分词
使用jieba精确模式进行分词，构造词典

## 将词汇向量化
创建词语字典，并返回每个词语的索引，词向量，以及每个句子所对应的词语索引

## 分类模型对比
SVM vs LSTM


## License
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FvirgoC0der%2FSentimentAnalysisOfProductReview.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2FvirgoC0der%2FSentimentAnalysisOfProductReview?ref=badge_large)