import streamlit as st
from agent import handle_customer_message
from memory import recall

st.set_page_config(
    page_title="RecallDesk",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 RecallDesk")
st.caption("Persistent Support & Incident Intelligence")

st.divider()

col1, col2 = st.columns(2)

# =========================
# CUSTOMER INPUT
# =========================

with col1:
    st.subheader("Customer")

    customer_name = st.text_input(
        "Customer name",
        value="Sarah Mitchell"
    )

    message = st.text_area(
        "Customer message",
        value="Hi, I'm still having the dashboard freezing problem.",
        height=150
    )

    if st.button("Send to RecallDesk", type="primary"):

        full_query = f"""
Customer: {customer_name}

Message:
{message}
"""

        # Retrieve customer history
        with st.spinner("Searching customer history..."):
            memories = recall(full_query)

        st.session_state["memories"] = memories

        # Generate AI response
        with st.spinner("Generating response..."):
            response = handle_customer_message(
                customer_name,
                message
            )

        st.session_state["response"] = response


# =========================
# RETRIEVED MEMORY
# =========================

with col2:
    st.subheader("🧠 Retrieved Memory")
    st.caption("Relevant previous interactions retrieved from Hindsight")

    if "memories" in st.session_state:

        if st.session_state["memories"]:

            # Show only the first 4 relevant memories
            for memory in st.session_state["memories"][:4]:
                st.info(str(memory))

        else:
            st.warning("No previous memories found.")

    else:
        st.caption("Send a message to retrieve customer history.")


# =========================
# AI RESPONSE
# =========================

st.divider()

st.subheader("🤖 RecallDesk Response")

if "response" in st.session_state:
    st.write(st.session_state["response"])
else:
    st.caption("The AI response will appear here.")