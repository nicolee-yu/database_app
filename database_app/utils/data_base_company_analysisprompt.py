# prompt_generator.py

def generate_risk_factor_prompt(company: str, year1: str, risk_text1: str, year2: str, risk_text2: str) -> str:
    return f"""
You are an SEC filing analyst. Below are two versions of the "Item 1A: Risk Factors" section from the 10-K filings of {company}, one from {year1} and one from {year2}.

Your task:
1. Identify risks that are newly added, removed, or reworded between the two reports.
2. Categorize each risk into a theme such as supply chain, geopolitical, regulation, ESG, AI, etc.
3. Detect vague language or changes in tone.
4. Return a Markdown summary with structured bullet points.

### Risk Factors Evolution: {company} ({year1} → {year2})

**🆕 Newly Added Risks**
- ...

**❌ Removed Risks**
- ...

**✏️ Rephrased Risks**
- ...

**📂 Risk Categories**
- Supply Chain: ...
- Regulation: ...
- AI: ...
- ESG: ...

**Tone & Language Observations**
- ...
"""
