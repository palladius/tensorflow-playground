
"""taken from this page: https://www.tensorflow.org/install/install_mac#ValidateYourInstallation

to validate Mac installation :)

"""

import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))

