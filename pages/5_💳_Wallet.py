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
st.set_page_config(page_title='Wallets - Near Dashboard',
                   page_icon=':bar_chart:', layout='wide')
st.title('💳Wallets')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache()
def get_data(query):
    if query == 'NEAR_Wallet1':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/1a51749a-2932-4ae4-b6c9-8911a93ff1b2/data/latest')
    elif query == 'NEAR_supply_richest':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/a9de75ce-2ed2-4394-ba02-55921a2b9aa0/data/latest')
    elif query == 'NEAR_Balance_Range':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/070d0011-42bc-465c-896f-d1a3f269e7d2/data/latest')
    return None


NEAR_Wallet1 = get_data('NEAR_Wallet1')
NEAR_supply_richest = get_data('NEAR_supply_richest')
NEAR_Balance_Range = get_data('NEAR_Balance_Range')

st.text(" \n")
st.subheader('Users Metrics')


df = NEAR_Wallet1
df3 = NEAR_supply_richest
df4 = NEAR_Balance_Range

# Total Number of Active Wallets Per Week With Cumulative Value
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df['WEEK'], y=df["ACTIVE_WALLETS"],
                     name='Number of ACTIVE WALLETS'), secondary_y=False)
fig.add_trace(go.Line(x=df['WEEK'], y=df["CUMULATIVE_ACTIVE_WALLET"],
                      name='CUMULATIVE ACTIVE WALLET'), secondary_y=True)
fig.update_layout(
    title_text='Total Number of Active Wallets Per Week With Cumulative Value')
fig.update_yaxes(
    title_text='Number of ACTIVE WALLETS', secondary_y=False)
fig.update_yaxes(title_text='CUMULATIVE Number', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Total Number of New Wallets Per Week With Cumulative Number
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df['WEEK'], y=df['NEW_WALLETS'],
                     name='NEW WALLETS'), secondary_y=False)
fig.add_trace(go.Line(x=df['WEEK'], y=df['CUMULATIVE_NEW_WALLET'],
                      name='CUMULATIVE NEW WALLET'), secondary_y=True)
fig.update_layout(
    title_text='Total Number of New Wallets Per Week With Cumulative Number')
fig.update_yaxes(
    title_text='Number of NEW WALLETS', secondary_y=False)
fig.update_yaxes(title_text='CUMULATIVE Number', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Richest Users
fig = px.bar(df3, x="RECEIVER", y="BALANCE", color="RECEIVER",
             title='Richest Users')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title="BALANCE".title())
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# NEAR supply- distrbution users based on Balance Range
fig = px.bar(df4.sort_values(["WALLET_NUMBER", "BALANCE_RANGE"], ascending=[
             True, False]), y="WALLET_NUMBER", x="BALANCE_RANGE", title='NEAR supply- distrbution users based on Balance Range'.title(), color="BALANCE_RANGE")
fig.update_layout(legend_title=None, xaxis_title="BALANCE_RANGE",
                  yaxis_title="BALANCE_RANGE")
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
