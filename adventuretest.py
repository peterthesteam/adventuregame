
# Adventure game test piece
# Written by Peter Griffiths
# Based on the original Colossal Cave adventure.

import random
#----------Stock Phrases
A1 = "Nothing happens."
A2 = "\nI'm sorry, I cannot obey that command."
A3 = "There is no"
A4 = "You do not have"
A5 = "'We wish you good luck in your adventures.' \nHe then bows, and disappears back into the tunnels."
A6 = "all this with interest. He then steps forward and says \n'Well done, we have been trying to get rid of that dragon for years'."
A7 = "The dwarf chuckles, and says 'I think you are a bit mixed up,"
A8 = "is this station.'"
A9 = "You are engulfed in a cloud of"
B1 = "a disembodied voice intones:-"
B2 = "\nThere is no dragon here."
B3 = "\nThe sign reads  - "
Nogo = "You can't go that way."
Ws = "The driver asks 'Which station do you want Guv?'"
Sp = "\nYou will have to be more specific in your instructions."
Poof = "\n      ------ POOF!!! ------\n"

#-------------   Class data for rooms
class LocationData:
        def __init__(self,Name,Description,exits,underground):
                self.Name=Name
                self.Description=Description
                self.exits=exits
                self.underground=underground

        def getexit(self,exitname):
                if exits.has_key(exitname):
                        return exits[exitname]
                else:
                        return None

#location data ------- name - description - exits - underground
Locations = {"ROOM1":
LocationData("ROOM1","standing on a cracked and broken road with a big building to the west. \nPiles of rubble surround you."
             "\nThe doorway to the building is open.",{"n":"ROOM1","w":"ROOM2","s":"ROOM21","e":"ROOM1"},False),
             "ROOM2":
LocationData("ROOM2","standing in a crumbling foyer of a disused public hall. \nThe entrance doorway is to the east, with another large door to the west."
             "\nA set of stairs lead upwards and a small doorway leads south. \nA faded sign reads VICTORIA HALL.",
             {"e":"ROOM1","s":"ROOM7","w":"ROOM3","u":"ROOM8"},False),
             "ROOM3":
LocationData("ROOM3","standing at the east end of the main hall under a balcony.",
             {"e":"ROOM2","w":"ROOM4","u":"ROOM3"},False),
             "ROOM4":
LocationData("ROOM4","standing at the west end of the hall by the stage. \nThere is a small door leading down under the stage front."
             "\nAnother door leads off to the south. \n A set of steps lead up onto the stage.",
             {"e":"ROOM3","s":"ROOM14","u":"ROOM5","d":"ROOM6"},False),
             "ROOM5":
LocationData("ROOM5","standing on the bare stage of the hall. \nThere is an old switchboard in the corner."
             "\nAbove it is a big red button with a sign attached. \nBeside it is a small turn switch marked \nGENERATOR",
              {"d":"ROOM4","e":"ROOM4"},False),
             "ROOM6":
LocationData("ROOM6","in a low, dimly lit space under the main stage. \nThe way out is east, but a small dark crawlway runs out south.",
             {"e":"ROOM4","s":"ROOM9"},False),
             "ROOM7":
LocationData("ROOM7","standing in what used to be an old Police Office. \nThere is a large sign on the wall saying:- \nDEPOSIT ALL VALUABLES HERE",
             {"n":"ROOM2","w":"ROOM66"},False),
             "ROOM8":
LocationData("ROOM8","on the balcony overlooking the hall interior. \nA set of stairs lead down.",
             {"d":"ROOM2"},False),
             "ROOM9":
LocationData("ROOM9","in a low north - south crawlway. \nHalfway along, there is a hole leading downwards.",
             {"n":"ROOM6","d":"ROOM10","s":"ROOM11"},True),
             "ROOM10":
LocationData("ROOM10","in a long steeply sloping corridor that curves round sharply. \nIt runs east to north.",
             {"e":"ROOM9","n":"ROOM31","d":"ROOM31","u":"ROOM9"},True),
             "ROOM11":
LocationData("ROOM11","in a large round cavern hewn out of solid rock. \nThere are small exits to the north and west,"
             " \nwith a large rounded tunnel running downwards to the east, \nand a high passage sloping down to the south.",
             {"n":"ROOM9","w":"ROOM12","d":"ROOM43","e":"ROOM43","s":"ROOM46"},True),
             "ROOM12":
LocationData("ROOM12","standing at a junction of two passages on the edge of a deep chasm."
             "\nLow passages lead off south and west.",{"s":"ROOM11","w":"ROOM22","d":"ROOM12"},True),
             "ROOM14":
LocationData("ROOM14","in a small box room to the side of the hall. \nThe doorway is north, and a small stairway leads upwards.",
             {"n":"ROOM4","u":"ROOM15"},False),
             "ROOM15":
LocationData("ROOM15","on a landing in the middle of a long set of stairs. \nThe stairway going down has plastered walls, but the stairway"
             " \ngoing upwards is cut from solid rock.",{"d":"ROOM14","u":"ROOM16"},False),
             "ROOM16":
LocationData("ROOM16","at the top of a long stairway. There is a trapdoor above you.",
             {"d":"ROOM15","u":"ROOM17"},False),
             "ROOM17":
LocationData("ROOM17","in the middle of a forest. Winding paths go in all directions. \nA trapdoor is set into the path here.",
             {"d":"ROOM16","w":"ROOM18","s":"ROOM18","n":"ROOM19","e":"ROOM20","in":"ROOM16"},False),
             "ROOM18":
LocationData("ROOM18","in the middle of a forest. Winding paths go in all directions.",
             {"n":"ROOM20","w":"ROOM19","s":"ROOM19","se":"ROOM21","e":"ROOM17","nw":"ROOM19"},False),
             "ROOM19":
LocationData("ROOM19","in the middle of a forest. Winding paths go in all directions.",
             {"n":"ROOM18","e":"ROOM18","w":"ROOM20","s":"ROOM21","sw":"ROOM21","ne":"ROOM18"},False),
             "ROOM20":
LocationData("ROOM20","in the middle of a forest. Winding paths go in all directions.",
             {"n":"ROOM18","s":"ROOM19","e":"ROOM17","w":"ROOM21","sw":"ROOM18"},False),
             "ROOM21":
LocationData("ROOM21","on a hill, with forest surrounding you on three sides. \nA small road starts here and curves down around the hillside towards"
             " \na large building.",{"e":"ROOM1","d":"ROOM1","w":"ROOM18","s":"ROOM19","nw":"ROOM17","n":"ROOM20"},False),
             "ROOM22":
LocationData("ROOM22","in a debris room filled with stuff washed down from the surface. \nA low wide passage with cobbles leads east,"
             " \nand and an awkward canyon leads downwards to the west. \nA large sign of fiery letters hovers near the roof.",
             {"e":"ROOM12","d":"ROOM23","w":"ROOM23"},True),
             "ROOM23":
LocationData("ROOM23","in an awkward sloping east/west canyon. \nA large passage slopes upwards to the north.",
             {"e":"ROOM22","w":"ROOM24","n":"ROOM46"},True),
             "ROOM24":
LocationData("ROOM24","in a splendid chamber 30 feet high. \nThe walls are frozen rivers of orange stone."
             " \nAn awkward canyon and a good passage exit from east and west side of the chamber."
             "\nHigh up on one wall there is an opening, \nbut you cannot get up to it.",
             {"e":"ROOM23","w":"ROOM25"},True),
             "ROOM25":
LocationData("ROOM25","standing next to a small pit breathing traces of white mist. \nA small crack leads to the east,"
             " \nand very rough stone steps lead down.",{"e":"ROOM24","d":"ROOM26"},True),
             "ROOM26":
LocationData("ROOM26","in the bottom of a small pit. The walls are extremely damp. \nThere is a small pool of water in the corner,"
             "\nfed by a trickle running out of a crack in the rock.\nVery rough stone steps lead upwards, and a passage leads north."
             "\nA notice is attached to the wall here.",{"u":"ROOM26","n":"ROOM27"},True),
             "ROOM27":
LocationData("ROOM27","standing in the bottom of a huge chasm. The chasm goes northwards, \nand passages lead off east, south and west.",
             {"e":"ROOM29","w":"ROOM35","n":"ROOM28","s":"ROOM26"},True),
             "ROOM28":
LocationData("ROOM28","at the north end of a huge chasm. \nPassages lead off east and west.",
             {"s":"ROOM27","e":"ROOM68","w":"ROOMx"},True),
             "ROOM29":
LocationData("ROOM29","in a maze of twisty little passages, all different.",
             {"n":"ROOM30","s":"ROOM27","d":"ROOM31","u":"ROOM30","e":"ROOM32","ne":"ROOM34"},True),
             "ROOM30":
LocationData("ROOM30","in a maze of little twisty passages, all different.",
             {"u":"ROOM29","n":"ROOM31","s":"ROOM32","e":"ROOM34"},True),
             "ROOM31":
LocationData("ROOM31","in a little maze of twisty passages, all different.",
             {"w":"ROOM10","e":"ROOM30","s":"ROOM34","n":"ROOM32","u":"ROOM29","sw":"ROOM29"},True),
             "ROOM32":
LocationData("ROOM32","in a twisty maze of little passages, all different.",
             {"w":"ROOM33","e":"ROOM31","n":"ROOM29","w":"ROOM30","d":"ROOM34","s":"ROOM34"},True),
             "ROOM33":
LocationData("ROOM33","at a dead end. The only way out is east.",{"e":"ROOM32"},True),
             "ROOM34":
LocationData("ROOM34","in a little twisty maze of passages, all different.",
             {"e":"ROOM31","s":"ROOM32","w":"ROOM30","d":"ROOM29","nw":"ROOM30","se":"ROOM32"},True),
             "ROOM35":
LocationData("ROOM35","on the edge of a wide canyon running north/south. \nDown in the canyon bottom narrow railway tracks can be seen.",
             {"n":"ROOM27","s":"ROOM36","d":"ROOM35"},True),
             "ROOM36":
LocationData("ROOM36","standing at the bottom of a very tall pit. \nA small opening goes north",
             {"n":"ROOM35","u":"ROOM37"},True),
             "ROOM37":
LocationData("ROOM37","in a large room full of dusty rocks. \nThere is a big hole in the floor,"
             "\nand a passage leading east",
             {"d":"ROOM36","e":"ROOM38"},True),
             "ROOM38":
LocationData("ROOM38","at a complex junction. A low hands and knees passage from \nthe north joins a higher from the east,"
             "\nto make a walking passage going west.",{"w":"ROOM37","e":"ROOM39","n":"ROOM67"},True),
             "ROOM39":
LocationData("ROOM39","in a large room carved out of sedimentary rock. \nThe floor and walls are filled with bits of shells"
             "\nembedded in the stone. A shallow passage leads downwards \nand a steeper one leads up."
             "\nA low passage enters from the west.",{"w":"ROOM38","u":"ROOM42","d":"ROOM40"},True),
             "ROOM40":
LocationData("ROOM40","in a long sloping corridor with jagged walls. \nThe corridor continues downwards."
             "\nThe large room is located upwards.",{"u":"ROOM39","d":"ROOM41"},True),
             "ROOM41":
LocationData("ROOM41","in a cul-de-sac about eight feet aross. \nThere is no obvious exit except back up the sloping corridor."
             "\nA huge clam nearly fills the cave here.",{"u":"ROOM40"},True),
             "ROOM42":
LocationData("ROOM42","in a large arched hall. \nThere are exits to the west and south.",
             {"w":"ROOM39","s":"ROOM67"},True),
             "ROOM43":
LocationData("ROOM43","in a large round tunnel lined with white glazed tiles. \nThe tunnel slopes down to the east.",
             {"w":"ROOM11","u":"ROOM11","e":"ROOM44","d":"ROOM44"},True),
             "ROOM44":
LocationData("ROOM44","standing on the platform of a small underground railway. \nNarrow tracks run into smaller tunnels at the"
             " \nnorth and south ends of the platform. \nA white tiled tunnel leads upwards to the west."
             " \nA large sign beside you reads S1,",{"w":"ROOM43","u":"ROOM43","n":"ROOM44","s":"ROOM44"},True),
             "ROOM45":
LocationData("ROOM45","in a large arched hall. \nThere are exits to the east and south.",
             {"e":"ROOMx","s":"ROOM47"},True),
             "ROOM46":
LocationData("ROOM46","in a long high passage that winds its way gently uphill \nin great sweeping curves.",
             {"u":"ROOM11","d":"ROOM23"},True),
             "ROOM47":
LocationData("ROOM47","standing at the north end of a huge hall. \nThe roof is held up by rock pillars,"
             "\nbeautifully carved to look like trees. \nA passage besides you leads north.",
             {"n":"ROOM45","s":"ROOM48"},True),
             "ROOM48":
LocationData("ROOM48","standing at the south end of a huge hall. \nThe roof is held up by wonderful carved pillars."
             "\nA wide stairway leads upwards.",{"n":"ROOM47","u":"ROOM49"},True),
             "ROOM49":
LocationData("ROOM49","standing on a landing at the top of a large staircase. \nA small corridor runs west and a large one runs east.",
             {"d":"ROOM48","w":"ROOM50","e":"ROOM51"},True),
             "ROOM50":
LocationData("ROOM50","in a little room with a window that overlooks a large hall.\nYou are nearly at the ceiling level of the hall."
             "\nThere is the top of a spiral staircase in one corner, \nand a doorway to the east.",{"e":"ROOM49","d":"ROOM55"},True),
             "ROOM51":
LocationData("ROOM51","in a huge smooth walled corridor leading east / west. \nA low doorway is set in the south wall.",
             {"e":"ROOM53","w":"ROOM49","s":"ROOM52"},True),
             "ROOM52":
LocationData("ROOM52","in a long narrow room with what look like stone desks against the walls. \nThere is a large rusty iron lever that stands"
             " \nin a slot, at the far end of the room. \nThe only exit is through the door in the north wall.",{"n":"ROOM51"},True),
             "ROOM53":
LocationData("ROOM53","in a large round room.",{"w":"ROOM51","e":"ROOM54"},False),
             "ROOM54":
LocationData("ROOM54","standing on a grassy ledge at the base of a large hill. \nIn front of you is a great plain of rolling grassland"
             "\nThe grass looks extremely tall, and waves in the breeze. \nPaths run off northeast and southeast into the grass."
             "\nTo the west is a huge cave entrance, flanked by two great holly trees.",
             {"w":"ROOM53","ne":"ROOMx","se":"ROOMx"},False),
             "ROOM55":
LocationData("ROOM55","in a small grey room. \nA spiral staircase runs up from the centre of the room, \nand passages run off north and west.",
             {"n":"ROOM63","w":"ROOM56","u":"ROOM50"},True),
             "ROOM56":
LocationData("ROOM56","standing in what seems to be an old workshop. \nOld work benches line the walls, and mysterious tool shapes"
             " \nare marked on the walls behind them. \nThe actual tools have been removed."
             "\nA passage runs east and a low crawl runs north.",{"e":"ROOM55","n":"ROOM57"},True),
             "ROOM57":
LocationData("ROOM57","standing on a ledge looking over a wide fissure. \nA stream of water emerges from a large pipe beneath your feet"
             "\nand falls over a waterwheel that turns slowly. \nA small crawlway runs south, but the ledge continues west.",
             {"s":"ROOM56","w":"ROOM58"},True),
             "ROOM58":
LocationData("ROOM58","at the end of a ledge that overlooks a wide fissure.\nA river runs at the bottom, fed by water falling"
             "\nover a waterwheel in the distance. The ledge runs east, \nand a very steep slippery path leads downwards.",
             {"e":"ROOM57","d":"ROOM59"},True),
             "ROOM59":
LocationData("ROOM59","on a tiny ledge at the edge of the river. \nUnfortunately the bottom of the path ended up as a sheer drop."
             "\nThere is no way you can get back up to the top. \nYour only chance of escaping is down the river,"
             "\nbut the current looks VERY strong!",{"d":"ROOMz"},True),
             "ROOM60":
LocationData("ROOM60","on a gravel shore at the edge of a huge underground lake.\nThe gravel area is quite small, with huge rocks at each end."
             "\nA water worn passage leads upwards to the north.",{"n":"ROOM62","u":"ROOM62"},True),
             "ROOM61":
LocationData("ROOM61","at the end of a small passage, standing on a rock ledge, \nnear the top of a huge 30 foot high chamber."
             "\nThe walls are frozen rivers of orange stone. \nIt would be possible to slide down to the bottom of the chamber,"
             "\nbut you would not get back up.",{"d":"ROOM24","s":"ROOM62"},True),
             "ROOM62":
LocationData("ROOM62","in a small room paved with round cobbles. \nA steep passage runs down south,"
             "\nand a low square passage runs upward to the north.",{"d":"ROOM60","s":"ROOM60","n":"ROOM61","u":"ROOM61"},True),
             "ROOM63":
LocationData("ROOM63","in a round north/south passage with white tiled walls. \nThe north end of the passage ends in a stairwell leading down.",
             {"s":"ROOM55","n":"ROOM64","d":"ROOM64"},True),
             "ROOM64":
LocationData("ROOM64","on an island platform for a narrow railway. \nEither side of you lie platforms going east/west."
             "\nThe tracks run into small dark tunnels. \nA set of stairs lead upwards.\nA large sign beside you reads S2,",
             {"u":"ROOM63","e":"ROOM64","w":"ROOM64"},True),
             "ROOM65":
LocationData("ROOM65","standing on the platform of a small underground railway. \nNarrow tracks run into smaller tunnels at the"
             " \nnorth and south ends of the platform. \nA cream tiled tunnel leads upwards to the east."
             " \nA large sign beside you reads S5,",
             {"u":"ROOM66","e":"ROOM66","n":"ROOM65","s":"ROOM65"},True),
             "ROOM66":
LocationData("ROOM66","standing in small dusty square room.\nA cream tiled tunnel leads downwards to the west"
             "\nA large polished brass button is set into the wall.",{"w":"ROOM65","d":"ROOM65","e":"ROOM7"},True),
             "ROOM67":
LocationData("ROOM67","in a very long low, wide crawlway which winds its \nway approximately in a north/south direction.",
             {"n":"ROOM42","s":"ROOM38"},True),
             "ROOM68":
LocationData("ROOM68","on a minstrels gallery overlooking a \nlarge ornate baronial hall."
             "\nA staircase leads down to the hall floor, \nand a doorway is to the west.",{"w":"ROOM28","d":"ROOM69"},True), 
             "ROOM69":
LocationData("ROOM69","in a large ornate baronial hall. \nA staircase leads up to an overlooking gallery."
             "\nA large doorway leads off to the north, \nand a smaller one leads east.",{"u":"ROOM68","n":"ROOM70","e":"ROOM71"},True),
             "ROOM70":
LocationData("ROOM70","in an oriental room. \nThe walls are vividly painted with oriental scenes."
             "\nThere is a large doorway to the south",{"s":"ROOM69"},True),
             "ROOM71":
LocationData("ROOM71","in a room that I haven't designed yet. \nA doorway leads west.",{"w":"ROOM69"},True),
             "ROOM72":
LocationData("ROOM72","in a room",{"e":"ROOMx"},True)}

# Item List Data ---- description - name - room - size number for carrying - score points
def ItemData():
        Item_list = ['a little jewel handled axe', 'axe','ROOM18', 2,2,'a silver coin','coin','ROOM8', 1,3,'a willow wand','wand','ROOM38',1,2,
                     'a small bunch of keys','keys','ROOM7',1,0,'a diamond encrusted tiara','tiara','ROOM22',1,5,
                     'a pearl earring','earring','ROOM14',1,2,'a polished brass bowl','bowl','ROOM4',2,2,
                     'a large jerrycan with a red label','jerrycan','ROOM24',4,0,'a small throwing knife','knife','ROOM201',0,0,
                     'a large pirates chest','chest','ROOM33',6,10,'a large diamond','diamond','ROOM47',1,5,
                     'a large glistening pearl','pearl','ROOM201',1,5,'a polished brass trumpet','trumpet','ROOM68',1,2,
                     'an oil tin with a spout','tin','ROOM56',1,0,'a jewel encrusted trident','trident','ROOM35',1,5,
                     'a gold nugget','nugget','ROOM9',1,6,'a large ruby','ruby','ROOM66',1,6,'a fine oriental rug','rug','ROOM70',2,5]
        return Item_list

# ----------- Routines -------------
def Blow_things():
        if CommandLine[1] == "null":
                print Sp
        elif CommandLine[1] == "trumpet":
                if Item_list[62] == CarryPlace:
                        #if CurrentRoom == "ROOMx":  ----  Jericho routine
                        #else:
                        print"\nPAAAARRRRP"
                else:
                        print A4,"the trumpet."
        else:
                print A2

#print out items I am carrying
def Carry():
        global Bowl_filled
        i = 1
        PrintedOut = False
        while i < len (Item_list):
                if Item_list[i+1] == CarryPlace:
                        if PrintedOut == False:
                                print "You are carrying"
                                PrintedOut = True
                        print "   ",Item_list[i-1]
                i=i+5
        if Bowl_filled == True and PrintedOut == True and Item_list[32] == CarryPlace:
                print "    The bowl is full of water."
        if PrintedOut == False:
                print "You are not carrying anything."

#Check for move command
def Check_move_command():
        global Move_command
        Move_command = False
        Move_list = ['n','s','e','w','u','d','nw','ne','sw','se']
        i = 0
        while i < len(Move_list):
                if Move_list[i] == Command:
                        Move_command = True
                i=i+1

#Climb Plant
def Climb_plant():
        global Plant_grown
        global CurrentRoom
        Np = " plant here."
        TooSmall = "The plant is far too small."
        if CommandLine[1] == "null":
                print Sp
                return
        if CommandLine[1] == "plant" and CommandLine[2] == "null" and CurrentRoom == "ROOM36":
                CommandLine[1] = "up"
                CommandLine[2] = "plant"
        elif CommandLine[1] == "plant" and CommandLine[2] == "null" and CurrentRoom == "ROOM37":
                CommandLine[1] = "down"
                CommandLine[2] = "plant"
        elif CommandLine[1] == "plant" and CommandLine[2] == "null":
                print A3 + Np
        if CurrentRoom == "ROOM36" or CurrentRoom == "ROOM37":
                if CommandLine[1] == "up" and CommandLine[2] == "plant":
                        if CurrentRoom == "ROOM36":
                                if Plant_grown == True:
                                        CurrentRoom = "ROOM37"
                                        PrintRoomData()
                                else:
                                        print TooSmall
                        else:
                                print "You cannot climb further up."
                elif CommandLine[1] == "down" and CommandLine[2] == "plant":
                        if CurrentRoom == "ROOM37":
                                if Plant_grown == True:
                                        CurrentRoom = "ROOM36"
                                        PrintRoomData()
                                else:
                                        print TooSmall
                        else:
                                print "You are already down."
        else:
                print A3 + Np

#Dead
def Dead_duck():
        global playing
        print "Oh dear, you seem to be dead..........."
        playing = False

#River description
def Down_river():
        print """
The river is so strong, it knocks you off your feet,
and washes you down into its deep caverns.
You seem to go for miles, with no chance of stopping.
Eventually you come out into a vast underground lake.

The current washes you ashore here, and I don't know how
you did it, but you have not dropped anything!!!!!

Obviously some magic has helped you to survive unscathed.
"""
        
#Main Dwarf Routine
def Dwarf_attack():
        global Dwarf_here
        global playing
        global Dwarf_happy
        global FuelLevel
        if Dwarf_here >0 and playing == True:
                if Locations[CurrentRoom].underground == True:
                        print "There is a threatening little dwarf in the room with you."
                        Dwarf_here = Dwarf_here + 1
                if Dwarf_here > 6:
                        print """
The dwarf has obviously finally lost patience with you,
and produces another knife, which he throws with deadly accuracy.
"""
                        Dead_duck()
        else:
                if Dwarf_total > 0 and FuelLevel > 0 and generate == True:
                        if Locations[CurrentRoom].underground == True and Dwarf_here <1:
                                if UnKnown < 5:
                                        if Dwarf_happy == False:
                                                print "\nA little dwarf appears and throws a knife towards you.\nLuckily for you, it misses."
                                                Item_list[42] = CurrentRoom
                                                Dwarf_here = 1
                                        else:
                                                print """
A little dwarf ambles past you and gives a cheery wave,
before disappearing back into the tunnels.
"""

#generator on
def GenerateRun():
        global generate
        global FuelLevel
        if CommandLine[1] == "null":
                print Sp
        elif CommandLine[1]=="switch":
                if CurrentRoom == "ROOM5":
                        if FuelLevel > 1:
                                if generate == False:
                                        print "There is the sound of a diesel engine starting up in the distance, \nthen a steady whine from a generator."
                                        generate = True
                                else:
                                        print "The distant sound of the generator dies away."
                                        generate = False
                        else:
                                print A2 ,
                                print " I think the generator has run out of fuel."
                else:
                        print A3,"switch to turn."
        else:
                print A2

#Get Water
def Get_water():
        global Bowl_filled
        Bowl_filled = False
        if CommandLine[1] == "null":
                print Sp
        elif CommandLine[0] == "fill" and CommandLine[1] == "bowl":
                CommandLine[1] = "water"
                CommandLine[2] = "with"
                CommandLine[3] = "bowl"
        if CommandLine[1]=="bowl" and CommandLine[3]=="water":
                CommandLine[1] = "water"
                CommandLine[3] = "bowl"
        if CommandLine[1] == "water":
                if CurrentRoom == "ROOM26":
                        if CommandLine[2]=="null":
                                print "How?"
                        elif CommandLine[3]=="bowl":
                                if Item_list[32]== CarryPlace:
                                        if Bowl_filled == True:
                                                print "The bowl is already full."
                                        else:
                                                print "You fill the bowl with water."
                                                Bowl_filled = True
                                else:
                                        print A4,"the bowl."
                        else:
                                print "I'm confused here. You cannot get water in the",CommandLine[3]
                else:
                        print A3,"water here."
        elif CommandLine[3] <> "water" or CommandLine[1] <> "bowl":
                print A2

#jump reply
def Jump_up():
        Reply_List = ["What am I, a kangeroo","WHEEEEEEEEEEEEEEEEE  ","I don't do jumping","BOINGGGGGGG","I don't like heights",
                      "Hmmm, will that do anything?"]
        UnKnown = random.randint(0, 5)
        print Reply_List[UnKnown]

#Kill answer routines
def Kill_reply():
        global y_n_request
        global Body_here
        y_n_request = 0
        if CommandLine[1] == "null":
                print Sp()
        elif CommandLine[1]=="dragon":
                if CurrentRoom=="ROOM27":
                        if DragonSlain == False:
                                if CommandLine[2]=="null":
                                        print "\nWith what, your bare hands?"
                                        y_n_request = 1
                                else:
                                        print "Sorry, that will not work."
                        elif Body_here == True:
                                print "The dragon is already dead."
                        else:
                                print B2
                else:
                        print B2
        elif CommandLine[1] == "dwarf":
                if Dwarf_here > 0:
                        print "\nHow? \nAnyway, that would not be a good idea."
                else:
                        print A3 ,"dwarf here."

#Kill off dragon
def Killoff_Dragon():
        global Body_here
        global DragonSlain
        global Treasure_total
        if DragonSlain == True:
                Treasure_total = Treasure_total + 10
                print """You throw the jerrycan out into the gap.
After a few seconds there is a clang, then a huge fireball
shoots up from the bottom of the chasm. There is a scream
of rage from the dragon, then a SPOINGGG sound.

The fireball disappears and there is silence.
It seems that the dragon has disappeared into another
dimension after your dastardly paraffin attack.
"""
        elif y_n_request >0:
                Body_here = True
                DragonSlain = True
                Treasure_total = Treasure_total + 20
                print "\nYou rush forward, and before the dragon knows it you have.........."
                print "GOOD GRIEF, you managed to strangle a dragon with your bare hands!!!!"
                print "Impressive!"
                Make_dwarf_happy()

# kill off things
def Kill_Off():
        global DragonSlain
        global Dwarf_happy
        global Dwarf_here
        global Dwarf_total
        global CarryAmount
        global playing
        ThrowUsed = False
        if CommandLine[1] == "null":
                print Sp
        elif CommandLine[1]=="jerrycan" and DragonSlain==False:
                if Item_list[37]==CarryPlace:
                        ThrowUsed = True
                        if CurrentRoom=="ROOM12":
                                Item_list[37]=None
                                CarryAmount = CarryAmount - Item_list[38]
                                DragonSlain = True
                                Killoff_Dragon()
                                Make_dwarf_happy()
                        elif CurrentRoom=="ROOM27":
                                print """
The jerrycan bursts open on the dragons scales.
It's fiery breath ignites the paraffin and produces a huge fireball.
Unfortunately you get incinerated by this.
"""
                                Dead_duck()
                return ThrowUsed
        elif CommandLine[1]=="knife":
                if Item_list[42] == CarryPlace:
                        UnKnown = random.randint(1, 100)
                        if Dwarf_here >0:
                                if UnKnown < 89:
                                        print "\nOh Dear. You killed a little dwarf. \nAs you watch, the body disappears in a puff of smoke."
                                        Dwarf_here = 0
                                        Dwarf_total = Dwarf_total - 1
                                        Item_list[42] = "ROOM201"
                                else:
                                        print "You Missed."
                                        Item_list[42] = CurrentRoom
                        else:
                                Item_list[42] = CurrentRoom
                                print "Knife thrown."
                        ThrowUsed = True
                        return ThrowUsed
        return ThrowUsed

#Magic Words
def Magic_words():
        global CurrentRoom
        Mword = False
        if CommandLine[0] == "izzywizzy":
                if CurrentRoom == "ROOM22":
                        CurrentRoom = "ROOM7"
                        Mword = True
                elif CurrentRoom == "ROOM7":
                        CurrentRoom = "ROOM22"
                        Mword = True
        if Mword == True:
                print Poof
                print A9,"orange smoke, which slowly clears......."
                PrintRoomData()
        else:
                print "\n",A1

#Make dwarfs happy
def Make_dwarf_happy():
        global Dwarf_happy
        global Dwarf_here
        if Dwarf_happy == False:
                Dwarf_happy = True
                if Dwarf_here > 0:
                        print " \nThe dwarf watches", A6
                        print A5
                        Dwarf_here = 0
                else:
                        print " \nA dwarf has appeared from the tunnels and has watched"
                        print A6
                        print A5    

# Help file
def MainHelp():
        print""" Welcome to Peters Test Adventure Game.

Find all the treasure, and bring it to the Police Office.
Magic sometimes works down in the caverns.

The caverns have mostly been opened up by the Dwarves,
in their never ending quest for GOLD.
Unfortunately they have been very badly treated by many
adventurers, and have got Very Annoyed! Be nice.

The main commands are :- n,s,e,w,ne,nw ..... u is up, d is down,
for moving north, south etc.

LOOK prints out your present location.
HELP will print this help out again.
QUIT or ESCAPE exits the game.
TAKE or GET an item, then DROP to put it down.
INVENT or INVENTORY will tell you what you are carrying.
READ to read notices etc.
PRESS
SCORE
THROW
TURN
UNLOCK

Some four word sentences can be understood, for example:
'Throw keys at dragon' will be understood (it won't do much good though!) 
More commands can be tried.
"""

#cannot move that way routine
def NoCanDo():
        if CurrentRoom == "ROOM1": print "Piles of rubble block your way."
        elif CurrentRoom == "ROOM3": print "It is far too high to get up there."
        elif CurrentRoom == "ROOM12" or CurrentRoom == "ROOM35": print "Oh come on - you would need a parachute to do that!"
        elif CurrentRoom == "ROOM26": print "The steps are far too wet and slippery to climb up."
        elif CurrentRoom == "ROOM44" or CurrentRoom == "ROOM64" or CurrentRoom == "ROOM65":
                print "An invisible force stops you, and",B1 , "\nNO UNAUTHORISED PERSONS ARE ALLOWED ON THE TRACKS."

#Open Things
def Open_Things():
        global Oyster_opened
        if CommandLine [1] == "null":
                print Sp
        elif CommandLine[1] == "clam" or CommandLine[1] == "oyster":
                if CurrentRoom == "ROOM41":
                        if Oyster_opened == False:
                                if Item_list[72] == CarryPlace:
                                        print """
The trident opens the shell nicely, and a huge pearl rolls out.
The clam was really an oyster! I'm not very good at sea shells!"
Having disgorged its pearl, the oyster shuts, and won't open again.
"""
                                        Item_list[57] = "ROOM41"
                                        Oyster_opened = True
                                else:
                                        print "You need the correct tool to open the",CommandLine[1]
                        else:
                                print "The oyster refuses to open again."
                else:
                        print A3, CommandLine[1], "here."
        elif CommandLine[1] == "jerrycan":
                if Item_list[37] == CarryPlace or Item_list[37] == CurrentRoom:
                        print "The lid is rusted shut. However the can gurgles as if it is full."
                else:
                        print A3,"jerrycan here."
        elif CommandLine[1] == "grating" or CommandLine[1] == "trapdoor":
                OpenExits()
        elif CommandLine[1] == "doors":
                if CurrentRoom == "ROOM53":
                        print "The doors are shut solidly."
                else:
                        print "There are no doors to open."
        else:
                print "I can't open the",CommandLine[1]

#Oil Lever
def Oil_lever():
        global Lever_oiled
        if CommandLine[1]=="null":
                print Sp
        elif CommandLine[1] == "lever":
                if CurrentRoom == "ROOM52":
                        if Item_list[67] == CarryPlace:
                                Lever_oiled = True
                                Item_list[67] = "ROOM201"
                                print """
The oil runs down the lever and into the mechanism below.
Unfortunately the now empty tin slips from your hand and disappears
down through the lever slot.
"""
                        else:
                                print A4,"any oil."
                else:
                        print A3,"lever here."
        else:
                print "I don't think oiling the", CommandLine[1], "will do any good."

#Unlock things
def OpenExits():
        global GratingOpen
        global TrapDoorOpen
        global CarryPlace
        ULPrint = "One of the keys unlocks the "
        ULPrint2 = " allowing it to open."
        if CommandLine[1] == "null":
                print Sp
                return
        if CurrentRoom == "ROOM6" or CurrentRoom == "ROOM9":
                if CommandLine[1] == "grating":
                        if GratingOpen == False:
                                if Item_list[17] == CarryPlace:
                                        print ULPrint + CommandLine[1] + ULPrint2
                                        GratingOpen = True 
                                else:
                                        print A4,"any keys."
                                        GratingOpen = False
                        else:
                                print "The grating is already unlocked."
        elif CurrentRoom == "ROOM16" or CurrentRoom == "ROOM17":
                if CommandLine[1] == "trapdoor":
                        if TrapDoorOpen == False:
                                if Item_list[17] == CarryPlace:
                                        print ULPrint + CommandLine[1] + ULPrint2
                                        TrapDoorOpen = True
                                else:
                                        print A4,"any keys."
                                        TrapDoorOpen = False
                        else:
                                print "The trapdoor is already unlocked."
        else:
                print A3, CommandLine[1], "to unlock."

#Pay dwarf
def Payment():
        global Dwarf_happy
        global Dwarf_here
        global CarryAmount
        global Treasure_total
        if CommandLine[1] == "dwarf" or CommandLine[3]=="dwarf":
                if Dwarf_here > 0:
                        if CommandLine[1]=="nugget" or CommandLine[3]=="nugget" or CommandLine[1]=="gold" or CommandLine[3]=="gold":
                                if Item_list[77] == CarryPlace:
                                        Dwarf_happy = True
                                        Dwarf_here = 0
                                        Item_list[77] = "ROOM201"
                                        CarryAmount = CarryAmount - 1
                                        Treasure_total = Treasure_total + 6
                                        print """
The dwarf accepts your donation, saying
'Welcome, friend!
You are free to roam the caverns without hindrance'.
"""
                                        print A5
                                else:
                                        print A4,"the gold nugget."
                        else:
                                print "The dwarf is not interested in anything but GOLD."
                else:
                        print A3,"dwarf here."
        else:
                print A2

#pick items up
def PickUp():
        global CarryAmount
        global Treasure_total
        if CommandLine[1] == "null":
                print Sp
                return
        if CommandLine[1]=="water":
                Get_water()
                return
        if CommandLine[1]=="clam":
                if CurrentRoom == "ROOM41":
                        print "The clam is far too big to carry, and the passage is far too narrow \nto get it out of here anyway."
                else:
                        print A3,"clam here."
                return
        if CommandLine[1]=="dragon":
                if CurrentRoom == "ROOM27" and DragonSlain == False:
                        print "Oh come on, you can't be serious about that!"
                elif CurrentRoom == "ROOM27" and Body_here == True:
                        print "The dragons body is far too heavy to move."                    
                else:
                        print A3,"dragon here."
                return
        if CommandLine[1]=="plant":
                if CurrentRoom == "ROOM36":
                        print "The plant is too deep rooted to remove."
                else:
                        print A3,"plant here."
                return
        if CommandLine[1] == "gold":
                CommandLine[1] = "nugget"
        i = 1
        while i < len (Item_list):
                if CommandLine[1] == Item_list[i]:
                        if Item_list[i+1] == CurrentRoom:
                                if Item_list[i+2] + CarryAmount > MaxCarryAmount:
                                        print "You can't carry any more."
                                        return
                                else:
                                        print Item_list[i], "taken."
                                        Item_list[i+1]=CarryPlace
                                        CarryAmount = CarryAmount + Item_list[i+2]
                                        if CurrentRoom == "ROOM7":
                                                Treasure_total = Treasure_total - Item_list[i+3]
                                        return
                        else:
                                print "\nThe",CommandLine[1], "is not here."
                i=i+5
        print A2

#press button routine
def PressButton():
        global playing
        global BB_pressed
        Bz = "There is a buzzing noise, ending in a 'POP'"
        Ds = "the east wall disappears as if by magic."
        if CommandLine[1] == "null":
                print Sp
        elif CommandLine[1]=="button":
                if CurrentRoom == "ROOM5":
                        print """
You just had to do it didn't you. Don't you read signs?
There is a huge explosion from under the stage,
resulting in th.........."""
                        Dead_duck()
                elif CurrentRoom == "ROOM44" or CurrentRoom == "ROOM64" or CurrentRoom == "ROOM65":
                        Train_run()
                elif CurrentRoom == "ROOM66":
                        if BB_pressed == False:
                                BB_pressed = True
                                print Bz
                                print "A whole section of",Ds
                        else:
                                BB_pressed = False
                                print Bz
                                print "The doorway in",Ds
                                
                else:
                        print A3,"button to press."
        else:
                print A2

# Print out location and items in room
def PrintRoomData():
        global Dark_count
        global playing
        Place = Locations[CurrentRoom]
        if Place.underground == True and generate == False:
                print "It is totally dark. \nIf you try to move, you may fall down a pit!"
                Dark_count = Dark_count + 1
                if Dark_count > 2:
                        print "Too late - you have tumbled down a pit."
                        Dead_duck()
        else:
                print ("You are"), Place.Description
                Dark_count = 0
                SpecialDescribe()
                i=2
                PrintedOut = False
                while i < len (Item_list):
                        if Item_list[i] == CurrentRoom:
                                if PrintedOut == False:
                                    print "There is:-"
                                    PrintedOut = True
                                print "   ",Item_list[i-2]
                        i=i+5
                if PrintedOut == True:
                        print "    here."
                if Item_list[32] == CurrentRoom and PrintedOut == True and Bowl_filled == True:
                        print "The bowl is filled with water."

#Pull Things
def Pull_lever():
        global Lever_oiled
        global Lever_pulled
        global Treasure_total
        if CommandLine[1] == "null":
                print Sp
        elif CommandLine[1] == "lever":
                if CurrentRoom == "ROOM52":
                        if Lever_oiled == True:
                                if Lever_pulled == False:
                                        Lever_pulled = True
                                        Treasure_total = Treasure_total + 10
                                        print """
With a loud grating sound, the lever slowly moves.
The oil you used obviously did it's job.
A low rumbling can be felt through the floor.
"""
                                else:
                                        print """
The lever is now stuck in it's open position, and cannot be moved again.
The oil tin you dropped has probably jammed the works.
"""
                        else:
                                print "The lever is rusted solid. It needs something to free it."
                else:
                        print A,"lever here."
        else:
                print A2

#drop items
def PutDown():
        global CarryAmount
        global DragonSlain
        global Dragon_Annoyed
        global Dwarf_here
        global Dwarf_total
        global playing
        global Treasure_total
        ThrowUsed = False
        if CommandLine[1] == "null":
                print Sp
                return
        if CommandLine[0]=="throw":
                ThrowUsed = Kill_Off()
        if ThrowUsed == True:
                return
        i = 1
        while i < len (Item_list):
                if CommandLine[1] == Item_list[i]:
                        if Item_list[i+1] == CarryPlace:
                                Item_list[i+1] = CurrentRoom
                                CarryAmount = CarryAmount - Item_list[i+2]
                                if CommandLine[0]=="throw" and Dwarf_here >0:
                                        print "The dwarf dodges the", CommandLine[1], "with ease."
                                        print "However, I have to warn you that he is looking VERY angry."
                                        Dwarf_here = Dwarf_here + 3
                                        return
                                elif CommandLine[0]=="throw" and CurrentRoom=="ROOM27" and DragonSlain==False:
                                        if Dragon_Annoyed == True:
                                                playing = False
                                                print "\nI told you not to try that again! \nThe dragon huffs at you and you are incinerated."
                                                Dead_duck()
                                                return
                                        else:
                                                print "\nThe",CommandLine[1],"bounces harmlessly off the dragons scales."
                                                print "I wouldn't try that again. The dragon is looking at you VERY angrily."
                                                Dragon_Annoyed = True
                                else:
                                        print "OK."
                                        if CurrentRoom == "ROOM7":
                                                Treasure_total = Treasure_total + Item_list[i+3]
                                return
                i=i+5
        print A4,"any", CommandLine[1]

# Read Things
def Read_Things():
        if CommandLine[1] == "null":
                print Sp
        elif CommandLine[1] == "notice":
                if CurrentRoom == "ROOM26":
                        print "\nThe notice reads - YOU WON'T GET UP THE STAIRS"
                else:
                        print A3,"notice here."
        elif CommandLine[1] == "sign":
                if CurrentRoom == "ROOM5":
                        print B3,"DO NOT PRESS THIS BUTTON"
                elif CurrentRoom == "ROOM22":
                        print B3,"IZZYWIZZY"
                else:
                        print A3,"sign here"
        elif CommandLine[1] == "jerrycan" or CommandLine[1] == "label":
                if Item_list[37] == CarryPlace or Item_list[37] == CurrentRoom:
                        print "\nThe label reads - PARAFFIN FLAMMABLE"
                else:
                        print "The jerrycan is not here."
        elif CommandLine[1] == "mirror" or CommandLine[1] == "frame" or CommandLine[1] == "lettering":
                if CurrentRoom == "ROOM42" or CurrentRoom == "ROOM45":
                        print """
The lettering reads:-
WAVE GOODBYE TO THE PLACES YOU KNOW
"""
                else:
                        print A3, CommandLine[1], "to read."
        else:
                print "I can't read the",CommandLine[1]

# re-incarnate
def Re_Incarnate():
        global playing
        global Re_stored
        global CurrentRoom
        global Quit
        global Dwarf_here
        global FuelLevel
        global LightWarning
        global generate
        if Re_stored > 2:
                print """
I'm sorry, I have re-incarnated you three times already.
I am afraid I have run out of magic to help you now.
Better luck next time.
"""
                Quit = True
                return
        Reply = raw_input (" \nDo you wish me to try to re-incarnate you?   y or n > ").lower()
        if Reply == "y":
                print "\nOK then, but I'm not very good at this. \nDon't blame me if something goes wr......"
                print Poof
                print A9,"green smoke. \nCoughing and gasping, you emerge from the smoke and find....\n"
                playing = True
                x = random.randint(49, 56)                        
                CurrentRoom = "ROOM" + chr(x)
                Dwarf_here = 0
                if FuelLevel < 1:
                        generate = True   
                FuelLevel = 100
                LightWarning = False
                Item_list[42] = "ROOM201"
                Re_stored = Re_stored + 1
                PrintRoomData()
        else:
                Quit = True

#Score
def Score():
        print " \nYou have got", Treasure_total, "points, in", Game_moves, "moves."

#Special Room Descriptions
def SpecialDescribe():
        ss = "There is a strange shimmering doorway to the"
        if CurrentRoom == "ROOM12" and DragonSlain == False:
                print """
There is a loud roaring and a large flickering of flame at the
bottom of the chasm.
It sounds as if there is a large dragon down there.
"""
        elif CurrentRoom == "ROOM6":
                if GratingOpen == False:
                        print "The crawlway is blocked by a locked grating."
                else:
                        print "The crawlway has been blocked by a grating, but this is now open."
        elif CurrentRoom == "ROOM7":
                if BB_pressed == True:
                        print ss,"west."
        elif CurrentRoom == "ROOM9":
                if GratingOpen == False:
                        print "The north end of the crawlway is blocked by a grating."
        elif CurrentRoom == "ROOM16" or CurrentRoom == "ROOM17":
                if TrapDoorOpen == False:
                        print "The trapdoor is locked shut."
                else:
                        print "The trapdoor is open."
        elif CurrentRoom == "ROOM27":
                if DragonSlain == False:
                        print """
There is a large unfriendly dragon in the middle of the chasm to your north.
It is breathing great gouts of flame, and looks at you balefully."""
                elif Body_here == True:
                        print "There is the large body of a dead dragon here."
        elif CurrentRoom == "ROOM36":
                if Plant_grown == False:
                        print "There is a small plant growing here. It murmers 'Water, Water'"
                else:
                        print """There is a huge plant here,
it's stem reaching up to the top of the pit.
It should be possible to climb up it."""
        elif CurrentRoom == "ROOM37":
                if Plant_grown == True:
                        print "There is a huge plant growing out of the pit.\nIt should be possible to climb down it."
                else:
                        print "There is a small plant to be seen in the bottom of the pit."
        elif CurrentRoom == "ROOM42" or CurrentRoom == "ROOM45":
             	print "There is a large full length mirror attached to the wall here. \nLettering runs round the frame."
        elif CurrentRoom == "ROOM44" or CurrentRoom == "ROOM64" or CurrentRoom == "ROOM65":
                print "and a small green button is beneath it."
        elif CurrentRoom == "ROOM53":
                if Lever_pulled == False:
                        print """Faint daylight comes from a round window high up near the roof.
Massive carved stone doors bar your way east,
but a wide passage goes west."""
                else:
                        print """Daylight comes streaming in from a huge doorway,
flanked by two massive carved stone doors.
A large passage goes west."""
        elif CurrentRoom == "ROOM66":
                if BB_pressed == True:
                        print ss,"east."
        elif Train_place == CurrentRoom:
                print """
A small steam train is here, hissing gently.
Two dwarves are leaning out of the cab windows."""

#Special Door exit refusals
def SpecialDoorPrintout():
        global Command
        Tt = "The trapdoor is locked shut."
        if Dwarf_here >0:
                print "The Dwarf blocks your way"
                Command = ""
        elif CurrentRoom == "ROOM6" and GratingOpen == False:
                if Command == "s":
                        print "The grating is locked shut. You cannot go that way."
                        Command = ""
        elif CurrentRoom == "ROOM7" and BB_pressed == False:
                if Command == "w":
                        Command = ""
                        print Nogo
        elif CurrentRoom == "ROOM9" and GratingOpen == False:
                if Command == "n":
                        print "Your way is blocked by a locked steel grating."
                        Command = ""
        elif CurrentRoom == "ROOM16" and TrapDoorOpen == False:
                if Command == "u":
                        print Tt
                        Command = ""
        elif CurrentRoom == "ROOM17" and TrapDoorOpen == False:
                if Command == "d" or Command == "in":
                        print Tt
                        Command = ""
        elif CurrentRoom == "ROOM27" and DragonSlain == False:
                if Command == "n":
                        print "The Dragon bars your way, and warms you up with a flaming snort."
                        Command = ""
        elif CurrentRoom == "ROOM36":
                if Command == "u":
                        if Plant_grown == False:
                                print "You can't get up there."
                                Command = ""
                        else:
                                print "You climb up the plant very easily, and reach the top of the pit."
        elif CurrentRoom == "ROOM37":
                if Command == "d":
                        if Plant_grown == False:
                                print "You can't get down there."
                                Command = ""
                        else:
                                print "You climb down the plant easily, and reach the bottom."
        elif CurrentRoom == "ROOM53":
                if Command == "e":
                        if Lever_pulled == False:
                                Command = ""
                                print "The doors are firmly shut."
        elif CurrentRoom == "ROOM66":
                if Command == "e" and BB_pressed == False:
                        Command = ""
                        print Nogo

def Train_ride():
        global CurrentRoom
        global Train_place
        Blurb = """
The driver shouts 'Righto Guv, Climb aboard!'
You jump in the carriage, the engine gives a toot,
and with a loud chuffing, you are off.

The train rattles through dark tunnels, with the occasional oil
lamp to be seen. Now and then, the train emerges from a cliff face
into daylight, and rattles across a bridge, before plunging back
into the dark tunnels.

Eventually, the train eases to a stop. You get out onto the platform,
then with a further Toot Toot, the train chugs off into the Tunnels.
"""
        if Train_place == CurrentRoom:
                if CommandLine[0]=="s1":
                        if CurrentRoom == "ROOM44":
                                print A7
                                print "s1",A8
                        else:
                                CurrentRoom = "ROOM44"
                                print Blurb
                                PrintRoomData()
                elif CommandLine[0]=="s2":
                        if CurrentRoom == "ROOM64":
                                print A7
                                print "s2",A8
                        else:
                                CurrentRoom = "ROOM64"
                                print Blurb
                                PrintRoomData()
                elif CommandLine[0]=="s3":
                        print "not built yet"
                elif CommandLine[0]=="s4":
                        print "not built yet"
                elif CommandLine[0]=="s5":
                        if CurrentRoom == "ROOM65":
                                print A7
                                print "s5",A8
                        else:
                                CurrentRoom = "ROOM65"
                                print Blurb
                                PrintRoomData()
                Train_place = "ROOM201"
        else:
                print A1
# get train
def Train_run():
        global Dwarf_happy
        global Train_place
        if Dwarf_happy == True and Train_place <> CurrentRoom:
                print """
A bell rings, then all is quiet for a few minutes.
A rumbling can then be heard, and a strong breeze
comes from one of the tunnels.
A small steam engine then puffs in, pulling a highly painted coach.

The train stops, and two dwarves lean out of the cab to wave at you.
"""
                print Ws
                Train_place = CurrentRoom
        else:
                print "\n",A1
        
#Water Plant
def Water_plant():
        global Plant_grown
        global Bowl_filled
        global Treasure_total
        Water_in_command = False
        if CommandLine[0] == "water" and CommandLine[1] == "plant":
                Water_in_command = True
        elif CommandLine[0] == "pour" and CommandLine[1] == "water" and CommandLine[3] == "plant":
                Water_in_command = True
        elif CommandLine[0] == "pour" and CommandLine[1] == "tin":
                if CommandLine[3] == "lever":
                        CommandLine[0] = "oil"
                        CommandLine[1] = "lever"
                        Oil_lever()
                elif CommandLine[2] == "null":
                        print Sp
                else:
                        print "Why oil a",CommandLine[3]
        else:
                print A2
                return
        if Water_in_command == True:
                if Bowl_filled == True and Item_list[32] == CarryPlace:
                        if Plant_grown == True:
                                print A1
                                Bowl_filled = False
                        else:
                                Bowl_filled = False
                                Plant_grown = True
                                Treasure_total = Treasure_total + 5
                                print """
You pour the water over the plant, and there is a few seconds pause.
The plant then erupts into life, growing rapidly up the height of the pit,
and nearly filling the pit bottom.
"""
                else:
                        print A4,"any water."
        
#wave routine
def Wave_things():
        global CurrentRoom
        Ans = "\nThe air shimmers, and you feel unsteady for a moment."
        if CommandLine[1] == "null":
                print A1
        elif CommandLine[1] == "wand":
                if Item_list[12] == CarryPlace:
                        if CurrentRoom == "ROOM42":
                                CurrentRoom = "ROOM45"
                                print Ans
                        elif CurrentRoom == "ROOM45":
                                CurrentRoom = "ROOM42"
                                print Ans
                        else:
                                print "Nothing seems to happen."
                else:
                        print A4,"the wand."
        else:
                print "I don't think that will help!"

#------------main game program--------------
# set all variables
# All these variables need to be saved in a SAVED_GAME file
Item_list = ItemData()
CurrentRoom = "ROOM1" #where the game starts
BB_pressed = False
Body_here = False # Dragons body left
Bowl_filled = False
Dragon_Annoyed = False
DragonSlain = False
Dwarf_happy = False
generate = False
GratingOpen = False
Lever_oiled = False
Lever_pulled = False
LightWarning = False
Move_command = False
Oyster_opened = False
Plant_grown = False
Quit = False
Trace = False
TrapDoorOpen = False
y_n_request = 0
Dark_count = 0
Dwarf_here = 0
Dwarf_total = 8 # total number of dwarves in caverns
CarryPlace = "ROOM200" #where my personal items are stored
CarryAmount = 0
MaxCarryAmount = 16 #Can't carry more than this
Game_moves = 0
Re_stored = 0
FuelLevel = 120 #set number of moves before lights go out
Train_place = "ROOM"
Treasure_total = 0
random.seed()

#start game
playing = True
MainHelp()
PrintRoomData()
while playing:
        Command = raw_input(" \nWhat Now? >").lower()
        UnKnown = random.randint(1, 100)
        Game_moves = Game_moves + 1
        if generate == True:
                FuelLevel = FuelLevel - 1
        Check_move_command()
#Deal with directions
        if Move_command == True:
                Place = Locations[CurrentRoom]
                if Place.underground == True and generate == False:
                        PrintRoomData()
                elif Locations[CurrentRoom].exits.has_key(Command):
                        if Locations[CurrentRoom].exits[Command] == "ROOMx": # Room Under Construction
                                print B1, "- THIS ROOM IS UNDER CONSTRUCTION. \nI will return you to your previous position.\n"
                                PrintRoomData()
                        elif Locations[CurrentRoom].exits[Command] == "ROOMz":
                                Down_river()
                                CurrentRoom = "ROOM60"
                                PrintRoomData()
                        elif CurrentRoom == Locations[CurrentRoom].exits[Command]:
                                NoCanDo()
                        else:
                                SpecialDoorPrintout()
                                if Command <> "":
                                        CurrentRoom = Locations[CurrentRoom].exits[Command]
                                        PrintRoomData()
                else:
                        print Nogo
        else:
                CommandLine = Command.split()
                while len(CommandLine)<4:
                        CommandLine.append('null')
#Deal with commands
                if CommandLine[1]=="can": CommandLine[1]="jerrycan"
                if CommandLine[1]=="oil": CommandLine[1]="tin"
                if CommandLine[0]=="say" or CommandLine[0]=="incant": CommandLine[0] = CommandLine[1]
                if CommandLine[0]=="back": print"I'm sorry, but I don't know the way back."
                elif CommandLine[0]=="blow": Blow_things()
                elif CommandLine[0]=="climb": Climb_plant()
                elif CommandLine[0]=="drop" or CommandLine[0]=="throw": PutDown()
                elif CommandLine[0]=="fill": Get_water()
                elif CommandLine[0]=="fly": print "Be sensible!"
                elif CommandLine[0]=="help": MainHelp()
                elif CommandLine[0]=="hit": print "Hitting does not work here."
                elif CommandLine[0]=="invent" or CommandLine[0]=="inventory": Carry()
                elif CommandLine[0]=="izzywizzy": Magic_words()
                elif CommandLine[0]=="jump": Jump_up()
                elif CommandLine[0]=="kick": print "Kicking will do nothing."
                elif CommandLine[0]=="kill": Kill_reply()
                elif CommandLine[0]=="look": PrintRoomData()
                elif CommandLine[0]=="move": Pull_lever()
                elif CommandLine[0]=="oil": Oil_lever()
                elif CommandLine[0]=="open": Open_Things()
                elif CommandLine[0]=="pay" or CommandLine[0]=="give": Payment()
                elif CommandLine[0]=="play": Blow_things()
                elif CommandLine[0]=="pour": Water_plant()
                elif CommandLine[0]=="press" or CommandLine[0]=="push": PressButton()
                elif CommandLine[0]=="pull": Pull_lever()
                elif CommandLine[0]=="quit" or CommandLine[0]=="escape":
                        playing = False
                        Quit = True
                elif CommandLine[0]=="read": Read_Things()
                elif CommandLine[0]=="run": print "Sorry, I don't do running!"
                elif CommandLine[0]=="s1" or CommandLine[0]=="s2" or CommandLine[0]=="s5": Train_ride()
                elif CommandLine[0]=="score": Score()
                elif CommandLine[0]=="take" or CommandLine[0]=="get" or CommandLine[0]=="grab": PickUp()
                elif CommandLine[0]=="turn": GenerateRun()
                elif CommandLine[0]=="unlock": OpenExits()
                elif CommandLine[0]=="water": Water_plant()
                elif CommandLine[0]=="wave": Wave_things()
                elif CommandLine[0]=="yes" and y_n_request > 0: Killoff_Dragon()
                
                elif CommandLine[0]=="trace":#--- For testing only
                        if Trace == True:
                                Trace = False
                                print "\nTrace Off"
                        elif Trace == False:
                                Trace = True
                elif CommandLine[0]=="xxx":
                        CurrentRoom = raw_input("Which Room >").upper() #--- xxx is for testing purposes only
                        generate = True
                        FuelLevel = 50
                        PrintRoomData()
                else:
                        print "I'm sorry, I cannot understand that command."
        if playing == True:
                if y_n_request >0:
                        if y_n_request >= 2:
                                y_n_request = 0
                        else:
                                y_n_request = y_n_request + 1
                Dwarf_attack()
                if Locations[CurrentRoom].underground == True and FuelLevel < 10 and LightWarning == False and generate == True:
                        print "The lights have started dimming and pulsing. \nIt would seem that the generator is rapidly running out of fuel."
                        LightWarning = True
                if FuelLevel < 1:
                        generate = False
        if playing == False and Quit == False:
                Re_Incarnate()
        if Quit == True:
                Score()
        if Trace == True:#---- For testing only
                print ""
                print "Current Room ",CurrentRoom
                print "Generate ",generate
                print "Fuel Level ",FuelLevel
                print "Light Warning ",LightWarning
                print "Dragon Annoyed ",Dragon_Annoyed
                print "Dwarf Happy ",Dwarf_happy
                print "Dwarf Here ",Dwarf_here
                print "Carry Amount ",CarryAmount
                print "Game Moves ",Game_moves
                print "Restored ",Re_stored


#End of program
