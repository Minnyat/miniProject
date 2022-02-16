import random

name_file_phone = "genphone10m.txt"
number_n = 100000
default_password = "123456"
default_number = "9"

def creat_phone_number():
    phone_number = "0"+default_number
    for i in range(8):
        phone_number+=str(random.randint(0,9))
    return phone_number

def main():
    f = open(name_file_phone,"w",encoding="utf8")
    for i in range(number_n):
        f.write(creat_phone_number()+":"+default_password+'\n')
    f.close()
    
if __name__ == "__main__":
    main()
