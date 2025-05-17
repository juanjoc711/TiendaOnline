#  Pruebas con Postman para el back

Este es un resumen de todas las pruebas realizadas con Postman para probar el funcionamiento del backend. Además, se elaborarán tests posteriormente que también lo comprueben.

---

## Configuración básica

- **Método:** `POST`
- **URL:** `http://localhost:5000/graphql`
- **Headers:**
    - `Content-Type: application/json`
- **Body:** JSON en formato `raw`

---

## 1. Consultar todos los productos

**Query:**
```json
{
  "query": "query { productos { id nombre precio stock disponible } }"
}
```

**¿Objetivo?**  
Comprobar que el backend devuelve la lista completa de productos con todos sus datos.

**¿Resultado?**  
```json
{
  "data": {
    "productos": [
      {
        "disponible": true,
        "id": 1,
        "nombre": "Teclado",
        "precio": 29.99,
        "stock": 10
      },
      {
        "disponible": false,
        "id": 2,
        "nombre": "Ratón",
        "precio": 19.99,
        "stock": 0
      },
      {
        "disponible": true,
        "id": 3,
        "nombre": "Pantalla",
        "precio": 129.99,
        "stock": 5
      }
    ]
  }
}
```
---

## 2. Aumentar el stock de un producto agotado

**Query:**
```json
{
  "query": "mutation { actualizarStock(id: 2, cantidad: 5) { producto { id nombre stock disponible } mensaje } }"
}
```

**¿Objetivo?**  
Verificar que, al aumentar el stock de un producto que estaba en cero, el campo "disponible" pase a "true"".

**¿Resultado?**  
```json
{
  "data": {
    "actualizarStock": {
      "mensaje": "Stock actualizado correctamente.",
      "producto": {
        "disponible": true,
        "id": 2,
        "nombre": "Ratón",
        "stock": 5
      }
    }
  }
}
```
---

## 3. Disminuir el stock de un producto con varias unidades

**Query:**
```json
{
  "query": "mutation { actualizarStock(id: 1, cantidad: -3) { producto { id nombre stock disponible } mensaje } }"
}
```

**¿Objetivo?**  
Asegurarme de que el stock disminuye correctamente y que el producto sigue disponible si el stock sigue siendo mayor a cero.

**¿Resultado?**  
```json
{
  "data": {
    "actualizarStock": {
      "mensaje": "Stock actualizado correctamente.",
      "producto": {
        "disponible": true,
        "id": 1,
        "nombre": "Teclado",
        "stock": 7
      }
    }
  }
}
```
---

## 4. Dejar el stock en cero

**Query:**
```json
{
  "query": "mutation { actualizarStock(id: 1, cantidad: -100) { producto { id nombre stock disponible } mensaje } }"
}
```

**¿Objetivo?**  
Ver que, al llegar el stock a cero, el campo "disponible" cambie a "false" y se muestre un mensaje de advertencia por acabarse el stock.

**¿Resultado?**  
```json
{
  "data": {
    "actualizarStock": {
      "mensaje": "¡Aviso! El producto se ha quedado sin stock.",
      "producto": {
        "disponible": false,
        "id": 1,
        "nombre": "Teclado",
        "stock": 0
      }
    }
  }
}
```
---

## 5. Intentar modificar el stock de un producto inexistente

**Query:**
```json
{
  "query": "mutation { actualizarStock(id: 999, cantidad: 1) { producto { id nombre stock disponible } mensaje } }"
}
```

**¿Objetivo?**  
Comprobar que el sistema devuelve un error si intento modificar el stock de un producto que no existe.

**¿Resultado?**  
```json
{
  "errors": [
    "Producto no encontrado\n\nGraphQL request:1:12\n1 | mutation { actualizarStock(id: 999, cantidad: 1) { producto { id nombre stock disponible } mensaje } }\n  |            ^"
  ]
}
```