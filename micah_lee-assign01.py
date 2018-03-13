#Micah lee 03/12/18

media_type = input("what is the media type? ")
title = input("what is the title ")
des = input("give me a brief description ")
yr = str(input("what year was it created "))
rating = float(input(" what rating would you give this media type (1/10) " ))
new_list = [ title, des, yr, rating ]
if media_type == "Book":
    print (new_list)
elif media_type == "movies":
     print (new_list)

    


