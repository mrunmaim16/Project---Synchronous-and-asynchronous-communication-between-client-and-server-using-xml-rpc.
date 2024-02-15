from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
import os

# Global variable
SERVER = SimpleXMLRPCServer(('localhost', 5050), logRequests=True)

SERVER_FOLDER = "./server/"
CLIENT_FOLDER = "./client/"


# Client upload file to server
def server_download(file_binary, file_name):
    file_path = SERVER_FOLDER + file_name
    with open(file_path, "wb") as file:
        file.write(file_binary.data)
    return True


# Client download file from server
def server_upload(file_name):
    file_path = SERVER_FOLDER + file_name
    with open(file_path, "rb") as file:
        return xmlrpc.client.Binary(file.read())
    

# Delete file from server
def server_delete(file_name):
    filepath = SERVER_FOLDER + file_name
    if os.path.exists(filepath) == True:
        os.remove(filepath)
        result = "Removed " + file_name + " from server"
        return result
    else:
        result = "File not exists in server"
        return result


# Rename file in server
def server_rename(old_filename, new_filename):
    old_path = SERVER_FOLDER + old_filename
    new_path = SERVER_FOLDER + new_filename
    if os.path.isfile(new_path) == True:
        result = "File Exists in server"
        return result
    else:
        os.rename(old_path, new_path)
        result = "Done in server"
        return result


# Main function
def main():
    try:
        # Function exceuted by client using rpc
        SERVER.register_function(server_download)
        SERVER.register_function(server_upload)
        SERVER.register_function(server_delete)
        SERVER.register_function(server_rename)
        print('Serving..')
        SERVER.serve_forever()
    except KeyboardInterrupt:
        print("Existing..")

# Execution start
if __name__ == "__main__":
    main()