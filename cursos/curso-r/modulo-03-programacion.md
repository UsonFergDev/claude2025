---
titulo: "Módulo 3 — Programación: control de flujo y funciones"
curso: "Programación en R: de cero a análisis de datos"
nivel: "principiante-intermedio"
duracion_h: 4
tags: [curso-r, modulo-3]
---

# Módulo 3 — Programación: control de flujo y funciones

- **Duración estimada:** 1.5 h teoría + 2.5 h práctica
- **Objetivos de aprendizaje.** Al finalizar, la persona podrá:
  1. **Implementar** decisiones con `if`/`else`, `ifelse()` y `dplyr::case_when()`.
  2. **Ejecutar** iteraciones con `for` y `while`.
  3. **Escribir** funciones propias con argumentos, valores por defecto y validaciones.
  4. **Comparar** un bucle con la alternativa vectorizada o funcional (`sapply()`, `purrr::map()`).

## Contenidos

1. Operadores lógicos: `&`, `|`, `!`, `&&`, `||`, `%in%`.
2. `if`, `else if`, `else`; `ifelse()` vectorizado.
3. Bucles `for` y `while`; `break` y `next`.
4. Anatomía de una función: nombre, argumentos, cuerpo, valor de retorno.
5. Valores por defecto y validación con `stop()`.
6. Alcance (scope) de variables.
7. Vectorización y familia `apply` (`sapply`, `lapply`) vs. `purrr::map()`.

## Desarrollo

### Condicionales

```r
unidades <- 25
if (unidades >= 20) {
  "Alta rotación"
} else if (unidades >= 10) {
  "Rotación media"
} else {
  "Baja rotación"
}

u <- c(3, 12, 25)
ifelse(u >= 10, "Suficiente", "Reabastecer")   # vectorizado
"Tablet" %in% c("Tablet", "Reloj")             # TRUE
```

### Bucles

```r
productos <- c("Smartphone A", "Tablet", "Reloj")
for (p in productos) {
  print(paste("Revisando inventario de", p))
}

stock <- 50
semanas <- 0
while (stock > 0) {
  stock <- stock - 12
  semanas <- semanas + 1
}
semanas        # semanas hasta agotar: 5
```

### Funciones

```r
ingreso <- function(precio, unidades, descuento = 0) {
  if (descuento < 0 || descuento >= 1) {
    stop("`descuento` debe estar en [0, 1).")
  }
  precio * unidades * (1 - descuento)
}

ingreso(4999, 10)
ingreso(4999, 10, descuento = 0.15)
ingreso(c(899, 2499), c(20, 8))     # funciona con vectores
```

### Vectorizar en lugar de iterar

```r
x <- 1:5
# Con bucle
cuadrados <- numeric(length(x))
for (i in seq_along(x)) cuadrados[i] <- x[i]^2
cuadrados
# Vectorizado (preferido)
x^2
# Funcional
sapply(x, function(v) v^2)
library(purrr)
map_dbl(x, \(v) v^2)               # \(v) es la sintaxis corta de function(v), R >= 4.1
```

## Actividades y ejercicios

1. Escribe `clasificar_rotacion(u)` que devuelva `"Alta"`, `"Media"` o `"Baja"` para un **vector** de unidades (umbrales 20 y 10).
2. Escribe `margen(precio, costo)` que devuelva el margen porcentual y lance error si `costo > precio`.
3. Con un bucle `for`, imprime el total de unidades por producto en `ventas`. Luego obtén lo mismo con `tapply()`.
4. Simula lanzar un dado 1 000 veces con `sample()` y calcula la proporción de seises.

<details>
<summary>Soluciones</summary>

```r
# 1 (dplyr::case_when es vectorizado y legible)
clasificar_rotacion <- function(u) {
  dplyr::case_when(
    u >= 20 ~ "Alta",
    u >= 10 ~ "Media",
    TRUE    ~ "Baja"
  )
}
clasificar_rotacion(c(3, 12, 25))

# 2
margen <- function(precio, costo) {
  if (any(costo > precio)) stop("El costo no puede ser mayor que el precio.")
  (precio - costo) / precio * 100
}
margen(100, 60)                   # 40

# 3
ventas <- read.csv("datos/ventas.csv")
for (p in unique(ventas$producto)) {
  total <- sum(ventas$unidades[ventas$producto == p], na.rm = TRUE)
  cat(p, ":", total, "\n")
}
tapply(ventas$unidades, ventas$producto, sum, na.rm = TRUE)

# 4
set.seed(1)
dado <- sample(1:6, 1000, replace = TRUE)
mean(dado == 6)
```

</details>

## Evaluación (sumativa parcial)

Entrega un script `funciones_ventas.R` con 3 funciones documentadas (comentario de propósito, argumentos y retorno) y al menos una validación con `stop()`. Rúbrica:

| Criterio | 3 — Logrado | 2 — En proceso | 1 — Inicial |
|---|---|---|---|
| Correctitud | Las 3 funciones dan el resultado esperado | 2 funciones correctas | ≤ 1 correcta |
| Vectorización | Aceptan vectores sin bucles innecesarios | Parcial | Solo escalares |
| Validación | Mensajes de error claros | Validación incompleta | Sin validación |
| Estilo | Nombres claros, comentarios útiles | Aceptable | Difícil de leer |

## Referencias verificadas

- 📚 Wickham, H., Çetinkaya-Rundel, M., & Grolemund, G. (2023). *R for Data Science* (2.ª ed.). O'Reilly Media. ISBN 978-1-4920-9740-2. Español: https://davidrsch.github.io/r4ds-es/ [ES] [OA] — caps. "Funciones" e "Iteración".
- 📚 Grolemund, G. (2014). *Hands-On Programming with R*. O'Reilly Media. ISBN 978-1-4493-5901-0. https://rstudio-education.github.io/hopr/ [EN] [OA en línea] — proyecto "Slot machine" (if/else, bucles, funciones).
- 📚 Wickham, H. (2019). *Advanced R* (2.ª ed.). CRC Press. ISBN 978-0-8153-8457-1. https://adv-r.hadley.nz/ [EN] [OA en línea] — cap. 5 "Control flow" y cap. 6 "Functions".

[[modulo-02-estructuras-de-datos|← Módulo 2]] · [[modulo-04-importar-y-ordenar|Módulo 4 →]]
