import plaidml.keras
plaidml.keras.install_backend()

import numpy as np
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers.core import Dense, Activation

# completely random training data...
n = 1000
x0 = np.random.normal(3, 1, n*2)
x1 = np.random.normal(0, 1, n*2)
X = np.stack([x0, x1], axis=1)
y = np.zeros((n*2, 2))
y[:n, 0] = 1
y[n:, 1] = 1

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

model = Sequential()
model.add(Dense(10, input_shape=(2,)))
model.add(Activation('sigmoid'))
model.add(Dense(2))
model.add(Activation('softmax'))

model.compile(loss='categorical_crossentropy',
        optimizer='adagrad', metrics=['accuracy'])

model.fit(X_train, y_train, epochs=20, batch_size=75, verbose=1, validation_data=(X_test, y_test))
print()
print(model.evaluate(X, y)[1])
