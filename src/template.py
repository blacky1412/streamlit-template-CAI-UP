import streamlit as st
import pandas as pd

# I have provided most of what you need for to use streamlit here and in README.md
# You can also check the streamlit docs at https://docs.streamlit.io/get-started
# Also, you can check a simple example from class:
# Page: https://simpson-dashboard-class.streamlit.app/
# GitHub Repo: https://github.com/RodrigoGrijalba/python-dashboard-class

st.set_page_config(page_title = "<<Your page title here>>", layout = "wide")

tab1, tab2, tab3, tab4 = st.tabs(["Original Paper", "Proposed Extention", "Extension Results", "References"])

with tab1:
    st.markdown("""
### Experiment Design Description

##### Objective
The trial aimed to evaluate the effectiveness of an e-STI testing and results service (SH:24) on the uptake of STI testing and the number of STI cases diagnosed and treated.

##### Participants
- **Eligibility Criteria:**
  - Young people aged 16 to 30 years.
  - Residents of the London boroughs of Lambeth and Southwark.
  - Sexually active (at least one sexual partner in the last 12 months).
  - Willingness to take an STI test.
  - Access to the internet.
- **Exclusion Criteria:**
  - Inability to read English (the websites were only in English).
  - Inability to provide consent.

##### Recruitment
- **Timeframe:** Between 24 November 2014 and 31 August 2015.
- **Methods:**
  - Community settings such as universities, colleges, market stalls, barber shops, bars, and nightclubs.
  - Online platforms like Facebook, Twitter, and Grindr.
  - Advertisements through advocacy and health promotion groups.

##### Randomisation and Allocation
- An independent computer-based randomisation program allocated participants to either the intervention or control group.
- **Randomisation Method:** Minimisation algorithm balancing for gender, age, number of sexual partners in the last 12 months, and sexual orientation.
- Participants received an automated SMS text message with the URL of the allocated STI service.

##### Intervention and Control
- **Intervention Group:** Received access to the SH:24 e-STI testing and results service, which included postal self-sampling test kits for chlamydia, gonorrhoea, HIV, and syphilis; results delivered via text message or telephone; and web-based safer sex health information.
- **Control Group:** Received access to usual STI testing services.

##### Blinding
- Laboratory staff and researchers assessing outcomes were blinded to the treatment allocation.

##### Data Collection
- **Baseline Data:** Collected through face-to-face interactions or entered by participants on the trial website.
- **Follow-up Data:** Self-reported data collected by post or directly entered on a website, incentivised with monetary rewards.
- **Objective Measures:** Searched SH:24 database and hospital patient records for STI testing, diagnosis, and treatment data.

##### Sample Size and Statistical Analysis
- **Sample Size:** 3,000 participants.
- **Power:** 90% power to detect a relative risk (RR) of 3.5 for STI diagnosis and 99% power to detect an absolute difference of 25% in the proportion of participants who completed a test.
- **Analysis Method:** Intention to treat basis, using Stata version 14.2, with effect measures as RRs with 95% confidence intervals and time to outcomes.

### Data
Description of Data: The data includes participants aged 16 to 30, residing in London boroughs of Lambeth and Southwark, who are sexually active, have internet access, and are willing to take an STI test.
* Unit of Observation: The units of observation are at the individual level
* Experiment or Quasi-experiment: An RCT experimental design is followed.

### Original results

- **Result 1:** Increase in self-report STI testing by 23.4*** (control group mean = 26.6%)
- **Result 2:** Increase in STI diagnosis by 1.4*(control group mean = 1.4%)
- **Result 3:** Treated units tested for STI 7.7*** days sooner on average (control groupmean = 36.5)
- **Results 4:** No signifcant heterogeneous effects were found.

    
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
    ### Causal Forest Results

  
    """
    )
    st.image("src/causalforest.png") # uncomment this line if you would like to add an image
    table = pd.read_csv("src/het_doublelasso.csv") # load a table from csv to show it on the page
    st.table(table) # show table

    st.markdown(""" ### Double Lasso Results """)
    
    table = pd.read_csv("src/ate_doublelasso.csv") # load a table from csv to show it on the page
    st.table(table) # show table
    st.markdown(""" ### Generalize Random Forest Results """)

with tab4:

    st.markdown("""
    Wilson E, Free C, Morris TP, Syred J, Ahamed I, Menon-Johansson AS, et al. (2017) Internet-accessed sexually transmitted infection (eSTI) testing and results service: A randomised, single-blind, controlled trial. PLoS Med 14(12): e1002479. https://doi.org/10.1371/journal.pmed.1002479
    """
    )
    # st.image("<<path to image from project's root, if needed>>") # uncomment this line if you would like to add an image

