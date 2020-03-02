import numpy as np 
import matplotlib.pyplot as plt 
import json

# d = np.fromfile("records.npy", dtype=np.int, count=-1,sep=",")
# d = np.load("records.npy")
# print(d[0])
# print(d.shape)

def ananlyze_shunyi_json():
    with open('records.json') as f:
        data = json.load(f)
        data_1 = data['1']
        data_3 = data['3']
        data_5 = data['5']
        data_6 = data['6']
        data_8 = data['8']
        data_10 = data['10']
        data_11 = data['11']

    print(len(data_1))
    data_1_not_zero = []
    for v_1 in data_1:
        v_1[0] = v_1[0][0:8]
        if v_1[1] != 0:
            data_1_not_zero.append(v_1)
    # print(data_1_not_zero)
    print(len(data_1_not_zero))

    data_1_not_zero_dict = {}
    for v in data_1_not_zero:
        if data_1_not_zero_dict.get(v[0]) is None:
            data_1_not_zero_dict[v[0]] = v[1]
        else:
            data_1_not_zero_dict[v[0]] += v[1]
    print(data_1_not_zero_dict)


    data_1_not_zero_key = []
    data_1_not_zero_value = []
    for k, v in data_1_not_zero_dict.items():
        data_1_not_zero_key.append(k)
        data_1_not_zero_value.append(v)
         
    plt.plot(data_1_not_zero_key, data_1_not_zero_value)
    # plt.bar(data_1_not_zero_key,data_1_not_zero_value)
    plt.show()

    
    



if __name__ == "__main__":
    ananlyze_shunyi_json()
