import panel as pn
import threading
import time
from datetime import datetime
from trend_hunter_crewai.crew import (
    TrendHunterApp,
)
import trend_hunter_crewai.crew as crew_module

chat_interface = pn.chat.ChatInterface()
crew_module.chat_interface = chat_interface


pn.extension(design="material")


# Global state
user_input = None
crew_started = False


def initiate_chat(message):
    global crew_started
    crew_started = True
    try:
        inputs = {
            "topic": message,
        }
        crew = TrendHunterApp().crew()
        result = crew.kickoff(inputs=inputs)
        # Final result is optional to show again
        chat_interface.send(f"Final Result:\n{result}", user="Assistant", respond=False)
        # After the full crew finishes, send a final message
        chat_interface.send(
            "The trend analysis is complete! You can enter another topic now.",
            user="Assistant",
            respond=False,
        )
    except Exception as e:
        chat_interface.send(f"An error occurred: {e}", user="Assistant", respond=False)
    crew_started = False


def callback(contents: str, user: str, instance: pn.chat.ChatInterface):
    global crew_started
    global user_input

    if not crew_started:
        thread = threading.Thread(target=initiate_chat, args=(contents,))
        thread.start()
    else:
        user_input = contents


# Set the callback
chat_interface.callback = callback

# Welcome message
chat_interface.send(
    "👋 Welcome! I'm the Trend Hunter AI. What trend would you like me to research today?",
    user="Assistant",
    respond=False,
)

# Make it servable
chat_interface.servable()
