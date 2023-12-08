import yuvio
from PIL import Image
import numpy as np
import pandas as pd
import re

SQ_PATH_DICT = {
    "vidyo4" : "../Sequences/vidyo4_720p_60.yuv",
    "FourPeople_1280x720_60" : "/home/ruhan/Trabalho-ML/Sequences/FourPeople_1280x720_60.yuv",
    "Johnny_1280x720_60" : "/home/ruhan/Trabalho-ML/Sequences/Johnny_1280x720_60.yuv",
    "KristenAndSara_1280x720_60" : "/home/ruhan/Trabalho-ML/Sequences/KristenAndSara_1280x720_60.yuv",
    "ArenaOfValor_1920x1080_60_8bit_420" : "/home/ruhan/Trabalho-ML/Sequences/ArenaOfValor_1920x1080_60_8bit_420.yuv",
    "BasketballDrive_1920x1080_50" : "/home/ruhan/Trabalho-ML/Sequences/BasketballDrive_1920x1080_50.yuv",
    "BQTerrace_1920x1080_60" : "/home/ruhan/Trabalho-ML/Sequences/BQTerrace_1920x1080_60.yuv",
    "CatRobot_3840x2160_60fps_10bit_420" : "/home/ruhan/Trabalho-ML/Sequences/CatRobot_3840x2160_60fps_10bit_420_jvet.yuv",
    "Tango2_3840x2160_60fps_10bit_420" : "/home/ruhan/Trabalho-ML/Sequences/Tango2_3840x2160_60fps_10bit_420.yuv",
    "FoodMarket4_3840x2160_60fps_10bit_420" : "/home/ruhan/Downloads/YUV/1600/FoodMarket4_3840x2160_60fps_10bit_420.yuv",
    "SlideShow_1280x720_20" : "/home/ruhan/Trabalho-ML/Sequences/SlideShow_1280x720_20.yuv",
    "ParkRunning3_3840x2160_50fps_10bit_420" : "/home/ruhan/Trabalho-ML/Sequences/ParkRunning3_3840x2160_50fps_10bit_420.yuv",
    "MarketPlace_1920x1080_60fps_10bit_420" : "/home/ruhan/Trabalho-ML/Sequences/MarketPlace_1920x1080_60fps_10bit_420.yuv",
    "RitualDance_1920x1080_60fps_10bit_420" : "/home/ruhan/Trabalho-ML/Sequences/RitualDance_1920x1080_60fps_10bit_420.yuv",
    "Cactus_1920x1080_50" : "/home/ruhan/Trabalho-ML/Sequences/Cactus_1920x1080_50.yuv",
    "SlideEditing_1280x720_30" : "/home/ruhan/Trabalho-ML/Sequences/SlideEditing_1280x720_30.yuv"
    }

# VIDEOS = ["ParkRunning3_3840x2160_50fps_10bit_420",
#           "MarketPlace_1920x1080_60fps_10bit_420", "RitualDance_1920x1080_60fps_10bit_420",
#           "Cactus_1920x1080_50", "FourPeople_1280x720_60", "KristenAndSara_1280x720_60",
#           "SlideEditing_1280x720_30", "FoodMarket4_3840x2160_60fps_10bit_420"]

VIDEOS = ["FourPeople_1280x720_60", "Johnny_1280x720_60", "KristenAndSara_1280x720_60",
          "ArenaOfValor_1920x1080_60_8bit_420", "BasketballDrive_1920x1080_50", "BQTerrace_1920x1080_60",
          "CatRobot_3840x2160_60fps_10bit_420", "Tango2_3840x2160_60fps_10bit_420", "FoodMarket4_3840x2160_60fps_10bit_420",
          "SlideShow_1280x720_20"]

for video in VIDEOS:
    video_width = int(re.findall("[\w_\d]+\_(\d+)x(\d+).*", video)[0][0])
    video_height = int(re.findall("[\w_\d]+\_(\d+)x(\d+).*", video)[0][1])
    # print(video, video_width, video_height)
    # continue
    yuv_frame = yuvio.imread(SQ_PATH_DICT[video], video_width, video_height, "yuv420p10le" if "10bit" in SQ_PATH_DICT[video] else "yuv420p")
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
    yuv444[:,:,0] = y/4 if "10bit" in SQ_PATH_DICT[video] else y
    yuv444[:,:,1] = u2/4 if "10bit" in SQ_PATH_DICT[video] else u2
    yuv444[:,:,2] = v2/4 if "10bit" in SQ_PATH_DICT[video] else v2


    img = Image.fromarray(yuv444,mode='YCbCr')
    img.save(video + ".jpg")

    #rgb = yuvio.to_rgb(yuv_frame, specification='bt709', value_range='limited')




