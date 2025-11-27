import pandas as pd
import plotly.express as px

import streamlit as st

st.set_page_config(
    page_title="Dashboard",
    layout="wide"
)

st.title("Dashboard")

df = pd.read_csv("WHO_time_series.csv")
df.head()


df['Date_reported'] = pd.to_datetime(df['Date_reported'])

fig1 = px.line(df, x='Date_reported', y='Cumulative_cases', color='Country', title="Casos por ano.")

fig1.update_layout(xaxis_title="Data", yaxis_title="Casos", title_font_size=30)
fig1.show()

st.plotly_chart(fig1, use_container_width=True)

dfbrasilusa = df.query('Country == "Brazil" or Country == "United States of America"')

dfbrasilusa.head()

fig1 = px.line(dfbrasilusa, x = 'Date_reported', y='Cumulative_cases', color='Country', title='Casos acumulados em Brasil x USA')
fig1.update_layout(xaxis_title="Data", yaxis_title="Casos")

fig1.show()
st.plotly_chart(fig1, use_container_width=True)

df_brasil_usa_india = df.query('Country == "Brazil" or Country=="India" or Country=="United States of America"')

fig1 = px.pie(df_brasil_usa_india, values='Cumulative_cases', names='Country')
fig1.show()

st.plotly_chart(fig1, use_container_width=True)





