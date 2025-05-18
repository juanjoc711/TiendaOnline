import requests

API_URL = "http://localhost:5000/graphql"

def print_title(title):
    print(f"\n=== {title} ===")

def test_obtener_productos():
    print_title("Test: Obtener productos")
    query = {
        "query": "query { productos { id nombre stock disponible } }"
    }
    response = requests.post(API_URL, json=query)
    assert response.status_code == 200, "Fallo al obtener productos: código de estado distinto de 200"
    data = response.json()["data"]["productos"]
    assert isinstance(data, list), "La respuesta no contiene una lista de productos"
    print(" Productos recibidos correctamente:", data)

def test_actualizar_stock_positivo():
    print_title("Test: Aumentar stock")
    query = {
        "query": "mutation { actualizarStock(id: 1, cantidad: 2) { mensaje producto { id stock disponible } } }"
    }
    response = requests.post(API_URL, json=query)
    assert response.status_code == 200, "Fallo al aumentar el stock"
    print("Stock aumentado con éxito:", response.json())

def test_actualizar_stock_negativo():
    print_title("Test: Disminuir stock")
    query = {
        "query": "mutation { actualizarStock(id: 1, cantidad: -2) { mensaje producto { id stock disponible } } }"
    }
    response = requests.post(API_URL, json=query)
    assert response.status_code == 200, "Fallo al disminuir el stock"
    print("Stock disminuido con éxito:", response.json())

def test_stock_cero_disponible():
    print_title("Test: Stock a 0 desactiva disponible")
    query = {
        "query": "mutation { actualizarStock(id: 1, cantidad: -100) { mensaje producto { stock disponible } } }"
    }
    response = requests.post(API_URL, json=query)
    assert response.status_code == 200, "Fallo al intentar dejar stock en 0"
    data = response.json()["data"]["actualizarStock"]["producto"]
    assert data["stock"] == 0, f"El stock no se redujo a 0, valor actual: {data['stock']}"
    assert data["disponible"] == False, "El producto no fue marcado como NO disponible"
    print("Producto marcado como no disponible correctamente.")

def test_producto_inexistente():
    print_title("Test: Producto inexistente")
    query = {
        "query": "mutation { actualizarStock(id: 999, cantidad: 1) { producto { id } } }"
    }
    response = requests.post(API_URL, json=query)
    assert response.status_code == 400, "La API no devolvió error al actualizar un producto inexistente"
    print(" Error recibido correctamente al intentar modificar producto inexistente")

if __name__ == "__main__":
    test_obtener_productos()
    test_actualizar_stock_positivo()
    test_actualizar_stock_negativo()
    test_stock_cero_disponible()
    test_producto_inexistente()
    print("\n Todos los tests se ejecutaron sin errores.")
