# -*- utf-8 -*-
from tkinter import *


class ui:
    t1 = None
    t2 = None
    t3 = None

    def start(self):
        panel = Tk()
        panel.geometry("300x150")
        panel.title("make data")
        Label(panel, text="输入配置文件夹地址：").grid(row=1, column=0)
        self.t1 = Entry(panel)
        self.t1.grid(row=1, column=1)

        Label(panel, text="输入生成数量：").grid(row=2)
        self.t2 = Entry(panel)
        self.t2.grid(row=2, column=1)

        Button(panel, text="数据生成", command=self.deal).grid(row=3)

        self.t3 = Label(panel)
        self.t3.grid(row=4)
        panel.mainloop()

    def deal(self):
        sa = self.t1.get()
        count = self.t2.get()
        if str(sa).strip() == '':
            import os
            file_path = os.path.join(os.path.expanduser("~"), 'Desktop')
            file_path = str(file_path) + "//1"
            sa = file_path
        import Uc as uc
        uu = uc
        uu.file_p = sa
        uu.xml_path = sa + "\\生成结果\\"

        print(str(count) + ".........")
        if str(count).strip() == '':
            tmp_cot = 1000
        elif int(count) > 0:
            tmp_cot = int(count)

        print(tmp_cot)
        uu.count = tmp_cot
        import threading
        threading.Thread(target=(self.uu_start), args=(uu,)).start()
        self.t3["text"] = "数据生成中...稍等片刻"
        print("end")

    def uu_start(self, uu):
        uu.man()
        self.t3["text"] = "生成完成"


if __name__ == "__main__":
    ui().start()
