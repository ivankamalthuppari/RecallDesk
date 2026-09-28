from memory import setup_memory
from agent import handle_customer_message

setup_memory()

response = handle_customer_message(
    "Sarah Mitchell",
    "Hi, I'm still having the dashboard freezing problem."
)

print("\n--- AGENT RESPONSE ---\n")
print(response)