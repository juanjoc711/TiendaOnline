import requests

def test_query_productos():
    query = '''
    query {
        productos {
            id
            nombre
            precio
            stock
            disponible
        }
    }
    '''
    response = requests.post("http://localhost:5000/graphql", json={"query": query})
    print("Consulta productos:", response.json())

def test_mutacion_actualizar_stock():
    mutation = '''
    mutation {
        actualizarStock(id: 2, cantidad: 5) {
            producto {
                id
                nombre
                stock
                disponible
            }
        }
    }
    '''
    response = requests.post("http://localhost:5000/graphql", json={"query": mutation})
    print("Mutación actualizar stock:", response.json())

if __name__ == "__main__":
    test_query_productos()
    test_mutacion_actualizar_stock()
