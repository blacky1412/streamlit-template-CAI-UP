import streamlit as st

# I have provided most of what you need for to use streamlit here and in README.md
# You can also check the streamlit docs at https://docs.streamlit.io/get-started
# Also, you can check a simple example from class:
# Page: https://simpson-dashboard-class.streamlit.app/
# GitHub Repo: https://github.com/RodrigoGrijalba/python-dashboard-class

st.set_page_config(page_title = "<<Your page title here>>", layout = "wide")

tab1, tab2, tab3, tab4 = st.tabs(["Original Paper", "Proposed Extention", "Extension Results", "Referencres"])

with tab1:
    st.markdown("""
    ### Design description
    
    ### Data

    ### Original results
    <<Your description here, in Markdown>>
    """
    )
    # st.image("<<path to image from project's root, if needed>>") # uncomment this line if you would like to add an image

with tab2:

    st.markdown("""
    ### Proposed extension

### Causal Tree
* Why this method fits: This methods allows us to find possible heterogeneous effects among covariate groups. The group selection isn’t done arbitrarily, but rather based on how much belonging in a specific group explains the outcome’s variance. 
* Hypothesis when using Causal Machine Learning Method: We think age will be the first variable of the regression tree.
### Double Lasso
* Having established the heterogeneities to be studied, we’ll estimate the interaction’s coefficient using partitioned regression (FWL) by using double lasso.
* Why this method fits: This method should allow us to reduce the point estimate’s standard error. This increases the chances of rejecting the null hypothesis on non-significance.
* Hypothesis when using Causal Machine Learning Method: We think that by doing double lasso we can find heterogeneous effects.
    
    
    """
    )
    # st.image("<<path to image from project's root, if needed>>") # uncomment this line if you would like to add an image
    # table = pd.read_csv("<<path/to/table.csv>>") # load a table from csv to show it on the page
    # st.table(table) # show table


with tab3:

    st.markdown("""
    ### Extension Results

    <<Your description here, in Markdown>>
    """
    )
    # st.image("<<path to image from project's root, if needed>>") # uncomment this line if you would like to add an image

with tab4:

    st.markdown("""
    Wilson E, Free C, Morris TP, Syred J, Ahamed I, Menon-Johansson AS, et al. (2017) Internet-accessed sexually transmitted infection (eSTI) testing and results service: A randomised, single-blind, controlled trial. PLoS Med 14(12): e1002479. https://doi.org/10.1371/journal.pmed.1002479
    """
    )
    # st.image("<<path to image from project's root, if needed>>") # uncomment this line if you would like to add an image

