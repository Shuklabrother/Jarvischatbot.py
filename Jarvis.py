import pyfiglet
print(pyfiglet.figlet_format("JARVIS"))

while True:
  a = str(input("ME:"))
  if a=="Hello ":
    print("Jarvis: Hello")
  elif a=="Hi":
    print("Jarvis: HI")
  else:
    print("Jarvis:")