import random
import time

def gethumanpick():
    pick = input("Pick Rock, Paper or Scissors: ")
    return pick.lower()

def getaipick():
  picks = ["rock", "paper", "scissors"]
  pick = random.choice(picks)
  return pick

def winner(humanpick, aipick):
  if humanpick == aipick:
    return "You tied, go again!"
  elif (
      (humanpick == "rock" and aipick == "scissors") or
      (humanpick == "paper" and aipick == "rock") or
      (humanpick == "scissors" and aipick == "paper")
  ):
      return "You won and beat the AI!"
  else:
      return "The AI Wins!"

def play():
  rounds = 0
  playerscore = 0
  aiscore = 0

  while True:
    print(" ")
    print("=== Round", rounds + 1, "===")
    time.sleep(1)
    humanpick = gethumanpick()
    aipick = getaipick()
    print("You picked: ", humanpick)
    time.sleep(2)
    print("AI chose: ", aipick)
    print(" ")
    time.sleep(1)
    tally = winner(humanpick, aipick)
    print(tally)

    if "won" in tally:
      playerscore += 1
    elif "Wins" in tally:
      aiscore += 1
    
    rounds += 1
    print(" ")
    print("Your score: ", playerscore, "AI Score: ", aiscore)
    print(" ")

    playagain = input("Play Again? |Yes/No|: ")
    if playagain.lower() != "yes":
      print("Thanks for playing!")
      time.sleep(2)
      break

play()

