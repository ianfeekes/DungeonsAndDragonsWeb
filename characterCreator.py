import random 

#Bunch of global variables 
races = ["human", "halfling", "gnome", "half-orc", "dwarf", "half-Elf", "elf"]
stats = {
    "Strength":0,
    "Dexterity":0,
    "Wisdom":0,
    "Charisma":0,
    "Constitution": 0,
    "Intelligence": 0, 
}

barbarianSkills = ["climb", "craft", "handle animal", "intimidate", "jump", "listen", "ride", "survival", "swim"]
bardSkills = ["appraise", "balance", "bluff", "climb", "concentration", "craft", "decipher script", "diplomacy", "disguise", "escape artist", "gather information", "hide", "jump", "listen", "move silently", "perform", "profession"]


"""classSkills = {
  "barbarian":barbarianSkills,
  "bard":bardSkills,
  "cleric":clericSkills,
  "druid":druidSkills,
  "fighter":fighterSkills,
  "monk":monkSkills,
  "paladin":paladinSkills,
  "ranger":rangerSkills,
  "rogue":rogueSkills,
  "sorcerer":sorcererSkills,
  "wizard":wizardSkills
}"""


classes = ["barbarian", "bard", "cleric", "druid", "fighter", "monk", "paladin", "ranger", "rogue", "sorcerer", "wizard"]
spellcasters = ["bard", "cleric", "druid", "sorcerer", "wizard"]


class character: 
  
  def __init__(self, name, gender, race, profession, stats): 
    #Fill out data fields 
    self.name = name 
    self.race = race 
    self.profession = profession 
    self.stats = stats 
    self.gender = gender 

    #Every character gets to choose their skills 
    #self.chooseSkills() 

    #self.chooseEquipment()

    #If we have a spellcaster character we want to choose their spells 
    #if self.profession in spellcasters: 
      #self.chooseSpells()

  """def chooseSkills(): 
    #TO DO


  def chooseEquipment(): 
    #TO DO 

  def chooseSpells():
    #TO DO 
  """
  def toFile(self, filename): 
    outFile = open(filename, "w")
    nameStr = "Name: "+self.name+"\n"
    outFile.write(nameStr)
    raceStr = "Race: "+self.race+"\n"
    outFile.write(raceStr)
    genderStr = "Gender: "+self.gender+"\n" 
    outFile.write(genderStr) 
    classStr = "Class: "+self.profession+"\n" 
    outFile.write(classStr)
    for i in self.stats: 
        numWhitespace = 15-len(i) 
        lineStr = i 
        for j in range(0,numWhitespace): 
            lineStr = lineStr+" "
        lineStr = lineStr+str(stats[i])+"\n"
        outFile.write(lineStr) 
    outFile.close() 
    
def generateStats(): 
    ret=[] 
    for i in range(0,6): 
        v = random.randint(1,6) 
        x  = random.randint(1,6)
        y = random.randint(1,6)
        z = random.randint(1,6)
        toAppend = v+x+y+z-min(v,x,y,z)
        ret.append(toAppend) 
    return ret 

def createCharacter(): 
  print("Enter the name of your new adventurer: ")
  name = input()
  print("Now to select your gender (Non-spectrum):" )
  gender = input() 
  while gender!= "male" and gender!= "female": 
    print("get outta here with that pc shit bro. Enter a real gender: ")
    gender = input() 
  print("Now to select your race: ") 
  print("Humans have no ability adjustments but get an extra feat (perk)")
  print("Dwarfs are extra hardy and tend to be a little uggo/unlikeable") 
  print("Elves have great hands (tossin) but aren't super healthy")
  print("Gnomes get that extra constitution but no strength. Great for not being a fighter while having strong fighting stats")
  print("Half elves literally get nothing lol") 
  print("Half orcs (you can be a full orc and I won't tell anyone) get extra strength and less intelligence") 
  print("Halflings get less dexterity and extra strength") 

  print(races)
  race = input() 
  while race not in races: 
      print("Enter a vlid race") 
      race = input().lower()  

  print("Now we are generating your stats. There are six attributes to choose from")
  print() 
  print("Strength affects your fighting prowess. Smashin skulls, intimidating thots, breaking the pussy's ankles") 
  print("Dexterity affects your nimbleness. Mostly useful for nasty heddies and juggling")
  print("Constitution affects how healthy you are and resistant to poison you are. More botfeld chicken you can eat.") 
  print("Intelligence is basically how good you are at python and fireballs") 
  print("Wisdom is your willpower. The time you can take on t breaks, and as a cleric the spells you can cast (how many lyrics you know from prince of egypt, how often you visit chabad") 
  constAttributes = generateStats()  
  constAttributes.sort() 
  attributes = constAttributes
  print("Your values to choose from are the following: ")
  print(attributes) 
  confirmation = "yes" 
  while confirmation == "y" or confirmation== "yes": 
    for i in stats: 
        stats[i]=0
        print("Your remaining values to allocate to your character's attributes are: ")
        print(attributes) 
        print("We are now choosing a value for: ",i)
        attributeInput = int(input())
        while attributeInput not in attributes:
            print("Error: You entered a value that is not presented in your generated attributes, retard. Keep trying...")
            attributeInput = int(input()) 
        stats[i]=attributeInput
        attributes.pop(attributes.index(attributeInput))
        print() 
    print("Now you have settled your attributes. With the racial adjustment, here is what they are: ") 
    for i in stats: 
      if race=="halfling":
          if i=="dexterity": stats[i]+=2
          elif i=="strength": stats[i]-=2
      elif race=="gnome": 
          if i=="constitution": stats[i]+=2
          elif i=="strength": stats[i]-=2
      elif race =="half-orc": 
          if i=="strength":stats[i]+=2
          elif i=="intelligence":stats[i]-=2
      elif race=="dwarf": 
          if i=="constitution":stats[i]+=2
          elif i=="charisma":stats[i]-=2
      elif race=="elf":
          if i=="dexterity":stats[i]+=2
          elif i=="constitution":stats[i]-=2 
      print(i, ": ", stats[i]) 
    print("If you made a mistake when allocating your attributes, or want to re-choose, then please press 'yes' or 'y' else type any other key: ") 
    confirmation = input()
    attributes = constAttributes
    if confirmation!="yes" and confirmation!="y": break 
  print()  
  print("Now to choose your class. This will give you benefits for what you want your character to do. The descriptions for your options are as following: ")
  print("Barbarian: a ferocious waarrior who uses fury and instinct to bring down foes (with the exception of Epstein") 
  print("Bard: A performer whose music works magic -- a wanderer, a tale-teller, and a jack of all trades") 
  print("Cleric: A master of divine jewish magic and a capable warrior as well") 
  print("Druid: A porter specimen who dwars energy from the natural vegan whole foods world to cast divine spells and gain strange magical powers") 
  print("Fighter: A warrior with exceptional combat capability and unequaled skill with weapons. Probably owns a replica katana")
  print("Monk: A martial artist whose unarmed strikes hit fast and hard -- a master of exotic powers. Meditates at least twice a day")
  print("Paladin: A paladin of social justic and destroyer of evil, protected and strengthened by an array of divine jewish powers") 
  print("Ranger: A cunning, skilled warrior of the wilderness. Gets a favored enemy")
  print("Rogue: A tricky, skillful scout and spy who wins the battle by stealth rather than brute force. Basically the nigga who ate all my protein scoop by fucking scoop over the last three months you fucker") 
  print("Sorcerer: A spellcaster with inborn magical ability (doesn't have to use a book but can't specialize")
  print("Wizard: has to own a spellbook, but can specialize eg enchanter, conjurer, necromancer, etc")
  print()
  print("Now enter which class you wish to be: ")
  print(classes) 
  charClass = input() 
  while charClass not in classes:
    print("Please enter a valid class name") 
    print(classes) 
    charClass = input().lower() 

  c = character(name, gender, race, charClass, stats) 
  
  

  

  print("Great. We're done generating everything for now. Please enter an alphanumeric filename you wish this to be saved as: ")
  fileStr = input() 
  c.toFile(fileStr)  

  
createCharacter() 