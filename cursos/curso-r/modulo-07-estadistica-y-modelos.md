---
titulo: "Módulo 7 — Estadística y modelos en R"
curso: "Programación en R: de cero a análisis de datos"
nivel: "intermedio"
duracion_h: 4
tags: [curso-r, modulo-7, estadistica]
---

# Módulo 7 — Estadística y modelos en R

- **Duración estimada:** 1.5 h teoría + 2.5 h práctica
- **Objetivos de aprendizaje.** Al finalizar, la persona podrá:
  1. **Calcular** estadísticos descriptivos (media, mediana, desviación estándar, cuantiles, correlación).
  2. **Ejecutar** pruebas de hipótesis básicas (`t.test()`, `wilcox.test()`, `chisq.test()`).
  3. **Ajustar** un modelo de regresión lineal con `lm()` usando la sintaxis de fórmulas.
  4. **Interpretar** coeficientes, valores p, R² y residuos, y **justificar** si el modelo es adecuado.

## Contenidos

1. Estadística descriptiva por grupo con `dplyr`.
2. Correlación: `cor()` (Pearson y Spearman).
3. Pruebas de hipótesis: t de Welch, Mann‑Whitney/Wilcoxon, chi‑cuadrada.
4. Fórmulas en R: `y ~ x1 + x2`.
5. Regresión lineal: `lm()`, `summary()`, `coef()`, `confint()`, `predict()`.
6. Diagnóstico con residuos; resultados ordenados con `broom::tidy()`.

## Desarrollo

```r
library(tidyverse)
ventas  <- read_csv("datos/ventas.csv", show_col_types = FALSE)
tiendas <- read_csv("datos/tiendas.csv", show_col_types = FALSE)
ventas_det <- ventas |>
  left_join(tiendas, by = "tienda_id") |>
  drop_na(unidades) |>
  mutate(temporada = if_else(month(fecha) %in% 11:12, "Nov-Dic", "Resto"))
```

### Descriptivos

```r
ventas_det |>
  summarise(
    media   = mean(unidades),
    mediana = median(unidades),
    de      = sd(unidades),
    p90     = quantile(unidades, 0.9),
    .by = producto
  )
```

### Prueba t: ¿la temporada cambia las ventas?

```r
reloj <- ventas_det |> filter(producto == "Reloj")
t.test(unidades ~ temporada, data = reloj)       # Welch por defecto
wilcox.test(unidades ~ temporada, data = reloj)  # alternativa no paramétrica
```

> **Cuidado:** las observaciones semanales de una misma tienda no son del todo independientes. Aquí la prueba es ilustrativa; en un análisis formal hay que considerar la autocorrelación.

### Chi‑cuadrada: ¿la mezcla de productos depende del canal?

```r
tabla <- xtabs(unidades ~ canal + producto, data = ventas_det)
tabla
chisq.test(tabla)
```

### Regresión lineal

```r
semanal <- ventas_det |>
  summarise(unidades = sum(unidades), .by = c(fecha, canal, temporada))

modelo <- lm(unidades ~ temporada + canal, data = semanal)
summary(modelo)
confint(modelo)

library(broom)
tidy(modelo)          # coeficientes como tibble
glance(modelo)        # R², AIC, etc.

nuevo <- tibble(temporada = "Nov-Dic", canal = "En línea")
predict(modelo, newdata = nuevo, interval = "prediction")
```

### Diagnóstico

```r
aug <- augment(modelo)
ggplot(aug, aes(.fitted, .resid)) +
  geom_point(alpha = 0.5) +
  geom_hline(yintercept = 0, linetype = "dashed") +
  labs(title = "Residuos vs. ajustados", x = "Ajustado", y = "Residuo")
```

## Actividades y ejercicios

1. Calcula la matriz de correlación entre `precio` y `unidades` a nivel registro. ¿Qué signo esperas y por qué?
2. Prueba si las unidades de **Audífonos** difieren entre las regiones **Norte** y **Sur**.
3. Ajusta `lm(unidades ~ temporada * canal)` y compara su R² ajustado con el modelo sin interacción.
4. Redacta en 3 líneas la interpretación del coeficiente `temporadaResto` para un público no técnico.

<details>
<summary>Soluciones</summary>

```r
# 1: negativo; los productos caros se venden en menos unidades
cor(ventas_det$precio, ventas_det$unidades)
cor(ventas_det$precio, ventas_det$unidades, method = "spearman")

# 2
audif <- ventas_det |> filter(producto == "Audífonos", region %in% c("Norte", "Sur"))
t.test(unidades ~ region, data = audif)

# 3
modelo_int <- lm(unidades ~ temporada * canal, data = semanal)
c(sin_interaccion = glance(modelo)$adj.r.squared,
  con_interaccion = glance(modelo_int)$adj.r.squared)
anova(modelo, modelo_int)

# 4 (ejemplo): "Fuera de noviembre-diciembre, cada canal vende en promedio
# alrededor de X unidades menos por semana que en temporada alta, manteniendo
# el canal constante; la diferencia es estadísticamente clara (p < 0.001)."
coef(modelo)["temporadaResto"]
```

</details>

## Evaluación (sumativa parcial)

Informe breve (1 página) con: pregunta de negocio, prueba o modelo elegido y **por qué**, resultado con intervalo de confianza, verificación de supuestos y una limitación. Rúbrica: pertinencia del método (30 %), ejecución correcta (30 %), interpretación (30 %), comunicación (10 %).

## Referencias verificadas

- ▶️ StatQuest with Josh Starmer. *Linear Regression in R, Step-by-Step* [Video]. YouTube. https://www.youtube.com/watch?v=u1cc1r_Y7M0 [EN] *[fecha POR VERIFICAR]*
- ▶️ StatQuest with Josh Starmer. *Linear Regression and Linear Models* [Lista de reproducción]. YouTube. https://www.youtube.com/playlist?list=PLblh5JKOoLUIzaEkCLIUxQFjPIlapw8nU [EN]
- 🌐 R Core Team. *An Introduction to R* — sección "Statistical models in R". https://cran.r-project.org/doc/manuals/r-release/R-intro.html [EN] [OA]
- 📚 Wickham, H., Çetinkaya-Rundel, M., & Grolemund, G. (2023). *R for Data Science* (2.ª ed.). O'Reilly Media. ISBN 978-1-4920-9740-2. Español: https://davidrsch.github.io/r4ds-es/ [ES] [OA] — caps. de análisis exploratorio como base para modelar.

[[modulo-06-visualizacion-ggplot2|← Módulo 6]] · [[modulo-08-reportes-quarto-y-proyecto|Módulo 8 →]]
