from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import pandas as pd

class review(object):
    def init_driver(self):
        self.url = "https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.2.23214f68QQOUjC&id=589880871893&skuId=4200907042830&standard=1&user_id=2616970884&cat_id=2&is_b=1&rn=1b1d09e8340c83f0d4244c7119db9893"
        self.path = "/Users/chensx/Desktop/graduation_project/chromedriver"
        self.driver = webdriver.Chrome(executable_path=self.path)

    def login(self):
        self.init_driver()
        self.driver.get(url=self.url)
        # Wait login certification
        input("请回车输入")
        self.get_review()

    def get_review(self):
        print("get")
        self.driver.find_element_by_css_selector("a[tabindex=\"-1\"][href=\"#J_Reviews\"]").click()
        num = 0
        # DataFrame for writing into csv
        review_data_list = pd.DataFrame(columns=['text'])

        while num < 20:
            sleep(3)
            # Stimulate scrolling
            self.scroll()
            # Get review texts
            review_list = self.driver.find_elements_by_class_name("tm-col-master")
            for review in review_list:
                text = str(review.find_element_by_class_name("tm-rate-fulltxt").text)
                if text != "此用户没有填写评论!" and len(text) > 5:
                    review_data_list = review_data_list.append({'text': text}, ignore_index=True)
                    print(text)
            try:
                self.driver.find_element_by_link_text("下一页>>").click()
                num += 1
            except:
                print('No more pages!')
                break

        # Write into csv
        review_data = pd.read_csv("review.csv", encoding='utf-8')
        review_data = review_data.append(review_data_list, ignore_index=True)
        print(review_data)
        review_data.to_csv("review.csv", encoding='utf-8', index=False)
        self.driver.close()

    def scroll(self):
        i = 0
        while i < 9:
            self.driver.find_element_by_tag_name("body").send_keys(Keys.SPACE)
            i += 1
            if i == 4:
                sleep(1)


if __name__ == '__main__':
    get_review = review()
    get_review.login()
