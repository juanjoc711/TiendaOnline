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

    def mutate(root, info, id, cantidad):

        for p in productos:

            if p["id"] == id:
                p["stock"] += cantidad
                if p["stock"] <= 0:
                    p["stock"] = 0
                    p["disponible"] = False
                else:
                    p["disponible"] = True
                return ActualizarStock(producto=p)
            
        raise Exception("Producto no encontrado")

class Mutation(graphene.ObjectType):
    actualizar_stock = ActualizarStock.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
