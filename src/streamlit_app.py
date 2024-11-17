import streamlit as st
import service as ser
import constants as const
import os
import sys

# Ensure the path is set correctly for module imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Sidebar option for choosing the mode
check = st.sidebar.radio("Select Mode", ["Chat", "User Train"])

if check == "Chat":
    st.title("Ask anything about Devi")

    st.warning("I am still under training, so don't expect a good response.")

    # Input field for the user prompt
    prompt = st.text_input("Enter your Prompt", placeholder="Enter your Prompt")

    # Button to submit the prompt
    if st.button("Submit"):
        st.write("User: " + str(prompt))

        # Get the output from the service and display it
        out_put = ser.get_output(prompt)
        st.write("AI: " + str(out_put))

if check == "User Train":
    # Create two tabs: "Train" and "Test"
    train_tab, test_tab = st.tabs(["Train", "Test"])

    # Content for the "Train" tab
    with train_tab:
        st.header("Train Model")
        prompt = st.text_input("Tell About Devi You Know", placeholder="Tell About Devi You Know..")
        if st.button("Submit Training Data"):
            ser.add_content_user(prompt)
            st.success("Data saved!")

    # Content for the "Test" tab
    with test_tab:
        st.header("Test Model")
        test_prompt = st.text_input("Test the Model", placeholder="Enter your Prompt")
        if st.button("Submit Test Query"):
            st.write("User: " + str(test_prompt))

            # Get the output from the service and display it
            out_put = ser.get_output_user(test_prompt)
            st.write("AI: " + str(out_put))

