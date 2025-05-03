import streamlit as st
import pandas as pd
import numpy as np



#Creación del archivo csv.

np.random.seed(42)
dates = pd.date_range(start="2024-01-01", end="2024-12-31", freq="D")
products = ["Laptop", "Phone", "Tablet", "Headphones", "Smart watch"]
categories = ["Electronics", "Accessories"]
data = {
    "Date": np.random.choice(dates, 50),
    "Product": np.random.choice(products, 50),
    "Category": np.random.choice(categories, 50),
    "Price": np.random.uniform(50, 500, 50).round(2),
    "Quantity": np.random.randint(1, 5, 50)
}
df = pd.DataFrame(data)
df["Total_Sales"] = df["Price"] * df["Quantity"]
df.to_csv("sales_data.csv", index=False)


##Cálculos del ejercicio



# Título de la aplicación
st.title("Análisis Básico de Ventas")

# Cargar el dataset
# TODO: Carga el archivo 'sales_data.csv'
st.subheader("DataFrame")
df = pd.read_csv('sales_data.csv')
st.dataframe(df)

# Mostrar dataset completo
st.subheader("Datos Completos")
st.write(df)


# Filtros en la barra lateral
st.sidebar.header("Filtros") 
Category = st.sidebar.selectbox("Selecciona una categoría", options=df["Category"].unique())


# TODO: Crea un slider para el rango de precios
min_price = float(df["Price"].min())
max_price = float(df["Price"].max())

st.sidebar.subheader("Rango")
price_range = st.sidebar.slider("Rango en el precio de los artículos", min_value=min_price, max_value=max_price, value=(min_price, max_price))



# Aplicar filtros
# TODO: Filtra el DataFrame por categoría y rango de precios
filtro_df = df[(df["Category"] == Category) & (df["Price"]>= price_range[0]) & (df["Price"]<=price_range[1])]


# Mostrar datos filtrados
st.subheader("Datos Filtrados")
# TODO: Muestra el DataFrame filtrado y el número de registros
st.write(f"{len(filtro_df)} registros filtrados.")
st.dataframe(filtro_df)

# Estadísticas
st.subheader("Estadísticas")
if not filtro_df.empty:
    # TODO: Calcula el total de ventas y el precio promedio
    total_sales = filtro_df["Total_Sales"].sum()
    avg_price = filtro_df["Price"].mean()
    # TODO: Muestra las estadísticas con st.metric
    st.metric("Total en ventas:", f"${total_sales:,.2f}")
    st.metric("Promedio de precios:", f"${avg_price:,.2f}")
else:
    st.write("No hay datos para los filtros seleccionados.")
