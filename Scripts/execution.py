import subprocess
import os

ENCODER_PATH = "./../VTM_DataExtraction/bin/EncoderAppStatic"
AI_CFG_PATH = "../VTM_DataExtraction/cfg/encoder_intra_vtm.cfg"
FOLDER_CSV = "../Outputs"

QP=["22","27","32","37"]
VIDEOS = ["vidyo4"]

SQ_CFG_DICT = {
    "vidyo4" : "../VTM_DataExtraction/cfg/per-sequence/Vidyo4.cfg"
    }

SQ_PATH_DICT = {
    "vidyo4" : "../Sequences/vidyo4_720p_60.yuv"
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
        EXEC_STR.append("--FramesToBeEncoded=5")
        EXEC_STR.append("--TemporalSubsampleRatio=1")
        EXEC_STR.append(f"--QP={qp}")
        EXEC_STR.append(f"> {video}_{qp}.txt")
        EXEC = " ".join(EXEC_STR)
        print(EXEC)
        os.system(EXEC)
        os.system(f"mv cudata.csv {FOLDER_CSV}/codingdata_{video}_{qp}.csv")
        os.system(f"mv desfecho.csv {FOLDER_CSV}/encodeddata_{video}_{qp}.csv")