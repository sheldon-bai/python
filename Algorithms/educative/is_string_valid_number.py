# class STATE:
#   START, INTEGER, DECIMAL, UNKNOWN, AFTER_DECIMAL = range(5)

# def get_next_state(current_state, c):
#   match current_state:
#     case STATE.START:
#       if c == '.':
#         return STATE.DECIMAL
#       if c >= '0' and c <= '9':
#         return STATE.INTEGER
#       return STATE.UNKNOWN
#     case STATE.INTEGER:
#       if c == '.':
#         return STATE.DECIMAL
#       if c >= '0' and c <= '9':
#         return STATE.INTEGER
#       return STATE.UNKNOWN
#     case STATE.DECIMAL:
#       if c >= '0' and c <= '9':
#         return STATE.AFTER_DECIMAL
#       return STATE.UNKNOWN
#     case STATE.AFTER_DECIMAL:
#       if c >= '0' and c <= '9':
#         return STATE.AFTER_DECIMAL
#       return STATE.UNKNOWN

# def is_number_valid(s):
#   if not s:
#     return True
  
#   i = 0

#   if s[i] is '+' or s[i] is '-':
#     i = i + 1

#   current_state = STATE.START

#   for c in s[i:]:
#     current_state = get_next_state(current_state, c)

#     if current_state == STATE.UNKNOWN:
#       return False
    
#   return True

class STATE:
  START, INTEGER, DECIMAL, UNKNOWN, AFTER_DECIMAL = range(5)

def get_next_state(current_state, c):
  if current_state is STATE.START or current_state is STATE.INTEGER:
    if c >= '0' and c <= '9':
      return STATE.INTEGER

    if c is '.':
      return STATE.DECIMAL

    return STATE.UNKNOWN

  if current_state is STATE.DECIMAL or current_state is STATE.AFTER_DECIMAL:
    if c >= '0' and c <= '9':
      return STATE.AFTER_DECIMAL

    return STATE.UNKNOWN

  return STATE.UNKNOWN



def is_number_valid(s):
  if not s:
    return True

  i = 0

  if s[i] is '+' or s[i] is '-':
    i += 1

  current_state = STATE.START

  for c in s[i:]:
    current_state = get_next_state(current_state, c)

    if current_state is STATE.UNKNOWN:
      return False

  return True

def main():
  # print("Is the number valid 4.325?  ",
  #   "Yes" if is_number_valid("4.325") else "No")
  print("Is the number valid 1.1.1?  ",
    "Yes" if is_number_valid("1.1.1") else "No")
  print("Is the number valid -22.22.?  ",
    "Yes" if is_number_valid("-22.22.") else "No")
  # print("Is the number valid 222?    ",
  #   "Yes" if is_number_valid("222") else "No")
  # print("Is the number valid 22.?    ",
  #   "Yes" if is_number_valid("22.") else "No")
  # print("Is the number valid 0.1?    ",
  #   "Yes" if is_number_valid("0.1") else "No")
  # print("Is the number valid 22.22.? ",
  #   "Yes" if is_number_valid("22.22.") else "No")
  # print("Is the number valid 1.?     ",
  #   "Yes" if is_number_valid("1.") else "No")
  
if __name__ == '__main__':
  main()