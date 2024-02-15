import time
import xmlrpc.client
import os

PROXY = xmlrpc.client.ServerProxy('http://localhost:5050')

# main function
def main():
    last_check_file = os.listdir('./client/')
    last_checked_time = time.time()
    try:
        while True:
            print("Consistency check will run after 15 sec")
            time.sleep(15)
            print("Checking for consistency now...")
            # code to scan file-s check
            current_file_client = os.listdir('./client/')
            for file in current_file_client:
                # time check
                file_path = './client/' + file
                if os.path.getmtime(file_path) > last_checked_time:
                    if file not in last_check_file:
                        print(f"Uploading new {file} file")
                        # code to upload file to the server
                        file_path = "./client/" + file
                        with open(file_path, "rb") as files:
                            file_binary =  xmlrpc.client.Binary(files.read())
                        PROXY.server_download(file_binary, file)
                        last_check_file.append(file)
                    else:
                        print("Uploading " + file)
                        # code to upload file to the server
                        file_path = "./client/" + file
                        with open(file_path, "rb") as files:
                            file_binary =  xmlrpc.client.Binary(files.read())
                        PROXY.server_download(file_binary, file)
            for file in last_check_file:
                if file not in current_file_client:
                    print(f'Deleting {file} from server')
                    # code to delete file from server
                    filepath = "./client/" + file
                    result = PROXY.server_delete(file)
                    print(result)
                    last_check_file.remove(file)
            last_checked_time = time.time()
    except KeyboardInterrupt:
        print("Existing Client")

if __name__ == "__main__":
    main()