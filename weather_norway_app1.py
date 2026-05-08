import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Mock weather data for 3 cities
weather_data = {
    "Oslo": {
        "temp": 10, "feels_like": 8.6, "humidity": 82, "pressure": 1012, "wind_speed": 4.6,
        "weather_main": "Clouds", "description": "Overcast clouds"
    },
    "Bergen": {
        "temp": 9, "feels_like": 7.5, "humidity": 90, "pressure": 1010, "wind_speed": 5.2,
        "weather_main": "Rain", "description": "Light rain showers"
    },
    "Tromsø": {
        "temp": 2, "feels_like": -1, "humidity": 75, "pressure": 1022, "wind_speed": 3.0,
        "weather_main": "Snow", "description": "Snow flurries"
    }
}

# Dropdown to select city
city = st.selectbox("Choose a city in Norway", list(weather_data.keys()))

# Extract data
data = weather_data[city]
st.title("🌦️ Current Weather Dashboard")
st.subheader(f"📍 Location: {city}, NO")

# Metric display
col1, col2 = st.columns(2)
with col1:
    st.metric("🌡 Temperature (°C)", data["temp"])
    st.metric("🤔 Feels Like (°C)", data["feels_like"])
    st.metric("🌬 Wind Speed", f"{data['wind_speed']} m/s")

with col2:
    st.metric("🌤 Weather", data["weather_main"])
    st.metric("💧 Humidity", f"{data['humidity']}%")
    st.metric("📈 Pressure", f"{data['pressure']} hPa")

st.info(f"📝 Description: {data['description']}")

# Generate dummy historical data
np.random.seed(0)
days = pd.date_range(end=pd.Timestamp.today(), periods=10)
historical = pd.DataFrame({
    "Date": days,
    "Temperature": data["temp"] + np.random.normal(0, 2, size=10),
    "Feels Like": data["feels_like"] + np.random.normal(0, 2, size=10),
    "Wind_Speed": data["wind_speed"] + np.random.normal(0, 2, size=10),
    "Humidity": data["humidity"] + np.random.normal(0, 5, size=10)
})



# Histogram plots
st.subheader("📊 Weather History (Last 10 Days)")

# Show historical data
st.write("#### Historical Data", historical)
st.plotly_chart(px.bar(historical, x="Date", y="Temperature", title="Temperature Trend"))
st.plotly_chart(px.bar(historical, x="Date", y="Humidity", title="Humidity Trend"))
st.plotly_chart(px.bar(historical, x="Date", y="Feels Like", title="Feels Like"))
st.plotly_chart(px.line(historical, x="Date", y="Wind_Speed", title="Wind Speed"))


# plot the line chart for historical wind speed and abr chart for feel like