# Genera el conjunto de datos de práctica del curso: ventas simuladas de retail.
# Uso: source("datos/generar_ventas.R")  -> crea datos/ventas.csv y datos/tiendas.csv

set.seed(2025)

tiendas <- data.frame(
  tienda_id = sprintf("T%02d", 1:12),
  canal     = rep(c("Departamental", "Autoservicio", "En línea"), each = 4),
  region    = rep(c("Norte", "Centro", "Sur", "Occidente"), times = 3)
)

productos <- data.frame(
  producto = c("Smartphone A", "Smartphone B", "Tablet", "Audífonos", "Reloj"),
  precio   = c(4999, 7999, 6499, 899, 2499)
)

fechas <- seq(as.Date("2025-01-06"), as.Date("2025-12-29"), by = "week")

ventas <- expand.grid(
  fecha     = fechas,
  tienda_id = tiendas$tienda_id,
  producto  = productos$producto,
  stringsAsFactors = FALSE
)
ventas <- merge(ventas, productos, by = "producto")

# Demanda base por producto + estacionalidad de fin de año + ruido
base <- c("Smartphone A" = 12, "Smartphone B" = 6, "Tablet" = 4,
          "Audífonos" = 20, "Reloj" = 8)
mes <- as.integer(format(ventas$fecha, "%m"))
factor_temporada <- ifelse(mes %in% c(11, 12), 1.6, 1)
ventas$unidades <- rpois(nrow(ventas), base[ventas$producto] * factor_temporada)

# Algunos faltantes intencionales para practicar limpieza
ventas$unidades[sample(nrow(ventas), 40)] <- NA

ventas <- ventas[order(ventas$fecha, ventas$tienda_id, ventas$producto),
                 c("fecha", "tienda_id", "producto", "precio", "unidades")]

write.csv(ventas, "datos/ventas.csv", row.names = FALSE)
write.csv(tiendas, "datos/tiendas.csv", row.names = FALSE)
