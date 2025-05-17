import graphene
from data import productos

class Producto(graphene.ObjectType):
    id = graphene.Int()
    nombre = graphene.String()
    precio = graphene.Float()
    stock = graphene.Int()
    disponible = graphene.Boolean()

class Query(graphene.ObjectType):
    productos = graphene.List(Producto)

    def resolve_productos(root, info):
        return productos

class ActualizarStock(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        cantidad = graphene.Int(required=True)

    producto = graphene.Field(lambda: Producto)
    mensaje = graphene.String()

    def mutate(root, info, id, cantidad):
        producto = next((p for p in productos if p["id"] == id), None)
        if not producto:
            raise Exception("Producto no encontrado")

        producto["stock"] += cantidad
        if producto["stock"] <= 0:
            producto["stock"] = 0
            producto["disponible"] = False
            mensaje = "¡Aviso! El producto se ha quedado sin stock."
        else:
            producto["disponible"] = True
            mensaje = "Stock actualizado correctamente."

        return ActualizarStock(producto=producto, mensaje=mensaje)

class Mutation(graphene.ObjectType):
    actualizar_stock = ActualizarStock.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
