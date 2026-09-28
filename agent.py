import os

from dotenv import load_dotenv
from groq import Groq

from memory import remember, recall

load_dotenv()

groq = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


SYSTEM_PROMPT = """
You are RecallDesk, an AI customer support agent.

Use relevant customer history from Hindsight to help answer the customer.

Rules:
- Use remembered information when relevant.
- Do not invent memories.
- Do not ask for information already known.
- Acknowledge previous failed troubleshooting.
- Suggest the next reasonable troubleshooting step.
- Never invent APIs, features, policies, previous actions, or system capabilities.
- Only recommend actions supported by the available information.
- Be concise and professional.
"""


def handle_customer_message(customer_name, customer_message):

    # Create a search query containing both the customer and issue.
    query = f"""
Customer: {customer_name}

Current issue:
{customer_message}
"""

    # 1. Retrieve relevant historical memories from Hindsight
    memories = recall(query)

    # Keep only a few memories so we don't exceed Groq's token limit.
    memory_text = "\n".join(
        str(memory) for memory in memories[:4]
    )

    # Extra protection against an oversized prompt.
    memory_text = memory_text[:6000]

    # 2. Generate an AI response using the retrieved history
    response = groq.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "system",
                "content": f"""
Relevant customer history retrieved from Hindsight:

{memory_text}
"""
            },
            {
                "role": "user",
                "content": customer_message
            }
        ],
        temperature=0.3
    )

    answer = response.choices[0].message.content

    # 3. Store this new interaction for future conversations
    remember(
        f"""
Customer: {customer_name}

Customer message:
{customer_message}

RecallDesk response:
{answer}
"""
    )

    return answer