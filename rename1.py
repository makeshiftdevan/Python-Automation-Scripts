# Python code to rename multiple files in a directory or folder 
   
# importing os module which has rename function
import os, time, glob
  

while True:
                                                                                
    file = input("What path are your pictures in?")  #allows for user input

    newFile = file.replace ("\\", "/") #new variable to replace \ with /.  Had to escape the / with a an extra one.

    fileLoc = newFile +"/" #another new variable to add a / to the end of the file path

    time.sleep(1)

    print ("WARNING THIS WILL RENAME ALL FILES REGARDLESS OF FILETYPE!")

    time.sleep(2)


    title =input("What title would you like these pictures to have?")

    # Function to rename multiple files
    def main(): 
                     # enumerate function adds a counter to the number of iterations, in this case files renamed
        for count, filename in enumerate(os.listdir(fileLoc)): 
            dst = title + str(count) + ".jpg"
            src = str(fileLoc) + filename 
            dst1 =str(fileLoc) + dst 
          
            # rename() function will 
            # rename all the files 
            os.rename(src, dst1)
             # Driver Code 
    if __name__ == '__main__': 
      
        #  Calling main() function 
        main() 



    morePics = str(input("Would you like to rename more pictures?"))
    
            #below allows for capital or lower case answer
    if  morePics.lower() in ["yes", "y"]:
        continue #returns to while loop top
    else:
        print("Good bye")
        break
   


    
