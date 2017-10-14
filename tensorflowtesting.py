import tensorflow as tf
node1 = tf.constant(3.0, dtype=tf.float32)
node2 = tf.constant(4.0) # also tf.float32 implicitly
# print(node1, node2)

sess=tf.Session()
print(sess.run([node1,node2]))
node3 = tf.add(node1,node2)
print('node3:',node3)
print(sess.run(node3))

a=tf.placeholder(tf.float32)
b=tf.placeholder(tf.float32)

adder_triple=(a+b)*3

print(sess.run(adder_triple,{a:3,b:4.5}))
print(sess.run(adder_triple,{a:[1,3],b:[2,4]}))

W=tf.Variable([.3],dtype=tf.float32)
y=tf.Variable([-.3],dtype=tf.float32)
g=tf.placeholder(tf.float32)
linear_model=W*y*g

init=tf.global_variables_initializer()
sess.run(init)

print(sess.run(linear_model,{g:[1,2,3,5]}))