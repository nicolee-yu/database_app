# streamlit_app.py

import streamlit as st
from utils.sec_get import find_10k_filing_url
from utils.sec_get import extract_item_1a_text

# 模拟 GPT 分析输出
def simulate_analysis_output(company, year):
    return f"""
### Risk Analysis Summary for {company} ({year})

**📂 Risk Categories**
- Supply Chain
- Regulatory
- AI
- ESG

**⚠️ Vague or Repetitive Statements**
- Several clauses include "could materially affect..."

**🧠 Tone and Style**
- Legalistic with forward-looking language

**🔍 Key Observations**
- Focus on macroeconomic trends and cyber threats.
"""

st.title("🛡️ 10-K Risk Analyzer (Item 1A)")

company = st.text_input("Company Ticker", value="AAPL")
year = st.text_input("Filing Year", value="2023")

if st.button("Analyze Risk"):
    with st.spinner("Searching 10-K filing..."):
        url = find_10k_filing_url(company, year)
        st.markdown(f"📄 **Filing URL**: [Open Filing]({url})")

        if url.startswith("http"):
            text = extract_item_1a_text(url)
            if "❌" in text or len(text) < 100:
                st.error("Failed to extract Item 1A.")
                st.text(text)
            else:
                st.success("✅ Extracted Item 1A successfully.")
                st.markdown("### 🧠 Simulated GPT Analysis")
                st.markdown(simulate_analysis_output(company, year))
        else:
            st.error(url)