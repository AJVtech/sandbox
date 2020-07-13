# import libraries
import os
import shutil
from os import listdir
from os.path import isfile, join

# Create Function and Define lists and dictionaries  
def file_organizer(mypath):

# files is a list that stores all files in path expect already created folders. 
# So that it does not alter previously created folder.
# join method is used to skip folders and only include files.
    files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    file_type_variation_list=[]
    filetype_folder_dict={}

# use .split() method to split a file name and the result will be a list 
# and stored in filenamebrake.
# To get the extension we access the last word in the list. 
    for file in files:
        filenamebrake=file.split('.')
        filetype=filenamebrake[len(filenamebrake)-1]

# Appending file_type_variation_list
        if filetype not in file_type_variation_list:
            file_type_variation_list.append(filetype)

# Creating new folder for file extention and storing in dictionary
            new_folder_name=mypath+'/'+ filetype + '_folder'
            filetype_folder_dict[str(filetype)]=str(new_folder_name)
            if os.path.isdir(new_folder_name)==True:  #folder exists
                continue
            else:
                os.mkdir(new_folder_name)

# Moving Files to their respective Positions
    for file in files:
        src_path=mypath+'/'+file
        filenamebrake=file.split('.')
        filetype=filenamebrake[len(filenamebrake)-1]
        if filetype in filetype_folder_dict.keys():
            dest_path=filetype_folder_dict[str(filetype)]
            shutil.move(src_path,dest_path)
    print("File Organization Completed "+str(mypath))

#  Get Path and Call Function   
mypath=str(input("Enter Path "))
file_organizer(mypath)