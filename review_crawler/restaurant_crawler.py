from selenium import webdriver
from time import sleep
import pandas as pd

class restaurant(object):
    def init_driver(self):
        self.url = "https://meituan.com/meishi/1467844/"
        self.path = "/Users/chensx/Desktop/graduation_project/chromedriver"
        self.driver = webdriver.Chrome(executable_path=self.path)

    def get_review(self):
        self.init_driver()
        self.driver.get(url=self.url)
        comment_data_list = pd.DataFrame(columns=['text'])
        for i in range(10):
            sleep(1)
            comment_div = self.driver.find_element_by_class_name('comment')
            com_cont = comment_div.find_element_by_class_name('com-cont')
            # div = com_cont.find_elements_by_css_selector('div')
            comment_list = com_cont.find_elements_by_css_selector("[class='list clear']")
            for comment in comment_list:
                text = str(comment.find_element_by_class_name('desc').text)
                print(text)
                if text != '':
                    comment_data_list = comment_data_list.append({'text': text}, ignore_index=True)
            try:
                com_cont.find_element_by_css_selector("[class='iconfont icon-btn_right']").click()
            except:
                print("no page")
                break

        review_data = pd.read_csv("../data/res_comment.csv", encoding='utf-8')
        review_data = review_data.append(comment_data_list, ignore_index=True)
        print(review_data)
        review_data.to_csv("../data/res_comment.csv", encoding='utf-8', index=False)
        self.driver.close()


if __name__ == '__main__':
    res = restaurant()
    res.get_review()
