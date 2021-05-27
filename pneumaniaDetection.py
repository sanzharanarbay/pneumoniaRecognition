import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import pickle

#path to the folder
dir = 'chest_xray'
test_dir = os.path.join(dir,'test')
train_dir =os.path.join(dir,'train')
val_dir =os.path.join(dir,'val')

categ = ['NORMAL', 'PNEUMONIA']
for ca in categ:
    path = os.path.join(train_dir,ca)
    for img in os.listdir(path):
        img_arr =Image.open(os.path.join(path,img))
        arr = np.array(img_arr)
        plt.imshow(np.array(img_arr),cmap='gray')
        plt.show()
        break

img_size = 250
new_img = img_arr.resize((img_size,img_size))
plt.imshow(new_img,cmap='gray')
plt.show()

# filtering the image
for ca in categ:
    path = os.path.join(test_dir,ca)
    for img in os.listdir(path):
        img_arr =Image.open(os.path.join(path,img))
        print(np.array(img_arr).shape)
        plt.imshow(img_arr,cmap='gray')
        plt.show()
        break
    break

def creat_data(my_list,categ,my_dir):
    img_size = 250
    for ca in categ:
        path = os.path.join(my_dir,ca)
        class_num = categ.index(ca)
        for img in os.listdir(path):
            try:
                img_arr =Image.open(os.path.join(path,img))
                new_img = img_arr.resize((img_size,img_size))
                new_img = np.asarray(new_img)
                arr = new_img.reshape((img_size, img_size, 1))
                my_list.append([arr,class_num])
            except Exception as e:
                e = e
train_list = []
test_list = []
val_list = []
creat_data(train_list,categ,train_dir)
print(len(train_list))

creat_data(test_list,categ,test_dir)
print(len(test_list))

creat_data(val_list,categ,val_dir)
print(len(val_list))

def split_data(X,y,my_list):
    img_size = 250
    for fe,la in my_list:
        X.append(fe)
        y.append(la)
    X = np.array(X).reshape(-1, img_size, img_size, 1)

X_train = []
y_train = []
X_test = []
y_test = []
X_val = []
y_val = []
split_data(X_train, y_train, train_list)
split_data(X_test, y_test, test_list)

split_data(X_val, y_val, val_list)

X_train = np.asarray(X_train)
y_train = np.asarray(y_train)
X_test = np.asarray(X_test)
y_test = np.asarray(y_test)
X_val = np.asarray(X_val)
y_val = np.asarray(y_val)

X_train = X_train/255.0
X_test = X_test/255.0
X_val = X_val/255.0


import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D

from tensorflow.keras.callbacks import EarlyStopping
early_stop = EarlyStopping(monitor = 'val_loss', patience = 5, restore_best_weights=True)

model = Sequential()
model.add(Conv2D(64, (3,3), input_shape = X_train.shape[1:]))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size = (2,2)))
model.add(Dropout(0.5))

model.add(Conv2D(64, (3,3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size = (2,2)))
model.add(Dropout(0.5))



model.add(Flatten())
model.add(Dense(64))

model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer = tf.keras.optimizers.Adam(lr=1e-5),
              metrics=['accuracy'])



model.fit(X_train, y_train,epochs = 12, batch_size = 32, validation_data = (X_val,y_val),callbacks = [early_stop])

model.evaluate(X_test,y_test)