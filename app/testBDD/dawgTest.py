import pickle


with open('dawgFile.dawg', 'rb') as dawgFile:
    dawgObj = pickle.load(dawgFile)

print(dawgObj)

print('manger' in dawgObj)

print(dawgObj.keys('m'))