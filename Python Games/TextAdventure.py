import sys
import time
import random

def printvfast(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.008)

def scenescroll():
  for i in range(50):
    print(' ')
    time.sleep(0.05)

printvfast("""           _________   _________________________    _____    ___________________
          /  _  \   \ /   /\_   _____/\______   \  /  _  \  /  _____/\_   _____/
         /  /_\  \   Y   /  |    __)_  |       _/ /  /_\  \/   \  ___ |    __)_
        /    |    \     /   |        \ |    |   \/    |    \    \_\  \|        \\
        \____|__  /\___/   /_______  / |____|_  /\____|__  /\______  /_______  /
                \/                 \/         \/         \/        \/        \/         """)
print('\n')
print(' ')
printvfast("""    _____  ____________   _______________ ______________________ ________________________
   /  _  \ \______ \   \ /   /\_   _____/ \      \__    ___/    |   \______   \_   _____/
  /  /_\  \ |    |  \   Y   /  |    __)_  /   |   \|    |  |    |   /|       _/|    __)_
 /    |    \|    `   \     /   |        \/    |    \    |  |    |  / |    |   \|        \\
 \____|__  /_______  /\___/   /_______  /\____|__  /____|  |______/  |____|_  /_______  /
        \/        \/                 \/         \/                         \/        \/ """)
print('\n')
print(' ')
printvfast("""                        ________    _____      _____  ___________
                       /  _____/   /  _  \    /     \ \_   _____/
                      /   \  ___  /  /_\  \  /  \ /  \ |    __)_
                      \    \_\  \/    |    \/    Y    \|        \\
                       \______  /\____|__  /\____|__  /_______  /
                              \/         \/         \/        \/                       """)
print()

time.sleep(3)
scenescroll()

#Title Screen
print('        __                                           __')
print('       (**)                                         (**)')
print('       IIII                                         IIII')
print('       ####                                         ####')
print('       HHHH                 Welcome                 HHHH')
print('       HHHH                   to                    HHHH')
print('       ####                 AVERAGE                 ####')
print('    ___IIII___             ADVENTURE             ___IIII__')
print(' .-`_._"**"_._`-.            GAME!            .-`_._"**"_._`-.')
print('|/``  .`\/`.  ``\|                           |/``  .`\/`.  ``\|')
print("`     }    {     '                           `     }    {     '")
print('      ) () (                                       ) () (')
print('      ( :: )                                       ( :: )')
print('      | :: |                                       | :: |')
print('      | )( |                                       | )( |')
print('      | || |                                       | || |')
print('      | || |                                       | || |')
print('      | || |                                       | || |')
print('      | || |                                       | || |')
print('      | || |                                       | || |')
print('      ( () )                                       ( () )')
print('       \  /                                         \  /')
print('        \/                                           \/')

health = 100
mhealth = 50
reward = 20
money = 10
armor = 0
sword = 0
potion = 0
spiderpaper = 0
griffinpaper = 0
goblinpaper = 0
trollpaper = 0

def scenescroll():
  for i in range(50):
    print(' ')
    time.sleep(0.05)

def smallscroll():
  for i in range(5):
    print(' ')
    time.sleep(0.08)

def starty():
    while True:
        selecty = input("               Start? (Y/N): ").lower()
        if selecty == "":
            printvfast("You can't choose nothing, a hero is needed!")
            print(" ")
            time.sleep(3)
        else:
            if selecty == "n":
              printvfast('I know you said no, but a hero is needed')
              print(" ")
            if selecty == "y":
              printvfast("Your Adventure Begins...")
              print(" ")
              time.sleep(3)
              scenescroll()
              break
starty()

printvfast('How fast would you like the text?')
print(" ")
speed = input("slow, normal or fast?: ")
if speed == "fast":
  fasty = 0.05
if speed == "normal":
  fasty = 0.08
if speed == "slow":
  fasty = 0.1
if speed == "dev":
  fasty = 0.001

def printslow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(fasty)

scenescroll()

printslow("""Once upon a time, in a world of magic and wonder,
there was a small village nestled amidst lush green
fields and towering mountains. This village, known
as Wildridge, was a peaceful haven for its
inhabitants, who led simple lives filled with harmony
and contentment.

However, the tranquility of Wildridge was about
to be shattered by a grave problem that plagued the
villagers. A malevolent curse had befallen the land,
causing the once bountiful harvests to wither and the
villagers' spirits to wane. Crops failed, livestock
fell ill, and a dark shadow seemed to cast a pall
over the entire village.

Amidst this despair, a new hope emerged—the arrival
of a legendary hero, a savior who could lift the curse
and restore prosperity to Wildridge. As fate would
have it, you are that hero. But first, you must embark
on a perilous journey, facing untold dangers and
unraveling ancient mysteries to save the village
from its imminent doom.

Before you set foot on this extraordinary adventure,
you must choose your name, for it shall be whispered
across the realm in tales of your courage and triumphs.

What is your name, brave adventurer?""")

print(" ")

def choosename():
    while True:
        name = input('Name: ')
        if name == "":
            printvfast("You can't be an adventurer without a name! How can people tell your tales?")
            print(" ")
            time.sleep(3)
        else:
            printvfast(f"Ready to be a hero, {name}?")
            print(" ")
            startad = input('Start? Y/N: ').lower()
            if startad == "n":
              printvfast('I thought you were a brave adventurer!')
              print(" ")
            if startad == "y":
              printvfast("Let's Begin...")
              print(" ")
              time.sleep(3)
              scenescroll()
              break

choosename()

printslow("""As you venture through the dense forest, the sounds of chirping
birds and rustling leaves guide your way. The air is crisp,
carrying a hint of anticipation as you draw closer to the small
village of Wildridge. Rays of sunlight filter through the towering
ancient trees, casting a golden glow upon the forest floor.

You emerge from the verdant wilderness onto a narrow path, meandering
through rolling hills and wildflower meadows. The gentle breeze carries
the sweet fragrance of wild lavender, creating an atmosphere of serenity.

As you walk, you catch glimpses of smoke rising from chimneys, wafting
into the azure sky. The distant sound of laughter and bustling activity
reaches your ears, indicating signs of life and community.

Drawing nearer, you spot the village of Wildridge nestled in a valley,
surrounded by majestic mountains on three sides. Colorful thatched-roof
cottages with blooming flower boxes line the main street, and a bubbling
brook runs alongside it, providing a soothing soundtrack to the village's
rhythm.

The village square comes into view, adorned with a weathered stone fountain
at its center. Villagers, dressed in vibrant garbs, go about their daily tasks.
Some haggle at the market stalls, while others gather in animated conversations,
their faces painted with expressions of both joy and worry.

Wildridge exudes an aura of resilience, despite the curse that has befallen its lands.
The villagers maintain an unwavering spirit, determined to overcome the hardships they face.

With a deep breath, you step forward, ready to lend your strength and embark on the
adventure that awaits within the heart of Wildridge.

The fate of the village and its people now rests in your hands.""")

smallscroll()

printvfast("""~         ~~          __")
       _T      .,,.    ~--~ ^^")
 ^^   // \                    ~")
      ][O]    ^^      ,-~ ~")
   /''-I_I         _II____")
__/_  /   \ ______/ ''   /'\_,__")
  | II--'''' \,--:--..,_/,.-{ },")
; '/__\,.--';|   |[] .-.| O{ _ }")
:' |  | []  -|   ''--:.;[,.'\,/")
'  |[]|,.--'' '',   ''-,.    |")
  ..    ..-''    ;       ''. '""")
time.sleep(3)

smallscroll()



def goinvil():
    while True:
        printslow('Ready to enter the village?')
        print(" ")
        choice = input('Choose Y/N: ').lower()
        if choice == "":
            printvfast("You have to make a choice!")
            print(" ")
            time.sleep(3)
        if choice == "n":
            printvfast("That is not very adverturer like of you.")
            print(" ")
            time.sleep(3)
        if choice == "y":
            printvfast("You proceed into Wildridge")
            print(" ")
            time.sleep(3)
            scenescroll()
            break
        else:
          printvfast("That's not a valid input!")

goinvil()

printslow("""As you approach the troubled village of Wildridge,
a sense of urgency hangs in the air. The once vibrant
and lively atmosphere is tinged with an aura of worry
and unease. Eyes turn to you, the adventurer who has
arrived to face the village's plight.

Your gaze is drawn to a weathered wooden signpost at the
village entrance, adorned with notices and papers. It
serves as a makeshift board, where desperate pleas for
help and announcements of recent events are pinned.
The parchment flutters in the wind, bearing witness to
the troubles that have befallen the village.

To your left, you spot an armor and weapons store, its
windows adorned with polished shields and gleaming swords.
The door creaks open, inviting you to browse its wares.
The blacksmith, with sweat glistening on their brow, works
diligently on a newly forged weapon behind the counter.

Just a few steps away stands the apothecary, its shelves
lined with glass jars containing various herbs and potions.
A pungent aroma of medicinal concoctions fills the air,
mixed with the gentle whispers of the apothecary attending
to a worried villager seeking remedies for their ailments.

Across the way, a bustling tavern comes into view. The
sounds of clinking mugs and merry laughter spill out from
its open doors. Weary adventurers and locals alike find
solace within its walls, sharing tales of valor and seeking
brief respite from the troubles that plague Wildridge. The
tavern keeper wipes down the bar with a weary smile, their
eyes betraying the weight of the village's hardships.

Dominating the village square is a grand structure that can
only be the town hall. Its sturdy stone walls and imposing
architecture speak of the village's history and resilience.
A large wooden door stands before you, beckoning you to step
inside. Behind those doors lie the village council, where
decisions are made and the fate of Wildridge is debated.

As you take in the sights and sounds, you can't help but feel
the weight of responsibility on your shoulders. The people of
Wildridge look to you with hopeful eyes, seeking a savior to
lift the curse that has befallen their once prosperous home.
With determination in your heart, you prepare to step forward,
ready to face the challenges that await within the
village and beyond.""")

smallscroll()

def winning():
  global money
  money += 20
  printslow(f"You have defeated the monster in battle and gained {reward} coins!")
  printslow(f"You now have {money} coins")
  smallscroll()
  locmenu()
  gowhere()

def losing():
  printslow("You have failed as an adventurer, should have ran!")
  time.sleep(3)
  printslow("You wake up back in town having been rescued.")
  time.sleep(2)
  smallscroll()
  locmenu()
  gowhere()


def potdrink():
  print("You take the potion prepare to drink it.")
  print(" ")
  global health
  if health == 100:
    print("You are already full HP!")
    print(" ")
    time.sleep(3)
  if health >= 75:
    print("You are not injured enough. (heals 25)")
    print(" ")
    time.sleep(3)
  if health <= 75:
    print("You drink the potion in one gulp gaining 25 HP!")
    health += 25
    potion -= 1
    time.sleep(3)

def ncombatroll():
  def attacky():
    global mhealth
    roll = random.randint(1,99)
    if sword == 1:
      roll += 20
    if roll > 50:
      damage = random.randint(1,20)
      print(f"You slashed for {damage} damage")
      mhealth
      mhealth -= damage
    if roll < 50:
      print("You have missed!")
      print(" ")
    print(f"The monster has {mhealth} health remaining!")
  while True:
    attack = input("Attack, Drink Potion or Run(30% Chance): A/P/R: ").lower()
    if attack == "p":
        print("You take the potion prepare to drink it.")
        print(" ")
        global health
        global potion
        if health <= 75:
          print("You drink the potion in one gulp gaining 25 HP!")
          health += 25
          potion -= 1
          time.sleep(3)
        elif health >= 75:
          print("You are not injured enough. (heals 25)")
          print(" ")
          time.sleep(3)
        elif health == 100:
          print("You are already full HP!")
          print(" ")
          time.sleep(3)
    if attack == "a":
      print("You take a swing at the monster")
      time.sleep(1)
      attacky()
      time.sleep(2)
      print(" ")
      roll = random.randint(1,99)
      if armor == 1:
        roll -= 20
      if roll > 50:
        damage = random.randint(1,20)
        print("The monster swings at you!")
        time.sleep(2)
        print(f"You were hit for {damage} damage")
        print(" ")
        time.sleep(1)
        health -= damage
        print(f"You have {health} health remaining!")
        print(" ")
        time.sleep(2)
      if roll < 50:
        if armor == 1:
          time.sleep(1)
          print("The attack clangs off your armor!")
          time.sleep(2)
          print(" ")
        else:
          print("The monster swings at you!")
          time.sleep(1)
          print("You skillfully dodge the attack!")
          print(" ")
          time.sleep(2)
    if health <= 0:
      winning()
      break
    if mhealth <= 0:
      winning()
      break
    if attack == "r":
      run = random.randint(1,99)
      gethit = random.randint(1,99)
      if gethit < 50:
        if armor == 1:
          get += 20
        damage = random.randint(1,20)
        print(f"The monster swings as you turn around and hits for {damage}!")
        time.sleep(1)
        health -= damage
        print(f"You have {health} health remaining.")
        if health <= 0:
          print("You died while trying to run!")
          time.sleep(3)
          break
      if gethit > 50:
        if armor == 1:
          gethit += 20
        time.sleep(1)
        print("The monster takes a swing at you as you turn and misses.")
        time.sleep(2)
      if run < 30:
        print(" ")
        print("You have escaped.")
        time.sleep(3)
        break
      else:
        time.sleep(1)
        print("You failed to escape!")
        time.sleep(2)

def spiderloc():
  if spiderpaper == 1:
    print("Spiders are here!")
    smallscroll()
    ncombatroll()
  else:
    print("You don't see anything here, maybe go take a paper.")
    time.sleep(3)
    smallscroll()
    outmenu()
    outwhere()

def goblinloc():
  if goblinpaper == 1:
    print("goblins are here!")
    smallscroll()
    ncombatroll()
  else:
    print("You don't see anything here, maybe go take a paper.")
    time.sleep(3)
    smallscroll()
    outmenu()
    outwhere()

def trollloc():
  if trollpaper == 1:
    print("Trolls are here!")
    smallscroll()
    ncombatroll()
  else:
    print("You don't see anything here, maybe go take a paper.")
    time.sleep(3)
    smallscroll()
    outmenu()
    outwhere()

def griffinloc():
  if griffinpaper == 1:
    print("The griffin is here!")
    smallscroll()
    ncombatroll()
  else:
    print("You don't see anything here, maybe go take a paper.")
    time.sleep(3)
    smallscroll()
    outmenu()
    outwhere()

def thall():
  print(" ")
  printslow("You head into the town hall...")
  smallscroll()
  printslow("""As you step into the grand hall of the town, the imposing figure of the
mayor catches your attention. Dressed in resplendent robes and engrossed in a
flurry of activity, the mayor's presence commands respect. The room hums with
a sense of urgency, as villagers and officials scurry about, attending to their
duties.

You approach the mayor's desk, hoping to gain their attention. With a quick
glance in your direction, the mayor's eyes convey a mix of fatigue and
determination. A weary smile appears on their face as they motion for you to
take a seat.

"Ah, another brave soul seeking to aid our beloved village," the mayor says,
their voice carrying the weight of responsibility. "I apologize for the bustling
atmosphere, but our village is beset by troubles, and every moment is crucial."

Leaning forward, the mayor continues, "You see, adventurer, we face a myriad of
challenges. From marauding beasts threatening our fields to a mysterious illness
afflicting our people, the burdens we carry are many."

The mayor's gaze drifts towards the window, their eyes momentarily lost in the
distance. "I wish I could give you my undivided attention, but the demands of
leadership are relentless. I am but one person amidst a sea of responsibilities."

A determined expression replaces any sign of weariness as the mayor looks back
at you. "However, fear not. If you truly seek to help our village, I implore
you to make your way to the town center. There, in the heart of our community,
you will find the town board."

The mayor describes the scene outside, the bustling town center filled with
villagers going about their daily lives. "The town board stands proudly, adorned
with notices and requests for aid. It serves as a beacon of hope, where the
village gathers to share information and seek assistance."

With a gesture towards the door, the mayor adds, "Venture outside, adventurer,
and explore the town center. The board awaits you, presenting a myriad of urgent
tasks, requests for aid, and vital information."

You express your gratitude to the mayor for their guidance. Determined, you rise
from your seat, your mind set on heading to the town center, where the town
board beckons. The weight of responsibility settles on your shoulders as you
prepare to embrace the challenges that lie ahead, ready to make a difference
for the village and its people.""")
  time.sleep(3)
  print(" ")
  printslow("You step back out into the town center.")
  print(" ")
  time.sleep(3)
  scenescroll()
  locmenu()
  gowhere()


def board():
  printslow("You walk over to the board covered in papers")
  print(" ")
  time.sleep(5)

def pshop():
  global money
  printslow("""As you enter the apothecary, the soothing aroma of herbs and potions
fills the air, creating an atmosphere of tranquility. The shelves
are adorned with labeled jars, each containing a wide assortment of
mystical ingredients and colorful elixirs. Soft light filters through
the stained glass windows, casting enchanting patterns upon the room.

Behind the counter stands the apothecary, dressed in a flowing robe
and exuding an air of wisdom. They greet you with a warm smile, their
eyes reflecting a deep understanding of the healing arts.

"How may I assist you, traveler?" the apothecary asks, their voice
carrying a gentle tone.

Expressing your desire to aid the village, you inquire if there is any
way the apothecary can assist you in your quest. The apothecary's eyes
light up, appreciating your willingness to help.

"In our efforts to support the village, we offer a variety of potent
potions," the apothecary explains, gesturing to a display of vials on
the counter. "One such potion is our renowned healing elixir, capable
of mending wounds and restoring vitality."

With a glimmer of hope in their eyes, the apothecary continues, "For
a humble sum of 10 coins, you can obtain a healing potion. It is a small
investment that can make a significant difference in your endeavors to
aid the village.""")
  print(" ")
  printslow(f"You have {money} coins.")
  print(" ")
  wantit = input("Buy potion for 10 coins? Y/N: ").lower()
  if wantit == "n":
    time.sleep(1)
    printslow("Understanding the potion seller puts the health potion back.")
    print(" ")
    time.sleep(3)
    printslow("You turn and head back into the town square.")
    time.sleep(3)
    scenescroll()
    locmenu()
    gowhere()
  if wantit == "y":
    time.sleep(1)
    printslow(""""The potion seller smiles as you hand over 10 coins and in turn
you place the health potion into your bag.""")
    potion += 1
    time.sleep(3)
    printslow("You turn and head back into the town square.")
    time.sleep(2)
    scenescroll()
    locmenu()
    gowhere()

def ashop():
  global money
  printslow("""As you enter the weapon and armor store, a metallic tang fills the air,
accompanied by the faint scent of leather. The shop is adorned with
racks of gleaming weapons and rows of sturdy armor, each piece promising
strength and protection. Soft torchlight casts a warm glow, emphasizing
the craftsmanship of the displayed items.

Behind the counter stands the shopkeeper, their weathered hands resting
upon the polished surface. They greet you with a nod, their eyes glinting
with knowledge of the trade.

"Welcome, adventurer, to the emporium of armaments," the shopkeeper says,
their voice echoing with experience. "How may I assist you on your journey?"

Expressing your desire to aid the village and protect yourself, you inquire
about the availability of weapons and armor. The shopkeeper's gaze sweeps
across the store, pride evident in their demeanor.

"Our selection of weapons and armor is renowned," the shopkeeper replies,
gesturing to the displays. "We offer a variety of options to suit different
fighting styles and levels of protection."

They point towards a set of gleaming armor, constructed with meticulous
attention to detail. "For a sum of 50 coins, you can acquire a set of sturdy
armor, crafted to shield you from the perils that lie ahead."

The shopkeeper's gaze then shifts to an assortment of weapons, their edges
honed to perfection. "Alternatively, we have an array of weapons available for
30 coins. Each weapon is designed to unleash your combat potential and vanquish
any adversaries you may encounter." He says.""")
  print(" ")
  printslow(f"You have {money} coins")
  print(" ")
  printslow("Choices: A = Armor, S = Sword, Leave = Leave shop.")
  print(" ")
  wantstuff = input("Would you like to buy from the armor shop?:" ).lower()
  if wantstuff == "":
    printslow("You have to enter something!")
    time.sleep(2)
  if wantstuff == "a":
    printslow("Let's see how much money you have.")
    time.sleep(3)
    if money < 50:
      print(" ")
      printslow("You can not afford this armor says the shopkeep as they put it back up.")
      time.sleep(3)
      scenescroll()
      locmenu()
      gowhere()
    if money >= 50:
      print(" ")
      printslow("A wise choice! You exchange 50 coins and put the armor on.")
      global armor
      armor = 1
      money -= 50
      time.sleep(3)
      printslow("You turn and head back into the town square.")
      time.sleep(3)
      scenescroll()
      locmenu()
      gowhere()
  if wantstuff == "s":
    printslow("The shop keep lays a masterful crafted sword on the table")
    print(" ")
    printslow('"Lets see how much money you have" He says.')
    print(" ")
    if money >= 30:
      printslow('"Wise choice!" He says as you had over 30 coins and take the sword.')
      money -= 30
      global sword
      sword = 1
      time.sleep(3)
      printslow("You turn and head back into the town square.")
      time.sleep(3)
      scenescroll()
      locmenu()
      gowhere()
    if money < 30:
      printslow('"Im sorry, but you dont have enough coins for this" says the shopkeeper.')
  if wantstuff == "leave":
      printslow("The shop keep waves as you turn and head back into the town square.")
      time.sleep(3)
      scenescroll()
      locmenu()
      gowhere()
  else:
    printslow("That's not a valid input!")
    locmenu()
    gowhere()

def outside():
  printslow(""""You head outside of Wildridge along the roads you've heard to be troubled.
You come to a fork in the road with 4 paths. Yes, 4 paths. I'm running out of time and brainpower
to think of how to get to these locations, get over it adventurer. AS I WAS SAYING.

You come to a fork of 4 paths, the first leads to the area you've heard villagers were
being attacked by goblins at. The second leads to a den occupied by spiders terrorizing
villagers as they get near. The third leads along a road known to be frequented by trolls.
Lastly a road leads to neaby farms where you've heard a griffin is. You may find these
monsters while travelling to these locations if you have taken the contract from the
town board. (That means go get the proper paper or nothing will happen, adventurer.)""")
  smallscroll()
  outmenu()
  outwhere()


def tavern():
  printslow("""As you step inside the bustling tavern, the lively sounds of clinking mugs
and cheerful laughter fill the air. Warmth embraces you as the cozy ambiance
welcomes weary adventurers and villagers alike. The aroma of hearty meals and
rich ale permeates the room, enticing the senses. Patrons gather around sturdy
wooden tables, engrossed in animated conversations and boisterous tales of their
exploits.

Behind the worn wooden bar stands the tavern keeper, a friendly face with a
twinkle in their eye. They skillfully pour drinks and serve plates piled high
with savory dishes. The crackling fireplace casts a soft glow, casting dancing
shadows upon the walls adorned with weathered maps and old weapons. In one corner,
a group of adventurers huddle together, planning their next daring quests. Their
gear, worn and marked by battles fought, speaks of their experiences and the
dangers they have faced.

As you find a seat at an empty table, you catch snippets of conversations—a
whispered rumor about a long-lost treasure, a bard playing a haunting melody,
and a weary traveler seeking refuge from a recent encounter with mythical creatures.

The tavern provides solace and camaraderie, a place where friendships are forged,
and stories are shared. It is a sanctuary where the weight of the world momentarily
lifts, offering respite from the perils that await beyond its walls.

In this haven of tales and merriment, you take a moment to rest, gather information,
and perhaps find companions for your own grand adventures that lie ahead.""")
  print(" ")
  time.sleep(3)
  printslow("""After resting you feel much better and go back outside.
  YOUR HEALTH HAS BEEN HEALED""")
  print(" ")
  health = 100
  scenescroll()
  time.sleep(3)
  locmenu()
  gowhere()

def notdone():
  print(" ")
  printslow("Unfortunately this is as far as I've gotten :(")
  print(" ")
  printslow("Game will close in 30 seconds.")
  print(" ")
  print("30")
  time.sleep(1)
  print("29")
  time.sleep(1)
  print("28")
  time.sleep(1)
  print("27")
  time.sleep(1)
  print("26")
  time.sleep(1)
  print("25")
  time.sleep(1)
  print("24")
  time.sleep(1)
  print("23")
  time.sleep(1)
  print("22")
  time.sleep(1)
  print("21")
  time.sleep(1)
  print("20")
  time.sleep(1)
  print("19")
  time.sleep(1)
  print("18")
  time.sleep(1)
  print("17")
  time.sleep(1)
  print("16")
  time.sleep(1)
  print("15")
  time.sleep(1)
  print("14")
  time.sleep(1)
  print("13")
  time.sleep(1)
  print("12")
  time.sleep(1)
  print("11")
  time.sleep(1)
  print("10")
  time.sleep(1)
  print("9")
  time.sleep(1)
  print("8")
  time.sleep(1)
  print("7")
  time.sleep(1)
  print("6")
  time.sleep(1)
  print("5")
  time.sleep(1)
  print("4")
  time.sleep(1)
  print("3")
  time.sleep(1)
  print("2")
  time.sleep(1)
  print("1")
  time.sleep(1)
  print("Goodbye")
  time.sleep(1)



def goblins():
  printslow("""'The village is plagued by mischievous goblins! These cunning
creatures have been causing chaos in the surrounding area, stealing supplies,
and harassing the villagers. Their hideout is rumored to be in the
nearby forest. The village desperately seeks a brave adventurer to
confront the goblin problem and restore peace to the land.'""")
  print(" ")
  time.sleep(5)
  printslow("You put the paper in your bag to keep for later")
  time.sleep(2)

def spiders():
  printslow("""'Giant spiders have infested the village outskirts,
spinning their webs and terrorizing the locals. Their venomous bites pose
a grave threat to the villagers, and the webs are hindering trade
routes. The village is in urgent need of a fearless hero to venture
into the dark depths where the spiders dwell and eliminate the
eight-legged menace once and for all.'""")
  print(" ")
  time.sleep(5)
  printslow("You put the paper in your bag to keep for later")
  time.sleep(2)

def trolls():
  printslow("""'Danger lurks beneath the ancient bridge that connects the village
to the neighboring lands. Ferocious trolls have claimed the area as their own,
demanding tolls from travelers and causing fear among the villagers.
Their immense strength and thick skin make them formidable adversaries.
The village seeks a strong and skilled warrior to stand against the
troll menace and safeguard the village's access to the outside world.'""")
  print(" ")
  time.sleep(5)
  printslow("You put the paper in your bag to keep for later")
  time.sleep(2)

def griffin():
  printslow("""'A mythical and fearsome creature, the Killer Griffin, has been sighted
in the skies above the village. This majestic yet deadly beast preys on livestock
and poses a threat to the villagers' safety. Its razor-sharp talons and
powerful beak make it a formidable opponent. Any adventurer willing
to face this deadly creature would be wise to equip themselves with
sturdy armor to withstand its attacks.' The beast can be found outside of town.""")
  print(" ")
  time.sleep(5)
  printslow("You put the paper in your bag to keep for later")
  time.sleep(2)

def boptions():
  tasks = ["Goblin Problem!", "Creepy Spiders!", "Troll Menace!", "Killer Griffin!"]
  selection = random.choice(tasks)
  printslow(f"You reach out and take a paper titled {selection}")
  print(" ")
  time.sleep(3)
  if selection == "Goblin Problem!":
    printslow(f"The paper details a problem with nearby populace of goblins.")
    print(" ")
    printslow("You begin reading...")
    smallscroll()
    print(" ")
    time.sleep(2)
    goblins()
    global goblinpaper
    goblinpaper += 1
    time.sleep(3)
    smallscroll()
    locmenu()
    gowhere()
  if selection == "Creepy Spiders!":
    printslow(f"The paper details an infestation of spiders in a den nearby.")
    print(" ")
    printslow("You begin reading...")
    smallscroll()
    print(" ")
    time.sleep(2)
    spiders()
    time.sleep(3)
    global spiderpaper
    spiderpaper += 1
    smallscroll()
    locmenu()
    gowhere()
  if selection == "Troll Menace!":
    printslow(f"The paper details a group of trolls nearby attacking travellers.")
    print(" ")
    printslow("You begin reading...")
    smallscroll()
    print(" ")
    time.sleep(2)
    trolls()
    global trollpaper
    trollpaper += 1
    smallscroll()
    locmenu()
    gowhere()
  if selection == "Killer Griffin!":
    printslow(f"The paper details a problem with a griffin attacking farmers.")
    print(" ")
    printslow("You begin reading...")
    smallscroll()
    print(" ")
    time.sleep(2)
    griffin()
    time.sleep(3)
    global griffinpaper
    griffinpaper += 1
    smallscroll()
    locmenu()
    gowhere()

def locmenu():
  print(" ")
  printslow("Where would you like to go?")
  print(" ")
  printslow("(Enter Number of Option)")
  print(" ")
  print("[1] Help Wanted Board")
  print("[2] Armor and Weapons Shop")
  print("[3] Apothecary Shop")
  print("[4] Tavern")
  print("[5] Town Hall")
  print("[6] Stand and do nothing")
  print("[7] Head out of the oposite side of town")
  print(" ")
locmenu()

def outmenu():
  print(" ")
  printslow("Where would you like to go?")
  print(" ")
  printslow("(Enter Number of Option)")
  print(" ")
  print("[1] Goblin Road")
  print("[2] Spider Den")
  print("[3] Troll Road")
  print("[4] Griffin Farms")
  print("[5] Back to Town")
  print(" ")

def outwhere():
    while True:
      choice = input('Enter 1-5: ')
      if choice == "":
          printslow("You have to enter something!")
          print(" ")
          time.sleep(3)
          break
      if choice == "1":
          printslow("You head down the road plagued by goblins.")
          print(" ")
          time.sleep(3)
          smallscroll()
          goblinloc()
          break
      if choice == "2":
          printslow("You head down the path to the spiders den.")
          print(" ")
          time.sleep(3)
          smallscroll()
          spiderloc()
          break
      if choice == "3":
          printslow("You head down the road where trolls were sighted.")
          print(" ")
          time.sleep(3)
          smallscroll()
          trollloc()
          break
      if choice == "4":
          printslow("You head towards the farms where the griffin was sighted.")
          print(" ")
          time.sleep(3)
          smallscroll()
          griffinloc()
          break
      if choice == "5":
          printslow("You head back into town.")
          print(" ")
          time.sleep(3)
          smallscroll()
          locmenu()
          gowhere()
          break
      else:
        printslow("That's not a valid choice!")
        print(" ")
        time.sleep(3)

def gowhere():
    while True:
      choice = input('Enter 1-7: ')
      if choice == "":
          printslow("You have to enter something!")
          print(" ")
          time.sleep(3)
          break
      if choice == "1":
          printslow("You walk over to the paper covered board.")
          print(" ")
          time.sleep(3)
          smallscroll()
          boptions()
          break
      if choice == "2":
          printslow("You walk into the armor shop.")
          print(" ")
          time.sleep(3)
          smallscroll()
          ashop()
          break
      if choice == "3":
          printslow("You head into the potion shop greeted with sweet smells.")
          print(" ")
          time.sleep(3)
          smallscroll()
          pshop()
          break
      if choice == "4":
          printslow("You head into the noisey tavern.")
          print(" ")
          time.sleep(3)
          smallscroll()
          tavern()
          break
      if choice == "5":
          printslow("You walk into the town hall.")
          print(" ")
          time.sleep(3)
          smallscroll()
          thall()
          break
      if choice == "6":
          printslow("You decide to stand and do nothing at all.")
          print(" ")
          time.sleep(3)
          smallscroll()
          print("Then you decide you need to do soemthing.")
          smallscroll()
          locmenu()
          gowhere()
      if choice == "7":
          printslow("You head outside of town to the troubled areas.")
          print(" ")
          time.sleep(2)
          outside()
          time.sleep(3)
          smallscroll()
          outmenu()
          outwhere()
          break
      else:
        printslow("That's not a valid choice!")
        print(" ")
        time.sleep(3)

gowhere()

