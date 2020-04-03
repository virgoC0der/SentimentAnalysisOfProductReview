from selenium import webdriver
from time import sleep

class restaurant(object):
    def init_driver(self):
        self.url = "https://www.meituan.com/meishi/194049193/"
        self.path = "/Users/chensx/Desktop/graduation_project/chromedriver"
        self.driver = webdriver.Chrome(executable_path=self.path)

    def get_review(self):
        self.init_driver()
        self.driver.get(url=self.url)
        sleep(1)
        comment_list = self.driver.find_elements_by_class_name('list clear')
        print(comment_list)
        for comment in comment_list:
            text = str(comment.find_element_by_class_name('desc').text)
            print(text)

if __name__ == '__main__':
    res = restaurant()
    res.get_review()
