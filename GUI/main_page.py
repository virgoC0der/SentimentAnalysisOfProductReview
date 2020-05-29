from tkinter import *
from tkinter import ttk
from lstm.lstm_test import lstm_predict_single
from svm.train_svm import svm_predict


class predict_gui():
    def __init__(self, init_window_name):
        self.init_window_name = init_window_name

    def set_window(self):
        self.init_window_name.title("评论文本情感分析")

        self.input_label = Label(self.init_window_name, text="请输入文本：")
        self.input_label.grid(row=0, column=0, sticky=E)

        # 输入框
        self.input_text = Entry(self.init_window_name, width=30)
        self.input_text.grid(row=0, column=1, sticky='nsew')

        self.result_label = Label(self.init_window_name, text="情感预测结果：")
        self.result_label.grid(row=1, column=0, sticky=E)

        # 输出结果
        self.result_label = Label(self.init_window_name)
        self.result_label.grid(row=1, column=1, sticky='nsew')

        self.var = StringVar(self.init_window_name)
        self.var.set('LSTM')
        self.model_select = ttk.OptionMenu(self.init_window_name, self.var, '', 'LSTM', 'SVM')
        self.model_select.grid(row=2, column=0)

        self.predict_button = ttk.Button(self.init_window_name, text="开始检测", command=self.click_predict)
        self.predict_button.grid(row=2, column=1)

        self.delete_button = ttk.Button(self.init_window_name, text="删除", command=self.click_delete)
        self.delete_button.grid(row=2, column=2)

    def click_predict(self):
        text = self.input_text.get()
        method = self.var.get()
        if method == "LSTM":
            if text=="":
                result="请输入文本"
            else:
                result = lstm_predict_single(text)
        else:
            if text=="":
                result="请输入文本"
            else:
                result = svm_predict(text)
                print(result)
        self.result_label['text'] = result

    def click_delete(self):
        self.input_text.delete(0, END)
        self.result_label['text'] = ""


if __name__ == '__main__':
    init_window = Tk()
    gui = predict_gui(init_window)
    gui.set_window()
    init_window.mainloop()
