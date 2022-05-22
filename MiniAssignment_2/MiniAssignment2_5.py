def merge(dict1,dict2):
    return dict1.update(dict2)

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

merge(dict1,dict2)
print(dict1)