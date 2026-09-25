---
titulo: "Módulo 5 — Transformar datos con dplyr"
curso: "Programación en R: de cero a análisis de datos"
nivel: "intermedio"
duracion_h: 5
tags: [curso-r, modulo-5, dplyr]
---

# Módulo 5 — Transformar datos con dplyr

- **Duración estimada:** 1.5 h teoría + 3.5 h práctica
- **Objetivos de aprendizaje.** Al finalizar, la persona podrá:
  1. **Aplicar** los verbos de `dplyr` (`filter`, `select`, `mutate`, `arrange`, `summarise`) encadenados con `|>`.
  2. **Calcular** indicadores agregados por grupo con `group_by()` / `.by`.
  3. **Combinar** tablas con uniones (`left_join`, `inner_join`, `anti_join`).
  4. **Usar** `lubridate` y `stringr` para trabajar con fechas y texto.
  5. **Analizar** el desempeño por canal, región y producto a partir de datos crudos.

## Contenidos

1. Los cinco verbos principales y el *pipe*.
2. `mutate()` con `if_else()` y `case_when()`.
3. `group_by()` + `summarise()`; `count()`; agrupación temporal con `.by`.
4. Funciones de ventana: `lag()`, `cumsum()`, `rank()`, `slice_max()`.
5. Uniones de tablas y llaves.
6. Fechas con `lubridate`: `year()`, `month()`, `floor_date()`.
7. Texto con `stringr`: `str_detect()`, `str_to_upper()`, `str_replace()`.

## Desarrollo

```r
library(tidyverse)
ventas  <- read_csv("datos/ventas.csv", show_col_types = FALSE)
tiendas <- read_csv("datos/tiendas.csv", show_col_types = FALSE)
```

### Los verbos básicos

```r
ventas |>
  filter(producto == "Tablet", unidades >= 8) |>
  select(fecha, tienda_id, unidades) |>
  arrange(desc(unidades))

ventas <- ventas |>
  mutate(ingreso = precio * unidades)
```

### Resúmenes por grupo

```r
ventas |>
  group_by(producto) |>
  summarise(
    unidades = sum(unidades, na.rm = TRUE),
    ingreso  = sum(ingreso,  na.rm = TRUE),
    ticket_promedio = ingreso / unidades
  ) |>
  arrange(desc(ingreso))

ventas |> count(producto)                         # conteo rápido
```

### Uniones

```r
ventas_det <- ventas |>
  left_join(tiendas, by = "tienda_id")

ventas_det |>
  summarise(ingreso = sum(ingreso, na.rm = TRUE), .by = c(canal, region)) |>
  arrange(canal, desc(ingreso))

# ¿Hay ventas de tiendas que no existen en el catálogo?
ventas |> anti_join(tiendas, by = "tienda_id") |> nrow()   # 0
```

### Fechas

```r
mensual <- ventas_det |>
  mutate(mes = floor_date(fecha, "month")) |>
  summarise(ingreso = sum(ingreso, na.rm = TRUE), .by = c(mes, canal)) |>
  arrange(canal, mes) |>
  group_by(canal) |>
  mutate(var_pct = (ingreso / lag(ingreso) - 1) * 100) |>
  ungroup()
mensual
```

### Texto

```r
ventas_det |>
  filter(str_detect(producto, "Smartphone")) |>
  mutate(producto = str_to_upper(producto)) |>
  distinct(producto)
```

## Actividades y ejercicios

1. ¿Cuál fue la **tienda** con mayor ingreso anual? Muestra el top 3 con su canal y región.
2. Calcula la **participación (%)** de cada canal en el ingreso total.
3. Para cada producto, encuentra la **semana** de mayores unidades vendidas (`slice_max()`).
4. Compara el ingreso promedio semanal de **noviembre–diciembre** vs. el resto del año por producto.
5. Reto: con `anti_join()`, verifica que cada combinación tienda–semana tenga los 5 productos.

<details>
<summary>Soluciones</summary>

```r
# 1
ventas_det |>
  summarise(ingreso = sum(ingreso, na.rm = TRUE), .by = c(tienda_id, canal, region)) |>
  slice_max(ingreso, n = 3)

# 2
ventas_det |>
  summarise(ingreso = sum(ingreso, na.rm = TRUE), .by = canal) |>
  mutate(participacion = ingreso / sum(ingreso) * 100)

# 3
ventas |>
  summarise(unidades = sum(unidades, na.rm = TRUE), .by = c(producto, fecha)) |>
  group_by(producto) |>
  slice_max(unidades, n = 1, with_ties = FALSE)

# 4
ventas |>
  mutate(temporada = if_else(month(fecha) %in% 11:12, "Nov-Dic", "Resto")) |>
  summarise(ingreso_sem = sum(ingreso, na.rm = TRUE), .by = c(producto, temporada, fecha)) |>
  summarise(promedio = mean(ingreso_sem), .by = c(producto, temporada)) |>
  pivot_wider(names_from = temporada, values_from = promedio) |>
  mutate(incremento_pct = (`Nov-Dic` / Resto - 1) * 100)

# 5
esperado <- expand_grid(
  tienda_id = unique(ventas$tienda_id),
  fecha     = unique(ventas$fecha),
  producto  = unique(ventas$producto)
)
esperado |> anti_join(ventas, by = c("tienda_id", "fecha", "producto")) |> nrow()  # 0
```

</details>

## Evaluación (sumativa parcial)

**Mini‑reporte de KPIs:** script que produzca una tabla con ingreso, unidades y ticket promedio por canal y región, más la variación mensual por canal. Se evalúa: resultados correctos (40 %), uso idiomático de `dplyr` (30 %), legibilidad (30 %).

## Referencias verificadas

- 📚 Wickham, H., Çetinkaya-Rundel, M., & Grolemund, G. (2023). *R for Data Science* (2.ª ed.). O'Reilly Media. ISBN 978-1-4920-9740-2. Español: https://davidrsch.github.io/r4ds-es/ [ES] [OA] — caps. "Transformación de datos", "Uniones", "Fechas y horas", "Cadenas".
- 🌐 R para Ciencia de Datos (traducción de la 1.ª ed. por la comunidad latinoamericana de R). https://es.r4ds.hadley.nz/ [ES] [OA] — alternativa en español.
- 📄 Wickham, H., et al. (2019). Welcome to the tidyverse. *Journal of Open Source Software, 4*(43), 1686. https://doi.org/10.21105/joss.01686 [EN] [OA]
- ▶️ Gomila Salas, J. G. (Frogames). *Curso completo de R para Data Science con Tidyverse* [Video]. YouTube. https://www.youtube.com/watch?v=9NJyhs5PlGQ [ES] *[canal y fecha POR VERIFICAR]*

[[modulo-04-importar-y-ordenar|← Módulo 4]] · [[modulo-06-visualizacion-ggplot2|Módulo 6 →]]
