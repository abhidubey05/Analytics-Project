import streamlit as st
import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv("../analysis/kc_house_data.csv")
 # Replace with your actual file name/path

st.title("🏠Kc House Dataset")


# unfiltered data
st.subheader("🌟Unfiltered Data")
st.dataframe(df, use_container_width= True)
st.sidebar.markdown("Select the option to filter the dataset")


# Sidebar filters
st.sidebar.header("🔍 Filter Options")

# Price Filter
min_price, max_price = float(df['price'].min()), float(df['price'].max())
price_range = st.sidebar.slider("Price Range", min_price, max_price, (min_price, max_price))

# Bedroom Filter
bedrooms = st.sidebar.multiselect("Bedrooms", sorted(df['bedrooms'].unique()), default=sorted(df['bedrooms'].unique()))

# Bathroom Filter
bathrooms = st.sidebar.multiselect("Bathrooms", sorted(df['bathrooms'].unique()), default=sorted(df['bathrooms'].unique()))

# Zipcode Filter
zipcodes = st.sidebar.multiselect("Zipcodes", sorted(df['zipcode'].unique()), default=sorted(df['zipcode'].unique()))

# Apply filters
filtered_df = df[
    (df['price'] >= price_range[0]) & (df['price'] <= price_range[1]) &
    (df['bedrooms'].isin(bedrooms)) &
    (df['bathrooms'].isin(bathrooms)) &
    (df['zipcode'].isin(zipcodes))
]

st.subheader("📊 Filtered Data")
st.write(f"Total Results: {filtered_df.shape[0]}")
st.dataframe(filtered_df)

# Visualizations
st.subheader("💰 Price Distribution")
fig_price = px.histogram(filtered_df, x="price", nbins=30, title="Price Histogram", template="plotly_dark")
st.plotly_chart(fig_price, use_container_width=True)

st.subheader("🛏 Bedrooms Distribution")
fig_bed = px.histogram(filtered_df, x="bedrooms", title="Bedrooms Count", template="plotly_dark")
st.plotly_chart(fig_bed, use_container_width=True)

st.subheader("🛁 Bathrooms Distribution")
fig_bath = px.histogram(filtered_df, x="bathrooms", title="Bathrooms Count", template="plotly_dark")
st.plotly_chart(fig_bath, use_container_width=True)

st.subheader("📍 Price vs Sqft Living")
fig_scatter = px.scatter(filtered_df, x="sqft_living", y="price", color="grade", title="Price vs Sqft Living", template="plotly_dark")
st.plotly_chart(fig_scatter, use_container_width=True)





