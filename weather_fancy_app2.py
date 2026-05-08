import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

# --------------------
# Mock weather data
# --------------------
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

# --------------------
# App Layout
# --------------------
st.set_page_config(page_title="Norway Weather Dashboard", layout="wide")
st.title("🌦️ Norway Weather Dashboard")
city = st.selectbox("🏙️ Select City", list(weather_data.keys()))

# Get selected city data
data = weather_data[city]

st.markdown(f"### 🌍 Weather Report for **{city}**, Norway")
st.markdown(f"📝 {data['description'].capitalize()}")

# --------------------
# Fancy Dials for Weather Metrics
# --------------------
def dial_chart(value, title, min_val=0, max_val=100, unit=""):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        gauge={'axis': {'range': [min_val, max_val]},
               'bar': {'color': "#E4080A"}},
        title={'text': title + f" ({unit})"},
        number={'suffix': f" {unit}"}
    ))
    #fig.update_layout(height=150, margin=dict(t=20, b=10))


    fig.update_layout(
        height=300,  # Increased height
        margin=dict(t=60, b=60, l=5, r=5)  # Adjusted margins
    )
    return fig

# Layout

dial_col1, dial_col2 = st.columns(2)

dial_col1.plotly_chart(dial_chart(data['temp'], "Temperature", -20, 40, "°C"), use_container_width=True)
dial_col2.plotly_chart(dial_chart(data['wind_speed'], "Wind Speed", 0, 15, "m/s"), use_container_width=True)


dial_col3, dial_col4 = st.columns(2)
dial_col3.plotly_chart(dial_chart(data['humidity'], "Humidity", 0, 100, "%"), use_container_width=True)

dial_col4.plotly_chart(dial_chart(data['feels_like'], "Feels_Like", -20, 40, "°C"), use_container_width=True)

# --------------------
# Historical Charts
# --------------------
np.random.seed(0)
days = pd.date_range(end=pd.Timestamp.today(), periods=10)
historical = pd.DataFrame({
    "Date": days,
    "Temperature": data["temp"] + np.random.normal(0, 2, size=10),
    "Humidity": data["humidity"] + np.random.normal(0, 5, size=10)
})

st.write("#### Historical Data", historical)

st.subheader("📈 Historical Trends")
hist_col1, hist_col2 = st.columns(2)
hist_col1.plotly_chart(px.line(historical, x="Date", y="Temperature", title="Temperature Over 10 Days"))
hist_col2.plotly_chart(px.line(historical, x="Date", y="Humidity", title="Humidity Over 10 Days"))

# make one more dial for feel like and then distribute it in two columns:
# first colum will have temp and humidity
# second column will have feels  like and wind speed.
