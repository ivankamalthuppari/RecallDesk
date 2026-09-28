import os

from dotenv import load_dotenv
from hindsight_client import Hindsight

load_dotenv()

API_KEY = os.getenv("HINDSIGHT_API_KEY")

if not API_KEY:
    raise RuntimeError("HINDSIGHT_API_KEY is missing from .env")

client = Hindsight(
    api_key=API_KEY,
    base_url="https://api.hindsight.vectorize.io"
)

BANK_ID = "recall-desk"


def setup_memory():
    try:
        client.create_bank(
            bank_id=BANK_ID,
            name="RecallDesk Customer Memory"
        )
        print("Memory bank created.")

    except Exception as e:
        if "already exists" in str(e).lower():
            print("Memory bank already exists.")
        else:
            print("Bank setup:", e)


def remember(conversation):
    client.retain(
        bank_id=BANK_ID,
        content=conversation,
        context="Customer support conversation"
    )

    print("Memory stored.")


def recall(query):
    response = client.recall(
        bank_id=BANK_ID,
        query=query,
        max_tokens=1500
    )

    memories = []

    for result in response.results[:5]:
        memories.append(
            f"[{result.type}] {result.text}"
        )

    return memories