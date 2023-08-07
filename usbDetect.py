import os.path

def usb():
    def diff(list1, list2):
        list_difference = [item for item in list1 if item not in list2]
        return list_difference
    


    dl = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    print("")
    print("Press x to exit.")
    print("")
    print("Available Drives :")
    drives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]
    print(drives)

    while True:
        uncheckeddrives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]
        x = diff(uncheckeddrives, drives)
        if x:
            print("New drives:     " + str(x))
            print("New dive introduced")
            
        x = diff(drives, uncheckeddrives)
        if x:
            print("Removed drives: " + str(x))
            print("Drive disconnected")
            
            
            
        drives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]
        
        s = input("")
        if s == "x":
            exit()
        
        