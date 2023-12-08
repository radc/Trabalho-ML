import yuvio
from PIL import Image
import numpy as np
import pandas as pd

def tracelines(yuv,x,y,w,h) :
    if(w == 0 or h == 0):  
        return 
    yuv[y:y+h,x,0] = 255    
    yuv[y:y+h,x,1:2] = 128    
    yuv[y,x:x+w,0] = 255
    yuv[y,x:x+w,1:2] = 128
    
    

yuv_frame = yuvio.imread("/home/ruhan/Trabalho-ML/Sequences/Johnny_1280x720_60.yuv", 1280, 720, "yuv420p")
y = yuv_frame.y
u = yuv_frame.u
v = yuv_frame.v
u2 = np.zeros((2*u.shape[0],2*u.shape[1]))
v2 = np.zeros((2*u.shape[0],2*v.shape[1]))

u2[::2,::2] = u
u2[1::2,::2] = u
u2[1::2,1::2] = u
u2[::2,1::2] = u

v2[::2,::2] = v
v2[1::2,::2] = v
v2[1::2,1::2] = v
v2[::2,1::2] = v

yuv444 = np.zeros((y.shape[0],y.shape[1],3),dtype=np.uint8)
yuv444[:,:,0] = y
yuv444[:,:,1] = u2
yuv444[:,:,2] = v2

df = pd.read_csv("/home/ruhan/Trabalho-ML/Outputs/encodeddata_Johnny_1280x720_60_37.csv",delimiter="\t",header=None,names=['idx','poc','depth','x','y','width','height'])
for i in range(len(df)):
    poc = df.loc[i]['poc']
    
    if(poc) :
        break
    x = df.loc[i]['x']
    y = df.loc[i]['y']
    w = df.loc[i]['width']
    h = df.loc[i]['height']
    tracelines(yuv444,x,y,w,h)
    


img = Image.fromarray(yuv444,mode='YCbCr')
img.save("teste.jpg")

#rgb = yuvio.to_rgb(yuv_frame, specification='bt709', value_range='limited')




