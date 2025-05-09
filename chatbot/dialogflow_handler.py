from google.cloud import dialogflow_v2 as dialogflow
from google.oauth2 import service_account
import config
import logging

def get_dialogflow_response(user_input):
    """Fetches response from Google Dialogflow for user queries."""
    try:
        # Load credentials from the service account file
        credentials_json = config.GOOGLE_APPLICATION_CREDENTIALS_JSON

        # Create the Dialogflow client with authentication
        client = dialogflow.SessionsClient(credentials=credentials_json)
        session = client.session_path(config.GOOGLE_PROJECT_ID, config.SESSION_ID)

        text_input = dialogflow.TextInput(text=user_input, language_code="en")
        query_input = dialogflow.QueryInput(text=text_input)

        response = client.detect_intent(session=session, query_input=query_input)
        logging.debug(f"Dialogflow API Response: {response.query_result.fulfillment_text}")
        
        return response.query_result.fulfillment_text

    except Exception as e:
        logging.error(f"Dialogflow API Error: {str(e)}")
        return None  # If Dialogflow fails, let Gemini handle it
