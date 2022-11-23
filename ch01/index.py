import tensorflow as tf

tensol = tf.constant([3,4,5])
# tf.Tensor([3 4 5], shape=(3,), dtype=int32)

tensol2 = tf.constant([6,7,8])

print(tensol + tensol2)
# tf.Tensor([ 9 11 13], shape=(3,), dtype=int32)

tensol3 = tf.constant([[1,2],
                       [3,4]])
tensol4 = tf.constant([[2,2],
                       [3,4]])

print(tf.add(tensol3,tensol4))
# tf.Tensor(
# [[3 4]
#  [6 8]], shape=(2, 2), dtype=int32)

tensol5 = tf.zeros([2,2,3])
print(tensol5)
# tf.Tensor(
# [[[0. 0. 0.]
#   [0. 0. 0.]]
#  [[0. 0. 0.]
#   [0. 0. 0.]]], shape=(2, 2, 3), dtype=float32)

print(tensol5.shape)
# (2, 2, 3)

w = tf.Variable(1.0)
# 딥러닝 상 변수 weight
print(w.numpy())
# 변수 안에 값
# 1.0

w.assign(2)
# 변수 변경
print(w)
# <tf.Variable 'Variable:0' shape=() dtype=float32, numpy=2.0>

# tf.add()
# tf.subtract()
# tf.divide()
# tf.multiply()
# tf.matmul()