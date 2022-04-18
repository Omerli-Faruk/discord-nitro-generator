#IMPORTS
import requests
import random
import string
import time

print("♥♥♥Loading♥♥♥")
time.sleep(1)
#CREATOR
print("""  _____  ____  __  __ 
 |  __ \|___ \|  \/  |
 | |__) | __) | \  / |
 |  _  / |__ <| |\/| |
 | | \ \ ___) | |  | |
 |_|  \_\____/|_|  |_|
""")
time.sleep(2)
#CODE GENERATION
num = int(input('How Many Codes to Generate: '))

with open("Nitro Codes.txt", "w", encoding='utf-8') as file:
    print("Your nitro codes are being generated.")

    start = time.time()

    for i in range(num):
        code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k=16
        ))
        file.write(f"https://discord.gift/{code}\n")
#THE PROGRAM STARTS
    print(f"Generated {num} codes | Time taken: {time.time() - start}\n")

with open("Nitro Codes.txt") as file:
    for line in file.readlines():
        nitro = line.strip("\n")
#DISCORD API
        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)
#CHECK DISCORD NITRO CODE
        if r.status_code == 200:
            print(f" Valid | {nitro} ")
            break
        else:
            print(f" Invalid | {nitro} ")

input("\nYou have generated.")