import streamlit as st
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from competitor_analysis.crew import CompetitorAnalysisCrew

# ---- Page Config ----
st.set_page_config(
    page_title="AI Competitor Analysis Tool",
    page_icon="🚀",
    layout="wide"
)

# ---- Custom CSS ----
st.markdown("""
    <style>
    .main-header {
        text-align: center;
        padding: 20px;
    }
    .stButton > button {
        background-color: #FF4B4B;
        color: white;
        font-size: 18px;
        font-weight: bold;
        border-radius: 10px;
        padding: 12px;
    }
    .stDownloadButton > button {
        background-color: #0083B8;
        color: white;
        font-weight: bold;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# ---- Header ----
st.markdown("""
    <div class='main-header'>
        <h1>🚀 AI Competitor Analysis Tool</h1>
        <p style='font-size:18px; color:gray;'>
            Powered by CrewAI + Groq + Llama 3.3 70B
        </p>
        <p style='font-size:15px;'>
            Enter any company name and get a full 
            professional competitor analysis report in minutes!
        </p>
    </div>
""", unsafe_allow_html=True)

st.divider()

# ---- Input Section ----
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    company_name = st.text_input(
        "🏢 Company / Startup Name",
        placeholder="e.g. Nexus Cognitive Technologies",
    )
    analyze_btn = st.button(
        "🔍 Analyze Competitors",
        use_container_width=True,
        type="primary"
    )

st.divider()

# ---- Analysis ----
if analyze_btn:
    if not company_name.strip():
        st.warning("⚠️ Please enter a company name!")

    else:
        os.makedirs("output", exist_ok=True)

        # ---- Progress ----
        st.markdown(f"### ⏳ Analyzing: **{company_name}**")
        st.markdown("*This may take 1-2 minutes. Please wait...*")

        progress_bar = st.progress(0)

        col1, col2, col3 = st.columns(3)

        with col1:
            agent1 = st.status(
                "🤖 Agent 1 — Finding Competitors",
                expanded=False
            )
        with col2:
            agent2 = st.status(
                "📊 Agent 2 — Analyzing Strengths & Weaknesses",
                expanded=False
            )
        with col3:
            agent3 = st.status(
                "🎯 Agent 3 — Building Strategy Report",
                expanded=False
            )

        try:
            # Update Agent 1 status
            agent1.update(
                label="🤖 Agent 1 — Finding Competitors...",
                state="running"
            )
            progress_bar.progress(10)

            inputs = {"company_name": company_name.strip()}
            
            # Run the crew
            CompetitorAnalysisCrew().crew().kickoff(inputs=inputs)

            # Update all statuses on completion
            agent1.update(
                label="✅ Agent 1 — Competitors Found!",
                state="complete"
            )
            progress_bar.progress(50)

            agent2.update(
                label="✅ Agent 2 — Analysis Complete!",
                state="complete"
            )
            progress_bar.progress(80)

            agent3.update(
                label="✅ Agent 3 — Report Ready!",
                state="complete"
            )
            progress_bar.progress(100)

        except Exception as e:
            agent1.update(label="❌ Error occurred", state="error")
            st.error(f"Something went wrong: {e}")
            st.stop()

        # ---- Display Report ----
        report_path = "output/strategy_report.md"

        if os.path.exists(report_path):
            with open(report_path, "r") as f:
                report = f.read()

            st.divider()
            st.success("✅ Analysis Complete!")

            # ---- Metrics ----
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("🏢 Company Analyzed", company_name)
            col2.metric("🔍 Competitors Found", "5")
            col3.metric("📊 Sections in Report", "10")
            col4.metric("🎯 Strategies Generated", "3")

            st.divider()

            # ---- Full Report ----
            st.markdown("## 📄 Full Competitor Analysis Report")
            st.markdown(report)

            st.divider()

            # ---- Download Buttons ----
            st.markdown("### 📥 Download Your Report")
            col1, col2 = st.columns(2)

            with col1:
                st.download_button(
                    label="📥 Download as Markdown (.md)",
                    data=report,
                    file_name=f"{company_name}_competitor_analysis.md",
                    mime="text/markdown",
                    use_container_width=True
                )
            with col2:
                st.download_button(
                    label="📥 Download as Text (.txt)",
                    data=report,
                    file_name=f"{company_name}_competitor_analysis.txt",
                    mime="text/plain",
                    use_container_width=True
                )

        else:
            st.error("❌ Report file not found. Something went wrong!")

# ---- Footer ----
st.divider()
st.markdown("""
    <div style='text-align: center; color: gray;'>
        <p>Built with ❤️ using CrewAI + Groq + Streamlit</p>

    </div>
""", unsafe_allow_html=True)