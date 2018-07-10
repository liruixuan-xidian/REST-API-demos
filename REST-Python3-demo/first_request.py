from  HuobiServices import *
from  sklearn import preprocessing
import matplotlib.pyplot as plt
import time
#import csv
#
#with open('names.csv', 'w') as csvfile:
#    fieldnames = ['first_name', 'last_name']
#    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#
#    writer.writeheader()
#    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
#    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
#    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
import numpy as np
import csv
# 功能：将一字典写入到csv文件中
# 输入：文件名称，数据字典
def createDictCSV(dataDict={}, key=""):
    fileName = dataDict['ch'][7:-13]+'_'+str(dataDict['ts'])+'.csv'
    print(fileName)
    with open(fileName, "w") as csvFile:
        #fieldnames = ['first_name', 'last_name']
        #print((dataDict['data']))
        fieldnames = dataDict['data'][0]['data'][0].keys()#['id','amount','count','open','close','low','high','vol']
        #print(fieldnames)
        csvWriter = csv.DictWriter(csvFile, fieldnames=fieldnames)
        csvWriter.writeheader()
        data = dataDict[key]
        for k in data:
            #print(k)
            csvWriter.writerow(k['data'][0])
            #csvWriter.writerow({'first_name': 'Baked', 'last_name': 'Beans'})

def convert_dict_to_list(dictdata, key):
    resualt = []
    for k in range(len(dictdata)):
        resualt.append(dictdata[k][key])
    return resualt

def min_max_normalize(array):
    return ((array-min(array))/(max(array)-min(array)))

def save_history_trade(symbol="", size=10, key=""):
    dataDict = get_history_trade(symbol, size)
    #print(dataDict)
    createDictCSV(dataDict, key)
while (1):
    try:
        save_history_trade('btcusdt', 2000, 'data')
    except:
        print('request_error')
        pass
    time.sleep(240)


#data = get_kline('btcusdt', '1min', 2000)
##print(data['data'][1] ['vol'])
##createDictCSV('btc2usdt.csv', data)
#vol = convert_dict_to_list(data['data'], 'vol')
#vol = np.array(vol)
#vol = min_max_normalize(vol)
#high = convert_dict_to_list(data['data'], 'high')
#high = np.array(high)
##high = preprocessing.scale(high)
#high = min_max_normalize(high)
#
#
#id = convert_dict_to_list(data['data'], 'id')
#
#plt.plot(id, vol, label = 'vol')
#plt.plot(id, high, label = 'high')
#
#plt.xlabel('id')
#plt.ylabel('y label')
#plt.legend()
#plt.show()
##id = np.array(id)
##id = min_max_normalize(id)
##print(vol)
##ret = get_balance(981196)
##print(ret)
