from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import pandas as pd
import csv
import json

class review(object):
    def init(self):
        self.login_url = "https://login.tmall.com/?spm=a220o.1000855.a2226mz.2.7b6a493atgGt1e&redirectURL=https%3A%2F%2Fdetail.tmall.com%2Fitem.htm%3Fspm%3Da230r.1.14.1.78d33b3a4zmgeA%26id%3D602909085750%26ns%3D1%26abbucket%3D1%26sku_properties%3D10004%3A709990523%3B5919063%3A6536025"
        self.url = "https://detail.tmall.com/item.htm?spm=a230r.1.14.9.76f96228yVEeeJ&id=602659642364&cm_id=140105335569ed55e27b&abbucket=1"
        self.drivername = "chrome"
        self.path = "/Users/chensx/Desktop/graduation_project/chromedriver"
        self.driver = webdriver.Chrome(executable_path=self.path)

    def get_review(self):
        print("get")
        self.driver.find_element_by_css_selector("a[tabindex=\"-1\"][href=\"#J_Reviews\"]").click()
        num = 0
        while num < 20:
            sleep(3)
            # Stimulate scrolling
            i = 0
            while i < 4:
                self.driver.find_element_by_tag_name("body").send_keys(Keys.SPACE)
                i += 1
            # Get review texts
            review_list = self.driver.find_elements_by_class_name("tm-col-master")
            for review in review_list:
                text = str(review.find_element_by_class_name("tm-rate-fulltxt").text)
                # Write into csv

                with open("review.csv", 'a') as fp:
                    fp_csv = csv.writer(fp)
                    fp_csv.writerow([' ',text])
                print(text)
            sleep(3)
            try:
                self.driver.find_element_by_link_text("下一页>>").click()
                num += 1
            except:
                self.driver.close()
                break
        self.driver.close()

    def login(self):
        self.init()
        self.driver.get(url=self.login_url)
        # Wait login certification
        input("请回车输入")
        self.dict_cookies = self.driver.get_cookies()
        self.json_cookies = json.dumps(self.dict_cookies)
        print(self.dict_cookies)
        self.get_review()



if __name__ == '__main__':
    get_review = review()
    get_review.login()