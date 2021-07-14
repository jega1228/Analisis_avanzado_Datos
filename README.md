# MÉTODOS AVANZADOS DE ANÁLISIS DE DATOS - MAAD
Repositorio creado para propósitos académicos por (Grupo 01):

- Juanita Piraban Barbosa - <j.piraban188@uniandes.edu.co>
- Lorena Morales Rodríguez - <l.moralesr@uniandes.edu.co>
- Alejandro Barinas Guio - <jh.trujillo@uniandes.edu.co>
- Jaime Humberto Trujillo Perea - <ja.barinas@uniandes.edu.co>
- Alexander Zapata Galindo - <a.zapata12@uniandes.edu.co>


## CONTENIDO

### _____________________________________________________________________

### E2 - TSA 

Para esta tarea tomamos de Google Trends la popularidad de búsqueda de las palabras ***Vicente Fernandez - Cantante*** con corte mensual durante los últimos 5 años:

**Vicente Fernandez - Cantante** (Guadalajara, 17 de febrero de 1940)1, es un cantante de música ranchera, empresario, productor discográfico y actor mexicano, padre del también cantante Alejandro Fernández, es considerado un símbolo de la cultura hispanoamericana y uno de los artistas más populares de México. Las contribuciones de Fernández a la música junto con su vida personal publicitada, le han convertido en una figura global y representativa de la cultura ranchera durante más de cinco décadas. Su trabajo le ha valido dos premios Grammy, ocho premios Grammy Latinos, catorce premios Lo Nuestro y una estrella en el paseo de la fama de Hollywood. En abril de 2010 alcanzó la cifra de 75 millones de copias vendidos en todo el mundo.

| Item | Elemento |
| --- | --- |
| Fuente    | Datos de búsqueda en Google Trends de la palabra  [Vicente Fernandez - Cantante](https://trends.google.es/trends/explore?date=today%205-y&geo=CO&q=%2Fm%2F067swc)|
| Notebook           | [E2 - Python TSA Analysis](https://github.com/jega1228/MAAD_Grupo_1/blob/master/E2%20-%20Python%20TSA%20Analysis.ipynb)|

### _____________________________________________________________________

### E3 - ARIMA

En esta tarea se realizaron los análisis de 4 series de tiempo del dataset [data_arma.csv](https://github.com/jega1228/MAAD_Grupo_1/blob/master/DataSet/data_arma.csv), así como de la serie [shampoo.csv](https://github.com/jega1228/MAAD_Grupo_1/blob/master/DataSet/shampoo.csv):

| Item | Elemento |
| --- | --- |
| Notebook  | [E3 - ARIMA](https://github.com/jega1228/MAAD_Grupo_1/blob/master/E3%20-%20ARIMA.ipynb)|

### _____________________________________________________________________

### E5 - Prophet 

En esta tarea se realizó el análisis de la series de tiempo del dataset [example_retal_sales.csv](https://github.com/jega1228/MAAD_Grupo_1/blob/master/DataSet/example_retail_sales.csv):

| Item | Elemento |
| --- | --- |
| Notebook  | [E5 - Prophet](https://github.com/jega1228/MAAD_Grupo_1/blob/master/E5%20-%20Prophet.ipynb)|


### _____________________________________________________________________

### P1 - TSA - Internet en Colombia

### Datos anuales
Para el desarrollo del proyecto, se utilizó la serie de tiempo del repositorio de datos del Banco Mundial para Colombia, correspondiente al número de personas que utilizan Internet (% de la población).

Los usuarios de Internet son personas que han utilizado Internet (desde cualquier lugar) en los últimos tres meses. Internet puede ser usado a través de una computadora, teléfono móvil, asistente digital personal, máquina de juegos, TV digital, etc.

Fuente: International Telecommunication Union (ITU) World Telecommunication/ICT Indicators Database
https://datos.bancomundial.org/indicador/IT.NET.USER.ZS?locations=CO

### Datos trimestrales
Para el desarrollo del proyecto, se utilizó la serie de tiempo del porcentaje de penetración de Internet dedicado en Colombia (% de la población).

Número de suscriptores con acceso a Internet, fijo y móvil, según los datos reportados por los proveedores al último día de cada trimestre como porcentaje de la población basados en las proyecciones de población del DANE.

Fuente: Ministerio de las TIC
https://colombiatic.mintic.gov.co/


| Item | Periodo | Elemento |
| --- | --- | --- |
| Serie anual | 1994-2019 |[Uso Internet en Colombia](https://github.com/jega1228/MAAD_Grupo_1/blob/master/DataSet/P1_Serie_Uso_Internet.xlsx)|
| Notebook  | [P1 - Uso Internet](https://github.com/jega1228/MAAD_Grupo_1/blob/master/P1%20-%20Uso%20Internet.ipynb)|
| --- | --- |
| Serie trimestral | dic08-dic20 |[Acceso Internet en Colombia](https://github.com/jega1228/MAAD_Grupo_1/blob/master/DataSet/P1_Serie_Acceso_Internet_Trim.xlsx)|
| Notebook  | [P1 - Acceso Internet](https://github.com/jega1228/MAAD_Grupo_1/blob/master/P1%20-%20Acceso%20%20Internet%20Trim.ipynb)|


