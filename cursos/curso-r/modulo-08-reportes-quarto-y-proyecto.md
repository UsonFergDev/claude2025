---
titulo: "Módulo 8 — Reportes reproducibles con Quarto y proyecto integrador"
curso: "Programación en R: de cero a análisis de datos"
nivel: "intermedio-avanzado"
duracion_h: 5
tags: [curso-r, modulo-8, quarto, capstone]
---

# Módulo 8 — Reportes reproducibles con Quarto y proyecto integrador

- **Duración estimada:** 1 h teoría + 4 h proyecto
- **Objetivos de aprendizaje.** Al finalizar, la persona podrá:
  1. **Crear** un documento Quarto (`.qmd`) que combine texto, código R y resultados.
  2. **Configurar** opciones de *chunks* (`echo`, `warning`, `fig-cap`) y formatos de salida (HTML, Word, PDF).
  3. **Organizar** un proyecto reproducible (estructura de carpetas, rutas relativas, `renv`).
  4. **Diseñar** y **producir** un análisis completo de principio a fin (proyecto integrador).

## Contenidos

1. Por qué la reproducibilidad: el código *es* la documentación del análisis.
2. Anatomía de un `.qmd`: encabezado YAML, Markdown y *chunks* de código.
3. Opciones de *chunk* con `#|`.
4. Tablas con `knitr::kable()`; gráficos con leyenda.
5. Renderizar: botón **Render** en RStudio o `quarto render` en terminal.
6. Estructura de proyecto y control de dependencias con `renv`.
7. Guía de estilo del tidyverse; control de versiones con Git (introducción).

## Desarrollo

### Un documento Quarto mínimo

Guarda esto como `reporte.qmd` dentro del proyecto y presiona **Render**:

````markdown
---
title: "Reporte de ventas 2025"
author: "Tu nombre"
format:
  html:
    toc: true
execute:
  warning: false
---

## Resumen

```{r}
#| label: datos
#| echo: false
library(tidyverse)
ventas <- read_csv("datos/ventas.csv", show_col_types = FALSE) |>
  mutate(ingreso = precio * unidades)
total <- sum(ventas$ingreso, na.rm = TRUE)
```

El ingreso total del año fue de **`r scales::dollar(total)`**.

```{r}
#| label: fig-producto
#| fig-cap: "Ingreso anual por producto"
ventas |>
  summarise(ingreso = sum(ingreso, na.rm = TRUE), .by = producto) |>
  ggplot(aes(ingreso, fct_reorder(producto, ingreso))) +
  geom_col() +
  labs(x = "Ingreso", y = NULL)
```
````

- `` `r expresion` `` inserta resultados **dentro del texto**: si cambian los datos, el número se actualiza solo.
- Cambia `format: html` por `docx` o `pdf` (este último requiere TinyTeX: `quarto install tinytex`).

### Proyecto reproducible

```
mi-analisis/
├── mi-analisis.Rproj
├── datos/          # datos crudos: nunca se editan a mano
├── R/              # funciones reutilizables
├── reporte.qmd
└── salidas/        # gráficos y tablas generadas
```

```r
# Registrar versiones de paquetes del proyecto (una vez, en la consola):
# install.packages("renv"); renv::init()
# Después de instalar o actualizar paquetes:
# renv::snapshot()
```

## Proyecto integrador (capstone)

**Caso:** Eres analista de una cadena de electrónica. Dirección pide un **reporte de desempeño 2025** con recomendaciones para la temporada alta de 2026.

**Entregables:**

1. Proyecto de RStudio con la estructura anterior.
2. `reporte.qmd` renderizado a HTML que incluya:
   - Limpieza documentada (faltantes, tipos, verificación de llaves).
   - Tabla de KPIs por canal y región (ingreso, unidades, ticket promedio, participación).
   - Al menos 3 gráficos con títulos que afirmen la conclusión.
   - Una prueba estadística o modelo con interpretación.
   - Al menos una función propia en `R/` usada en el reporte.
   - Conclusiones y 3 recomendaciones accionables.
3. Presentación oral de 5 minutos.

### Rúbrica global del proyecto

| Criterio (peso) | 4 — Excelente | 3 — Bueno | 2 — Suficiente | 1 — Insuficiente |
|---|---|---|---|---|
| Reproducibilidad (20 %) | Renderiza sin errores en otra computadora; rutas relativas; `renv` | Renderiza con ajustes menores | Requiere varios ajustes | No renderiza |
| Manejo de datos (20 %) | Limpieza completa y justificada; verificación de llaves | Limpieza correcta, poco documentada | Limpieza parcial | Datos sin revisar |
| Transformación y KPIs (20 %) | KPIs correctos, código `dplyr` idiomático | Correctos con código redundante | Errores menores | Errores graves |
| Visualización (15 %) | Gráficos adecuados, claros y con mensaje | Adecuados, mejorables | Tipo de gráfico poco apropiado | Ilegibles |
| Estadística (15 %) | Método pertinente, supuestos revisados, interpretación correcta | Pertinente, interpretación parcial | Método dudoso | Ausente o incorrecto |
| Comunicación (10 %) | Conclusiones y recomendaciones claras y accionables | Claras pero generales | Confusas | Ausentes |

## Referencias verificadas

- 🌐 Posit / Quarto. *Tutorial: Computations* (RStudio). https://quarto.org/docs/get-started/computations/rstudio [EN] [gratuito]
- 🌐 Posit / Quarto. *Using R*. https://quarto.org/docs/computations/r.html [EN] [gratuito]
- 🌐 Posit / Quarto. *Tutorial: Hello, Quarto*. https://quarto.org/docs/get-started/hello/rstudio.html [EN] [gratuito]
- 📚 Wickham, H., Çetinkaya-Rundel, M., & Grolemund, G. (2023). *R for Data Science* (2.ª ed.). O'Reilly Media. ISBN 978-1-4920-9740-2. Español: https://davidrsch.github.io/r4ds-es/ [ES] [OA] — caps. "Quarto" y "Formatos de Quarto".
- 📄 Wickham, H. (2014). Tidy data. *Journal of Statistical Software, 59*(10), 1–23. https://doi.org/10.18637/jss.v059.i10 [EN] [OA]

[[modulo-07-estadistica-y-modelos|← Módulo 7]] · [[README|Índice]]
