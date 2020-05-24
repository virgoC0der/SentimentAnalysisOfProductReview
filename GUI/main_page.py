from tkinter import *
from lstm.lstm_test import lstm_predict_single
from svm.train_svm import svm_predict


class predict_gui():
    def __init__(self, init_window_name):
        self.init_window_name = init_window_name

    def set_window(self):
        self.init_window_name.title = ("评论文本情感分析")
        self.init_window_name.geometry('1068x681+10+10')

        self.var = StringVar()
        self.var.set("请选择模型")
        self.option_menu = OptionMenu(self.init_window_name, self.var, "LSTM", "SVM")
        self.option_menu.grid(row=0, column=0)
        self.option_menu.pack()

        self.input_label = Label(self.init_window_name, text="请输入文本")
        self.input_label.grid(row=1, column=0)
        self.input_label.pack()

        self.input_text = Entry(self.init_window_name, width=67)
        self.input_text.grid(row=2, column=0, rowspan=10, columnspan=10)
        self.input_text.pack()

        self.result_label = Label(self.init_window_name)
        self.result_label.grid(row=2, column=12, rowspan=15, columnspan=10)
        self.result_label.pack()

        self.predict_button = Button(self.init_window_name, text="开始检测", width=10, bg='light blue', command=self.click_predict)
        self.predict_button.grid(row=2, column=11)
        self.predict_button.pack()



    def click_predict(self):
        method = self.var.get()
        text = self.input_text.get()
        result="请先选择模型"
        if method=="LSTM":
            result = lstm_predict_single(text)
            print(result)
        if method=="SVM":
            result = svm_predict(text)
            print(result)
        self.result_label['text'] = result

if __name__ == '__main__':
    init_window = Tk()
    gui = predict_gui(init_window)
    gui.set_window()
    init_window.mainloop()