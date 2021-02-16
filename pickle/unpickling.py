import pickle

with open('car.pkl', 'rb') as carpkl:
    mycar = pickle.load(carpkl)

print(mycar['audi'])