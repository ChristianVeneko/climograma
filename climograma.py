import matplotlib.pyplot as plt

meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
temperaturas = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
precipitaciones = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
fig, ax1 = plt.subplots()

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
                
                 
ciudad = input('Ingrese la ciudad: ')                 
solicitarDatos(temperaturas, 'temperatura')
print(temperaturas)
solicitarDatos(precipitaciones, 'precipitacion')
print(precipitaciones)

ax1.bar(meses, precipitaciones, color='b')
ax1.set_xlabel('Mes')
ax1.set_ylabel('Precipitación (mm)', color='b')
ax1.tick_params(axis='y', labelcolor='b')
ax1.axhline(y=sum(precipitaciones)/len(precipitaciones), linestyle='--', color='b')

ax2 = ax1.twinx()

ax2.plot(meses, temperaturas, color='r')
ax2.set_ylabel('Temperatura (°C)', color='r')
ax2.tick_params(axis='y', labelcolor='r')
ax2.axhline(y=sum(temperaturas)/len(temperaturas), linestyle='--', color='r')

plt.title('Climograma de ' + ciudad)
plt.show()












