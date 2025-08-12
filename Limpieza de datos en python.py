import pandas as pd

# 1. Leer CSV con separador correcto
df = pd.read_csv("C:/Users/User/Documents/EXCEL/entel_lima_ventas_2024_dirty.csv", sep=";")

# 2. Quitar espacios extra en todos los textos
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# 3. Convertir la columna de fecha a tipo datetime
df["fecha"] = pd.to_datetime(df["fecha"], errors="coerce", dayfirst=True)

# 4. Convertir columnas numéricas
num_cols = ["monto_venta", "descuento", "total_con_descuento"]
for col in num_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# 5. (Opcional) Eliminar filas con datos vacíos críticos
df.dropna(subset=["id", "nombre", "apellido", "fecha"], inplace=True)

# 6. Guardar en nuevo CSV limpio
df.to_csv("C:/Users/User/Documents/EXCEL/entel_python_ventas_2024_dirty.csv", index=False)

print("✅ Archivo limpio guardado como 'entel_lima_ventas_2024_clean.csv'")
df.head()