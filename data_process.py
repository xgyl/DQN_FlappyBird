lines = open('data1.txt','r')
import matplotlib.pyplot as plt
for line in lines:
    my_list = eval(line)

lis = [i for i in range(1000)]
# plt.title('训练过程')
plt.subplot(221)
plt.plot(my_list)
plt.xlabel('turn')
plt.ylabel('score')
plt.subplot(222)
plt.plot(my_list)
plt.xlabel('turn')
plt.ylabel('score')
plt.ylim(0, 20)
plt.subplot(223)
plt.plot([i+5700 for i in range(len(my_list[5700:]))], my_list[5700:])
plt.xlabel('turn')
plt.ylabel('score')
plt.show()
