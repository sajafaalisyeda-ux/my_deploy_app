
import streamlit as st
import pandas as pd

# -------------------------------
# PAGE CONFIGURATION
# -------------------------------
st.set_page_config(
    page_title="Streamlit Cloud Guide",
    page_icon="☁️",
    layout="wide"
)

# -------------------------------
# SIDEBAR NAVIGATION
# -------------------------------
st.sidebar.title("☁️ Streamlit Cloud")
st.sidebar.write("Complete Deployment Guide")

page = st.sidebar.radio(
    "Select Section",
    [
        "Get Started",
        "Quickstart",
        "Create Your Account",
        "Connect GitHub",
        "Explore Workspace",
        "Deploy From Template",
        "Fork and Edit App",
        "Trust and Security",
        "Deploy Your App"
    ]
)

# -------------------------------
# HOME / GET STARTED
# -------------------------------
if page == "Get Started":

    st.title("☁️ Streamlit Community Cloud")
    st.subheader("Deploy and Share Your Applications")

    st.write("""
    Streamlit Community Cloud allows you to deploy
    your Python Streamlit applications online.

    You can share your applications with other people
    using a public web link.
    """)

    st.info("First create your account and connect GitHub.")

    st.markdown(
        "[Open Streamlit Community Cloud](https://share.streamlit.io/)"
    )

# -------------------------------
# QUICKSTART
# -------------------------------
elif page == "Quickstart":

    st.title("🚀 Quickstart")

    st.write("Follow these steps to deploy your first app.")

    steps = [
        "Create a Streamlit Community Cloud account.",
        "Connect your GitHub account.",
        "Create a GitHub repository.",
        "Upload your app.py file.",
        "Open Streamlit Community Cloud.",
        "Select Create app.",
        "Choose your repository and app.py file.",
        "Click Deploy."
    ]

    for i, step in enumerate(steps, 1):
        st.write(f"**Step {i}:** {step}")

# -------------------------------
# CREATE ACCOUNT
# -------------------------------
elif page == "Create Your Account":

    st.title("👤 Create Your Account")

    st.write("""
    Create an account on Streamlit Community Cloud
    to host your applications.
    """)

    st.markdown(
        "[Create Streamlit Account](https://share.streamlit.io/)"
    )

    st.write("You can sign up using a supported account provider.")

    st.success("After signing in, explore your workspace.")

# -------------------------------
# CONNECT GITHUB
# -------------------------------
elif page == "Connect GitHub":

    st.title("🐙 Connect Your GitHub Account")

    st.write("""
    GitHub stores your application code.

    Streamlit Community Cloud reads your repository
    and uses your Python files to run your application.
    """)

    st.markdown(
        "[Open GitHub](https://github.com/)"
    )

    st.write("Steps:")

    st.write("1. Sign in to GitHub.")
    st.write("2. Create a repository.")
    st.write("3. Upload your app.py file.")
    st.write("4. Connect GitHub with Streamlit Community Cloud.")

# -------------------------------
# EXPLORE WORKSPACE
# -------------------------------
elif page == "Explore Workspace":

    st.title("🖥️ Explore Your Workspace")

    st.write("""
    Your Streamlit workspace allows you to manage
    and create your deployed applications.
    """)

    st.subheader("Workspace Features")

    col1, col2, col3 = st.columns(3)

    col1.metric("Applications", "Manage")
    col2.metric("Deployment", "Create")
    col3.metric("Repositories", "Connect")

    st.info("Use your workspace to create and manage apps.")

# -------------------------------
# DEPLOY FROM TEMPLATE
# -------------------------------
elif page == "Deploy From Template":

    st.title("📋 Deploy From a Template")

    st.write("""
    Templates provide ready-made applications.
    You can use an existing template instead of
    building everything from scratch.
    """)

    st.write("Steps:")

    st.write("1. Open the Streamlit app gallery.")
    st.write("2. Select an application template.")
    st.write("3. Fork or copy the project as instructed.")
    st.write("4. Open the project in GitHub.")
    st.write("5. Deploy it using Community Cloud.")

    st.markdown(
        "[Explore Streamlit App Gallery](https://streamlit.io/gallery)"
    )

# -------------------------------
# FORK AND EDIT PUBLIC APP
# -------------------------------
elif page == "Fork and Edit App":

    st.title("🍴 Fork and Edit a Public App")

    st.write("""
    Forking means creating your own copy of
    another person's public GitHub repository.
    """)

    st.write("Steps:")

    st.write("1. Open a public Streamlit project on GitHub.")
    st.write("2. Click Fork.")
    st.write("3. Open your copied repository.")
    st.write("4. Edit the Python code.")
    st.write("5. Commit your changes.")
    st.write("6. Deploy your copied application.")

    st.info("You can customize the application after forking.")

# -------------------------------
# TRUST AND SECURITY
# -------------------------------
elif page == "Trust and Security":

    st.title("🔐 Trust and Security")

    st.write("""
    Protect your application and sensitive information
    when deploying it online.
    """)

    st.subheader("Security Practices")

    st.write("- Never publish passwords.")
    st.write("- Never upload API keys to public repositories.")
    st.write("- Use Streamlit secrets for sensitive information.")
    st.write("- Check repository permissions.")
    st.write("- Share private information carefully.")

    st.warning("Never write passwords or secret API keys directly in public code.")

    st.subheader("Example: Access a Secret")

    st.code("""
# Add your secret through
# Streamlit Cloud app settings.

api_key = st.secrets["API_KEY"]
""", language="python")

# -------------------------------
# DEPLOY YOUR APP
# -------------------------------
elif page == "Deploy Your App":

    st.title("🚀 Deploy Your Streamlit App")

    st.write("""
    Before deploying, make sure your application
    and required libraries are available in GitHub.
    """)

    st.subheader("Required Files")

    st.code("""
my_project/
│
├── app.py
└── requirements.txt
""")

    st.subheader("requirements.txt")

    st.code("""
streamlit
pandas
""", language="text")

    st.subheader("Deployment Steps")

    st.write("1. Push your project to GitHub.")
    st.write("2. Open Streamlit Community Cloud.")
    st.write("3. Click Create app.")
    st.write("4. Select your GitHub repository.")
    st.write("5. Select the branch.")
    st.write("6. Select app.py as the main file.")
    st.write("7. Click Deploy.")

    st.success("Your app is ready for deployment!")

    st.markdown(
        "[Open Streamlit Community Cloud](https://share.streamlit.io/)"
    )

# -------------------------------
# FOOTER
# -------------------------------
st.sidebar.divider()
st.sidebar.caption("Streamlit Community Cloud Guide")
st.sidebar.caption("Learn • Build • Deploy")
