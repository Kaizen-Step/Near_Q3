# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp

# Global Variables
theme_plotly = None  # None or streamlit
week_days = ['Monday', 'Tuesday', 'Wednesday',
             'Thursday', 'Friday', 'Saturday', 'Sunday']

# Layout
st.set_page_config(page_title='Bridge - Near Dashboard',
                   page_icon=':bar_chart:', layout='wide')
st.title('🌉Bridge')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache()
def get_data(query):
    if query == 'Near_Bridge5':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/62a94ba4-64a4-4bee-bf00-09cf995e5c78/data/latest')
    elif query == 'Near_Bridge3':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/b3bbad0f-0d6c-4bb9-9379-748182d0d051/data/latest')
    elif query == 'Near_Bridge2':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/92267a89-0f8d-48b1-91bb-f10260c0d1c0/data/latest')
    elif query == 'daily_bridge_detail':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/3b5c115f-5335-4233-b6a8-9bd9ffec9226/data/latest')
    return None


Near_Bridge5 = get_data('Near_Bridge5')
Near_Bridge3 = get_data('Near_Bridge3')
Near_Bridge2 = get_data('Near_Bridge2')
daily_bridge_detail = get_data('daily_bridge_detail')

st.text(" \n")
st.subheader('Bridging Metrics')


df = Near_Bridge5
df2 = Near_Bridge3
df3 = Near_Bridge2
df4 = daily_bridge_detail


# Weekly USERs of Bridge from Ethereum to NEAR by Token
fig = px.bar(df2.sort_values(["DATE", "UNIQUE_WALLETS_FROM"], ascending=[
    True, False]), x="DATE", y="UNIQUE_WALLETS_FROM", color="SYMBOL", title='Weekly USERs of Bridge from Ethereum to NEAR by Token'.title())
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Number of Users')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Weekly Number of Bridge transactions from Ethereum to NEAR by Token
fig = px.bar(df2.sort_values(["DATE", "NUMBER_TRANSACTIONS"], ascending=[
    True, False]), x="DATE", y="NUMBER_TRANSACTIONS", color="SYMBOL", title='Weekly Number of Bridge transactions from Ethereum to NEAR by Token'.title())
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Number of TX')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# Weekly Volume (USD) of Bridge Transactions from Ethereum to NEAR by Token
fig = px.bar(df2.sort_values(["DATE", "USD_VOLUME"], ascending=[
    True, False]), x="DATE", y="USD_VOLUME", color="SYMBOL", title='Weekly Volume (USD) of Bridge Transactions from Ethereum to NEAR by Token'.title())
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Volume [USD]')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Top Categories in terms of actions after bridging to Near: Number of transactions, normalised
fig = px.area(df3, x="DATE", y="NUMBER_TRANSACTIONS", color="APP_USED",
              title='Top Categories in terms of actions after bridging to Near: Number of transactions, normalised', groupnorm='percent')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title="NUMBER_TRANSACTIONS")
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
st.text(" \n")
st.text(" \n")
st.text(" \n")
st.subheader('Cumulative Metrics')


# Cumulative bridge from Ethereum to NEAR - (Weekly volume in $USD)
fig = px.line(df, x="DATE", y="CUM_TOTAL_AMOUNT_USD",
              color="SYMBOL", title='Cumulative bridge from Ethereum to NEAR - (Weekly volume in $USD)')
fig.update_layout(showlegend=True, xaxis_title='NUMBER_TRANSACTIONS'.title(),
                  yaxis_title=None)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Proportion of Volume Bridged From Ethereum to NEAR by Token
fig = px.pie(df2, values="USD_VOLUME",
             names="SYMBOL", title='Proportion of Volume Bridged From Ethereum to NEAR by Token')
fig.update_layout(legend_title=None, legend_y=0.5)
fig.update_traces(textinfo='percent+value', textposition='inside')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
