import subprocess
import os

ENCODER_PATH = "./../VTM_DataExtraction/bin/EncoderAppStatic"
AI_CFG_PATH = "../VTM_DataExtraction/cfg/encoder_intra_vtm.cfg"
SQ_CFG_PATH = "../VTM_DataExtraction/cfg/per-sequence/Vidyo4.cfg"
SQ_PATH = "../Sequences/vidyo4_720p_60.yuv"

EXEC_STR = [ENCODER_PATH]
EXEC_STR.append("-c")
EXEC_STR.append(AI_CFG_PATH)
EXEC_STR.append("-c")
EXEC_STR.append(SQ_CFG_PATH)
EXEC_STR.append("--InputFile="+SQ_PATH)
EXEC_STR.append("--FramesToBeEncoded=81")

EXEC = " ".join(EXEC_STR)
os.system(EXEC)


# output = subprocess.call(EXEC_STR)
