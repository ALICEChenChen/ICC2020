
# import os
import matplotlib.pyplot as plt
import numpy as np



f, ax = plt.subplots(figsize = (7, 6))
x = np.arange(5)
plt.grid(linestyle=":",color="k")
#client
y = [0.082, 0.0845, 0.0879, 0.089, 0.091]
#server
y1 = [0.146, 0.151, 0.155, 0.157, 0.161]
#blockchain
y2 = [0.39, 0.778, 1.558, 3.114, 6.23]
bar_width = 0.25

font1 = {'family': 'Times New Roman', 'weight': 'normal', 'size': 23}
plt.tick_params(labelsize=23)
tick_label = ["10K", "20K", "40K", "80K", "160K"]
A=plt.bar(x, y, bar_width, align="center", color="r", label="Owner-side states", alpha=0.7)
B=plt.bar(x+bar_width, y1, bar_width,  align="center",color="b", label="On-chain checklist", alpha=0.7)
C=plt.bar(x+2*bar_width, y2, bar_width,  align="center", color="y",label="Server-side indexes", alpha=0.7)
legend = plt.legend(handles=[A,B,C], prop=font1)

labels = ax.get_xticklabels() + ax.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]
plt.xlabel("Number of keyword-fileID pairs",font1)
plt.ylabel("Storage cost (MB) ", font1)

plt.xticks(x+bar_width/2, tick_label)

# plt.legend()
plt.savefig('cost.pdf')
plt.show()

# , alpha=0.5






