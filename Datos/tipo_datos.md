# Unicode

Es el estándar universal de codificación de caracteres predominante, diseñado para representar texto de casi cualquier idioma, símbolos e ideogramas en sistemas digitales. Asigna un valor único a cada carácter, siendo UTF-8 la forma más común de implementarlo. Reemplazó al limitado ASCII, que solo cubría 128 caracteres.

- Unicode (estándar moderno): Es el sistema estándar para la mayoría de los sistemas operativos y la web. Permite la representación de texto bidireccional y una amplia gama de alfabetos, asegurando compatibilidad internacional.
- UTF-8: Es la codificación más utilizada de Unicode, que es eficiente y compatible con el código ASCII original.
  ASCII (American Standard Code for Information Interchange): Estándar histórico de 7 bits diseñado para inglés, definiendo 128 valores numéricos para caracteres, números y símbolos de control. Aunque es limitado, sigue siendo la base de muchos sistemas.
- ASCII Extendido: Amplía el estándar a 8 bits (256 caracteres), permitiendo soporte para algunos caracteres especiales adicionales, utilizado comúnmente en los primeros sistemas informáticos.

Antes existían cosas como:

- ASCII
- ISO-8859-1
- Windows-1252

El problema era que cada sistema tenía su propio mapa de caracteres. Unicode vino a decir:

“Vamos a asignar un número único a cada carácter del mundo.”

Ese número se llama code point.
