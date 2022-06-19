import os
def clear_console():
  cmd = 'clear'
  if os.name in ('nt', 'dos'):
    cmd = 'cls'
  os.system(cmd)
  