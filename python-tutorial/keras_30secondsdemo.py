from keras.models import Sequential
from keras.layers import Dense
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split


#data
digits=load_digits()
train_x,test_x,train_y,test_y=train_test_split(digits.data,digits.target,test_size=0.2)

#model
model=Sequential()
model.add(Dense(units=100,activation='relu',input_dim=64))#unites表示节点数，input_dim表示向量维度
model.add(Dense(units=10,activation='softmax'))
model.compile(loss='sparse_categorical_crossentropy',optimizer='sgd',metrics=['accuracy'])
# model.compile(loss=keras.losses.categorical_crossentropy,optimizer=keras.optimizer.SGD(lr=0.01,momentum=0.9,nesterov=True))
model.fit(train_x,train_y,epochs=5,batch_size=32)
loss_and_metrics=model.evaluate(test_x,test_y,batch_size=128)
print(loss_and_metrics)