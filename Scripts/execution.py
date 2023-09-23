import subprocess

ENCODER_PATH = "./../VTM_DataExtraction/bin/xcode/clang-14.0/x86_64/release/EncoderApp"
AI_CFG_PATH = "../VTM_DataExtraction/cfg/encoder_intra_vtm.cfg"
SQ_CFG_PATH = "../VTM_DataExtraction/cfg/per-sequence/Vidyo4.cfg"
SQ_PATH = "../../Sequences/vidyo4_720p_60.yuv"

EXEC_STR = [ENCODER_PATH]
EXEC_STR.append("-c")
EXEC_STR.append(AI_CFG_PATH)
EXEC_STR.append("-c")
EXEC_STR.append(SQ_CFG_PATH)
EXEC_STR.append("--InputFile="+SQ_PATH)


output = subprocess.run(EXEC_STR)
