import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


# Define a set of stopwords to filter out common words
stop_words = set(stopwords.words('english'))

def preprocess_input(user_input):
    # Tokenize the input and convert to lowercase
    tokens = word_tokenize(user_input.lower())
    
    # Remove stopwords from the token list
    filtered_tokens = [token for token in tokens if token not in stop_words]
    
    # Reconstruct the preprocessed sentence
    preprocessed_input = ' '.join(filtered_tokens)
    
    return preprocessed_input

def chatbot_response(user_input):
    preprocessed_input = preprocess_input(user_input)
    
    # Define the predefined rules and responses
    rules = {
        r".*\bhi\b.*": "Hello! How can I assist you today?",
        r".*\bhello\b.*": "Hi! How can I help you?",
        r".*\bbye\b.*": "Goodbye! Have a great day!",
        r".*\b(?:apple|orange|banana)\b.*": "Yes, we have {} in stock.",
        r".*\b(?:How are you ?)\b.*": "I am always good.thanks for asking...!",
        r".*\b(?:Question)\b.*": "Answer.",
        r".*\b(?:how\sare\syou|howdy)\b.*": "I'm just a bot, but I'm doing fine, thanks for asking!",
        r".*\b(?:thank\syou|thanks)\b.*": "You're welcome!",
        r".*": "I'm sorry, I don't understand. Can you please rephrase your question?"
    }
    
    # Check preprocessed user input against each rule and provide the appropriate response
    for pattern, response in rules.items():
        if re.match(pattern, preprocessed_input, re.IGNORECASE):
            if "{}" in response:
                return response.format(preprocessed_input.split()[-1])  # Fill the '{}' with the last word
            return response
    
    return rules[".*"]  # Default response if no pattern matches

if __name__ == "__main__":
    print("Chatbot: Hello! How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print("Chatbot:", response)
