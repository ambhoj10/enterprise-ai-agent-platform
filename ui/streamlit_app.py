import streamlit as st
import requests

# --------------------------------------------------
# Configuration
# --------------------------------------------------

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

# --------------------------------------------------
# Authentication
# --------------------------------------------------

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

        try:

            response = requests.post(
                f"{BASE_URL}/auth/login",
                json={
                    "username": username.strip().lower(),
                    "password": password.strip()
                }
            )

            data = response.json()

            if "access_token" in data:

                st.session_state[
                    "token"
                ] = data[
                    "access_token"
                ]

                st.session_state[
                    "role"
                ] = data[
                    "role"
                ]

                st.session_state[
                    "username"
                ] = username.strip()

                st.success(
                    f"Logged in as {data['role']}"
                )

            else:

                st.error(
                    data.get(
                        "error",
                        "Invalid credentials"
                    )
                )

        except Exception as ex:

            st.error(
                f"Login Error: {str(ex)}"
            )

    if "role" in st.session_state:

        st.success(
            f"User: {st.session_state['username']}"
        )

        st.info(
            f"Role: {st.session_state['role']}"
        )

# --------------------------------------------------
# Chat Section
# --------------------------------------------------

st.subheader(
    "Ask Enterprise AI"
)

question = st.text_area(
    "Question"
)

if st.button(
    "Ask AI"
):

    if (
        "token"
        not in st.session_state
    ):

        st.error(
            "Please login first"
        )

        st.stop()

    try:

        response = requests.post(
            f"{BASE_URL}/orchestrator/chat",
            headers={
                "Authorization":
                f"Bearer {st.session_state['token']}"
            },
            json={
                "session_id": "demo",
                "question": question
            }
        )

        result = response.json()

        st.subheader(
            "Response"
        )

        st.write(
            result.get(
                "response",
                "No response received"
            )
        )

        with st.expander(
            "Execution Details"
        ):

            st.json(
                {
                    "plan":
                        result.get(
                            "plan"
                        ),

                    "history_count":
                        result.get(
                            "history_count"
                        ),

                    "prompt_tokens":
                        result.get(
                            "prompt_tokens"
                        ),

                    "completion_tokens":
                        result.get(
                            "completion_tokens"
                        ),

                    "total_tokens":
                        result.get(
                            "total_tokens"
                        ),

                    "estimated_cost":
                        result.get(
                            "estimated_cost"
                        )
                }
            )

    except Exception as ex:

        st.error(
            f"Chat Error: {str(ex)}"
        )

# --------------------------------------------------
# Metrics
# --------------------------------------------------

st.divider()

st.subheader(
    "Platform Metrics"
)

if st.button(
    "Refresh Metrics"
):

    if (
        "token"
        not in st.session_state
    ):

        st.error(
            "Please login first"
        )

        st.stop()

    try:

        response = requests.get(
            f"{BASE_URL}/orchestrator/metrics",
            headers={
                "Authorization":
                f"Bearer {st.session_state['token']}"
            }
        )

        if response.status_code == 200:

            st.json(
                response.json()
            )

        else:

            st.error(
                response.text
            )

    except Exception as ex:

        st.error(
            f"Metrics Error: {str(ex)}"
        )

# --------------------------------------------------
# Admin Logs
# --------------------------------------------------

st.divider()

st.subheader(
    "Execution Logs (Admin Only)"
)

if st.button(
    "View Logs"
):

    if (
        "token"
        not in st.session_state
    ):

        st.error(
            "Please login first"
        )

        st.stop()

    try:

        response = requests.get(
            f"{BASE_URL}/orchestrator/logs",
            headers={
                "Authorization":
                f"Bearer {st.session_state['token']}"
            }
        )

        if response.status_code == 200:

            st.json(
                response.json()
            )

        else:

            st.error(
                response.text
            )

    except Exception as ex:

        st.error(
            f"Logs Error: {str(ex)}"
        )
