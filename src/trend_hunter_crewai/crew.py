import os
from dotenv import load_dotenv

load_dotenv()
from langtrace_python_sdk import langtrace

langtrace.init(api_key=os.getenv("LANGTRACE_KEY"))

from crewai import Agent, Crew, Process, Task, TaskOutput
from crewai.project import CrewBase, agent, crew, task

from trend_hunter_crewai.llm_config import llm

from crewai_tools import SerperDevTool, WebsiteSearchTool

chat_interface = None

search_tool = SerperDevTool()
web_rag_tool = WebsiteSearchTool()


# This function will be called after every task finishes
def print_output(output: TaskOutput):
    if chat_interface:
        message = output.raw  # get raw text
        chat_interface.send(message, user=output.agent, respond=False)


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
            tools=[search_tool, web_rag_tool],
            allow_self_reflection=True,
            max_iterations=5,
        )

    @agent
    def analysis_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["analysis_agent"],
            llm=llm,
            verbose=True,
            max_iterations=5,
        )

    @agent
    def report_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["report_agent"],
            llm=llm,
            verbose=True,
            max_iterations=5,
        )

    @task
    def search_task(self) -> Task:
        return Task(
            config=self.tasks_config["search_task"],
            callback=print_output,
            tools=[search_tool, web_rag_tool],
        )

    @task
    def analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config["analysis_task"],
            callback=print_output,
        )

    @task
    def report_task(self) -> Task:
        return Task(
            config=self.tasks_config["report_task"],
            output_file="trend_report.md",
            callback=print_output,
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
