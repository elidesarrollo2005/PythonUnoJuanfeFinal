#COMO USAR PANDAS PARA CREAR FILTROS 

#1.Importarlo
import pandas as pd
#2. traer los datos
from Data.simulador import  generar_ventas
#3. convertir los datos en un DATAFRAME
DataFrame=pd.dataFrame(generar_ventas())

#4. aplicar los filtros (5)
#print(DataFrame)

#yo como administrador de la tienda Quiero tener las ventas de Eliana Restrepo
filtroUno=DataFrame.query("vendedor=='Eliana Restrepo'")
#print(filtroUno)

#yo como administrador de la tienda quiero ver ventas con mas de tres productos
filtroDos=DataFrame.query("cantidad>= 3")
#print(filtroDos)

#yo como administrador de la tienda quiero ver ventas por valores de mas de 900 mil
filtroTres=DataFrame.query("total>900000")
#print(filtroTres)

#yo como administrador de la tienda quiero ver ventas de las camisetas polo
filtroCuatro=DataFrame.query("producto=='camiseta POLO'")
#print(filtroCuatro)

#yo como administrador de la tienda quiero ver las ventas de los productos que menos se venden 
filtroCinco=DataFrame.query("producto=='gorra beisbol' or producto=='bufanda' or producto=='bermuda'")
print(filtroCinco)
