# Introductory Lines
print("You wake up on an island, uncertain of your whereabouts but all you can think of")
print("is your need to survive. You see that there are trees, materials, plants, animals.")
print("You can do three things for the day, do you:")
print("A: Build a raft to leave the island")
print("B: Create shelter to survive and gather food")
print("C: Create an SOS sign for passing planes (if there are any)\n")

# First choice of events
choice_main = input("What option do you choose? (A, B, C): ").upper()

if choice_main == "A": # Scenario if user picked choice A
  print("\nYou have created a raft to leave the island, you now have left the island and")
  print("are now sailing away, you then find yourself on route to crash into a giant")  
  print("rock, you have no choice but to:")
  print("A: Steer Left")
  print("B: Steer Right")
  print("C: Dismount raft\n")
  choice_a = input("What option do you choose? (A, B, C): ").upper()
  if choice_a == "A":
    print("\nYou steered left, the wind pushed to further right and crashed you straight into the rock")
    print("\nTragic ending! Rerun the program to aim for a different ending!")
  elif choice_a == "B":
    print("\nYou steered right and successfully dodged the rock, you are now safe and you")
    print("begin to see mainland. You arrive on mainland and are greeted by nearby villagers.")
    print("You were cared for by the kind villagers and were flown back to your home town")
    print("\nBravery ending! Rerun the program to aim for a different ending!")
  elif choice_a == "C":
    print("\nYou dismounted the raft while it crashed into the rock, you are now stranded at sea.")
    print("You developed hypothermia due to the cold of the water, and died.")
    print("\nCold ending! Rerun the program to aim for a different ending!")
  else:
    print("Invalid answer!")
elif choice_main == "B": # Scenario if user picked choice B
  print("\nYou created a shelter and decided to live on the island for the time being, you")
  print("lived on berries and wild rabbit for the majority of your time. You decide to wander")
  print("the island and you stumble upon a sacred temple. You walk into the temple and see a")
  print("artifact that you have an urge to take. Do you:")
  print("A: Take the artifact")
  print("B: Take the artifact but pull an Indiana Jones with a nearby stone")
  print("C: Leave it alone and leave the temple\n")
  choice_b = input("What option do you choose? (A, B, C): ").upper()
  if choice_b == "A":
    print("\nYou touch the artifact, as you begin to go closer to it, it shines brighter")
    print("As you touch the artifact, you begin wake up from your dream")
    print("\nMysterious ending! Rerun the program to aim for a different ending!")
  elif choice_b == "B":
    print("\nYou touch the artifact, as you begin to go closer to it, it shines brighter")
    print("As you touch the artifact, you begin wake up from your dream")
    print("\nMysterious ending! Rerun the program to aim for a different ending!")
  elif choice_b == "C":
    print("\nYou leave the temple and live your regular life on the island,")
    print("you get more bored and lonely for everyday that passes, and you begin to cry")
    print("\nLonely ending! Rerun the program to aim for a different ending!")
  else:
    print("Invalid answer!")
elif choice_main == "C": # Scenario if user picked choice C
  print("\nYou created an sos sign using rocks and wood, nobody flies by. The tide washed")
  print("away your sign in the morning, so you decide on something else. Do you:")
  print("A: Build a raft to leave the island")
  print("B: Create shelter to survive and gather food")
  choice_c_one = input("What option do you choose? (A, B): ").upper()
  if choice_c_one == "A": # Scenario if user picked choice A
    print("\nYou have created a raft to leave the island, you now have left the island and")
    print("are now sailing away, you then find yourself on route to crash into a giant")  
    print("rock, you have no choice but to:")
    print("A: Steer Left")
    print("B: Steer Right")
    print("C: Dismount raft\n")
    choice_c_two = input("What option do you choose? (A, B, C): ").upper()
    if choice_c_two == "A":
      print("\nYou steered left, the wind pushed to further right and crashed you straight into the rock")
      print("\nTragic ending! Rerun the program to aim for a different ending!")
    elif choice_c_two == "B":
      print("\nYou steered right and successfully dodged the rock, you are now safe and you")
      print("begin to see mainland. You arrive on mainland and are greeted by nearby villagers.")
      print("You were cared for by the kind villagers and were flown back to your home town")
      print("\nBravery ending! Rerun the program to aim for a different ending!")
    elif choice_c_two == "C":
      print("\nYou dismounted the raft while it crashed into the rock, you are now stranded at sea.")
      print("You developed hypothermia due to the cold of the water, and died.")
      print("\nCold ending! Rerun the program to aim for a different ending!")
    else:
      print("Invalid answer!")
  elif choice_c_one == "B": # Scenario if user picked choice B
    print("\nYou created a shelter and decided to live on the island for the time being, you")
    print("lived on berries and wild rabbit for the majority of your time. You decide to wander")
    print("the island and you stumble upon a sacred temple. You walk into the temple and see a")
    print("artifact that you have an urge to take. Do you:")
    print("A: Take the artifact")
    print("B: Take the artifact but pull an Indiana Jones with a nearby stone")
    print("C: Leave it alone and leave the temple\n")
    choice_c_three = input("What option do you choose? (A, B, C): ").upper()
    if choice_c_three == "A":
      print("\nYou touch the artifact, as you begin to go closer to it, it shines brighter")
      print("As you touch the artifact, you begin wake up from your dream")
      print("\nMysterious ending! Rerun the program to aim for a different ending!")
    elif choice_c_three == "B":
      print("\nYou touch the artifact, as you begin to go closer to it, it shines brighter")
      print("As you touch the artifact, you begin wake up from your dream")
      print("\nMysterious ending! Rerun the program to aim for a different ending!")
    elif choice_c_three == "C":
      print("\nYou leave the temple and live your regular life on the island,")
      print("you get more bored and lonely for everyday that passes, and you begin to cry")
      print("\nLonely ending! Rerun the program to aim for a different ending!")
    else:
      print("Invalid answer!")
  else:
    print("Invalid answer!")
else:
  print("Invalid answer!")