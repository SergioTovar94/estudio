# ¿Qué es la arquitectura limpia?

La arquitectura limpia es una filosofía de diseño de software presentada por Robert C. Martin en 2017 en un libro con el mismo nombre . Básicamente se refiere a la organización del código en componentes o módulos separados y cómo estos elementos se relacionan entre sí.

El objetivo principal de Clean Architecture es proporcionar una metodología para desarrollar código que funcione mejor, tenga pocas dependencias y sea fácil de entender y mantener, lo que reduce los costos y maximiza la productividad del programador.

En los últimos años, Clean Architecture se ha vuelto bastante popular y muchos equipos de desarrollo de software la están adoptando en todo el mundo. Una de las principales razones es que ayuda a diseñar aplicaciones con muy bajo acoplamiento y alta cohesión . De esa manera, las aplicaciones se vuelven más probables y flexibles para cambiar a medida que crece el proyecto.

## Cohesión

La cohesión mide qué tan relacionadas están entre sí las responsabilidades dentro de una clase. En otras palabras:

¿Las cosas que hace esta clase tienen sentido juntas?

Si una clase tiene alta cohesión, significa que:

Hace una sola cosa. Todas sus partes trabajan hacia el mismo propósito. No tiene funcionalidades “metidas con calzador”

```Python
class Factura:
    def calcular_total(self):
        pass

    def aplicar_descuento(self):
        pass

    def generar_pdf(self):
        pass
```

Todo tiene que ver con facturación. Eso es cohesión alta.

Ejemplo de baja cohesión

```Python
class Factura:
    def calcular_total(self):
        pass

    def enviar_correo(self):
        pass

    def conectar_base_datos(self):
        pass

    def convertir_moneda(self):
        pass
```

Aquí la clase está haciendo:

- lógica de negocio
- infraestructura
- comunicación
- conversión

Eso ya no es una sola responsabilidad. Es una mezcla. Baja cohesión.

## Acomplamiento

El acoplamiento mide qué tan dependiente es una clase de otras clases. ¿Cuánto necesita esta clase saber de las demás para funcionar?

```Pyhon
class Pedido:
    def procesar(self):
        db = MySQLDatabase()
        db.conectar()
```

Aquí Pedido depende directamente de una implementación concreta (MySQLDatabase). Si cambias la base de datos, tienes que modificar Pedido. Eso es alto acoplamiento.

Bajo acoplamiento

```Python
class Pedido:
    def __init__(self, base_datos):
        self.base_datos = base_datos
```

Aquí no le importa qué base de datos sea. Solo necesita algo que cumpla cierta interfaz. Eso es bajo acoplamiento.

## Principales características de una Arquitectura Limpia

La representación más común de Clean Architecture es un diagrama que consta de capas circulares concéntricas, que recuerdan mucho a The Onion Architecture . Las capas internas representan políticas abstractas de alto nivel, mientras que las capas externas son los detalles técnicos de implementación.

La arquitectura de software de una aplicación define dónde el sistema realiza su funcionalidad principal y cómo interactúa con cosas como la base de datos y la interfaz de usuario.

![alt text](image.png)

En el centro del círculo, tenemos el Dominio o las reglas comerciales. Las reglas comerciales son la razón por la que existe un sistema de software. Son la funcionalidad principal de una aplicación.

Idealmente, el código que representa las reglas de negocio debería ser el corazón del sistema, con preocupaciones menores conectadas a ellas. Las reglas comerciales deben ser el código más independiente e inmutable del sistema.

Cuanto más exterior vayas en el círculo, los elementos se vuelven menos críticos y más propensos a cambiar. En este sentido, la presentación y los datos son menos importantes ya que son implementaciones que eventualmente pueden ser reemplazadas.
