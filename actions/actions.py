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

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionRecommendCareer(Action):

    def name(self) -> Text:
        return "action_recommend_career"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Get the last user message
        user_message = tracker.latest_message.get('text', '').lower()

        # Simple keyword-based logic
        if any(word in user_message for word in ['tech', 'technology', 'programming', 'coding', 'software']):
            recommendation = "You seem interested in technology! Consider careers like Software Developer, Data Scientist, or IT Consultant."
        elif any(word in user_message for word in ['art', 'painting', 'drawing', 'music', 'design']):
            recommendation = "You seem interested in the arts! Consider careers like Graphic Designer, Musician, or Animator."
        elif any(word in user_message for word in ['commerce', 'business', 'finance', 'accounting', 'economics']):
            recommendation = "You seem interested in commerce! Consider careers like Accountant, Financial Analyst, or Business Manager."
        else:
            recommendation = "Tell me more about your interests so I can recommend a suitable career path!"

        dispatcher.utter_message(text=recommendation)
        return []

