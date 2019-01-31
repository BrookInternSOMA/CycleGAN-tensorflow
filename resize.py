from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import collections
import os
import numpy as np
import pickle as pkl
import scipy.io as sio
import scipy.misc
import matplotlib.pyplot as plt

from utils import *


dataset_dir = 'rendering2barcode'
data = glob('./datasets/{}/*.*'.format(dataset_dir + '/trainC'))
save_dir = './datasets/' + dataset_dir + '/trainD/'

a = 1
for i in range(len(data)):
  img = get_image(data[i], resize=256)
  scipy.misc.imsave(save_dir + str(a).zfill(6) + '.jpg', img)
  a += 1

