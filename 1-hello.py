
"""taken from this page: https://www.tensorflow.org/install/install_mac#ValidateYourInstallation

to validate Mac installation :)

"""


#import os
#os.environ['TF_CPP_MIN_LOG_LEVEL']='2' # to remove the warnings

import tensorflow as tf
import _common

hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))

