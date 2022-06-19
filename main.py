import os
from colorama import init, Style, Fore

from util.grammar import is_allowed_true, get_answer_as_number
from util.clear_console import clear_console
from util.start_screen import print_copyright

init()

clear_console()
print_copyright("I")
print(f"[{Fore.YELLOW}WARNING{Style.RESET_ALL}] This game contains violence. This is probably classed as a PEGI 12.")

a=input("Press ENTER to start: ")
skip_to_part = 1

if a.startswith("!debug"):
  print("Debugger starting..")
  print("Choose part")
  skip_to_part = get_answer_as_number([1, 2])

if skip_to_part == 1:
  clear_console()
  print_copyright("one")
    
  import part.one
  skip_to_part=2
  
  while True:
    print("Well done, you've survived part one!")
    print("Would you like to try part two?")
    if is_allowed_true(input("Do you want to (yes/no)? ")):
      break
    else:
      print("Oh, ok. We'll keep the option ready for you. Press enter in the console once you are ready:")
      input()

if skip_to_part == 2:
  clear_console()
  
  print_copyright("two")
  
  import part.two
  
  while True:
    print("Well done, you've survived part two!")
    print("Would you like to try part three?")
    if is_allowed_true(input("Do you want to (yes/no)? ")):
      break
    else:
      print("Oh, ok. We'll keep the option ready for you. Press enter in the console once you are ready:")
      input()

