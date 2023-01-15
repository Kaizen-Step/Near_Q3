# Libraries
import streamlit as st
from PIL import Image

# Layout
st.set_page_config(page_title='Near Quarter 3 Dashboard',
                   page_icon=':bar_chart:', layout='wide')
st.title('Near Quarter 3 Dashboard')

# Content
c1, c2, c3, c4 = st.columns(4)
c4.image(Image.open('Images/near-logo.png'))


with c1:
    st.text(" \n")
    st.text(" \n")
    st.text(" \n")
    st.text(" \n")

    st.write("""  # ♾️Near Q3 (Transparency) #   """)
st.write("""

NEAR Protocol is software that aims to incentivize a network of computers to operate a platform for developers to create and launch decentralized applications.  
Central to NEAR Protocol’s design is the concept of sharding, a process that aims to split the network’s infrastructure into several segments in order for computers, also known as nodes, to only have to handle a fraction of the network’s transactions.  
By distributing segments of the blockchain, rather than the complete blockchain across network participants, sharding is expected to create a more efficient way to retrieve network data and scale the platform.  
NEAR operates in a similar manner to other centralized data storage systems like Amazon Web Services (AWS) that serve as the base layer on which applications are built. But rather than being run by a single entity, NEAR is operated and maintained by a distributed network of computers.  
Just as AWS allows developers to deploy code in the cloud without needing to create their own infrastructure, NEAR Protocol facilitates a similar architecture built around a network of computers and its native cryptocurrency, the NEAR token.  

### History ###
NEAR Protocol was founded by Alex Skidanov and Illia Polosukhin. Skidanov was formerly director of engineering at the database company MemSQL. Polosukhin previously worked at Google, where he helped develop its artificial intelligence capabilities and search engine products. 

Over multiple rounds, NEAR has raised more than $20 million from leading venture capital firms including Andreessen Horowitz and Pantera Capital.


""")

st.write("""   
##### Sources #####   """)
st.write("""    1.https://www.coindesk.com/learn/what-is-near-protocol-and-how-does-it-work/  
        2.https://www.kraken.com/en-gb/learn/what-is-near-protocol
      
              """)
c1, c2 = st.columns(2)
with c2:
    st.info(
        '**Project Supervisor:  [MetricsDao](https://metricsdao.notion.site/)**', icon="👨🏻‍💼")
with c1:
    st.info(
        '**Data:  [Flipside Crypto](https://flipsidecrypto.xyz/)**', icon="🧠")
