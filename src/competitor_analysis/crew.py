from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List


@CrewBase
class CompetitorAnalysisCrew():
    """Competitor Analysis Crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # -------- Agents --------
    @agent
    def competitor_finder(self) -> Agent:
        return Agent(
            config=self.agents_config["competitor_finder"],
            verbose=True
        )

    @agent
    def competitor_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["competitor_analyst"],
            verbose=True
        )

    @agent
    def strategy_advisor(self) -> Agent:
        return Agent(
            config=self.agents_config["strategy_advisor"],
            verbose=True
        )

    # -------- Tasks --------
    @task
    def find_competitors_task(self) -> Task:
        return Task(
            config=self.tasks_config["find_competitors_task"]
        )

    @task
    def analyze_competitors_task(self) -> Task:
        return Task(
            config=self.tasks_config["analyze_competitors_task"],
            context=[self.find_competitors_task()]  # ✅ gets Agent 1 output
        )

    @task
    def strategy_task(self) -> Task:
        return Task(
            config=self.tasks_config["strategy_task"],
            context=[                               # ✅ gets BOTH Agent 1 & 2 output
                self.find_competitors_task(),
                self.analyze_competitors_task()
            ],
            output_file="output/strategy_report.md"
        )

    # -------- Crew --------
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )