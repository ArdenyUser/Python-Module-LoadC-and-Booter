# LOADX FREE SOFTWARE (Made by Avery Stafford)
# Module code is below!

def File_add_data(file, data):
  file = open(file, "a")
  file.write('\n' + data);
  file.close()
def Output_log(log):
  file = open("output_log.txt", "a")
  file.write('\n' + log);
  file.close()
def Reload_direct():
  import game_boot
def Reload_full():
  import main_boot
def LoadX_info():
  print("LoadX Copyright 2021 by Avery Stafford, this is free software! GNU Free Software License")
  print("!License Included!")
  print("This is a module, or addon, if you are using the Full version, aka using the booter with this, it is all copyrighted: ")
  print("LoadX Booter/Python-Module-LoadX-and-Booter Copyright 2021 by Avery Stafford, this is free software!")
  print("!License Included!")
  print("And, Tinker (or is it Tkinker) is not mine, nor PySimpleGui.")
  
