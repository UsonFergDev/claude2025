---
titulo: "Módulo 2 — Estructuras de datos"
curso: "Programación en R: de cero a análisis de datos"
nivel: "principiante"
duracion_h: 4
tags: [curso-r, modulo-2]
---

# Módulo 2 — Estructuras de datos

- **Duración estimada:** 1.5 h teoría + 2.5 h práctica
- **Objetivos de aprendizaje.** Al finalizar, la persona podrá:
  1. **Crear** vectores, factores, listas, matrices y data frames.
  2. **Explicar** la coerción de tipos y el reciclaje de vectores.
  3. **Aplicar** indexación por posición, nombre y condición lógica (`[ ]`, `[[ ]]`, `$`).
  4. **Clasificar** qué estructura conviene para un problema dado.

## Contenidos

1. Vectores atómicos: `c()`, `seq()`, `rep()`, `length()`.
2. Operaciones vectorizadas y reciclaje.
3. Coerción: jerarquía `logical < integer < numeric < character`.
4. Valores especiales: `NA`, `NULL`, `NaN`, `Inf`.
5. Factores: niveles y orden.
6. Matrices: `matrix()`, `dim()`.
7. Listas: estructuras heterogéneas.
8. Data frames: la tabla de datos; `str()`, `head()`, `summary()`, `nrow()`.
9. Indexación: `[ ]`, `[[ ]]`, `$` y filtros lógicos.

## Desarrollo

### Vectores y vectorización

```r
unidades <- c(12, 7, 20, 3, 15)
precios  <- c(4999, 7999, 899, 6499, 2499)
ingresos <- unidades * precios          # operación elemento a elemento
sum(ingresos)
mean(unidades)
length(unidades)
1:10 * 2                                # reciclaje de un escalar
```

### Coerción y NA

```r
c(1, "dos", TRUE)       # todo se vuelve character
c(1, TRUE, FALSE)       # 1 1 0 (logical -> numeric)
x <- c(4, NA, 10)
sum(x)                  # NA
sum(x, na.rm = TRUE)    # 14
is.na(x)                # FALSE TRUE FALSE
```

### Factores

```r
canal <- factor(c("En línea", "Departamental", "En línea", "Autoservicio"))
levels(canal)                   # orden alfabético por defecto
table(canal)
talla <- factor(c("M", "S", "L", "M"), levels = c("S", "M", "L"), ordered = TRUE)
talla < "L"
```

### Matrices y listas

```r
m <- matrix(1:6, nrow = 2)
dim(m)
m[2, 3]                         # fila 2, columna 3

tienda <- list(id = "T01", region = "Norte", ventas = c(120, 98, 143))
tienda$region
tienda[["ventas"]][2]           # 98
str(tienda)
```

### Data frames

```r
df <- data.frame(
  producto = c("Smartphone A", "Tablet", "Audífonos"),
  precio   = c(4999, 6499, 899),
  unidades = c(12, 4, 20)
)
str(df)
df$ingreso <- df$precio * df$unidades   # nueva columna
df[df$unidades > 10, ]                  # filas que cumplen condición
df[, c("producto", "ingreso")]          # columnas por nombre
nrow(df); ncol(df)
```

### Leer el conjunto de datos del curso (R base)

```r
ventas <- read.csv("datos/ventas.csv")
head(ventas)
summary(ventas$unidades)
```

## Actividades y ejercicios

1. Crea un vector con las temperaturas `c(22, 25, NA, 30, 28)` y calcula su promedio ignorando el `NA`.
2. Con `ventas`, ¿cuántas filas y columnas tiene? ¿Cuántos `NA` hay en `unidades`?
3. Convierte `ventas$producto` en factor y muestra cuántos registros hay por producto.
4. Extrae las filas de `ventas` del producto `"Tablet"` con más de 8 unidades.
5. Crea una lista `resumen` con el total de unidades y el producto más frecuente.

<details>
<summary>Soluciones</summary>

```r
# 1
temp <- c(22, 25, NA, 30, 28)
mean(temp, na.rm = TRUE)                       # 26.25

# 2
dim(ventas)
sum(is.na(ventas$unidades))                    # 40

# 3
ventas$producto <- factor(ventas$producto)
table(ventas$producto)

# 4
tablets <- ventas[ventas$producto == "Tablet" &
                  !is.na(ventas$unidades) &
                  ventas$unidades > 8, ]
head(tablets)

# 5
resumen <- list(
  total_unidades = sum(ventas$unidades, na.rm = TRUE),
  mas_frecuente  = names(which.max(table(ventas$producto)))
)
str(resumen)
```

</details>

## Evaluación (formativa)

- **Quiz:** ¿Qué devuelve `c(1, "a")`? ¿Cuál es la diferencia entre `lista["x"]` y `lista[["x"]]`? ¿Para qué sirve `levels=` en `factor()`?
- **Práctica calificada:** script que lea `ventas.csv`, cree la columna `ingreso` y muestre las 5 filas con mayor ingreso (pista: `order()`, con `decreasing = TRUE`).

## Referencias verificadas

- 📚 Grolemund, G. (2014). *Hands-On Programming with R*. O'Reilly Media. ISBN 978-1-4493-5901-0. https://rstudio-education.github.io/hopr/ [EN] [OA en línea] — cap. "R Objects" y "R Notation".
- 📚 Wickham, H. (2019). *Advanced R* (2.ª ed.). CRC Press. ISBN 978-0-8153-8457-1. https://adv-r.hadley.nz/ [EN] [OA en línea, CC BY-NC-SA 4.0] — cap. 3 "Vectors" y cap. 4 "Subsetting" (lectura de profundización).
- 🌐 R Core Team. *An Introduction to R* — secciones "Simple manipulations; numbers and vectors" y "Lists and data frames". https://cran.r-project.org/doc/manuals/r-release/R-intro.html [EN] [OA]
- ▶️ freeCodeCamp.org. *R Programming Tutorial – Learn the Basics of Statistical Computing* [Video]. YouTube. https://youtu.be/_V8eKsto3Ug [EN] — secciones "Data Formats", "Factors", "Entering Data", "Importing Data".

[[modulo-01-primeros-pasos|← Módulo 1]] · [[modulo-03-programacion|Módulo 3 →]]
