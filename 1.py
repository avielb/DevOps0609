from os import getenv
env = getenv("ENVIRONMENT")
action = getenv("ACTION")
if env == "dev" and action == "stop":
    print("good")
if 66 == 66:
    print("1")