from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

from trend_hunter_crewai.llm_config import llm


@CrewBase
class TrendHunterApp:
    """Trend Hunter Crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def search_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["search_agent"],
            llm=llm,
            verbose=True,
        )

    @agent
    def analysis_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["analysis_agent"],
            llm=llm,
            verbose=True,
        )

    @agent
    def report_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["report_agent"],
            llm=llm,
            verbose=True,
        )

    @task
    def search_task(self) -> Task:
        return Task(
            config=self.tasks_config["search_task"],
        )

    @task
    def analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config["analysis_task"],
        )

    @task
    def report_task(self) -> Task:
        return Task(
            config=self.tasks_config["report_task"],
            output_file="trend_report.md",
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
