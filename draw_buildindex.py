
import matplotlib.pyplot as plt

# plt.style.use('ggplot')
# 数据设置
x1 = ['10K', '20K', '40K', '80K', '160K'];
y1 = [0.85, 1.63, 3.29, 6.41, 12.7];


# y2 = [0, 214, 445, 627, 800];
#
#
#
# y3 = [0, 20, 40, 60, 80];

# font1 = {'family': 'Times New Roman', 'weight': 'normal', 'size': 15}
# 设置输出的图片大小
figsize = 7, 6
figure, ax = plt.subplots(figsize=figsize)
plt.grid(linestyle=":",color="k")
# 在同一幅图片上画两条折线
A,= plt.plot(x1, y1, '*-r', label='Build inverted indexes', linewidth=3.0, alpha=0.7,markersize=15)


# 设置图例并且设置图例的字体及大小
font1 = {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 23,
         }
legend = plt.legend(handles=[A], prop=font1)

# 设置坐标刻度值的大小以及刻度值的字体
plt.tick_params(labelsize=23)
labels = ax.get_xticklabels() + ax.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]

# 设置横纵坐标的名称以及对应字体格式
font2 = {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 23,
         }
plt.xlabel('Number of keyword-fileID pairs', font1)
plt.ylabel('Time cost (s) ', font1)

# 将文件保存至文件中并且画出图
# plt.savefig('figure.eps')
plt.savefig('buildindex.pdf')
plt.show()

