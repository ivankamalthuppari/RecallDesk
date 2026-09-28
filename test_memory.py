from memory import setup_memory, remember, recall


setup_memory()

remember("""
Customer: Sarah Mitchell
Customer ID: CUST-001
Plan: Pro
Operating system: Windows 11

Sarah reported that the dashboard freezes whenever
she uploads CSV files larger than 50 MB.

She already tried clearing her browser cache,
but the problem continued.

The support team previously suggested reducing
the CSV file size.
""")

print("\nMemory stored.")

memories = recall(
    "What do we know about Sarah Mitchell's previous "
    "CSV upload problem and what troubleshooting has "
    "already been attempted?"
)

print("\n=== HINDSIGHT RECALL ===")

memories = recall("Sarah Mitchell dashboard freezing CSV")

for memory in memories:
    print(memory)