import pickle
import time
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.callbacks import TensorBoard

NAME = f'cat-vs-dog-prediction-{int(time.time())}'
tensorboard = TensorBoard(log_dir=f'logs\\{NAME}\\')

x = pickle.load(open('x.pkl', 'rb'))
y = pickle.load(open('y.pkl', 'rb'))

x=x/255

model = Sequential()

model.add(Conv2D(64, (3,3), activation = 'relu'))      #64 feature detetor with size 3x3 and activation function
model.add(MaxPooling2D((2,2)))

model.add(Conv2D(64, (3,3), activation = 'relu'))     
model.add(MaxPooling2D((2,2)))

model.add(Conv2D(64, (3,3), activation = 'relu'))     
model.add(MaxPooling2D((2,2)))


model.add(Flatten())

model.add(Dense(128, input_shape = x.shape[1:], activation = 'relu'))

model.add(Dense(2, activation = 'softmax'))    #return values 0 and 1

model.compile(optimizer = 'adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(x,y, epochs=5, validation_split=0.1, batch_size=32, callbacks=[tensorboard]) 

