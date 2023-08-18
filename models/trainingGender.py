from utils.inference import generator
from utils.datasets import getData
from models.cnn import simple_CNN
import numpy as np


X_train, y_train = getData('../datasets/gender_datasets/Training')
X_test, y_test = getData('../datasets/gender_datasets/Validation')


X_train_scaled = np.array([x.ravel()/255. for x in X_train])
X_test_scaled = np.array([x.ravel()/255. for x in X_test])

model, simple_CNN = simple_CNN((50, 50, 1), 2)

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(generator(X_train, y_train),steps_per_epoch=5,
          epochs=500,validation_data=generator(X_test, y_test),
          validation_steps=5)

simple_CNN.save(r'E:\AI\face\trained_models\gender_models\gender_simple_CNN.hdf5')