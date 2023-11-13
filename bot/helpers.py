import math
import subprocess
import numpy as np
import datetime

def get_time_since(time: datetime.datetime):
    now = datetime.datetime.now()

    time = datetime.datetime.fromtimestamp(time.timestamp(), now.tzinfo)
    
    difference = now - time

    time_since: str

    days = math.floor(difference.seconds / 86400)
    hours = math.floor(difference.seconds / 3600)
    minutes = math.floor(difference.seconds / 60)
    seconds = difference.seconds

    if days >= 1:
        if days == 1:
            time_since = "1 day ago"
        else:
            time_since = f"{days} days ago"
    elif hours >= 1:
        time_since = f"{hours} hours ago"
    elif minutes >= 1:
        time_since = f"{minutes} minutes ago"
    else:
        time_since = f"{seconds} seconds ago"

    return time_since

def chunks(data, chunk_size=5):
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]

def run_command(args: [str]) -> str:
    result: str

    try:
        result = subprocess.check_output(args,shell=True)

    except Exception as e:
        result = str(e)

    return result

def rng(args):

    if args:
        
        if "--digits" in args:
            digits = int(args[args.index("--digits") + 1])

            min = int("-%s" % "".join(["9" for i in range(digits)]))
            max = int("%s" % "".join(["9" for i in range(digits)]))

        else:

            if "--min" in args:
                min = int(args[args.index("--min") + 1])
            else:
                min = 0
            
            if "--max" in args:
                max = int(args[args.index("--max") + 1])
            else:
                max = 100


        if "--amount" in args:
            amount = int(args[args.index("--amount") + 1])
        else:
            amount = 1

    else:
        min = 0
        max = 100
        amount = 1

    return np.random.randint( min, max, size=amount)
