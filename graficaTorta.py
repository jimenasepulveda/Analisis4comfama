import matplotlib.pyplot as plt 

años=[2013,2014,2015,2016,2017,2018,2019,2020,2021,2022]
consumidores=[4000,10000,8000,4500,4000,5000,4800,12000,14000,10000]
colores=["#1FF8E7","#F81FDA","#C31FF8","#1FACF8","#1FF89F","#E1F81F","#F8B31F","#F81F88","#F81F5A","#F81FF8"]

plt.pie(consumidores,labels=años)
plt.title("Consumidores por Años")
plt.show()