import dawg
import pickle

list = []
with open('wordList.txt', 'r', encoding='utf-8') as wordListe:
    total = wordListe.readlines()
    for line in total:
        line = line.replace('\n', '')
        list.append(line)

base_dawg = dawg.CompletionDAWG(list)

print('a\n' in base_dawg)
with open('dawgFile.dawg', 'wb') as dawgFile:
    p1 = pickle.dump(base_dawg, dawgFile)



