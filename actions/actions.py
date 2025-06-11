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

import random
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionRecommendCareer(Action):
    def name(self):
        return "action_recommend_career"

    def run(self, dispatcher, tracker, domain):
        # Try to get the slot value for main_interest
        main_interest = tracker.get_slot('main_interest')
        user_message = tracker.latest_message.get('text', '').lower()

        tech_careers = [
            "Software Developer", "Data Scientist", "Cybersecurity Analyst", "AI Engineer", "Web Developer"
        ]
        arts_careers = [
            "Graphic Designer", "Musician", "Animator", "Writer", "Photographer"
        ]
        commerce_careers = [
            "Accountant", "Financial Analyst", "Business Manager", "Marketing Specialist", "Entrepreneur"
        ]

        if main_interest:
            if "tech" in main_interest or "technology" in main_interest or "coding" in main_interest:
                response = (
                    "Great! Are you more interested in software development, data science, or cybersecurity?"
                )
            elif "art" in main_interest or "arts" in main_interest or "music" in main_interest:
                response = (
                    "Wonderful! Are you more interested in visual arts, performing arts, or writing?"
                )
            elif "commerce" in main_interest or "business" in main_interest or "finance" in main_interest:
                response = (
                    "Awesome! Would you like to know more about business management, finance, or marketing?"
                )
            else:
                response = (
                    "That's interesting! Could you tell me more about what you enjoy?"
                )
        else:
            # Fallback to keyword-based detection if slot is not set
            if any(word in user_message for word in ['tech', 'technology', 'programming', 'coding', 'software', 'it', 'developer']):
                career = random.choice(tech_careers)
                response = (
                    f"It sounds like you're interested in technology! "
                    f"Have you considered becoming a {career}? "
                    "What specific areas in tech excite you most?"
                )
            elif any(word in user_message for word in ['art', 'painting', 'drawing', 'music', 'design', 'photography', 'writing', 'creative']):
                career = random.choice(arts_careers)
                response = (
                    f"Your passion for the arts is wonderful! "
                    f"Have you thought about a career as a {career}? "
                    "Are you more interested in visual arts, performing arts, or writing?"
                )
            elif any(word in user_message for word in ['commerce', 'business', 'finance', 'accounting', 'economics', 'marketing', 'entrepreneur']):
                career = random.choice(commerce_careers)
                response = (
                    f"Business and commerce offer many exciting opportunities. "
                    f"You might enjoy working as a {career}. "
                    "Would you like to know more about business management, finance, or marketing?"
                )
            else:
                response = (
                    "I'm here to help you find a career path! "
                    "Could you tell me more about your interests or what you enjoy doing?"
                )

        dispatcher.utter_message(text=response)
        return []



