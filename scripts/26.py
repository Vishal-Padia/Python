#Read and write using pickle
import pickle

dataObject = []
for num in range(10,15):
    dataObject.append(num)

file_handler = open('languages', 'wb')
pickle.dump(dataObject, file_handler)

file_handler.close()

file_handler = open('languages', 'rb')

dataObject = pickle.load(file_handler)
for val in dataObject:
    print('The data value: ', val)
file_handler.close()