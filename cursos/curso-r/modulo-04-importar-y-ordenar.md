---
titulo: "Módulo 4 — Importar y ordenar datos (tidy data)"
curso: "Programación en R: de cero a análisis de datos"
nivel: "intermedio"
duracion_h: 4
tags: [curso-r, modulo-4, tidyverse]
---

# Módulo 4 — Importar y ordenar datos (tidy data)

- **Duración estimada:** 1.5 h teoría + 2.5 h práctica
- **Objetivos de aprendizaje.** Al finalizar, la persona podrá:
  1. **Explicar** los tres principios de los datos ordenados (*tidy data*).
  2. **Importar** archivos CSV y Excel con `readr` y `readxl`, controlando tipos de columna.
  3. **Transformar** tablas entre formato ancho y largo con `pivot_longer()` / `pivot_wider()`.
  4. **Diferenciar** los problemas de calidad más comunes (tipos erróneos, `NA`, duplicados).

## Contenidos

1. El *tidyverse* y los *tibbles*.
2. Principios de datos ordenados: cada variable una columna, cada observación una fila, cada valor una celda.
3. `readr::read_csv()`, especificación de tipos con `col_types`, `problems()`.
4. `readxl::read_excel()`: hojas y rangos.
5. `tidyr::pivot_longer()` y `pivot_wider()`.
6. `separate_wider_delim()` y `unite()`.
7. Manejo de `NA`: `drop_na()`, `replace_na()`; duplicados con `distinct()`.
8. Exportar: `write_csv()`.

## Desarrollo

### Importar con readr

```r
library(tidyverse)

ventas <- read_csv("datos/ventas.csv", col_types = cols(
  fecha     = col_date(),
  tienda_id = col_character(),
  producto  = col_character(),
  precio    = col_double(),
  unidades  = col_integer()
))
ventas
glimpse(ventas)
tiendas <- read_csv("datos/tiendas.csv", show_col_types = FALSE)
```

### Excel

```r
library(readxl)
# excel_sheets("datos/archivo.xlsx")                 # lista las hojas
# read_excel("datos/archivo.xlsx", sheet = "Ventas", range = "A1:E500")
```

### De ancho a largo y de regreso

Muchas hojas de cálculo guardan un mes por columna: eso **no** es *tidy*, porque "mes" es una variable.

```r
reporte_ancho <- tribble(
  ~tienda, ~ene, ~feb, ~mar,
  "T01",    120,   98,  143,
  "T02",     87,  110,   95
)

reporte_largo <- reporte_ancho |>
  pivot_longer(cols = ene:mar, names_to = "mes", values_to = "unidades")
reporte_largo

reporte_largo |>
  pivot_wider(names_from = mes, values_from = unidades)
```

> `|>` es el *pipe* nativo de R (≥ 4.1): `x |> f(y)` equivale a `f(x, y)`. Léelo como "y luego".

### Separar y unir columnas

```r
codigos <- tibble(sku = c("CEL-001-NEGRO", "TAB-014-GRIS"))
codigos |>
  separate_wider_delim(sku, delim = "-", names = c("categoria", "numero", "color"))
```

### Valores faltantes y duplicados

```r
ventas |> summarise(faltantes = sum(is.na(unidades)))
ventas_sin_na <- ventas |> drop_na(unidades)
ventas |> mutate(unidades = replace_na(unidades, 0L)) |> head()
ventas |> distinct(tienda_id, fecha, producto) |> nrow()   # verifica llave única
```

## Actividades y ejercicios

1. Importa `ventas.csv` con `read_csv()` sin `col_types` y compara el tipo que asigna a `unidades` y `fecha` con la versión especificada.
2. Convierte `ventas` a formato ancho: una fila por `fecha` y `tienda_id`, una columna por producto con las unidades.
3. Regresa el resultado anterior a formato largo y comprueba que recuperas el mismo número de filas.
4. Cuenta los `NA` de `unidades` por producto.

<details>
<summary>Soluciones</summary>

```r
# 1
v2 <- read_csv("datos/ventas.csv", show_col_types = FALSE)
spec(v2)          # readr infiere fecha como date y unidades como double

# 2
ancho <- ventas |>
  select(fecha, tienda_id, producto, unidades) |>
  pivot_wider(names_from = producto, values_from = unidades)
ancho

# 3
largo <- ancho |>
  pivot_longer(-c(fecha, tienda_id), names_to = "producto", values_to = "unidades")
nrow(largo) == nrow(ventas)    # TRUE

# 4
ventas |>
  group_by(producto) |>
  summarise(n_na = sum(is.na(unidades)))
```

</details>

## Evaluación (formativa)

- **Quiz:** Da un ejemplo de tabla que viole cada principio de *tidy data*. ¿Qué función usarías para arreglarla?
- **Práctica:** Recibe un Excel "reporte mensual" con meses en columnas y entrégalo en formato largo como CSV con `write_csv()`.

## Referencias verificadas

- 📄 Wickham, H. (2014). Tidy data. *Journal of Statistical Software, 59*(10), 1–23. https://doi.org/10.18637/jss.v059.i10 [EN] [OA]
- 📄 Wickham, H., Averick, M., Bryan, J., Chang, W., McGowan, L. D., François, R., … Yutani, H. (2019). Welcome to the tidyverse. *Journal of Open Source Software, 4*(43), 1686. https://doi.org/10.21105/joss.01686 [EN] [OA, CC BY 4.0]
- 📚 Wickham, H., Çetinkaya-Rundel, M., & Grolemund, G. (2023). *R for Data Science* (2.ª ed.). O'Reilly Media. ISBN 978-1-4920-9740-2. Español: https://davidrsch.github.io/r4ds-es/ [ES] [OA] — caps. "Ordenar datos", "Importación de datos", "Hojas de cálculo".
- ▶️ Gomila Salas, J. G. (Frogames). *Curso completo de R para Data Science con Tidyverse – R for Data Science en Español* [Video]. YouTube. https://www.youtube.com/watch?v=9NJyhs5PlGQ [ES] *[nombre exacto del canal y fecha POR VERIFICAR]*

[[modulo-03-programacion|← Módulo 3]] · [[modulo-05-transformar-con-dplyr|Módulo 5 →]]
