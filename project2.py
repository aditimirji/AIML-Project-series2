user_data = {}

def greet_user():
    return "Hello! Welcome to the College Admission Assistant. How can I assist you today?"

def get_response(user_input, user_id):
    global user_data
    responses = {
        "pes": "great choice, that is a good university",
        "how are you": "I'm just a bot, but I'm here to help you with college admissions!",
        "what is your name": "I'm the College Admission Assistant, at your service.",
        "what can you do": "I can provide information about college admissions, requirements, deadlines, and more.",
        "yes, i do": "Great! Feel free to ask me anything related to college admissions.",
        "good": "I'm glad to hear that! How can I assist you today?",
        "tell me a joke": "Why did the student bring a ladder to college? Because they heard the course was 'uplifting'!",
        "bye": "Goodbye! If you have more questions, feel free to ask anytime!",
        "yes": "so u already missed srm, pessat deadline but its alright there are many left for you such as UPES",
        "pes": "great choice, that is a good university",
        "srm":"OOOOOOH"
    }
    
    if user_input.lower().startswith("my name is"):
        user_data[user_id] = {'name': user_input[11:].strip()}
        return f"Nice to meet you, {user_data[user_id]['name']}! How can I assist you today?"
    
    if user_id in user_data and 'name' in user_data[user_id]:
        return responses.get(user_input.lower(), "I'm not sure how to respond to that. Can you ask something else?")
    else:
        return responses.get(user_input.lower(), "I'm not sure how to respond to that. Can you please tell me your name first?")

def remember_context(user_input, user_id):
    if user_id not in user_data:
        user_data[user_id] = {'context': []}
    user_data[user_id]['context'].append(user_input)

def get_previous_context(user_id):
    return user_data.get(user_id, {}).get('context', [])

def ask_admission_questions():
    questions = [
        "What colleges are you interested in?",
        "other than that which other college are you interested in knowing ",
        "Do you need information about application deadlines?"
    ]
    return questions

def chatbot():
    user_id = 1  # In a real scenario, this could be a session ID or user identifier
    print(greet_user())
    
    for question in ask_admission_questions():
        print(question)
        user_input = input("Your response: ")
        remember_context(user_input, user_id)
        print(get_response(user_input, user_id))
        
    while True:
        user_input = input("You: ")
        remember_context(user_input, user_id)
        if user_input.lower() == "bye":
            print("College Admission Assistant: Goodbye! If you have more questions, feel free to ask anytime!")
            break
        response = get_response(user_input, user_id)
        print(f"College Admission Assistant: {response}")

# Run the chatbot
chatbot()
