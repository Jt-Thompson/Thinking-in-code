# 700 Batch — Episode 9+10 Capstone
# Dictionaries (structured meaning) + Loops (batch review)

# --- sample week of recaps ---
week = [
    {"date": "2025-10-13", "mood": "⬆", "friction": "",                 "summary": "Deep flow on lists & methods"},
    {"date": "2025-10-14", "mood": "➡", "friction": "Debugger noise",   "summary": "Small tooling friction, kept momentum"},
    {"date": "2025-10-15", "mood": "⬇", "friction": "Syntax slip",      "summary": "Fixed bug, learned == vs = reflex"},
    {"date": "2025-10-16", "mood": "⬆", "friction": "",                 "summary": "Clean run — functions + routing"},
    {"date": "2025-10-17", "mood": "⬆", "friction": "Context switching","summary": "Recovered focus, tight exercise loop"},
]
print("\n--- Weekly Timeline ---")
for r in week:
    tag = " (friction: " + r["friction"] + ")" if r["friction"] else ""
    print(f"{r['date']} → {r['mood']} — {r['summary']}{tag}")
ups = downs = neutrals = 0
for r in week:
    if r["mood"] == "⬆":
        ups += 1
    elif r["mood"] == "⬇":
        downs += 1
    else:
        neutrals += 1

print("\n--- Mood Counts ---")
print("Positive (⬆):", ups)
print("Negative (⬇):", downs)
print("Neutral  (➡):", neutrals)
frictions = set()
for r in week:
    if r["friction"]:
        frictions.add(r["friction"])

print("\n--- Unique Frictions ---")
if frictions:
    for f in sorted(frictions):
        print("-", f)
else:
    print("None")
