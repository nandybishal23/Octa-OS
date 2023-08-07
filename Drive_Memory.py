import psutil

def dmem():
    s = input("Which drive : ")
    hdd = psutil.disk_usage(s+':/')

    print ("Total: %d GiB" % (hdd.total // (2**30)))
    print ("Used: %d GiB" % (hdd.used // (2**30)))
    print ("Free: %d GiB" % (hdd.free // (2**30)))