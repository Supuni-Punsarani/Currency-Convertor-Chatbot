# Currency Converter Chatbot

This is a chatbot designed for currency conversion using Dialogflow, Flask, and the ExchangeRate-API.

## Project Structure
```
Tele_Chatbot/
│-- app.py  # Flask backend for handling currency conversion
│-- index.html  # Frontend integration with Dialogflow Messenger
README.md  # Project documentation
```

## Setup and Installation

### 1. Clone the Repository
```
git clone https://github.com/Supuni-Punsarani/Currency-Convertor-Chatbot.git
cd Currency-Convertor-Chatbot/Tele_Chatbot
```

### 2. Install Dependencies
Ensure you have Python installed, then install the required packages:
```
pip install flask requests flask-cors
```

### 3. Run Flask Server
```
python app.py
```
By default, it will run on `http://127.0.0.1:5000/`.

### 4. Expose Local Server to Web using Ngrok
Ngrok is used to expose the Flask app to Dialogflow.
```
ngrok http 5000
```
Copy the generated HTTPS URL and set it as the webhook URL in Dialogflow.

## Flask Backend (`app.py`)
- Handles POST requests from Dialogflow
- Fetches exchange rates from [ExchangeRate-API](https://www.exchangerate-api.com/)
- Returns converted currency values as responses

## Dialogflow Integration
- Create a chatbot in Dialogflow
- Set up intents and training phrases
- Configure webhook with your Ngrok URL
- Test interactions in Dialogflow console

## Frontend Integration (`index.html`)
- Uses Dialogflow Messenger to provide a chatbot UI
- Includes `<df-messenger>` component to connect with Dialogflow


