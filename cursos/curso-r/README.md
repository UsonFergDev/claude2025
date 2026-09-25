---
titulo: "Programación en R: de cero a análisis de datos"
nivel: "principiante → intermedio"
duracion_h: 34
modulos: 8
modalidad: "autoformación o híbrida"
tags: [curso-r, indice]
---

# Curso: Programación en R — de cero a análisis de datos

**Perfil:** capacitación en datos/analítica · **Nivel:** principiante → intermedio · **Duración:** 8 módulos, ~34 h · **Modalidad:** autoformación o híbrida (sesiones de 2 h + práctica) · **Idioma:** español

## ¿Para quién es?

Personas sin experiencia previa en programación (o que vienen de Excel) que quieren usar R para limpiar, analizar, visualizar y reportar datos. Los ejemplos usan un conjunto de **ventas simuladas de retail** (12 tiendas, 3 canales, 4 regiones, 5 productos, 52 semanas de 2025).

## Objetivos del curso (diseño inverso)

Al terminar, la persona podrá:

1. **Escribir** scripts de R legibles usando objetos, estructuras de datos, control de flujo y funciones propias.
2. **Importar y ordenar** datos de CSV/Excel siguiendo los principios de *tidy data*.
3. **Transformar** y **resumir** datos con `dplyr` para calcular indicadores por grupo.
4. **Construir** visualizaciones claras con `ggplot2` adecuadas a cada pregunta.
5. **Aplicar e interpretar** estadística descriptiva, pruebas de hipótesis y regresión lineal.
6. **Producir** un reporte reproducible con Quarto que responda una pregunta de negocio.

**Evidencia de logro:** ejercicios con solución en cada módulo, 3 entregas parciales (módulos 3, 5 y 7) y un **proyecto integrador** evaluado con rúbrica (módulo 8).

## Mapa del curso

| # | Módulo | Horas | Nivel de Bloom | Evaluación |
|---|---|---|---|---|
| 1 | [[modulo-01-primeros-pasos\|Primeros pasos con R y RStudio]] | 4 | Recordar · Aplicar | Quiz |
| 2 | [[modulo-02-estructuras-de-datos\|Estructuras de datos]] | 4 | Comprender · Aplicar | Quiz + práctica |
| 3 | [[modulo-03-programacion\|Programación: control de flujo y funciones]] | 4 | Aplicar · Analizar | **Entrega 1** (rúbrica) |
| 4 | [[modulo-04-importar-y-ordenar\|Importar y ordenar datos]] | 4 | Comprender · Aplicar | Quiz + práctica |
| 5 | [[modulo-05-transformar-con-dplyr\|Transformar datos con dplyr]] | 5 | Aplicar · Analizar | **Entrega 2**: mini‑reporte de KPIs |
| 6 | [[modulo-06-visualizacion-ggplot2\|Visualización con ggplot2]] | 4 | Aplicar · Evaluar | Revisión entre pares |
| 7 | [[modulo-07-estadistica-y-modelos\|Estadística y modelos]] | 4 | Aplicar · Evaluar | **Entrega 3**: informe breve |
| 8 | [[modulo-08-reportes-quarto-y-proyecto\|Quarto y proyecto integrador]] | 5 | Crear | **Proyecto final** (rúbrica global) |

> Los enlaces `[[...]]` funcionan en Obsidian. En GitHub abre los archivos `modulo-0N-*.md` directamente.

## Ponderación sugerida

| Componente | Peso |
|---|---|
| Quizzes y ejercicios (M1, M2, M4, M6) | 15 % |
| Entrega 1 — funciones (M3) | 15 % |
| Entrega 2 — KPIs con dplyr (M5) | 20 % |
| Entrega 3 — informe estadístico (M7) | 15 % |
| Proyecto integrador (M8) | 35 % |

## Preparación

1. Instala **R** (https://cran.r-project.org/) y **RStudio Desktop** (https://posit.co/download/rstudio-desktop/).
2. Instala los paquetes del curso:
   ```r
   install.packages(c("tidyverse", "readxl", "broom", "scales", "renv"))
   ```
3. Abre esta carpeta como **Proyecto de RStudio** y genera los datos de práctica (ya incluidos en `datos/`):
   ```r
   source("datos/generar_ventas.R")
   ```

Todo el código del curso se ejecutó y verificó con R 4.3.3 y tidyverse 2.0.0 usando este directorio como directorio de trabajo.

## Estructura de archivos

```
curso-r/
├── README.md                          # este índice
├── modulo-01-primeros-pasos.md
├── modulo-02-estructuras-de-datos.md
├── modulo-03-programacion.md
├── modulo-04-importar-y-ordenar.md
├── modulo-05-transformar-con-dplyr.md
├── modulo-06-visualizacion-ggplot2.md
├── modulo-07-estadistica-y-modelos.md
├── modulo-08-reportes-quarto-y-proyecto.md
└── datos/
    ├── generar_ventas.R               # script reproducible (semilla fija)
    ├── ventas.csv                     # 3 120 filas: fecha, tienda, producto, precio, unidades
    └── tiendas.csv                    # 12 tiendas: canal y región
```

## Bibliografía general

Leyenda: [ES] español · [EN] inglés · [OA] acceso abierto.

### Libros
- Grolemund, G. (2014). *Hands-On Programming with R*. O'Reilly Media. ISBN 978-1-4493-5901-0. https://rstudio-education.github.io/hopr/ [EN] [OA en línea]
- Wickham, H. (2019). *Advanced R* (2.ª ed.). CRC Press. ISBN 978-0-8153-8457-1. https://adv-r.hadley.nz/ [EN] [OA en línea]
- Wickham, H., Çetinkaya-Rundel, M., & Grolemund, G. (2023). *R for Data Science: Import, tidy, transform, visualize, and model data* (2.ª ed.). O'Reilly Media. ISBN 978-1-4920-9740-2. https://r4ds.hadley.nz/ [EN] [OA en línea]
  - Traducción al español (2.ª ed.): https://davidrsch.github.io/r4ds-es/ [ES] [OA]
  - Traducción comunitaria (1.ª ed.): https://es.r4ds.hadley.nz/ [ES] [OA]

### Artículos
- Wickham, H. (2014). Tidy data. *Journal of Statistical Software, 59*(10), 1–23. https://doi.org/10.18637/jss.v059.i10 [EN] [OA]
- Wickham, H., Averick, M., Bryan, J., Chang, W., McGowan, L. D., François, R., … Yutani, H. (2019). Welcome to the tidyverse. *Journal of Open Source Software, 4*(43), 1686. https://doi.org/10.21105/joss.01686 [EN] [OA]

### Documentación
- R Core Team. *An Introduction to R*. https://cran.r-project.org/doc/manuals/r-release/R-intro.html [EN] [OA]
- Quarto. *Tutorial: Computations*. https://quarto.org/docs/get-started/computations/rstudio [EN]

### Videos
- freeCodeCamp.org. *R Programming Tutorial – Learn the Basics of Statistical Computing* [Video] (Barton Poulson, ~2 h). https://youtu.be/_V8eKsto3Ug [EN]
- *Curso completo de R para Data Science con Tidyverse* [Video] (Juan Gabriel Gomila Salas). https://www.youtube.com/watch?v=9NJyhs5PlGQ [ES] *[canal y fecha POR VERIFICAR]*
- StatQuest with Josh Starmer. *Linear Regression in R, Step-by-Step* [Video]. https://www.youtube.com/watch?v=u1cc1r_Y7M0 [EN]

### Nota de verificación
Las referencias se verificaron mediante búsqueda web (título, autores, editorial, ISBN, DOI y existencia de la URL en índices de búsqueda) el 2026-09-25. No fue posible abrir directamente las páginas desde el entorno de trabajo, por lo que las **fechas de publicación de los videos** y el **nombre exacto del canal** del video en español quedan marcados como *POR VERIFICAR*. Revísalos antes de publicar el curso.
