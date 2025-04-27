#!/usr/bin/env python

import warnings
from datetime import datetime

from trend_hunter_crewai.crew import TrendHunterApp

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """Run the Trend Hunter crew."""
    print("Starting Trend Hunter App with OpenShift vLLM backend...\n")
    print("## Welcome to the Trend Hunter!")
    print("--------------------------------------")

    topic = input("Enter the trend you want to track:\n")
    inputs = {
        "topic": topic,
        "current_year": str(datetime.now().year),
    }

    try:
        TrendHunterApp().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


if __name__ == "__main__":
    run()
