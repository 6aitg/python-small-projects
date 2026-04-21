import random
# coin=random.choice(["heads","tails"])
# print(coin)

# cards=["jack","king","queen"]
# random.shuffle(cards)
# for card in cards:
#     print(card)
"""-------------------------------------"""
# import sys
# print("hello, my name is", sys.argv[1])

# import sys
# try:
#     print("hello, my name is",sys.argv[1])
# except IndexError:
#     print("Too few arguments")

# import sys
# if len(sys.argv)<2:
#     sys.exit("Too few arguments")
# for arg in sys.argv[1:-1]:
#     print ("hello, my name is ",arg)

# import cowsay
# import sys
# if len(sys.argv)==2:
#     cowsay.cow("hello, "+sys.argv[1])

# import requests
# import sys
# if len(sys.argv)!=2:
#     sys.exit()
# response=requests.get()
# print(response.json())

# import requests
# import sys
# import json
# if len(sys.argv)!=2:
#     sys.exit()
# response=requests.get()
# print(json.dumps(response.json(),indent=2))

import requests
import sys
import json
if len(sys.argv)!=2:
    sys.exit()
response=requests.get("")
o=response.json()
for result in o["result"]:
    print(result["trackName"])