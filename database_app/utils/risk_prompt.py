# risk_prompt.py

def generate_risk_factor_prompt(company: str, year: str, text: str) -> str:
    return f"""
You are a professional analyst reviewing SEC 10-K reports.

Below is the full text of **Item 1A: Risk Factors** from {company}'s {year} 10-K filing.

Your task:
1. Identify and summarize the major categories of risk (e.g., supply chain, regulation, AI, competition, geopolitical, ESG).
2. Highlight any particularly vague, forward-looking, or frequently repeated risk statements.
3. Comment on the tone and completeness of the risk disclosures.
4. Provide a concise bullet-point summary in Markdown format.

### Risk Analysis Summary for {company} ({year})

**📂 Risk Categories**
- ...

**⚠️ Vague or Repetitive Statements**
- ...

**🧠 Tone and Style**
- ...

**🔍 Key Observations**
- ...
"""
