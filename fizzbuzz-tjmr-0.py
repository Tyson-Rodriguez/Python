for n in range(1,101):
  string = ""
  if n % 3 == 0:
    string += "Fizz"
  if n % 5 == 0:
    string += "Buzz"
  if n % 5 != 0 and n % 3 != 0:
    string += str(n)
  print string


