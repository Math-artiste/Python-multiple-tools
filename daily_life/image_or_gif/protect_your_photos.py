from cryptography.fernet  import Fernet

key = Fernet.generate_key()

print("What do you want to do : ")
print("-Type 1 to protect your photos")
print("-Type 2 to unprotect your photos")
choice = input()
if choice == "1" :
    path = input("Enter the photos you want to protect : ")
    path = "C:\\Users\\montage du 60\\Documents\\Python\\test_image_or_pic\\" + path
    with open("key.key", "wb") as f :
        f.write(key)
    fernet = Fernet(key)
    with open(path, "rb") as f :
        Photo = f.read()

    lock = fernet.encrypt(Photo)
    with open(path, "wb") as lock_photo :
        lock_photo.write(lock)
    print("Your photo is locked")
else : 
    path = input("Enter the photos you want to unprotect : ")
    path = "C:\\Users\\montage du 60\\Documents\\Python\\test_image_or_pic\\" + path

    with open("key.key", "rb") as f :
        key = f.read()
    fernet = Fernet(key)
    with open(path, "rb") as f :
        Photo = f.read()
    lock = fernet.decrypt(Photo)
    with open("test.txt", "wb") as unlock_photo :
        unlock_photo.write(lock)
    print("Your photo is unlocked")