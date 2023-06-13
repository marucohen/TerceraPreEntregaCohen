# TerceraPreEntregaCohen
La primera parte pude hacerla sola, lo básico de creación de la app. Cuando tengo que empezar a editarla, armar formularios, etc, ya nose hacerla así que copie lo que estaba en el repositorio de la plataforma, el de Nico, para al menos tener el archivo “completo” y a medida que siga estudiando estos días poder revisarlo y arreglarlo.
1)  Inicio un proyecto Django en una carpeta, en este caso carpeta “Tercera PreEntregaIncompleta”
Para esto corro el comando: django-admin startproject TerceraPreEntregaCohen en la terminal.
Previamente indiqué git init en la terminal para que empiece a funcionar GIT y el correspondiente archivo .gitignore

2) Generación de BASE DE DATOS:
Corro el comando: python manage.py migrate en la terminal

3) Inicio la página WEB de mi proyecto con: python manage.py runserver en la terminal y me genera:
Starting development server at http://127.0.0.1:8000/

4) Si trabajo sobre mi proyecto y no sobre APP deberé armar views para definir las funciones de las vistas de mi página web. Las mismas luego deben linkearse mediante el archivo URLS.
Pero en este caso vamos a hacer una APP que contará con sus propias views, solo que deberé linkear los URLS del proyecto a los de la APP.

5) Inicio la app con el comando: python manage.py startapp AppTerceraEntrega
6) En el  settings del proyecto debo incluir la APP, solo la agrego al listado de Installed Apps.
7) Debo también, en los URLS de mi proyecto incluir mi APP.
8) En los modelos de mi APP defino las partes de la app que quiero hacer, serán: Curso, Estudiantes, Profesores, Entregables. 
9) Debo crear un archivo de URLS dentro de mi carpeta de APP.
10) CREACIÓN DE FORMULARIOS 
De aquí en adelante no comprendí la forma ya que debo repasar las clases, me fije el repositorio que provee la cátedra para tener el archivo completo y luego de repasar poder entenderlo sola.

