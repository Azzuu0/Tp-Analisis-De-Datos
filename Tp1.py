# ==============================
# TP - Limpieza y Análisis de Datos
# ==============================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# 1. Cargar el dataset en un DataFrame

df = pd.read_csv("dataset2 (1).csv")


# 2. Explorar la estructura de los datos

print("Dimensiones del dataset:", df.shape)
print("\nTipos de datos:")
print(df.dtypes)
print("\nPrimeras filas:")
print(df.head())

# ==============================
# 3. Detectar y manejar valores nulos
# ==============================
# Reemplazar la palabra "desconocido" por NaN para unificar
df = df.replace("desconocido", pd.NA)

print("\nValores nulos antes de limpiar:")
print(df.isnull().sum())

# Convertir Edad e Ingresos a valores numéricos (forzando errores a NaN)
df["Edad"] = pd.to_numeric(df["Edad"], errors="coerce")
df["Ingresos"] = pd.to_numeric(df["Ingresos"], errors="coerce")

# Rellenar nulos: Edad con la media, Ingresos con la mediana
df["Edad"] = df["Edad"].fillna(df["Edad"].mean())
df["Ingresos"] = df["Ingresos"].fillna(df["Ingresos"].median())

print("\nValores nulos después de limpiar:")
print(df.isnull().sum())

# ==============================
# 4. Identificar y eliminar duplicados
# ==============================
print("\nDuplicados antes de limpiar:", df.duplicated().sum())
df = df.drop_duplicates()
print("Duplicados después de limpiar:", df.duplicated().sum())

# ==============================
# 5. Corregir valores erróneos o inconsistentes
# ==============================
# Normalizar texto: quitar espacios extra y poner mayúscula inicial
df["Nombre"] = df["Nombre"].str.strip().str.title()
df["Ciudad"] = df["Ciudad"].str.strip().str.title()
df["Ocupacion"] = df["Ocupacion"].str.strip().str.title()

# ==============================
# 6. Análisis descriptivo de cada columna
# ==============================
print("\nAnálisis descriptivo de Edad:")
print(df["Edad"].describe())

print("\nAnálisis descriptivo de Ingresos:")
print(df["Ingresos"].describe())

print("\nCantidad por Ocupación:")
print(df["Ocupacion"].value_counts())

print("\nCantidad por Ciudad:")
print(df["Ciudad"].value_counts())

# ==============================
# 7. Generar al menos 3 visualizaciones
# ==============================

# Histograma de edades
plt.figure(figsize=(6,4))
sns.histplot(df["Edad"], bins=6, kde=True)
plt.title("Distribución de Edades")
plt.show()

# Gráfico de barras de ocupaciones
plt.figure(figsize=(6,4))
sns.countplot(x="Ocupacion", data=df)
plt.title("Cantidad de personas por Ocupación")
plt.show()

# Dispersión de Ingresos vs Edad
plt.figure(figsize=(6,4))
sns.scatterplot(x="Edad", y="Ingresos", data=df)
plt.title("Relación entre Ingresos y Edad")
plt.show()

# ==============================
# 8. Informe en PDF
# ==============================
# 👉 Este punto no se hace por código: 
# Tenés que sacar capturas de pantalla de:
#   - Exploración inicial
#   - Resultados de limpieza (nulos, duplicados)
#   - Análisis descriptivo
#   - Gráficos
# Luego armás un informe en Word o Google Docs:
#   - Introducción: qué dataset es y qué problemas tenía
#   - Desarrollo: capturas de cada paso
#   - Conclusiones: cómo estaba el dataset original y cómo quedó limpio
# Finalmente exportás el documento a PDF.