from time import sleep
import sys
from named_mtx import NamedMutex


def main(*args):
    wait_dur = int(args[0][1])
    print("running with wait duration: {0} ms".format(wait_dur))
    input("press enter to go")
    mutex = NamedMutex("shared_key_name_0c4ecb52-a861-482a-bfa0-d63d15222c31")
    counter = 0
    while True:
        try:
            mutex.acquire()
            print("working on round {} ...".format(counter))
            sleep(wait_dur / 1000.0)
        finally:
            mutex.release()
        counter += 1


if __name__ == '__main__':
    main(sys.argv)