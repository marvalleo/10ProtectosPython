#ZIP une 2 listas formando tuplas
nombres=['Ana', 'Hugo', 'Valeria']
edades=[65,29,42]
ciudades=['chimbarongo','tilcoco','ramuncho']

combinados = list(zip(nombres,edades,ciudades))
for nombre, edad, ciudad in combinados: 
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")
