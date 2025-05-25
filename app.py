import streamlit as st
import pandas as pd
import altair as alt

# Title
st.title("Cultural Atlas of India")
st.subheader("Showcasing Art, Culture & Tourism through Data")

# Description
st.markdown("""
Explore India's rich cultural diversity and tourism trends with a data-driven dashboard. 
This tool visualizes government initiatives, seasonal tourist flow, and highlights lesser-known cultural hotspots.
""")

# Load demo data
@st.cache_data
def load_data():
    data = pd.DataFrame({
        "State": ["Rajasthan", "Kerala", "Odisha", "Tamil Nadu", "Nagaland"],
        "Traditional Art": ["Miniature Painting", "Kathakali", "Pattachitra", "Bharatanatyam", "Naga Woodcraft"],
        "Tourists 2023 (in lakhs)": [85, 45, 12, 70, 3]
    })
    return data

df = load_data()

# Show table
st.markdown("### Cultural Art Forms and Tourism")
st.dataframe(df)

# Bar chart for tourists
chart = alt.Chart(df).mark_bar().encode(
    x='State',
    y='Tourists 2023 (in lakhs)',
    color='State'
).properties(title="Tourist Visits by State (2023)")

st.altair_chart(chart, use_container_width=True)

# Info section
st.markdown("""
**Key Insights:**
- Rajasthan and Tamil Nadu lead in cultural tourism.
- Northeastern states like Nagaland have untapped potential.
- Government support and visibility can boost regional tourism.
""")
