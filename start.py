import cli_util_custom

from ascii import ascii

def start():

  ascii("KASTELY")

  cli_util_custom.info_2("Welcome knights! The conquest is on, you must both race to the castle. The last one there will be decapitated.")

  name_1 = cli_util_custom.ask_string("May the first knight step up and identify themself.")

  name_2 = cli_util_custom.ask_string("May the second knight step up and identify themself.")

  if name_1 != None and name_2 != None:

    cli_util_custom.info_2("Thank you " + name_1 + " & " + name_2 + ". We will now begin the game....")

    return name_1, name_2

  else: 

    cli_util_custom.info_2("Invalid names. I will make my own up for you.")

    if name_1 == None:

      name_1 = "Dragon Destroyer"
    
    if name_2 == None:

      name_2 = "Sword Master"
    
    return name_1, name_2
      
    
    