import matplotlib.pyplot as plt

#Data for the pie chart
etiquetas = ['Category A','Category B','Category C']
datos = [30, 45, 25]

#Create a simple pie chart
plt.pie(datos, labels=etiquetas)
plt.axis('equal') #Equal aspect ratio ensures that pies is drawn as a circle

#Save the plot as an image file
plt.savefig('pie_chart.png')

#Optionally, clear the plot after saving to avoid replotting issues in the future
plt.close()
