# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionRecommendCareer(Action):
    def name(self):
        return "action_recommend_career"

    def run(self, dispatcher, tracker, domain):
        main_interest = tracker.get_slot('main_interest')
        if main_interest:
            if "tech" in main_interest or "technology" in main_interest or "coding" in main_interest:
                response = "Great! Are you more interested in software development, data science, or cybersecurity?"
            elif "art" in main_interest or "arts" in main_interest or "music" in main_interest:
                response = "Wonderful! Are you more interested in visual arts, performing arts, or writing?"
            elif "commerce" in main_interest or "business" in main_interest or "finance" in main_interest:
                response = "Awesome! Would you like to know more about business management, finance, or marketing?"
            else:
                response = "That's interesting! Could you tell me more about what you enjoy?"
        else:
            response = "I'm here to help you find a career path! Could you tell me more about your interests or what you enjoy doing?"

        dispatcher.utter_message(text=response)
        return []




