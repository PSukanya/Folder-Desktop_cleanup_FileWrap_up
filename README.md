SHORT_DESCRIPTION:
-----------------
The project : Folder_Cleanup/Filw_wrap_up moves the necessary files / groups similar files created or modified on the current day & moves them to a destination. 

AIM:
---
This helps in :
 Referencing the file repository for later use.
 Improves the speed of the system after a perfect desktop cleanup on a daily basis.
 Easy access to report based files on grouping and placing them to the same folder.
 Downloads folder can also be emptied by moving the necessary files/folders first and then deleting the others manually (as my code doesn't cover this task)

SOURCE CODE's description:
--------------------------
Note :The source and destination files in my code are with respect to windows.

This menu based python code can be placed in a task scheduler and can be run on a daily basis.
The source and destination can be obtained from the user during run time or can be hard coded in the program.

The user is prompted for the choice of files and based on the selection, the files are moved.
Here, the files are grouped based on the extensions like '.txt','.doc.,etc.
Hence similar files are grouped and moved to the desire folder.

A dictionary stores the file path and the last modified time of the files.
A comparison is made between the last modified time of the files and the present date and time.
Once they match all the files are moved to the destination folder.

INSTALLATION:
------------
The source code is written in python, hence installation of python would be feasible.

I have also placed an '.exe' file.




 







