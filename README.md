# Sistema Básico de Gestión de Garaje 

## Autor:
Fernanda Vaca

# Descripción

- Este proyecto consiste en el desarrollo de una aplicación de escritorio con interfaz gráfica utilizando Python y Tkinter.
- El sistema permite registrar vehículos que ingresan a un garaje y visualizar la información en una tabla dentro de la aplicación.
- El objetivo del proyecto es aplicar una arquitectura modular, separando el programa en diferentes capas para mejorar la organización del código y facilitar su mantenimiento.

# Funcionalidades del sistema

La aplicación permite:

- Registrar vehículos en el garaje.
- Ingresar información básica del vehículo:
* Placa
* Marca
* Propietario
- Visualizar los vehículos registrados en una tabla.
- Limpiar los campos del formulario.

# Tecnologías utilizadas
Python
Tkinter (interfaz gráfica)
Programación orientada a objetos
Arquitectura modular
Arquitectura del proyecto

# El sistema fue organizado siguiendo la estructura vista en clase:
garaje_app/
│
├── main.py
├── modelos/
│   └── vehiculo.py
├── servicios/
│   └── garaje_servicio.py
└── ui/
    └── app_tkinter.py

# Descripción de carpetas
- modelos
Contiene la clase que representa el vehículo dentro del sistema.

- servicios
Contiene la lógica del programa, como el registro y almacenamiento de vehículos.

- ui
Contiene la interfaz gráfica desarrollada con Tkinter.

- main.py
Archivo principal encargado de iniciar la aplicación.
