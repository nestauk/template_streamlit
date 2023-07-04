import streamlit as st
from PIL import Image
import altair as alt

# this is what allows for the option menu along the sidebar
from streamlit_option_menu import option_menu

# until nesta_ds_utils is hosted on pypi we won't be able to use it for apps hosted on streamlit cloud
# once that's the case, we should replace this with nesta_ds_utils altair formatting function
from utils.formatting import *

alt.themes.register("nestafont", nestafont)
alt.themes.enable("nestafont")
colours = NESTA_COLOURS

# INSERT THE TITLE OF YOUR APP HERE
APP_TITLE = "SAMPLE STREAMLIT APP"


# icon to be used as the favicon on the browser tab
im = Image.open("images/favicon.ico")

# sets page configuration with favicon and title specified on line 4
st.set_page_config(page_title=APP_TITLE, layout="wide", page_icon=im)


def app(app_title: str):
    """
    THIS IS A TEMPLATE APP TO GET YOU STARTED WITH BUILDING STREAMLIT APPS
    """
    header = st.container()
    with header:
        # nesta logo
        nesta_logo = Image.open(f"images/nesta_logo.png")

        # set title of app to be title specified
        st.title(app_title)
        col1, col2 = st.columns([1, 10])
        with col1:
            # add nesta logo on left side
            st.image(nesta_logo, width=None)
        with col2:
            # add nesta website next to logo
            st.markdown("           **website:** https://www.nesta.org/")
        # Indicate that this dashboard is still a draft. Remove once final.
        st.markdown(
            "**This dashboard is a under active development and plots and metrics should not be interpreted as final**"
        )

    # this creates a sidebar on the left of the app with the option menu
    with st.sidebar:
        choose = option_menu(
            app_title,
            [
                "PAGE_TITLE1",
                "PAGE_TITLE2",  # replace with your desired page title names
            ],
            icons=[
                "bookmark-star",
                "bookmark-star",  # bookmarks can be any icons available from https://icons.getbootstrap.com/
            ],
            default_index=0,
            orientation="vertical",
            styles={
                "container": {
                    "background-color": NESTA_COLOURS[12],
                },
                "icon": {"color": NESTA_COLOURS[10], "font-size": "25px"},
                "nav-link": {
                    "font-size": "16px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#eee",
                },
                "nav-link-selected": {"background-color": NESTA_COLOURS[0]},
            },
        )
    # This is where you will put the content on each of your tabs
    if choose == "PAGE_TITLE1":
        p1_tab1, p1_tab2 = st.tabs(["PAGE1_HOME", "About the Data"])
        with p1_tab1:
            st.markdown("**Use this tab as a homepage for your first module**")
            st.markdown("Add as many tabs as you would like to this module")
        with p1_tab2:
            st.markdown(
                "**Use this tab to describe the datasets relevant to this module**"
            )
            st.markdown(
                "Depending on your tool, it may make sense to have a single about the data tab on your option menu, if you don't have separate datasets for each module."
            )
    elif choose == "PAGE_TITLE2":
        p2_tab1, p2_tab2 = st.tabs(["PAGE2_HOME", "About the Data"])
        with p2_tab1:
            st.markdown("**Use this tab as a homepage for your second module**")
            st.markdown("Add as many tabs as you would like to this module")
        with p2_tab2:
            st.markdown(
                "**Use this tab to describe the datasets relevant to this module**"
            )
            st.markdown(
                "Depending on your tool, it may make sense to have a single about the data tab on your option menu, if you don't have separate datasets for each module."
            )


# THIS SECTION ADDS PASSWORD PROTECTION TO YOUR APP
# It requires that you have a folder called .streamlit located at the same level in your file structure as your app
# within that folder you must have a file called secrets.toml
# Note: we have pushed this file to the template folder for an example, but you should put it in the .gitignore of your repo so as not to push the password to github


# note: if you do not want password protection, you can delete the check_password() function definition and the associated if statement
# all you will need is a single line that calls your function (i.e. app(APP_TITLE))
def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store password
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show input for password.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 Password incorrect")
        return False
    else:
        # Password correct.

        return True


if check_password():
    app(APP_TITLE)
