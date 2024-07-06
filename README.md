# Streamlit Template

This repository holds the template you can use to create the streamlit dashboard for your project. To use it, fork the repository and the clone the fork into your machine, and fill out the template in `src/template.py`. For more information on streamlit, you can read [the docs](https://docs.streamlit.io/get-started). You can also check the [example from class](https://simpson-dashboard-class.streamlit.app/) and its [code](https://github.com/RodrigoGrijalba/python-dashboard-class).
## Run locally

If you would like to make your presentation from a localy hosted page

1. (Optional) Create an environment
2. Make sure to have streamlit installed

```shell
pip install streamlit
```

3. Run streamlit from the root directory

```shell
streamlit run src/template.py
```

A browser tab should automatically open. If not, click on the `Local URL`

## Deploy on Streamlit Cloud

1. You will need to create a [Streamlit Cloud](share.streamlit.io) account.
2. Once created, go to **Create app**.
3. Select the option for deploying an app from a pre-existing repo
4. Select your repo, the branch, and the path for the file you will be running
5. After a few minutes, the app should deploy 
