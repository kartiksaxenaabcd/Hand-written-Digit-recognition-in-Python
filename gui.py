import tensorflow as tf
import keras
from keras.models import load_model
from PIL import ImageGrab, Image
import numpy as np
model=load_model('savedmodel.h5')
img = Image.open('Input Image Location\\filename.png').convert('L')
img = img.resize((28,28), Image.ANTIALIAS)
data = np.array(img)
data = data/255.0 # for range b/w 0-1
data = data.reshape(-1,28, 28, 1).astype('float32')
result = model.predict(data)
a=[]
for i in result[0]:
    a.append(int(10*i))
count=-1
for c in a:
    count=count+1
    if(c==max(a)):
        break 
print('The number you just entered is ',count)    
e=[]
for s in range(10):
    e.append(s)
for m,n in zip(e,result[0]):
    print('Probability of',m,'---->',n)