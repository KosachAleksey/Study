#myfile = open("myCarShop.txt", "w")
#myfile = open("image.jpeg", "rd")
#myfile.close()
#myList = ["\n Хонда", "\n БМВ", "\n Ява"]
#with open("myCarShop.txt", "a") as file:
    #file.writelines(myList)
#print("Файл записан")


filename = "academy.txt"
with open(filename, encoding="UTF-8") as file:
    text = file.read()

    