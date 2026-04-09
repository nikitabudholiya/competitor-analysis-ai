# 🚀 AI Competitor Analysis Tool

<p align="center">
  <img src="https://img.shields.io/badge/Built%20With-CrewAI-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/LLM-Groq%20%7C%20Llama%203.3%2070B-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/UI-Streamlit-red?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Python-3.10%2B-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" />
</p>

<p align="center">
  <b>Enter any company or startup name and get a complete, professional competitor analysis report in minutes — powered by 3 autonomous AI agents.</b>
</p>

---

## 📸 Demo

<img width="1424" height="742" alt="Screenshot 2026-04-04 at 1 24 04 AM" src="https://github.com/user-attachments/assets/dd3bea36-bd72-4674-969b-890dbf7589c2" />

---

<img width="1448" height="782" alt="Screenshot 2026-04-04 at 1 27 09 AM" src="https://github.com/user-attachments/assets/52bdac4c-46bb-4636-b0a9-84b8ad42ff08" />



---

## 💡 What It Does

Most founders and analysts spend **days** manually researching competitors. This tool does it in **minutes**.

Enter any company name and 3 AI agents will automatically:

- 🔍 **Find** the top 5 real competitors with full details
- 💪 **Analyze** your company's own strengths, weaknesses, opportunities & threats (SWOT)
- ⚔️ **Break down** each competitor's strengths, weaknesses, and gaps
- 📈 **Research** market size, growth rate, TAM & 2025-2026 industry trends
- 🎯 **Generate** unique strategies to beat competitors
- 📊 **Build** a full comparison table
- 📄 **Deliver** a downloadable professional report

---

## 🤖 Multi-Agent Workflow

```
You enter Company Name
        ↓
🤖 Agent 1 — Market Research Specialist
   → Finds top 5 real competitors
   → Website, pricing, features, funding, market presence
        ↓
📊 Agent 2 — Senior Business Analyst
   → SWOT analysis of YOUR company
   → Deep strengths & weaknesses of each competitor
   → Market size, TAM, growth rate, industry trends
        ↓
🎯 Agent 3 — Chief Strategy Advisor
   → Combines all research into ONE complete report
   → Market gap analysis
   → Unique Value Proposition
   → 3 actionable strategies to beat competitors
   → Risk assessment
   → Competitor comparison table
        ↓
📄 Output → Beautiful downloadable strategy_report.md
```

---

## 📄 Report Sections

Every generated report includes:

| Section | Description |
|---|---|
| 📌 Executive Summary | Overview of company and competitive landscape |
| 📈 Market Overview | TAM, growth rate, trends, profitability |
| 💪 SWOT Analysis | Strengths, weaknesses, opportunities, threats of YOUR company |
| 🏢 Top 5 Competitors | Full details — website, pricing, features, funding |
| ⚔️ Competitor Analysis | Strengths, weaknesses, gaps for each competitor |
| 🎯 Market Gap Analysis | What nobody in the market is solving |
| 💡 Unique Value Proposition | Recommended UVP for your company |
| 🚀 3 Winning Strategies | Actionable differentiation strategies |
| ⚠️ Risks & Solutions | Top risks with mitigation plans |
| 📊 Comparison Table | Side-by-side feature comparison |
| ✅ Conclusion | Final strategic summary |

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| [CrewAI](https://crewai.com) | Multi-agent orchestration framework |
| [Groq](https://groq.com) | Free ultra-fast LLM API |
| [Llama 3.3 70B](https://groq.com) | Underlying language model |
| [Streamlit](https://streamlit.io) | Interactive web UI |
| Python 3.10+ | Core language |

---

## 📁 Project Structure

```
competitor-analysis-ai/
├── src/
│   └── competitor_analysis/
│       ├── crew.py          # CrewAI agents & tasks setup
│       ├── main.py          # CLI entry point
│       └── __init__.py
├── config/
│   ├── agents.yaml          # Agent roles, goals & backstories
│   └── tasks.yaml           # Task descriptions & expected outputs
├── output/
│   └── strategy_report.md   # Generated report saved here
├── app.py                   # Streamlit UI
├── .env.example             # Environment variable template
├── .gitignore
├── pyproject.toml
└── README.md
```

---

## ⚡ Quick Start

### Prerequisites
- Python 3.10+
- Free [Groq API Key](https://console.groq.com) — no credit card needed

### 1. Clone the repository
```bash
git clone https://github.com/nikitabudholiya/competitor-analysis-ai.git
cd competitor-analysis-ai
```

### 2. Create virtual environment
```bash
python -m venv .venv
source .venv/bin/activate        # Mac/Linux
.venv\Scripts\activate           # Windows
```

### 3. Install dependencies
```bash
pip install crewai streamlit groq python-dotenv
uv add "crewai[google-genai]"
```

### 4. Set up environment variables
```bash
cp .env.example .env
```
Open `.env` and add your free Groq API key:
```dotenv
MODEL=groq/llama-3.3-70b-versatile
GROQ_API_KEY=your_groq_api_key_here
```

### 5. Run the Streamlit UI
```bash
streamlit run app.py
```

Opens at `http://localhost:8501` 🎉

### Or run via CLI
```bash
crewai run
```

---

## 🔑 Getting Your Free Groq API Key

1. Go to [console.groq.com](https://console.groq.com)
2. Sign up with Google or email — **completely free**
3. Click **API Keys** → **Create API Key**
4. Copy and paste into your `.env` file

---

## 📊 Example Output

```
Company Analyzed  →  Amazon
Competitors Found →  5
Report Sections   →  11
Strategies        →  3
Download Formats  →  .md / .txt
```

---

## 🙋‍♀️ Author

**Nikita Budholiya**
Data & AI Engineer @ [Nexus Cognitive Technologies](https://www.nexuscognitive.com)

<p>
  <a href="https://linkedin.com/in/nikitabudholiya">
    <img src="https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat&logo=linkedin" />
  </a>
  <a href="https://github.com/nikitabudholiya">
    <img src="https://img.shields.io/badge/GitHub-Follow-black?style=flat&logo=github" />
  </a>
</p>

---

## 📝 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## ⭐ Support

If you found this useful, please consider giving it a **star** ⭐ — it helps others discover the project!

---

<p align="center">
  Built with ❤️ using CrewAI + Groq + Streamlit
</p>
