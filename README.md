# Api-rest-video-renta
desarrollo backend de api rest para una tienda de video construida con el lenguaje python y el framework fastapi . el objetivo es gestionar un catalogo de discos (peliculas o videos digitales) junto con las operaciones de regisytro de usuario , venta y alquileres

## Estructura del proyecto
|--Main.py #punto de entrada de la aplicacion  de la api , fastapi
|
  entidades/     #directorio de paquetes que contiene todas las clases
  |-__init__.py
  |-disco.py
  |-usuario.py
  |-venta.py
  |-alquiler.py
  |-catalogo.py
  ##instalacion y ejecucion 
    1.Clonar el repositorio 
       git clone https://github.com/usuario/test-alquiler-video.git
    2.cd alquiler-video
    3.crear yactivar entorno virtual (opcional, recomendado)
    4.python -m venv venv
    5.source venv/bin/activate #Linux
    6.venv\scripts\activate  #windows
    7.instalar dependencias 
      7.1. pip install fastapi uvicorn py
    8.Ejecutar el servidor
      8.1. uvicorn main:app --reload
    9.Acceder a la API
       *Documentacion interactiva: https//127.0.0.1:8000/docs
       *Documntacion alternativa (ReDoc):https://127.0.0.1:8000/redoc

    ##Endpoint principales (version inicial )
    metodo endpoint descripcion
    GET  /discos/        Lista de los discos disponibles
    POST /discos/        Agregar un nuevo disco
    PUT /discos/{id}     Actualizar informacion de un disco
    DELETE /disco/{id}   Eliminar un disco
    POST /usuario/     Registro de un nuevo usuario
    POST /Ventas/      Registar ventas
    POST /Alquileres/   Registar un alquiler

    ##Tecnologia utilizada
    * Python 3.12.8
    * FastAPI
    * Uvicorn (Servidor ASGI)

    ## Proyecto desarrollado como caso de estudio
    * Nombre: **Luis Marcos Acosta.** <aluismarcos@gmail.com>
    * Github: @LuisMarcos


