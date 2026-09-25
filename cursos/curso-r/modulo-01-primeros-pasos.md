---
titulo: "Módulo 1 — Primeros pasos con R y RStudio"
curso: "Programación en R: de cero a análisis de datos"
nivel: "principiante"
duracion_h: 4
tags: [curso-r, modulo-1]
---

# Módulo 1 — Primeros pasos con R y RStudio

- **Duración estimada:** 1.5 h teoría + 2.5 h práctica
- **Objetivos de aprendizaje.** Al finalizar, la persona podrá:
  1. **Identificar** los paneles de RStudio (consola, editor, entorno, archivos/gráficos/ayuda).
  2. **Ejecutar** instrucciones en la consola y desde un script `.R`.
  3. **Crear** objetos con `<-` y **reconocer** sus tipos básicos (`numeric`, `integer`, `character`, `logical`).
  4. **Usar** la ayuda (`?`, `help()`, `example()`) e **instalar** / **cargar** paquetes.

## Contenidos

1. Qué es R y qué es RStudio (el lenguaje vs. el entorno de desarrollo).
2. Instalación: R desde CRAN y RStudio Desktop (Posit).
3. Proyectos de RStudio (`.Rproj`) y el directorio de trabajo.
4. La consola como calculadora; operadores aritméticos y de comparación.
5. Objetos y asignación; reglas de nombres (`snake_case`).
6. Tipos de datos atómicos y `class()`, `typeof()`.
7. Funciones: argumentos por posición y por nombre.
8. Paquetes: `install.packages()` vs. `library()`.
9. Comentarios con `#` y buenas prácticas de scripts.

## Desarrollo

### R como calculadora

```r
2 + 3 * 4        # precedencia: 14
(2 + 3) * 4      # 20
10 / 3           # 3.333333
10 %/% 3         # división entera: 3
10 %% 3          # residuo (módulo): 1
2^10             # potencia: 1024
sqrt(144)        # 12
```

### Objetos y asignación

En R se asigna con `<-` (atajo en RStudio: `Alt` + `-`). El nombre va a la izquierda.

```r
precio   <- 4999
unidades <- 12
ingreso  <- precio * unidades
ingreso            # 59988
```

### Tipos básicos

```r
class(3.14)        # "numeric"
class(5L)          # "integer" (la L fuerza entero)
class("Norte")     # "character"
class(TRUE)        # "logical"
is.numeric(precio) # TRUE
as.numeric("42")   # convierte texto a número: 42
```

### Funciones y argumentos

```r
round(3.14159, digits = 2)   # por nombre: 3.14
round(3.14159, 2)            # por posición: 3.14
seq(from = 1, to = 10, by = 3)
```

### Ayuda

```r
?mean              # abre la ayuda de mean()
help("seq")
example(mean)      # ejecuta los ejemplos de la ayuda
```

### Paquetes

Un paquete se **instala una sola vez** por computadora y se **carga en cada sesión**:

```r
# install.packages("tidyverse")   # una vez (descomenta para instalar)
library(tidyverse)                # en cada sesión
```

> **Buena práctica:** trabaja siempre dentro de un **Proyecto de RStudio** (`File → New Project`). Así las rutas son relativas (`"datos/ventas.csv"`) y evitas `setwd()` con rutas absolutas que solo funcionan en tu computadora.

## Actividades y ejercicios

1. Crea un proyecto de RStudio llamado `curso-r` y un script `modulo-01.R`.
2. Calcula el ingreso de vender 35 audífonos de $899 con 10 % de descuento.
3. Guarda tu nombre en un objeto `nombre` y verifica su clase.
4. ¿Qué devuelve `class(5 > 3)`? ¿Y `as.numeric(TRUE)`?
5. Usa la ayuda para averiguar qué hace el argumento `na.rm` de `mean()`.

<details>
<summary>Soluciones</summary>

```r
# 2
ingreso_desc <- 35 * 899 * (1 - 0.10)
ingreso_desc                  # 28318.5

# 3
nombre <- "Ana"
class(nombre)                 # "character"

# 4
class(5 > 3)                  # "logical"
as.numeric(TRUE)              # 1

# 5: na.rm = TRUE elimina los NA antes de calcular
mean(c(10, NA, 20), na.rm = TRUE)   # 15
```

</details>

## Evaluación (formativa)

Quiz de 5 preguntas:

1. ¿Cuál es la diferencia entre R y RStudio?
2. ¿Qué operador asigna valores a un objeto en el estilo recomendado?
3. ¿Qué devuelve `10 %% 4`?
4. ¿Por qué `install.packages()` no se escribe en cada script?
5. Escribe una línea que calcule la raíz cuadrada de 2 redondeada a 3 decimales.

*Respuestas:* 1) R es el lenguaje/intérprete; RStudio es el IDE. 2) `<-`. 3) `2`. 4) Porque solo se instala una vez; en el script basta `library()`. 5) `round(sqrt(2), 3)`.

## Referencias verificadas

- 🌐 R Core Team. *An Introduction to R*. CRAN. https://cran.r-project.org/doc/manuals/r-release/R-intro.html [EN] [OA]
- 📚 Grolemund, G. (2014). *Hands-On Programming with R*. O'Reilly Media. ISBN 978-1-4493-5901-0. Versión en línea: https://rstudio-education.github.io/hopr/ [EN] [OA en línea] — caps. 1–2.
- 📚 Wickham, H., Çetinkaya-Rundel, M., & Grolemund, G. (2023). *R for Data Science* (2.ª ed.). O'Reilly Media. ISBN 978-1-4920-9740-2. Traducción al español: https://davidrsch.github.io/r4ds-es/ [ES] [OA] — cap. "Flujo de trabajo: conceptos básicos".
- ▶️ freeCodeCamp.org. *R Programming Tutorial – Learn the Basics of Statistical Computing* [Video] (instructor: Barton Poulson). YouTube. https://youtu.be/_V8eKsto3Ug [EN] — secciones "Installing R", "RStudio", "Packages". *[fecha de publicación POR VERIFICAR]*

[[README|← Índice]] · [[modulo-02-estructuras-de-datos|Módulo 2 →]]
