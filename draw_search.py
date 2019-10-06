
import matplotlib.pyplot as plt

# plt.style.use('ggplot')
# 数据设置
x1 = ['4K', '8K', '16K', '32K', '64K'];

y1 = [0.16,0.33,0.63,1.2,2.63];
y3 = [4.48,4.56,4.52,4.57,4.62];
y2=[1.8,2.2,2.42,2.93,3.77]
#
#
#
#

# font1 = {'family': 'Times New Roman', 'weight': 'normal', 'size': 15}
# 设置输出的图片大小
figsize = 7, 6
figure, ax = plt.subplots(figsize=figsize)

# 在同一幅图片上画两条折线
A,= plt.plot(x1, y1, '*-r', label='Our design', linewidth=3, alpha=0.7,markersize=15)
B,= plt.plot(x1, y2, "^-y", label='Verification', linewidth=3, alpha=0.7,markersize=15)
C,= plt.plot(x1, y3, "o-b", label='Cai et al. [4]', linewidth=3, alpha=0.7,markersize=15)
plt.grid(linestyle=":",color="k")

# C,= plt.plot(x1, y3, color="y", label='C', linewidth=4.0, alpha=0.7)

# 设置图例并且设置图例的字体及大小
font1 = {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 23,
         }
legend = plt.legend(handles=[A,B,C], prop=font1, loc='upper center',  bbox_to_anchor=(0.28, 0.92))


# 设置坐标刻度值的大小以及刻度值的字体
plt.tick_params(labelsize=23)
labels = ax.get_xticklabels() + ax.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]

# 设置横纵坐标的名称以及对应字体格式
font2 = {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 23,
         }
plt.xlabel('Number of return results', font1)
plt.ylabel('Time cost (s) ', font1)

# 将文件保存至文件中并且画出图
plt.savefig('search.pdf')
plt.show()

