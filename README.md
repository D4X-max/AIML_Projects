## AI Career Counsellor Chatbot
# Project Overview
This project is an AI-powered career counsellor chatbot built using Rasa and Streamlit. It guides users through a conversational flow to discover suitable career paths based on their interests in technology, arts, commerce, and more.

Features and Implementation Steps
Intent Creation and NLU Training

Created intents for major career domains such as tech, arts, and commerce.

Added detailed intents for sub-areas like software development, data science, cybersecurity, visual arts, performing arts, and commerce specializations.

Used NLU examples to train the model for accurate intent classification.

Text Preprocessing

Utilized NLTK for preprocessing user input to improve intent recognition and handle variations.

Rasa Chatbot Training

Developed stories and rules to manage multi-turn conversations.

Implemented slot filling to remember user preferences and personalize recommendations.

Added custom actions for dynamic career recommendations based on user input.

Career Recommendation Logic

Designed logic to recommend careers based on keywords and slot values.

Included detailed explanations for specific roles when users ask for more information.

Frontend Development with Streamlit

Created a modern, chat-like UI using Streamlit.

Implemented session state to maintain conversation history.

Styled messages to resemble phone text conversations for better user experience.

Testing and Debugging

Tested the chatbot extensively with real user inputs.

Debugged intent recognition and conversation flow issues.

Enhanced NLU data and stories to handle topic switching and fallback scenarios.

Deployment

Prepared the chatbot for deployment via Streamlit Cloud for easy access.

How to Run the Project
Train the Rasa model:

bash
rasa train
Run the Rasa server:

bash
rasa run --enable-api
Run the Streamlit frontend:

bash
streamlit run app.py
Future Enhancements
Add more detailed career paths and industries.

Implement Rasa Forms for structured slot filling.

Integrate external APIs for real-time career data.

Add multilingual support.
