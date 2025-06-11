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
        # Retrieve and normalize the main_interest slot
        main_interest = tracker.get_slot('main_interest')
        response = ""

        if main_interest:
            main_interest = main_interest.strip().lower()
            # Tech branch
            if any(keyword in main_interest for keyword in ["tech", "technology", "coding", "programming", "software", "computer"]):
                response = (
                    "Great! Are you more interested in software development, data science, or cybersecurity?"
                )
            # Arts branch
            elif any(keyword in main_interest for keyword in ["art", "arts", "music", "painting", "drawing", "creative", "design", "theater"]):
                response = (
                    "Wonderful! Are you more interested in visual arts, performing arts, or writing?"
                )
            # Commerce branch
            elif any(keyword in main_interest for keyword in ["commerce", "business", "finance", "accounting", "economics", "marketing"]):
                response = (
                    "Awesome! Would you like to know more about business management, finance, or marketing?"
                )
            # Fallback for unrecognized interests
            else:
                response = (
                    "That's interesting! Could you tell me a bit more about what you enjoy or your favorite subjects?"
                )
        else:
            # If the slot isn't set, ask for user interests
            response = (
                "I'm here to help you find a career path! Could you tell me more about your interests or what you enjoy doing?"
            )

        dispatcher.utter_message(text=response)
        return []





