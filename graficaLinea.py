#importando libreria 
import matplotlib.pyplot as plt 

#1. Tener una fuente de datos 
barrios=["Calasanz", "Laureles", "Castilla", "Robledo", "Belen", "Boston", "Buenos Aires", "Manrique", "Estadio", "Blanquizal"]
poblacion=[12000,25000,40000,100000,200000,50000,60000,250000,10000,5000]

barrios3=["Calasanz", "Laureles", "Castilla", "Robledo", "Belen", "Boston", "Buenos Aires", "Manrique", "Estadio", "Blanquizal"]
poblacion3=[13000,26000,41000,110000,200000,50000,6100,250000,10000,6000]

barriosBello=["La cumbre", "Santa Ana", "Niquia", "Bella Vista", "Paris", "Camacol", "Cabañas", "Barrio Obrero", "Navarra", "Pacheli"]
poblacionBello=[30000,12000,100000,50000,25000,3000,5500,48500,10000,5000]

#2. Procedo a utilizar el matplotlib para generar la grafica


#3. Modificamos la grafica
plt.plot(barrios,poblacion,marker="o",linestyle="-.",color="r")
plt.plot(barrios3,poblacion3,marker="4",linestyle="--",color="b")

plt.xlabel("Barrios de Medellín")
plt.ylabel("Población")
plt.title("Densidad de población Medellín 2023")

plt.savefig("Linea.png")
plt.show()