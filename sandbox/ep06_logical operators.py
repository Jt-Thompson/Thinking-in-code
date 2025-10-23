# 700 batch - ep 6 logical operators

def reflection_router (mood, energy, friction):
    # exmapole of compounfd logic
    if mood == "focused" and energy > 7 and not friction:
        print("growth day - deep flow")
    elif mood == "tired" or friction:
        print("recovery or truobleshooting day")
    else:
        print ("Neutral day - steady focus")

#----test case-----
reflection_router ("focused", 8, False)
reflection_router ("tired", 6, True)
reflection_router ("focused", 6, False)
    
