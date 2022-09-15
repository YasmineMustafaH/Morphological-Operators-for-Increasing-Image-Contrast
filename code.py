import numpy as np
from cv2 import cv2
from matplotlib import pyplot as plt
import math
import cmath 
from scipy import signal
import matplotlib.pyplot as plt
from PIL import Image
import PIL


def Dilation(image,e):
    height = image.shape[0]
    width = image.shape[1]

    h = e.shape[0]
    result = np.zeros(image.shape)
    
    for i in range(int(h/2),height-(h-1)):
     for j in range(int(h/2),width-(h-1)):
        neighbors = image[i-int(h/2):i+int(h/2)+1,j-int(h/2):j+int(h/2)+1]
        max = np.amax(neighbors)
        result[i,j]=max
       

    return result
#-----------------------------------------------------------------------------------------------------------------------------------------------
def Erosion(image,e):
    height = image.shape[0]
    width = image.shape[1]

    h = e.shape[0]
    result = np.zeros(image.shape)
    for i in range(int(h/2),height-(h-1)):
     for j in range(int(h/2),width-(h-1)):
        neighbors = image[i-int(h/2):i+int(h/2)+1,j-int(h/2):j+int(h/2)+1]
        min = np.amin(neighbors)
        result[i,j]=min



    return result
#-----------------------------------------------------------------------------------------------------------------------------------------
def Opening(image,e):
  result = Dilation(Erosion(image,e),e)

  return result
#--------------------------------------------------------------------------------------------------------------------------------------

def Closing(image,e):
  result = Erosion(Dilation(image,e),e)

  return result

#------------------------------------------------------------------------------------------------------------------------------------------
#main
image = Image.open('C:/Users/yasmi/Desktop/19-4/Mars.jpg')
image = np.array(image)
B = np.ones((3,3))
a=1
b=5

red = image[:,:,0]
green = image[:,:,1]
blue = image[:,:,2]

img = np.zeros(image.shape)
img[:,:,2] = blue + np.multiply(a,(blue-Opening(blue,B))) - np.multiply(b,(Closing(blue,B)-blue))
img[:,:,1] = green + np.multiply(a,(green-Opening(green,B))) - np.multiply(b,(Closing(green,B)-green))
img[:,:,0] = red + np.multiply(a,(red-Opening(red,B))) - np.multiply(b,(Closing(red,B)-red))

img[:,:,2] = np.clip(img[:,:,2],0,255)
img[:,:,1] = np.clip(img[:,:,1],0,255)
img[:,:,0] = np.clip(img[:,:,0],0,255)


#result.save('C:/Users/yasmi/Desktop/19-4/Mars1.jpg')
img = img.astype(np.uint8)
result = Image.fromarray(img)
result.save('C:/Users/yasmi/Desktop/19-4/a1_b5_element9_2.jpg')
             

#cv2.imshow('a=1 b=5 element 3 x 3',img)
#cv2.imshow('Input',image)

#cv2.imshow('Merged Output',result)
#cv2.waitKey(0)





#ret, bw_img = cv2.threshold(image,127,255,cv2. THRESH_BINARY)
#I = np.array(bw_img)
#a=1
#b=1
#result = I + a * (I-Opening(I,B))-b*(Closing(image,B)-I)
#result2 = Image.fromarray(result)
#result.save('C:/Users/yasmi/Desktop/19-4/Mars1.jpg')

#plt.imshow(result2)
#plt.show()
                
                
              
          
