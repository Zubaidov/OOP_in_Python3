
try:
    f = open('testfile', 'w')
    f.write("Write a test line")
except TypeError:
    print("There was a TypeError")
except OSError:
    print("There are an OSError")
except:
    print("All other errors")
finally:
    print("I always run")