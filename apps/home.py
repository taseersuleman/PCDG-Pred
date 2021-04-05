import streamlit as st
from PIL import Image

def app():
    st.subheader("""
    Cancer is driven by distinctive sorts of changes and basic variations in genes. Recognizing cancer driver genes is basic for accurate oncological analysis. Numerous progression calculations to distinguish drivers presently exist, but efficient tools to combine and optimize them on huge datasets are few. Most strategies for prioritizing transformations depend basically on frequency-based criteria. Strategies are required to dependably prioritize organically dynamic driver changes over inert passengers in high-throughput sequencing cancer information sets. """)
    image = Image.open('cancer_01.jpg')
    st.image(image)
    st.subheader("""
    This study proposes a model PCDG-Pred, an unsupervised utility capable of distinguishing cancer driver and passenger attributes of genes based on sequential data. Keeping in view the significance of the cancer driver genes an efficient method is proposed to identify the cancer driver genes. Further, various validation techniques are applied at different levels to establish the effectiveness of the model and to obtain metrics like accuracy, Mathew’s correlation coefficient, sensitivity, and specificity. The results of the study strongly indicate that the proposed strategy provides a fundamental functional advantage over other existing strategies for cancer driver genes identification.""")


