import pickle

car_dict = {'audi':'germany', 'ford':'USA', 'toyota':'japan', 'vinfast':'vietnam'}

# context messege
with open('car.pkl', 'wb') as car_pkl:
    pickle.dump(car_dict, car_pkl)