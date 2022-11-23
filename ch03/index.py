import pandas as pd

data = pd.read_csv('data.csv')

# print(data.isnull().sum())
# 빈칸 세주기
data = data.dropna()
# 빈칸 삭제

y데이터 = data['admit'].values
# value 값만 가져오기

x데이터 = []

# 가로줄 한 행씩 출력

for i,rows in data.iterrows():
   x데이터.append( [ rows['gre'] , rows['gpa'] , rows['rank'] ] )

# print(x데이터)

# print(data['gpa'].min())
# min()최소값 max() 최대값  count()갯수

# data = data.fillna(100)
# 빈칸 채워주기

# exit()
# 멈춤

import numpy as np
import tensorflow as tf

# 모델 생성(레이어 생성(노드,활성 함수)) 
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64,activation='tanh'),
    tf.keras.layers.Dense(128,activation='tanh'),
    tf.keras.layers.Dense(1,activation='sigmoid')
])


model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])
#              러닝레이트             획률예측  (이름 외우기)

model.fit( np.array(x데이터),y데이터 , epochs =1000)
# 학습( x데이터 ,y 데이터 , epochs =10)
# numpy array or tf tensor
#    학습데이터  실제 데이터    몇번 학습할지

# 예측

예측값 = model.predict( [[750,3.70,3], [400,2.2,1]])
print(예측값)

# 1.모델만들고
# 2.데이터 집어넣고 학습
# 3.새로운 데이터 예측