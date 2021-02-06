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
