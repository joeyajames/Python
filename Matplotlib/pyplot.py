import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. simple plot with 4 numbers
plt.plot([1, 3, 2, 4])
plt.show()

# 2. points have x and y values; add title and axis labels
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.title('Test Plot', fontsize=8, color='g')
plt.xlabel('number n')
plt.ylabel('n^2')
plt.show()

# 3. change figure size. plot red dots; set axis scales x: 0-6 and y: 0-20
plt.figure(figsize=(1,5))	# 1 inch wide x 5 inches tall
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')	# red-o
plt.axis([0, 6, 0, 20])						# [xmin, xmax, ymin, ymax]
plt.annotate('square it', (3,6))
plt.show()

# 4. bar chart with four bars
plt.clf()			# clear figure
x = np.arange(4)
y = [8.8, 5.2, 3.6, 5.9]
plt.xticks(x, ('Ankit', 'Hans', 'Joe', 'Flaco'))
plt.bar(x, y)
# plt.bar(x, y, color='y')
# plt.bar(x, y, color=['lime', 'r', 'k', 'tan'])
plt.show()

# 5. two sets of 10 random dots plotted
d = {'Red O' : np.random.rand(10),
     'Grn X' : np.random.rand(10)}
df = pd.DataFrame(d)
df.plot(style=['ro','gx'])
plt.show()

# 6. time series - six months of random floats
ts = pd.Series(np.random.randn(180), index=pd.date_range('1/1/2018', periods=180))
df = pd.DataFrame(np.random.randn(180, 3), index=ts.index, columns=list('ABC'))
df.cumsum().plot()
plt.show()

# 7. random dots in a scatter
N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
sizes = (30 * np.random.rand(N))**2  # 0 to 15 point radii
plt.scatter(x, y, s=sizes, c=colors, alpha=0.5)
plt.show()

# 8. load csv file and show multiple chart types
df = pd.read_csv('Fremont_weather.txt')
print(df)
plt.bar(df['month'], df['record_high'], color='r')
plt.bar(df['month'], df['record_low'], color='c')
plt.plot(df['month'], df['avg_high'], color='k')
plt.plot(df['month'], df['avg_low'], color='b')
plt.legend()   # or plt.figlegend for legend outside the plot area
plt.show() 

# 9. subplots
fig = plt.figure()
fig.suptitle('My SubPlots')
fig.add_subplot(221)   #top left
plt.plot([np.log(n) for n in range(1,10)])
fig.add_subplot(222, facecolor='y')   #top right
fig.add_subplot(223)   #bottom left
fig.add_subplot(224)   #bottom right 
plt.show()

fig, plots = plt.subplots(2, sharex=True)
fig.suptitle('Sharing X axis')
x = range(0,200,5)
y = [n**0.8 for n in x]
plots[0].plot(x, y, color='r')
plots[1].scatter(x, y)

# 10. save figure to image file
plt.figure(figsize=(4,3), dpi=100)
plt.plot([245, 170, 148, 239, 161, 196, 112, 258])
plt.axis([0, 7, 0, 300])
plt.title('Flight Data')
plt.xlabel('Speed')
# plt.savefig('Flights.png')
plt.show()

