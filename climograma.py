import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

#variables
meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
#temperaturas y precipitaciones por defecto para pruebas
temperaturas = [18.2, 18.8, 20.5, 22.6, 24.7, 26.2, 27.0, 26.8, 25.8, 23.7, 21.0, 18.8]
precipitaciones = [34.2, 35.0, 43.4, 69.2, 157.4, 246.9, 234.1, 209.8, 144.3, 67.6, 34.8, 32.1]

#funcion para solicitar datos del usuario
def solicitarDatos(array, string):
    for i in range(len(array)):
        j = i + 1
        j = str(j)
        while True:
            try:
                array[i] = int(input('Ingresa la ' + string + ' N°: ' + j + ': '))
                break
            except ValueError:
                print('Error!!! Ingresa una ' + string + ' Valida')
                
                 
#solicitar datos, ciudad, temperaturas, precipitaciones                 
ciudad = input('Ingrese la ciudad: ')                 
solicitarDatos(temperaturas, 'temperatura')
print(temperaturas)
solicitarDatos(precipitaciones, 'precipitacion')
print(precipitaciones)

fig, ax1 = plt.subplots()

# Graficar la barra de precipitación
ax1.bar(meses, precipitaciones, color='b')
ax1.set_ylabel('Precipitación (mm)', color='b')
ax1.tick_params(axis='y', labelcolor='b')
ax1.axhline(y=sum(precipitaciones)/len(precipitaciones), linestyle='--', color='b')

# Crear un segundo eje y para la temperatura
ax2 = ax1.twinx()

# Graficar la curva de temperaturas
ax2.plot(meses, temperaturas, color='r')
ax2.set_xlabel('Mes')
ax2.set_ylabel('Temperatura (°C)', color='r')
ax2.tick_params(axis='y', labelcolor='r')
ax2.axhline(y=sum(temperaturas)/len(temperaturas), linestyle='-.', color='r')

maxTemperatura = max(temperaturas)
maxTemperaturaMas1 = int(round(maxTemperatura)) + 10
ax2.set_ylim([0, maxTemperatura])
ax2.set_yticks(range(0, maxTemperaturaMas1, 2))


plt.title('Climograma de ' + ciudad)

#graficar todo
plt.show()


