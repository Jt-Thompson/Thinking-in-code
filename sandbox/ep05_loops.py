# 700 batch - ep 5 loops
def log_entry_point(day):
    print("-----")
    print(" 700 batch reflection entry")
    print("date:", day)

# test with a single day first

days = ["2025-10-18", "2025-10-19", "2025-10-20", "2025-10-21"]

for day in days:
    log_entry_point(day)

#dynamic routing example
for day in days:
    if day == "2025-10-18":
        print("Focus day - building foundation")
    elif day == "2025-10-19":
        print("debug day - fixing errors")
    elif day == "2025-10-20": 
        print("flow day - smooth learning")   
    else:
        print(" Reflection & review day")

print("--------")
log_entry_point(day)
print("--------\n")
