import sys

imie : str= input("Podaj imie: ")
try: 
    rok_urodzenia = int(input("Podaj rok urodzenia: "))
except ValueError:
    print("Error: Invalid input")
    sys.exit()
# try / except

# try:
#     rok_urodzenia = int(rok_urodzenia)
# except:
#     print("Error: invalid year")

if rok_urodzenia <1900 or rok_urodzenia > 2026:
    print("Error: invalid year")
    sys.exit()
else:
    wiek : int  = 2026 - rok_urodzenia
    #print("Hello", imie, "you're", 2026 - rok_urodzenia, "years old")
    print(f"Hello {imie} you're {2026-rok_urodzenia} years old!")
    print("Hello", imie, "you're", 2026 - rok_urodzenia , "years old!" )


