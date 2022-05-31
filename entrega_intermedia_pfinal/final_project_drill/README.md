# Instrucciones para ejecutar este proyecto

- Clonar el proyecto y cambiar de rama
```bash
git clone https://github.com/jmbel93/PrimeraEntregaPfinal-Belaga-CedielRodriguez.git

cd final_project_drill



```

- Crear y activar entorno virtual (Windows)
```bash
C:\>python -m venv c:\ruta\al\entorno\virtual
C:\>c:\ruta\al\entorno\virtual\scripts\activate.bat
```

- Crear y activar entorno virtual (Linux)
```bash
python3 -m venv venv
source venv/bin/activate
```
- Instalar Django
```bash
pip install Django
```

- Crear base de datos con los Modelos (hacer migraciones y migrar)
```bash
python manage.py makemigrations app_coder

python manage.py migrate
```

- Crear super-usuario
```bash
python manage.py createsuperuser
```

- Ejecutar proyecto
```bash
python manage.py runserver
```
----------
1er paso dentro del servidor(opcional): Buscar en la base de datos dentro de la pestaña catalogue los libros disponibles.
2do paso dentro del servidor: utilizar cualquiera de las pestañas del sitio para revisar los libros comprados, vendidos o alquilados.
3er paso dentro del servidor(opcional): clickear en los botones correspondientes para agregar libros a cualquiera de las otras tres bases de datos.
4to paso dentro del servidor: las pestañas se van a ver modificadas apenas se termine de ingresar los libros nuevos.



En la base de datos de BooksForRent se encuentra el catálogo del cual se pueden elegir los distintos libros a alquilar y/o comprar.
La base de datos y modelo BuyABook sirve para elegir qué libros comprar y en qué cantidad.
La base de datos y modelo RentABook sirve para elegir qué libros alquilar y para marcar en qué fecha fueron alquilados.
La base de datos y modelo SellABook sirve para que un usuario hipotético le venda libros usados a una biblioteca.