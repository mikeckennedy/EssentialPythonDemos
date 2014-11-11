import sys
import io_helper
import lib

moduelsToTest = [
    'closures',
    'downloader',
    'lib',
    'catpictures'
]

for m in moduelsToTest:
    #print("Processing module " + m + "... ", end="")
    try:
        lines = lib.count_lines(m)
        #count = lib.some_io_function(m)
        print("There are {2} lines, {0:,} chars in {1}".format(0, m, lines))
    except FileNotFoundError as fne:
        print("Ooops the file " + fne.filename + " apparently isn't found")
        print("More details: {}".format(fne))
    except Exception as e:
        print("Failed, don't know why: " + str(e))
        #raise NameError("other") from e
    finally:
        pass#print("done ["+m+"]")


        #
        # try:
        # count  =lib.some_io_function('catpictures')
        # print("There are {0:,} chars in {1}".format(count, "catpictures"))
        #     print(count)
        # except:
        #     print("Hmm, that didn't work so much")
        #
        # lib.some_io_function('catpictures')