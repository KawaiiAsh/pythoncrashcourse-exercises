import matplotlib.pyplot as plt

plt.scatter(2, 4, s=200)

plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of value",fontsize=14)

plt.tick_params(axis="both",which='major',labelsize=14)
plt.show()
