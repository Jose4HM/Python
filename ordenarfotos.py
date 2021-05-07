# files in a directory or folder 
import os 
import time
from datetime import datetime
folder_name = 'E:\\Imagenes\\speedrun\\2020\\'
dir_list = [os.path.join(folder_name, x) for x in os.listdir(folder_name)]
os.system('cls')
def main():
    
    try:
        option=int(input("OPTIONS\n1)RUN\n2)Test\n3)Exit\n"))
        if option==1:
            os.system('cls')
            global sign
            sign=input("Add some peculiar word\n Example\n year-month-day(your word)\n")
            action()
        elif option==2:
            os.system('cls')
            order()
        elif option==3:
            print("See you later nerds")
            time.sleep(2.4)
            os.system('cls')
            SystemExit("See u later nerds")
        else:
            os.system('cls')
            main()
    except TypeError:
        os.system('cls')
        main()
    except ValueError:
        os.system('cls')
        main()


def action(): 
    i=0

    for file in dir_list:
        filename, file_extension = os.path.splitext(file)
        date = datetime.fromtimestamp(os.path.getctime(file)).strftime('%Y-%m-%d-{}-{}'.format(sign,i)) #%Y_%m_%d_%H_%M_%S cada uno coloca la fecha 
        os.rename(file, os.path.join(folder_name,date + file_extension))
        i=i+1

    print("Files renamed successfully")
    time.sleep(2.4)
    os.system('cls')
    main()

def order():
    for file in dir_list:
        print(file)
    main()

if __name__ == '__main__': 
    main()


"""
    for count, filename in enumerate(os.listdir("E:\\Imagenes\\speedrun\\2020\\")): #if there is a unicode error, just duplicate all backslashes
        dst ="2020-" + str(count) + ".jpg" #destination
        src ="E:\\Imagenes\\speedrun\\20220\\" + filename  #source
        dst ="E:\\Imagenes\\speedrun\\2020\\" + dst     #destination
          
        # rename() function will 
        # rename all the files 
        os.rename(src, dst) """
     