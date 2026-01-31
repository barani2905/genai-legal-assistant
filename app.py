import streamlit as st

st.title("GenAI Legal Assistant for Indian SMEs")

st.write("Upload a contract file to analyze legal risks.")

uploaded_file = st.file_uploader(
    "Upload contract (TXT format for now)",
    type=["txt"]
)

if uploaded_file is not None:
    contract_text = uploaded_file.read().decode("utf-8")

    st.subheader("📄 Contract Text")
    st.text_area("Extracted Text", contract_text, height=250)

    if st.button("Analyze Contract"):
        st.subheader("🧠 Contract Summary")
        st.write(
            "This contract has been analyzed to identify potential legal risks "
            "that may affect small and medium businesses."
        )

        st.subheader("⚠️ Risk Analysis")

        if "terminate" in contract_text.lower():
            st.error("High Risk: Termination clause detected.")
        else:
            st.success("Low Risk: No obvious termination risk found.")
