import google.generativeai as genai
import streamlit as st

# Configure API Key
GEMINI_API_KEY = "AIzaSyAQuoS-si0fCcdmcpdP5dSlQ0H8KhB1HhM"
genai.configure(api_key=GEMINI_API_KEY)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Streamlit UI
st.title("🤖 Chatbot with Gemini AI")
st.write("Ask me anything!")

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if query := st.chat_input("Type your message here..."):
    # Display user message
    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.markdown(query)
    
    # Generate AI response
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(query)
    ai_response = response.text
    
    # Display AI response
    st.session_state.messages.append({"role": "assistant", "content": ai_response})
    with st.chat_message("assistant"):
        st.markdown(ai_response)
