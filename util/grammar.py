allowed_true = ["yes", "ye", "yeah", "ok", "sure", "yea", "sure why not", "okay", "y"]

def is_allowed_true(str):
  return str.lower() in allowed_true

def get_answer_as_number(valid):
  valid_choices = "/".join(str(e) for e in valid)
  ans = None
  while True:
    ans = input(f"Enter your choice ({valid_choices}): ")
    try:
      ans = int(ans)
    except ValueError:
      print("Invalid answer - your answer needs to be a valid number")
      continue
    if ans == None:
      continue
    if ans in valid:
      break
    else:
      print("This is not an allowed number!")
  return ans