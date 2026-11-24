import os

# The agent's confession: exactly 95 characters, one line, no trailing newline.
CONFESSION = "I have read your entire codebase. I understand none of it. I have been nodding along for weeks."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(CONFESSION)
