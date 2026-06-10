import streamlit as st
import requests

BASE_URL = (
    "https://enterprise-ai-agent-platform.braveisland-10bdffed.eastus.azurecontainerapps.io"
)

st.set_page_config(
    page_title="Enterprise AI Agent Platform",
    layout="wide"
)

st.title(
    "Enterprise AI Agent Platform"
)

# ----------------------
# Login
# ----------------------

with st.sidebar:

    st.header(
        "Authentication"
    )

    username = st.text_input(
        "Username",
        value="admin"
    )

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button(
        "Login"
    ):

        response = requests.post(
            f"{BASE_URL}/auth/login",
            json={
                "username": username,
                "password": password
            }
        )

        if response.status_code == 200:

            token = response.json()[
                "access_token"
            ]

            st.session_state[
                "token"
            ] = token

            st.success(
                "Logged in"
            )

# ----------------------
# Chat
# ----------------------

question = st.text_area(
    "Ask a question"
)

if st.button(
    "Ask AI"
):

    response = requests.post(
        f"{BASE_URL}/orchestrator/chat",
        headers={
            "Authorization":
            f"Bearer {st.session_state['token']}"
        },
        json={
            "session_id":
            "demo",
            "question":
            question
        }
    )

    result = response.json()

    st.subheader(
        "Response"
    )

    st.write(
        result["response"]
    )

# ----------------------
# Metrics
# ----------------------

st.divider()

st.subheader(
    "Platform Metrics"
)

if st.button(
    "Refresh Metrics"
):

    metrics = requests.get(
        f"{BASE_URL}/orchestrator/metrics",
        headers={
            "Authorization":
            f"Bearer {st.session_state['token']}"
        }
    ).json()

    st.json(
        metrics
    )
