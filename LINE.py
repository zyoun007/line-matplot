import matplotlib.pyplot as plt


plt.title ('Pace Chart')
plt.xlabel('Time (Minutes)')
plt.ylabel ('Distance (Miles)')

plt.grid()

x_coords =[0, 6, 14, 24, 36]
y_coords =[0, 1, 2, 3, 4]

plt.xlim(xmax = 42)
plt.ylim(ymax = 5)

plt.plot(x_coords, y_coords, marker = 'o')
#https://www.w3schools.com/python/matplotlib_markers.asp but mainly Tim helping me out as the websites weren't that useful
plt.show()

