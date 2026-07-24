# ==========================================
# Rule-Based Expert System
# Disease Diagnosis using Forward Chaining
# ==========================================

print("=" * 50)
print("        RULE-BASED EXPERT SYSTEM")
print("=" * 50)
print("Disease Diagnosis using Forward Chaining\n")

# Get symptoms from user
user_input = input("Enter symptoms separated by commas: ")

# Convert input into a set
facts = set()

for symptom in user_input.split(","):
    symptom = symptom.strip().lower()
    if symptom:
        facts.add(symptom)

print("\nSymptoms Entered:", facts)

# -----------------------------
# Knowledge Base (Rules)
# -----------------------------
rules = [

    {
        "conditions": {"fever", "cough"},
        "conclusion": "viral infection"
    },

    {
        "conditions": {"viral infection", "body pain"},
        "conclusion": "flu"
    },

    {
        "conditions": {"headache", "nausea"},
        "conclusion": "migraine"
    },

    {
        "conditions": {"sneezing", "runny nose"},
        "conclusion": "common cold"
    },

    {
        "conditions": {"itching", "skin rash"},
        "conclusion": "allergy"
    },

    {
        "conditions": {"chest pain", "shortness of breath"},
        "conclusion": "heart problem"
    }

]

print("\n========== Inference Process ==========\n")

changed = True

while changed:

    changed = False

    for rule in rules:

        if rule["conditions"].issubset(facts):

            if rule["conclusion"] not in facts:

                print("Matched Rule")
                print("IF :", ", ".join(rule["conditions"]))
                print("THEN :", rule["conclusion"])
                print()

                facts.add(rule["conclusion"])

                changed = True

print("========== Final Diagnosis ==========\n")

diseases = []

if "flu" in facts:
    diseases.append("Flu")

if "migraine" in facts:
    diseases.append("Migraine")

if "common cold" in facts:
    diseases.append("Common Cold")

if "allergy" in facts:
    diseases.append("Allergy")

if "heart problem" in facts:
    diseases.append("Heart Problem")

if diseases:

    print("Possible Disease(s):")

    for disease in diseases:
        print("•", disease)

else:

    print("No matching disease found.")
    print("Please consult a doctor.")

print("\n========== Facts After Inference ==========")

for fact in sorted(facts):
    print("-", fact)

print("\nThank you for using the Rule-Based Expert System.")