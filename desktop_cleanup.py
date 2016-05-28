# Import modules
import re ,glob ,sys ,os ,datetime,time ,shutil

#To determine the current system date
present_date_time=datetime.datetime.now().date()
print(present_date_time)


# Source from where the files need to be copied to the destination
source="C:\Users\Sukanya\Desktop\desktop"
destination="C:\Users\Sukanya\Desktop\destination"

#  To fetch the input from the user
# source=raw_input("Enter the source from where the files need to be moved")
# destination=raw_input("Enter the destination path to where the files need to be moved")

#######################################################################################
# ~~~Define func text_files~~~.
# This function uses the 'walk' method to determine the root , directories and files of the source path.
# They are stored in the respective variables
#######################################################################################

###############################################################################################################################################################
# fdmodified_time -
# The last modified time of the files are determined using the getmtime method. This method returns time in seconds and hence datetime.datetime.fromtimestamp is used.
# date() fetches the date from the specific format.
#
#  A dictionary is used to store the key = path of the source , values= last modified time
###############################################################################################################################################################

def text_files():
 my_dict={}

 try:
     for root,dirs,files in os.walk(source,topdown=False):
         for name in files:
             if(name.endswith(".txt")):
                 path=os.path.join(root,name)
                 fmodified_time=datetime.datetime.fromtimestamp(os.path.getmtime(path)).date()
                 my_dict[path]=fmodified_time
                 #print(my_dict)

#######################################################################################
# The present date and the file's last modified time are compared.
# Based on the equality , the files are moved from source to destination
#######################################################################################
     if (present_date_time == fmodified_time):
         for key in my_dict.keys():
             src_Dest=shutil.move(key,destination)
             print("moved")
     else:
         print("Stay there")
                 
 except IOError:
      print("No files")



def word_files():
 my_dict={}

 try:
     for root,dirs,files in os.walk(source,topdown=False):
         for name in files:
             if name.endswith(".doc") or name.endswith(".docx"):
                 path=os.path.join(root,name)
                 print(path)
                 fmodified_time=datetime.datetime.fromtimestamp(os.path.getmtime(path)).date()
                 print(fmodified_time)
                 my_dict[path]=fmodified_time
                # print(my_dict)
     if (present_date_time == fmodified_time):
         for key in my_dict.keys():
             src_Dest=shutil.move(key,destination)
         print("moved")
     else:
         print("Files have been moved already")

 except IOError:
      print("No files")

def excel_files():
 my_dict={}

 try:
     for root,dirs,files in os.walk(source,topdown=False):
         for name in files:
             if name.endswith(".xls") or name.endswith(".xlsx"):
                 path=os.path.join(root,name)
                 print(path)
                 fmodified_time=datetime.datetime.fromtimestamp(os.path.getmtime(path)).date()
                 print(fmodified_time)
                 my_dict[path]=fmodified_time
                 #print(my_dict)
     if (present_date_time == fmodified_time):
         for key in my_dict.keys():
             src_Dest=shutil.move(key,destination)
         print("moved")
     else:
         print("Files have already been moved")

 except IOError:
      print("No files")

def image_files():
 my_dict={}

 try:
     for root,dirs,files in os.walk(source,topdown=False):
         for name in files:
             if name.endswith(".png") or name.endswith(".bmp"):
                 path=os.path.join(root,name)
                 print(path)
                 fmodified_time=datetime.datetime.fromtimestamp(os.path.getmtime(path)).date()
                 print(fmodified_time)
                 my_dict[path]=fmodified_time
                 print(my_dict)
     if (present_date_time == fmodified_time):
         for key in my_dict.keys():
             src_Dest=shutil.move(key,destination)
         print("moved")
     else:
         print("Files have been already moved already")

 except IOError:
      print("No files")
    
      
###################################################################
# Define menu function to list the choice to the user
# Get the input from the user.
# Based on the choice , the respective function gets executed
###################################################################

def menu():
    print(30 * '*')
    print("MENU")
    print(30* '~')
    print("1.TEXT FILES")
    print("2.WORD DOCUMENTS")
    print("3.EXCEL")
    print("4.IMAGE FILES")
    print("5.EXIT")
    print(30 * '~')

    #chk_cond=0
    #while not chk_cond:
    try:
          choice=int(raw_input('Enter your choice[1-5]:'))
          chk_cond=1
    except IOError:
         print("Not a valid choice")

    if choice==1:
     text_files()
     menu()

    elif choice==2:
     word_files()
     menu()

    elif choice==3:
     excel_files()
     menu()

    elif choice==4:
      image_files()
      menu()

    elif choice==5:
      input=raw_input("Do u want to end the process")
      if (input == "Yes" or  "Y" or "y"):
        exit()
      else:
         menu()
      
          

    else:
     print("Invalid choice")

# Invoke menu function
menu()
