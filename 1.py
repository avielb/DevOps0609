from os import getenv
env = getenv("ENVIRONMENT")
action = getenv("ACTION")
if env == "dev" and action == "stop":
    print("good")
if 2 == 2:
    print("2")