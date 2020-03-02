import os
import time
import datetime
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 

class QiheAnalyze:
    def __init__(self):
        self.path = os.path.abspath(__file__) # 当前代码文件的绝对路径
        # print(self.path)
        self.data_path = os.path.join(os.getcwd(), 'qihe_data') # 数据文件路径
        # print(self.data_path)


    def delete_file(self):
        # 统计文件行数，删除数据不完整的文件

        all_file_num = 0  # 所有文件数量
        complete_file_num = 0  # 数据完整的文件数量
        file_remove_list = [] # 要删除的文件列表
        dirs = os.listdir(self.data_path)
        for file in dirs:
            filepath = os.path.join(self.data_path,file)
            with open(filepath,'rb') as f:
                all_file_num += 1
                lines = len(f.readlines())
                print("文件名：{}行数：{}".format(os.path.basename(filepath),lines))
                if lines == 405:
                    complete_file_num += 1
                else:
                    file_remove_list.append(filepath)
        print("文件总数量:{}\n数据完成的文件数量：{}".format(all_file_num,complete_file_num))
        # for filepath in file_remove_list:
            # os.remove(filepath)

    def tempdat_to_csv(self):
        for file in os.listdir(self.data_path):
            filepath = os.path.join(self.data_path,file)
            raw_data = []
            date_ = datetime.date(*map(int, file.split('日')[0].split('-'))) # 取出文件名中的日期
            print(date_)

            # 取出
            with open(filepath,'r') as f:
                for line in f.readlines():
                    s = line.split() # 将每一行中的数据分隔开
                    # print(s[0],s[1],s[2],s[3])
                    for str in s:
                        raw_data.append(str)


if __name__ == "__main__":
    a = QiheAnalyze()
    a.delete_file()
    # a.tempdat_to_csv()
    


