import os
import tensorflow as tf

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
if tf.test.gpu_device_name():
    print('Default GPU Device: {}'.format(tf.test.gpu_device_name()))
    print('Your tensorflow-gpu is available')
else:
    print('Your tensorflow-gpu is not available')
    print("Please install GPU version of TF")
import torch

if torch.cuda.is_available():
    print('Default GPU Device: {}'.format(torch.cuda.get_device_name()))
    print('Your pytorch-gpu is available')
else:
    print('Your pytorch-gpu is not available')
    print("Please install GPU version of Pytorch")
