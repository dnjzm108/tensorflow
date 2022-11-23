import tensorflow as tf

# 키 = [170,180,175,160]
# 신발 = [260,270,265,255]
# y = ax + b (신발 = a * 키 + b)  모르는 직선 추정하는 식

키 = 170
신발 = 260 
# 신발 = 키 * a + b

a = tf.Variable(0.1) 
b = tf.Variable(0.2) 

def 손실함수():
    예측값 = 키 * a + b
    return tf.square( 260 - 예측값)
    # return (실제값 - 예측값)^2
# 경사 하강법
opt = tf.keras.optimizers.Adam(learning_rate=0.1)
# 인자 필수 아님 변경하고 싶을때

for i in range(300):
    opt.minimize(손실함수,var_list=[a,b])
    print(170 * a.numpy()+b.numpy())
# 인자값 필수 (손실함수,var_list=[a,b])

