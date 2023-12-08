import subprocess
import os

ENCODER_PATH = "./../VVCSoftware_VTM_fast/bin/EncoderAppStatic"
ENCODER_TAG = "VTM-fast" # uma identificação curta do codificador usado, que será incluída no nome do arquivo de log de saída
AI_CFG_PATH = "../VTM_DataExtraction/cfg/encoder_intra_vtm.cfg"
FOLDER_CSV = "../Outputs"

QP=["22","27","32","37"]

# todos os vídeos (desatualizado):
# VIDEOS = ["vidyo4", "FourPeople_1280x720_60", "Johnny_1280x720_60", "KristenAndSara_1280x720_60",
#           "ArenaOfValor_1920x1080_60_8bit_420", "BasketballDrive_1920x1080_50", "BQTerrace_1920x1080_60",
#           "CatRobot_3840x2160_60fps_10bit_420", "Tango2_3840x2160_60fps_10bit_420", "FoodMarket4_3840x2160_60fps_10bit_420",
#           "SlideShow_1280x720_20"]

# vídeos do conjunto de treinamento (TODO):
# VIDEOS = ["FourPeople_1280x720_60", "Johnny_1280x720_60", "KristenAndSara_1280x720_60",
#           "ArenaOfValor_1920x1080_60_8bit_420", "BasketballDrive_1920x1080_50", "BQTerrace_1920x1080_60",
#           "CatRobot_3840x2160_60fps_10bit_420", "Tango2_3840x2160_60fps_10bit_420", "FoodMarket4_3840x2160_60fps_10bit_420",
#           "SlideShow_1280x720_20"]

# vídeos do conjunto de teste:
# VIDEOS = ["ParkRunning3_3840x2160_50fps_10bit_420",
#           "MarketPlace_1920x1080_60fps_10bit_420", "RitualDance_1920x1080_60fps_10bit_420",
#           "Cactus_1920x1080_50", "FourPeople_1280x720_60", "KristenAndSara_1280x720_60",
#           "SlideEditing_1280x720_30", "FoodMarket4_3840x2160_60fps_10bit_420"]

# lote atual:
VIDEOS = ["MarketPlace_1920x1080_60fps_10bit_420", "RitualDance_1920x1080_60fps_10bit_420",
          "Cactus_1920x1080_50", "FourPeople_1280x720_60", "KristenAndSara_1280x720_60",
          "SlideEditing_1280x720_30", "ParkRunning3_3840x2160_50fps_10bit_420"
          ]

SQ_CFG_DICT = {
    "vidyo4" : "../VTM_DataExtraction/cfg/per-sequence/Vidyo4.cfg",
    "FourPeople_1280x720_60" : "/home/ruhan/Trabalho-ML/VTM_DataExtraction/cfg/per-sequence/FourPeople.cfg",
    "Johnny_1280x720_60" : "/home/ruhan/Trabalho-ML/VTM_DataExtraction/cfg/per-sequence/Johnny.cfg",
    "KristenAndSara_1280x720_60" : "/home/ruhan/Trabalho-ML/VTM_DataExtraction/cfg/per-sequence/KristenAndSara.cfg",
    "ArenaOfValor_1920x1080_60_8bit_420" : "/home/ruhan/Trabalho-ML/VTM_DataExtraction/cfg/per-sequence/ArenaOfValor.cfg",
    "BasketballDrive_1920x1080_50" : "/home/ruhan/Trabalho-ML/VTM_DataExtraction/cfg/per-sequence/BasketballDrive.cfg",
    "BQTerrace_1920x1080_60" : "/home/ruhan/Trabalho-ML/VTM_DataExtraction/cfg/per-sequence/BQTerrace.cfg",
    "CatRobot_3840x2160_60fps_10bit_420" : "/home/ruhan/Trabalho-ML/VTM_DataExtraction/cfg/per-sequence/CatRobot.cfg",
    "Tango2_3840x2160_60fps_10bit_420" : "/home/ruhan/Trabalho-ML/VTM_DataExtraction/cfg/per-sequence/Tango2.cfg",
    "FoodMarket4_3840x2160_60fps_10bit_420" : "/home/ruhan/Trabalho-ML/VTM_DataExtraction/cfg/per-sequence/FoodMarket4.cfg",
    "SlideShow_1280x720_20" : "/home/ruhan/Trabalho-ML/VVCSoftware_VTM/cfg/per-sequence/SlideShow.cfg",
    "ParkRunning3_3840x2160_50fps_10bit_420" : "/home/ruhan/Trabalho-ML/VTM_DataExtraction/cfg/per-sequence/ParkRunning3.cfg",
    "MarketPlace_1920x1080_60fps_10bit_420" : "/home/ruhan/Trabalho-ML/VTM_DataExtraction/cfg/per-sequence/MarketPlace.cfg",
    "RitualDance_1920x1080_60fps_10bit_420" : "/home/ruhan/Trabalho-ML/VTM_DataExtraction/cfg/per-sequence/RitualDance.cfg",
    "Cactus_1920x1080_50" : "/home/ruhan/Trabalho-ML/VTM_DataExtraction/cfg/per-sequence/Cactus.cfg",
    "SlideEditing_1280x720_30" : "/home/ruhan/Trabalho-ML/VTM_DataExtraction/cfg/per-sequence/SlideEditing.cfg"
    }

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

FPS_DICT = {
    "vidyo4" : 60,
    "FourPeople_1280x720_60" : 60,
    "Johnny_1280x720_60" : 60,
    "KristenAndSara_1280x720_60" : 60,
    "ArenaOfValor_1920x1080_60_8bit_420" : 60,
    "BasketballDrive_1920x1080_50" : 50,
    "BQTerrace_1920x1080_60" : 60,
    "CatRobot_3840x2160_60fps_10bit_420" : 60,
    "Tango2_3840x2160_60fps_10bit_420" : 60,
    "FoodMarket4_3840x2160_60fps_10bit_420" : 60,
    "SlideShow_1280x720_20" : 20,
    "ParkRunning3_3840x2160_50fps_10bit_420" : 50,
    "MarketPlace_1920x1080_60fps_10bit_420" : 60,
    "RitualDance_1920x1080_60fps_10bit_420" : 60,
    "Cactus_1920x1080_50" : 50,
    "SlideEditing_1280x720_30" : 30
}

# SQ_CFG_PATH = "../VTM_DataExtraction/cfg/per-sequence/Vidyo4.cfg"
# SQ_PATH = "../Sequences/vidyo4_720p_60.yuv"

os.system("rm *.csv")

for video in VIDEOS :
    for qp in QP :
        EXEC_STR = [ENCODER_PATH]
        EXEC_STR.append("-c")
        EXEC_STR.append(AI_CFG_PATH)
        EXEC_STR.append("-c")
        EXEC_STR.append(SQ_CFG_DICT[video])
        EXEC_STR.append("--InputFile="+SQ_PATH_DICT[video])
        EXEC_STR.append(f"--FramesToBeEncoded={FPS_DICT[video]}")
        EXEC_STR.append("--TemporalSubsampleRatio=1")
        EXEC_STR.append(f"--QP={qp}")
        EXEC_STR.append(f"> {video}_{qp}_{ENCODER_TAG}.txt")
        EXEC = " ".join(EXEC_STR)
        print(EXEC)
        os.system(EXEC)
        # os.system(f"mv cudata.csv {FOLDER_CSV}/codingdata_{video}_{qp}.csv")
        # os.system(f"mv desfecho.csv {FOLDER_CSV}/encodeddata_{video}_{qp}.csv")