import pandas as pd

# df_codingdata = pd.read_csv("../cudata.csv",sep="\t", names=["baseqp","cost","cunumberpel","currbtdepth","currdepth","currmtdepth","currqtdepth","currtrdepth","diagavg",
#       "diagsad","diavar","diffminmax","distortion","fracbits","height","max","min","modetype","poc","qp",
#       "pelavg","pelcornersavg","peldiffdiagonal","peldifffullcorneravg","squaredcu","videoresheight","videoreswidth",
#       "treetype","width","x","y","prevpocheight","prevpocwidth","thisheightminusprevheight","thiswidthminusprevwidth",
#       "thissizeminusprevsize"])


# df_codingdata = df_codingdata[df_codingdata['poc']!=0]
# df_codingdata = df_codingdata[df_codingdata['cost']>=0]


# df_desfecho = pd.read_csv("../desfecho.csv",sep="\t", index_col=0 ,names=["poc","depth","x","y","w","h"])
# df_desfecho = df_desfecho[df_desfecho['poc']!=0]

# for line in df_codingdata['poc']:
#     print(line)

# # print(df_desfecho)



    

d = {'col1': [1, 2, 3], 'col2': [4, 5, 6]}
df = pd.DataFrame(data=d)
df.apply(setValue, axis=1)

print(df)