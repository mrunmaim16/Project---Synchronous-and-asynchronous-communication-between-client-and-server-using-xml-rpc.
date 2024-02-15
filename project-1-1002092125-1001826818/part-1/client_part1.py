import xmlrpc.client
import os

# Global variable
PROXY = xmlrpc.client.ServerProxy('http://localhost:5050')

CLIENT_FOLDER_PATH = "./client/"
SERVER_FOLDER_PATH = "./server/"

MENU = {
    1: "Upload File",
    2: "Download File",
    3: "Delete File",
    4: "Rename File",
    5: "Exit"
}

# Main function
def main():
    # Menu running forever
    while True:
        # menu_display()
        for key in MENU.keys():
            print(key, "--", MENU[key]) 
        option = " "

        try:
            user_option = int(input("Enter one option from the above list: "))

        except:
            print(" You have selected an invalid option. ")

        if user_option == 1:
            file_name = input("Enter filename to be uploaded to the server: ")
            # Code to upload file to server
            file_path = CLIENT_FOLDER_PATH + file_name
            if os.path.exists(file_path):
                print("Uploading File that you have mentioned to the server..")
                with open(file_path, "rb") as file:
                    file_binary =  xmlrpc.client.Binary(file.read())
                PROXY.server_download(file_binary, file_name)
            else:
                result = "Error: File not exists in client"
                print(result)

        elif user_option == 2:
            file_name = input("Enter filename to be download from the server: ")
            # Code to Download
            file_path = CLIENT_FOLDER_PATH + file_name
            if os.path.exists(file_path):
                with open(file_path, "wb") as file:
                    file.write(PROXY.server_upload(file_name).data)
                print("File has been downloaded from the server")    
            else:
                result = "Error: File not exists in client"
                print(result)        

        elif user_option == 3:
            file_name = input("Enter filename to deleted on both client and server: ")
            # Code to Delete File from client and server
            filepath = CLIENT_FOLDER_PATH + file_name
            if os.path.exists(filepath):
                os.remove(filepath)
                result = "Removed " + file_name + " from client"
                print(result)
                result = PROXY.server_delete(file_name)
                print(result)
            else:
                print("File not exists in client")
                result = PROXY.server_delete(file_name)
                print(result)

        elif user_option == 4:
            old_filename = input("Enter filename you wish to rename: ")
            new_filename = input("Enter the new fielname: ")
            # Code to Rename File in client and server
            old_path = CLIENT_FOLDER_PATH + old_filename
            new_path = CLIENT_FOLDER_PATH + new_filename
            if os.path.isfile(new_path):
                result = "File Exists in client"
                print(result)
            else:
                os.rename(old_path, new_path)
                result = "Done in client"
                print(result)
            print(PROXY.server_rename(old_filename, new_filename))

        elif user_option == 5:
            # Code to Exit client
            print("Exiting client..!")
            exit()            

# Execution start
if __name__ == '__main__':
    main()