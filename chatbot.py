import nltk
from nltk.chat.util import Chat, reflections

# Define patterns and responses
pairs = [
    (r"hi|hello", ["Hello!", "Hi there!", "Hey!"]),
    (r"how are you?", ["I'm fine, thank you!", "Doing well, how about you?"]),
    (r"what is sentinel edr?", ["Sentinel EDR is an endpoint detection and response system."]),
    (r"tell me about elk stack", ["ELK Stack consists of Elasticsearch, Logstash, and Kibana for log analysis."]),
    (r"(.*) logs?", ["I can help analyze logs! What log data do you have?"]),
    (r"quit|exit", ["Goodbye!", "Exiting now. Have a great day!"])
]

# Initialize chatbot
chatbot = Chat(pairs, reflections)

# Command-line chat loop
print("🤖 Chatbot: Hello! Type 'quit' or 'exit' to stop.")
while True:
    user_input = input("🧑 You: ").lower()
    if user_input in ["quit", "exit"]:
        print("🤖 Chatbot: Goodbye!")
        break
    response = chatbot.respond(user_input)
    print(f"🤖 Chatbot: {response}")
