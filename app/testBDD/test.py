import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.model.Word import *
print(os.getcwd())
os.chdir('../../')
print(os.getcwd())

engine = create_engine("postgresql://erkang:rrrrrrrr@localhost/test")
Session = sessionmaker(bind=engine)
session = Session()

with open('Lexique381.txt', 'r', encoding='utf-8') as source:
    content = source.readline()
    content2 = source.readlines()
    for line in content2:
        list = line.split('\t')
        ortho = list[0]
        phono = list[1]
        lemme = list[2]
        cgram = list[3]
        genre = list[4]
        nombre = list[5]
        freqlemfilms = float(list[6])
        freqlemlivres = float(list[7])
        freqfilms = float(list[8])
        freqlivres = float(list[9])
        infover = list[10]
        word = Word(ortho=ortho, phono=phono, lemme=lemme, cgram=cgram,
                    genre=genre, freqlemfilms=freqlemfilms, freqlemlivres=freqlemlivres,
                    freqfilms=freqfilms, freqlivres=freqlivres, infover=infover)
        session.add(word)
    session.commit()


