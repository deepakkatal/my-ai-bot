import streamlit as st
from groq import Groq
import base64

# 1. Page Config
st.set_page_config(page_title="Deek AI Pro", page_icon="🤖", layout="centered")

# 2. Styling
st.markdown("<h1 style='text-align: center;'>🤖 Deek AI Pro</h1>", unsafe_allow_html=True)

# 3. API Setup (Groq)
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

if "messages" not in st.session_state:
    st.session_state.messages = []

def encode_image(image_file):
    return base64.b64encode(image_file.read()).decode('utf-8')

# 4. Image Upload & Chat History
uploaded_file = st.file_uploader("Upload Image (Optional)", type=["jpg", "png", "jpeg"])

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 5. Main Chat Logic
if prompt := st.chat_input("Bhai, kuch bhi poocho..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # Model selection logic
            model = "llama-3.2-11b-vision-preview" if uploaded_file else "llama-3.3-70b-versatile"
            
            if uploaded_file:
                base64_img = encode_image(uploaded_file)
                # Correct Vision Content Structure - Line 40 Fixed!
                content =
            else:
                content = prompt

            response = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": content}]
            )
            
            ai_ans = response.choices[0].message.content
            st.markdown(ai_ans)
            st.session_state.messages.append({"role": "assistant", "content": ai_ans})
        except Exception as e:
            st.error(f"Error: {e}")
