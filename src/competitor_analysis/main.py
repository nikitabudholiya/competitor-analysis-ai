from competitor_analysis.crew import CompetitorAnalysisCrew
import os


def run():
    print("\n" + "="*50)
    print("   🚀 AI Competitor Analysis Tool")
    print("   Powered by CrewAI + Groq")
    print("="*50 + "\n")

    company_name = input("🏢 Enter Company / Startup Name: ").strip()

    if not company_name:
        print("❌ Please enter a company name!")
        return

    print(f"\n⏳ Analyzing competitors for: {company_name}")
    print("This may take 1-2 minutes...\n")

    os.makedirs("output", exist_ok=True)

    inputs = {"company_name": company_name}

    CompetitorAnalysisCrew().crew().kickoff(inputs=inputs)

    print("\n" + "="*50)
    print("✅ Done!")
    print("📄 Report saved to: output/strategy_report.md")
    print("="*50 + "\n")


if __name__ == "__main__":
    run()