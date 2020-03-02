"""
10个储粮害虫远程在线监测装置诱捕的害虫情况：
1)  1号装置：粉盗及幼虫、扁谷盗类，98头；
2)  2号装置：赤拟谷盗，2头；
3)  3号装置：扁谷盗，10头；
4)  4号装置、6号装置：扁谷盗各2头；
5)  5号装置：只有少量书虱子；
6)  8号装置：赤拟谷盗约150头；
7)  10号装置：赤拟谷盗和扁谷盗11头和1个赤拟谷盗幼虫
"""
import numpy as np
import re
import json
import os
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import matplotlib.ticker as ticker
font_zh = FontProperties(fname='/System/Library/Assets/com_apple_MobileAsset_Font4/32ee1600791572d4fc4b5664c1253d7073def14b.asset/AssetData/STHEITI.ttf', size="large", weight='normal')
font_en = FontProperties(fname='/Library/Fonts/Times New Roman.ttf', size='medium', weight='normal')
plt.rcParams['axes.unicode_minus'] = False


records_file_name = "records.json"
records_tsv_file_name = "records.tsv"
records_npy_file_name = "records.npy"
# records = {1: {}, 11: {}, 3: {}, 4: {}, 5: {}, 6: {}, 8: {}, 10: {}}
records = {1: {}, 11: {}, 3: {}, 5: {}, 6: {}, 8: {}, 10: {}}
pest_num_pattern = re.compile(r'\*(\d+)\*')
device_id_pattern = re.compile(r'slave-(\d{2})')
for log_file_name in os.listdir("./shunyi"):
    time = log_file_name.split('.')[0]
    for item in records:
        records[item][time] = 0
    log_file_name = "./shunyi/" + log_file_name
    with open(log_file_name) as f:
        for line in f:
            pest_num_res = re.search(pest_num_pattern, line)
            if pest_num_res:
                device_id_res = re.search(device_id_pattern, line)
                device_id = int(device_id_res.group(1))
                if device_id == 4:
                    continue
                pest_num = int(pest_num_res.group(1))
                if pest_num >= 9:  # 杂质
                    continue
                records[device_id][time] = pest_num
for item in records:
    records[item] = sorted(records[item].items(), key=lambda record: record[0])
# print(records)
with open(records_file_name, 'w+') as f:
    json.dump(records, f)
records_list = []
item_list = []
for item in records:
    item_list.append(str(item))
    time_num_list = []
    for record in records[item]:
        time_num_list.append(record[1])
    records_list.append(time_num_list)
records_list = list(zip(*records_list))  # 转置
time_list = []
for log_file_name in os.listdir("./shunyi"):
    time = log_file_name.split('.')[0]
    time_list.append(time)
time_list.sort()
with open(records_tsv_file_name, 'w+') as f:
    f.write('              \t'+'\t'.join(item_list)+'\n')
    for i in range(len(time_list)):
        f.write(time_list[i]+'\t'+'\t'.join([str(num) for num in records_list[i]])+'\n')
records_npy = np.array(records_list)
np.save(records_npy_file_name, records_npy)

for i in range(records_npy.shape[0]-1):
    records_npy[i+1, :] = records_npy[i+1, :] + records_npy[i, :]

print(records_npy)
def gen_artist(ax, data1, data2, param_dict={}):
    out = ax.plot(data1, data2, **param_dict)
    return out[0]

fig = plt.gcf()
ax1 = fig.add_subplot(1,1,1)
show_time = [0, 250, 500, 750, 1000, 1250, 1500, 1686]
x_time = np.array(range(records_npy.shape[0]))
for i in range(records_npy.shape[1]):
    print(x_time, records_npy[:, i])
    gen_artist(ax1, x_time, records_npy[:, i], {"label": 'DEVICE-'+("2" if item_list[i] == "11" else item_list[i])})
ax1.legend(prop=font_en)
ax1.xaxis.set_major_locator(ticker.FixedLocator(show_time))  # https://matplotlib.org/api/ticker_api.html?highlight=multiplelocator
ax1.xaxis.set_major_formatter(ticker.FixedFormatter([time_list[i][4:] for i in show_time]))
for t in ax1.get_xticklabels():
    t.set_fontproperties(font_en)
    t.set_rotation(30)
for t in ax1.get_yticklabels():
    t.set_fontproperties(font_en)
for i in range(records_npy.shape[1]):
    ax1.text(1686, records_npy[-1, i], str(records_npy[-1, i]), fontproperties=font_en,
             horizontalalignment='right', verticalalignment='top')
    ax1.text(750-i*20, records_npy[750-i*20, i], ("2" if item_list[i] == "11" else item_list[i]), fontproperties=font_en,
             horizontalalignment='left', verticalalignment='bottom', color="red")
ax1.yaxis.set_label_text('number', fontproperties=font_en)
ax1.set_title("顺义库", fontproperties=font_zh)


plt.show()