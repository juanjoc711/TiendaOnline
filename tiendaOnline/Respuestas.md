## ¿Qué ventajas ofrece GraphQL sobre REST en este contexto?

En este caso concreto, usar GraphQL tiene sentido porque el frontend necesita mostrar productos según el stock y el estado de disponibilidad. Con GraphQL, puedo pedir exactamente los campos que necesito (por ejemplo, solo nombre, stock y disponible) sin tener que traer todo el objeto como pasaría con un endpoint REST genérico. Eso hace que las respuestas sean más livianas y el frontend tenga más control.

Otra ventaja importante es que toda la lógica de consulta y modificación se maneja desde un único endpoint (/graphql). No tengo que crear rutas distintas para cada operación como con REST. Eso simplifica mucho tanto el backend como el código del frontend, sobre todo cuando tenés componentes que reaccionan a cambios en tiempo real del stock, como en este proyecto.

---

## ¿Cómo se definen los tipos y resolvers en una API con GraphQL?

En este proyecto usé Graphene, que es una librería de Python para armar APIs GraphQL. Para definir un tipo como "Producto", simplemente creé una clase Producto con los campos que necesitaba (id, nombre, precio, stock, disponible). Eso le dice a GraphQL qué estructura tienen los datos.

Después, para que la API sepa cómo responder cuando alguien pide productos, tuve que crear un resolver. Es básicamente una función que devuelve los datos correctos cuando alguien hace una consulta. En este caso, usé una lista en memoria que se carga al iniciar la app, y el resolver devuelve esa lista. También definí una mutación (actualizarStock) con su propia lógica, que actualiza el stock y el estado de disponibilidad de un producto.

En resumen, los tipos son como moldes, y los resolvers son las funciones que rellenan esos moldes con los datos correctos.

---

## ¿Por qué es importante que el backend también actualice disponible y no depender solo del frontend?

Porque si esa lógica estuviera solo en el frontend, habría muchas posibilidades de error. Por ejemplo, si otro frontend distinto se conecta a la API, o si se hace una petición directamente con herramientas como Postman, no se garantizaría que disponible se actualice como debería.

Lo correcto es que el backend sea el que se encargue de verificar si el stock está en 0 y, en ese caso, cambiar disponible a false. Lo mismo si el stock pasa de 0 a un número mayor: ahí se vuelve a poner como disponible. De esa forma, el backend mantiene siempre el control de la lógica y los datos son consistentes sin importar desde dónde se use la API.

---

## ¿Cómo garantizás que la lógica de actualización de stock y disponibilidad sea coherente?

Toda la lógica está centralizada en la mutación actualizarStock. Esa mutación no solo modifica el stock, sino que también se fija automáticamente si tiene que cambiar el campo disponible. Si el stock llega a 0, lo pone en false. Si sube desde 0, lo vuelve a poner en true.

Además, tengo una condición que evita que el stock baje de 0, así que nunca se generan valores negativos. Al estar todo eso en el backend, cada vez que alguien actualiza el stock desde cualquier lugar (frontend, Postman, etc.), los valores se ajustan de forma correcta sin necesidad de que el frontend haga cálculos o validaciones extra.

Esto hace que los datos estén siempre en un estado válido y coherente, sin depender del contexto desde donde se usen.