# Documentación backend tienda online (Flask + GraphQL)

En este repositorio se ha elaborado el backend de una tienda online, desarrollado con Flask y GraphQL. Incluye la opción de conectarlo a un frontend en Vue y permite gestionar el inventario de productos de forma reactiva: el stock puede aumentarse o disminuirse desde el frontend, y la disponibilidad de cada producto se actualiza dinámicamente.

---

## Funcionalidad principal

- Los productos se almacenan en memoria en una lista de Python (`data.py`), simulando una base de datos.
- Cada producto tiene los siguientes campos:  
    - `id` (int)
    - `nombre` (str)
    - `precio` (float)
    - `stock` (int)
    - `disponible` (bool)
- Al modificar el stock:
    - Si el stock llega a 0, el producto se marca como **no disponible**.
    - Si el stock sube desde 0, se marca como **disponible**.

---

## Cómo ejecutar el backend

### Opción 1: Ejecutar localmente sin Docker

Se requiere tener Python 3.11 y Flask instalados.

```bash
cd tiendaOnline
pip install -r requirements.txt
python app.py
```

La API estará disponible en:  
 http://localhost:5000/graphql

### Opción 2: Ejecutar con Docker

```bash
docker compose up --build
```

Esto levanta el contenedor en `localhost:5000`.
Además, está configurado para ejecutar los tests directamente al levantar con docker.

---

## ¿Cómo probar el backend?

El backend se ha probado con postman, tal y como se documenta en:

-  [pruebasPostman.md](pruebasPostman.md)

---

## Tests automáticos

El archivo `test.py` contiene pruebas básicas que verifican:

- Consulta de productos
- Aumento/disminución de stock
- Lógica de disponibilidad
- Control de errores al acceder a productos inexistentes

Para ejecutarlas (con el backend corriendo):

```bash
python test.py
```

---

## Frontend asociado

El frontend en Vue que consume este backend está en el siguiente repositorio:

 [https://github.com/juanjoc711/inventarioReactivo/tree/Practica2Front](https://github.com/juanjoc711/inventarioReactivo/tree/Practica2Front)

Esta rama contiene la versión adaptada para usar este backend en vez de Firebase. Permite ver el stock y la disponibilidad de productos en tiempo real. Se ejecuta dicho front con "npm run dev", y sirve tanto si usas el back dockerizado como si no.

---

## Respuestas teóricas

Las respuestas a las preguntas planteadas en el enunciado están en:

- [Respuestas.md](Respuestas.md)

---

## Estructura del backend

```
tiendaOnline/
├── app.py               # App principal de Flask
├── schema.py            # Definición del esquema GraphQL
├── data.py              # Productos almacenados en memoria
├── test.py              # Pruebas automáticas del backend
├── pruebasPostman.md    # Detalle de pruebas manuales realizadas
├── Respuestas.md        # Respuestas teóricas solicitadas
├── Dockerfile           # Imagen para ejecutar el backend
├── docker-compose.yml   # Configuración de servicio backend
└── requirements.txt     # Dependencias necesarias
```

---

## Diagrama de arquitectura:
![alt text](/img/diagramaArquitectura.png)

## Diagrama de clases:
![alt text](/img/diagramaDeClases.png)
