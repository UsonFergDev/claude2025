---
titulo: "Módulo 6 — Visualización con ggplot2"
curso: "Programación en R: de cero a análisis de datos"
nivel: "intermedio"
duracion_h: 4
tags: [curso-r, modulo-6, ggplot2]
---

# Módulo 6 — Visualización con ggplot2

- **Duración estimada:** 1.5 h teoría + 2.5 h práctica
- **Objetivos de aprendizaje.** Al finalizar, la persona podrá:
  1. **Explicar** la gramática de gráficos: datos, estéticas (`aes`), geometrías, escalas, facetas y temas.
  2. **Construir** gráficos de barras, líneas, dispersión, histogramas y cajas.
  3. **Seleccionar** el tipo de gráfico adecuado según la pregunta (comparar, tendencia, distribución, relación).
  4. **Producir** gráficos listos para reporte (títulos, etiquetas, formato de ejes) y exportarlos con `ggsave()`.

## Contenidos

1. La gramática de gráficos por capas.
2. `aes()`: `x`, `y`, `color`, `fill`, `size`; estéticas fijas vs. mapeadas.
3. Geometrías: `geom_col`, `geom_line`, `geom_point`, `geom_histogram`, `geom_boxplot`.
4. Facetas: `facet_wrap()`.
5. Escalas y formato: `scales::label_dollar()`, `label_percent()`.
6. Etiquetas y temas: `labs()`, `theme_minimal()`.
7. Exportar: `ggsave()`.

## Desarrollo

```r
library(tidyverse)
ventas  <- read_csv("datos/ventas.csv", show_col_types = FALSE) |>
  mutate(ingreso = precio * unidades)
tiendas <- read_csv("datos/tiendas.csv", show_col_types = FALSE)
ventas_det <- left_join(ventas, tiendas, by = "tienda_id")
```

### Comparar categorías: barras

```r
por_producto <- ventas |>
  summarise(ingreso = sum(ingreso, na.rm = TRUE), .by = producto)

ggplot(por_producto, aes(x = ingreso, y = fct_reorder(producto, ingreso))) +
  geom_col(fill = "steelblue") +
  scale_x_continuous(labels = scales::label_dollar(scale = 1e-6, suffix = " M")) +
  labs(title = "Ingreso anual por producto", x = "Ingreso (MXN)", y = NULL) +
  theme_minimal()
```

> Barras **horizontales** y **ordenadas** facilitan leer nombres largos y comparar magnitudes.

### Tendencia: líneas

```r
semanal <- ventas_det |>
  summarise(ingreso = sum(ingreso, na.rm = TRUE), .by = c(fecha, canal))

g_tendencia <- ggplot(semanal, aes(fecha, ingreso, color = canal)) +
  geom_line(linewidth = 0.8) +
  scale_y_continuous(labels = scales::label_dollar()) +
  labs(title = "Ingreso semanal por canal, 2025", x = NULL, y = "Ingreso", color = "Canal") +
  theme_minimal()
g_tendencia
```

### Distribución: histograma y cajas

```r
ggplot(ventas, aes(unidades)) +
  geom_histogram(binwidth = 2, fill = "grey40", color = "white") +
  facet_wrap(~ producto, scales = "free_y") +
  labs(title = "Distribución de unidades semanales por producto")

ggplot(ventas_det, aes(region, unidades, fill = region)) +
  geom_boxplot(show.legend = FALSE) +
  labs(title = "Unidades por región", x = NULL)
```

> Los `NA` de `unidades` se descartan con una advertencia ("Removed rows…"). Es informativa, no un error.

### Relación: dispersión

```r
por_tienda <- ventas_det |>
  summarise(unidades = sum(unidades, na.rm = TRUE),
            ingreso  = sum(ingreso,  na.rm = TRUE), .by = c(tienda_id, canal))

ggplot(por_tienda, aes(unidades, ingreso, color = canal)) +
  geom_point(size = 3) +
  geom_smooth(method = "lm", se = FALSE, color = "black", linewidth = 0.5) +
  labs(title = "Unidades vs. ingreso por tienda")
```

### Exportar

```r
ggsave("tendencia_canal.png", g_tendencia, width = 8, height = 4.5, dpi = 300)
```

## Actividades y ejercicios

1. Gráfico de barras apiladas al 100 % de la participación de cada producto dentro de cada canal (`position = "fill"`).
2. Líneas de unidades mensuales por producto con `facet_wrap()`.
3. Mejora un gráfico "por defecto" aplicando: orden, título que afirme la conclusión, ejes formateados y sin leyenda redundante.
4. Exporta tu mejor gráfico a PNG de 300 dpi.

<details>
<summary>Soluciones</summary>

```r
# 1
ventas_det |>
  summarise(ingreso = sum(ingreso, na.rm = TRUE), .by = c(canal, producto)) |>
  ggplot(aes(canal, ingreso, fill = producto)) +
  geom_col(position = "fill") +
  scale_y_continuous(labels = scales::label_percent()) +
  labs(title = "Mezcla de productos por canal", x = NULL, y = "Participación", fill = NULL)

# 2
ventas |>
  mutate(mes = floor_date(fecha, "month")) |>
  summarise(unidades = sum(unidades, na.rm = TRUE), .by = c(mes, producto)) |>
  ggplot(aes(mes, unidades)) +
  geom_line() +
  facet_wrap(~ producto, scales = "free_y") +
  labs(title = "Las ventas de todos los productos suben en noviembre y diciembre",
       x = NULL, y = "Unidades")
```

</details>

## Evaluación (formativa)

Galería de pares: cada persona presenta un gráfico y recibe retroalimentación con la lista de verificación: ¿responde una pregunta clara?, ¿el tipo de gráfico es adecuado?, ¿ejes y unidades legibles?, ¿el título dice la conclusión?, ¿colores con propósito?

## Referencias verificadas

- 📚 Wickham, H., Çetinkaya-Rundel, M., & Grolemund, G. (2023). *R for Data Science* (2.ª ed.). O'Reilly Media. ISBN 978-1-4920-9740-2. Español: https://davidrsch.github.io/r4ds-es/ [ES] [OA] — caps. "Visualización de datos", "Capas", "Análisis exploratorio", "Comunicación".
- 🌐 Wickham, H., Navarro, D., & Pedersen, T. L. *ggplot2: Elegant Graphics for Data Analysis* (3.ª ed., versión en línea). https://ggplot2-book.org/ [EN] [OA en línea] *[datos de edición impresa POR VERIFICAR]*
- ▶️ freeCodeCamp.org. *R Programming Tutorial – Learn the Basics of Statistical Computing* [Video]. YouTube. https://youtu.be/_V8eKsto3Ug [EN] — secciones de gráficos (`plot()`, barras, histogramas, dispersión) en R base, útil para contrastar con ggplot2.

[[modulo-05-transformar-con-dplyr|← Módulo 5]] · [[modulo-07-estadistica-y-modelos|Módulo 7 →]]
