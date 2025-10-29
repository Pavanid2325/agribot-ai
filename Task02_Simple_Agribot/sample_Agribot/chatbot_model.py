import random

# Agriculture chatbot responses
responses = {
    "greeting": [
        "Hello! I'm your agriculture assistant. 🌱 How can I help you today?",
        "Hi there! Ask me anything about farming and crops. 🚜"
    ],
    "fertilizer": [
        "For better yield, use organic compost and nitrogen-rich fertilizer like urea.",
        "Consider using phosphorus and potassium-based fertilizers for root growth."
    ],
    "pest": [
        "Neem oil spray is effective for many pests.",
        "Introduce natural predators like ladybugs to control pest population."
    ],
    "weather": [
        "Please check the local forecast before sowing seeds.",
        "Avoid watering plants if heavy rain is predicted."
    ],
    "default": [
        "I'm not sure about that. Could you please rephrase?",
        "Sorry, I don't understand. Can you ask another question?"
    ]
}

def get_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return random.choice(responses["greeting"])
    elif "fertilizer" in user_input:
        return random.choice(responses["fertilizer"])
    elif "pest" in user_input:
        return random.choice(responses["pest"])
    elif "weather" in user_input:
        return random.choice(responses["weather"])
    else:
        return random.choice(responses["default"])