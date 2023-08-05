def validate_password(password):
# Check length of the password
  if len(password) < 8:
     return False
# Check for uppercase letter, lowercase letter, and digit
  has_uppercase = False
  has_lowercase = False
  has_digit = False

  for char in password:
      if char.isupper():
          has_uppercase = True
      elif char.islower():
          has_lowercase = True
      elif char.isdigit():
          has_digit = True

  if not (has_uppercase and has_lowercase and has_digit):
      return False

  # Check for spaces
  if ' ' in password:
      return False

  return True
print(validate_password("Password123"))