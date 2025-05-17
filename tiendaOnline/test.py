import requests

URL = "http://localhost:5000/graphql"

def ejecutar_query(query):
    response = requests.post(URL, json={"query": query})
    print(response.json())
    print("-" * 40)

def test_obtener_productos():
    query = """
    query {
        productos {
            id
            nombre
            precio
            stock
            disponible
        }
    }
    """
    ejecutar_query(query)

def test_aumentar_stock():
    query = """
    mutation {
        actualizarStock(id: 2, cantidad: 5) {
            producto {
                id
                nombre
                stock
                disponible
            }
            mensaje
        }
    }
    """
    ejecutar_query(query)

def test_disminuir_stock():
    query = """
    mutation {
        actualizarStock(id: 1, cantidad: -3) {
            producto {
                id
                nombre
                stock
                disponible
            }
            mensaje
        }
    }
    """
    ejecutar_query(query)

def test_dejar_stock_a_cero():
    query = """
    mutation {
        actualizarStock(id: 1, cantidad: -100) {
            producto {
                id
                nombre
                stock
                disponible
            }
            mensaje
        }
    }
    """
    ejecutar_query(query)

def test_producto_no_existente():
    query = """
    mutation {
        actualizarStock(id: 999, cantidad: 1) {
            producto {
                id
                nombre
                stock
                disponible
            }
            mensaje
        }
    }
    """
    ejecutar_query(query)

if __name__ == "__main__":
    test_obtener_productos()
    test_aumentar_stock()
    test_disminuir_stock()
    test_dejar_stock_a_cero()
    test_producto_no_existente()
