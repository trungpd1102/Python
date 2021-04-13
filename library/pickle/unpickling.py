import pickle

with open('LDA_20210319154815.pkl', 'rb') as carpkl:
    mycar = pickle.load(carpkl)

print(mycar)