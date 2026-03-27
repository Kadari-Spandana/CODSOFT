import re

def get_response(user_input):
    user_input = user_input.lower()

    # Mapping patterns to responses using regular expressions
    # This allows the bot to find keywords within sentences
    rules = {
        # Greetings
        r'.*(hello|hi|hey|greetings).*': "Hello! I'm your AI assistant. How can I help you today?",
        
        # Identity and Origin
        r'.*(who are you|your name|what are you).*': "I am a Rule-Based Chatbot developed as part of my CodSoft AI internship.",
        r'.*(created|build|maker).*': "I was created by an aspiring AI engineer using Python and Pattern Matching.",
        
        # Technical/AI Questions
        r'.*(what is ai|artificial intelligence).*': "AI is the simulation of human intelligence by machines, especially computer systems.",
        r'.*(machine learning|ml).*': "Machine Learning is a subset of AI that focuses on building systems that learn from data.",
        r'.*(rule-based|how do you work).*': "I work based on predefined rules and pattern matching. I don't 'think', I match!",
        
        # Capabilities
        r'.*(what can you do|help|capabilities).*': "I can answer basic questions about AI, greet you, or tell you who I am. Try asking 'What is ML?'",
        
        # Common Conversation
        r'.*(how are you|how is it going).*': "I'm functioning within normal parameters! How are you doing?",
        r'.*(good|great|fine).*': "That's wonderful to hear!",
        r'.*(thank you|thanks).*': "You're very welcome! Is there anything else you need?",
        
        # Closing
        r'.*(bye|goodbye|exit|quit).*': "Goodbye! It was a pleasure chatting with you."
    }

    # Iterate through the dictionary to find a match
    for pattern, response in rules.items():
        if re.match(pattern, user_input):
            return response

    # Fallback response for unrecognized inputs
    return "I'm not sure I understand. Could you rephrase that? I'm still in the early stages of my training."

# Main interaction loop
print("--- CodSoft AI Internship: Rule-Based Chatbot ---")
print("(Type 'bye' to exit the conversation)")

while True:
    user_query = input("You: ").strip()
    
    # Check for exit command
    if re.match(r'.*(bye|exit|quit).*', user_query.lower()):
        print("Chatbot: Goodbye! Have a great day.")
        break
    
    # Get and print response
    response = get_response(user_query)
    print(f"Chatbot: {response}")