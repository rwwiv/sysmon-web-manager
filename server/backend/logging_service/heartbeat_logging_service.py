import datetime
import os

path = "./logs/heartbeat"
def err(message):
    date = datetime.datetime.today()

    if not os.path.exists(path):
        try:
            os.makedirs(path)
        except:
            print("Logging service failed when creating logs folder.")
    try:
        with open(f"{path}/{date.strftime('%d-%m-%Y--%H')}.txt",'a') as log:
            log.write(f'{date} - {message}\n')
            print(f'{date} - {message}\n')
    except:
        with open(f"{path}/{date.strftime('%d-%m-%Y--%H')}.txt",'w+') as log:
            log.write(f'{date} - ERR:{message}\n')
            print(f'{date} - {message}\n')
    finally:
        pass

def warn(message):
    date = datetime.datetime.today()

    if not os.path.exists(path):
        try:
            os.makedirs(path)
        except:
            print("Logging service failed when creating logs folder.")
    try:
        with open(f"{path}/{date.strftime('%d-%m-%Y--%H')}.txt",'a') as log:
            log.write(f'{date} - {message}\n')
            print(f'{date} - {message}\n')
    except:
        with open(f"{path}/{date.strftime('%d-%m-%Y--%H')}.txt",'w+') as log:
            log.write(f'{date} - WARN:{message}\n')
            print(f'{date} - {message}\n')
    finally:
        pass

def debug(message):
    date = datetime.datetime.today()

    if not os.path.exists(path):
        try:
            os.makedirs(path)
        except:
            print("Logging service failed when creating logs folder.")
    try:
        with open(f"{path}/{date.strftime('%d-%m-%Y--%H')}.txt",'a') as log:
            log.write(f'{date} - {message}\n')
            print(f'{date} - {message}\n')
    except:
        with open(f"{path}/{date.strftime('%d-%m-%Y--%H')}.txt",'w+') as log:
            log.write(f'{date} - DEBUG:{message}\n')
            print(f'{date} - {message}\n')
    finally:
        pass

