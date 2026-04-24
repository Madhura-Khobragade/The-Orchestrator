import streamlit as st
import ollama
from orchestrator import app # Ensure your file is named orchestrator.py

st.set_page_config(page_title="Sovereign AI", layout="wide")

st.title("🛡️ Sovereign AI Orchestrator")

with st.sidebar:
    st.header("📊 PM Strategy")
    st.info("RICE Score: 21.6")
    st.divider()
    st.header("🗺️ Roadmap")
    st.checkbox("Phase 1 & 2: Local Agents", value=True)
    st.checkbox("Phase 3: XAI", value=True)

user_input = st.text_area("Data for Analysis:", "Customer: Madhura. Transaction: €5200.")

# Use a container to make sure things show up in order
result_container = st.container()

if st.button("Run Sovereign Analysis"):
    with st.spinner("Local LLM is thinking..."):
        try:
            # Execute the Graph
            final_result = app.invoke({"raw_data": user_input})
            
            with result_container:
                st.divider()
                st.subheader("Analysis Results")
                
                t1, t2 = st.tabs(["🛡️ Privacy Output", "🔍 XAI Transparency"])
                
                with t1:
                    st.success(final_result.get('sanitized_output', 'No data'))
                with t2:
                    st.info(final_result.get('xai_report', 'No explanation'))
                
                # The Download Button
                report = f"Output:\n{final_result.get('sanitized_output')}\n\nXAI:\n{final_result.get('xai_report')}"
                st.download_button("📥 Download Report", data=report, file_name="ai_audit.txt")
                
        except Exception as e:
            st.error(f"Error connecting to Ollama: {e}")
            st.warning("Make sure you ran 'ollama serve' in your terminal!")

st.divider()
st.caption("Processing locally via Llama 3.2 on Ollama")