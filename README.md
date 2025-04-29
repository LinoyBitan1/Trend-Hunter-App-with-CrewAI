# TrendHunterCrewai Crew

An AI-powered application that autonomously hunts trending topics, analyzes the information,
and generates concise reports — all driven by CrewAI agents and a custom vLLM model hosted on OpenShift AI.

## Table of Contents

- Installation and Setup
- Connecting to the Hosted Model
- Designing Agents and Tasks
- Running the Application

## Installation and Setup

Install the required packages:

```bash
pip install crewai crewai-tools
```

Or with [uv](https://github.com/astral-sh/uv):

```bash
uv tool install crewai
```

For more information, check the [official CrewAI installation guide](https://docs.crewai.com/installation).

## Connecting to the Hosted Model

Make sure your model is deployed on OpenShift AI. Then, configure the following environment variables in a `.env` file:

```env
OPENAI_API_BASE=https://<your-model-endpoint>/v1
OPENAI_API_KEY=EMPTY  # Or your authentication token
```

Initialize the LLM:

```python
from crewai import LLM
import os

llm = LLM(
    model="openai/my-vlllm2",
    openai_api_base=os.getenv("OPENAI_API_BASE"),
    api_key=os.getenv("OPENAI_API_KEY")
)
```

Or using LangChain:

```python
from langchain_community.llms import VLLMOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = VLLMOpenAI(
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    openai_api_base=os.getenv("OPENAI_API_BASE"),
    model="openai/my-vlllm2",
    temperature=0,
)
```

> Make sure the `model` name matches the one you created inside OpenShift AI.

## Designing Agents and Tasks

The application is built using three agents:

- **SearchAgent**: Searches for the latest articles about a given trend.
- **AnalysisAgent**: Analyzes and ranks articles by relevance and popularity.
- **ReportAgent**: Summarizes the analysis into a trend report.

Agent and task configurations are defined in YAML files:

- `config/agents.yaml`
- `config/tasks.yaml`

## Running the Application - CLI mode

Run the app with:

```bash
crewai run
```

You will be prompted to enter a trend topic.  
The app will:

1. Search for related articles.
2. Analyze and rank them.
3. Generate a summarized trend report (`trend_report.md`).

## Running the Application - UI

To run the interactive UI version using Panel:

$ PYTHONPATH=src panel serve src/trend_hunter_crewai/app_ui.py --autoreload --port 5006

Once the UI loads in your browser, you'll be greeted by a chatbot interface.

1. You can enter a trend topic
2. The system will run all agents (Search, Analysis, Report).
3. Display each agent’s response in the chat.
4. Output the final trend report.
5. Prompt you to enter a new topic.
