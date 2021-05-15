from fastai.vision.all import *

path = untar_data(URLs.MNIST_SAMPLE)
dls = ImageDataLoaders.from_folder(path)
dls.show_batch()