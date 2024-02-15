Please refer below steps to execute the code for each part:

Unzip the folder 'project-1-1002092125-1001826818' which contains following structure:
- part-1
    - client
        test.txt
    - server
    - client_part1.py
    - server_part1.py    
- part-2
    - client
        test.txt
    - server
    - client_part2.py
    - server_part2.py 
- part-3
    - client_part3.py
    - server_part3.py 
- Readme.txt
- Report-project1.pdf


Note: 
    - Require python version >= 3.8
    - IDE used VS code
    - Download xml-rpc please using command : pip instal xml-rpc.


1. Part-1:
    - Go inside the part-1 folder location and:
      run server on cmd 1 using command: python server_part1.py
      run client on cmd 2 using command: python client_part1.py
    - Follow the menu.
    - Use the menu to perform operations like upload to server, Donload to client from the server,
      delete the files on client and server and rename file on client and server.


2. Part-2:
   - Go inside the part-2 folder location and:
     run server on cmd 1 using command : python server_part2.py
     run client on cmd 2 using command: python client_part2.py
   - To do changes sync start after 15 second. Program will notify the same on the client cmd.
   - Add new file like test2.txt or change the content of test.txt file or delete test.txt file at client folder and
     it will reflect the respective modifications at the server side when the check function runs a scan after every 15 seconds.


3. Part-3:
   - Go inside the part-3 folder location and:
     run server on cmd 1 using command: python server_part3.py
     run client on cmd 2 using command: python client_part3.py
   - Follow menu
   - For sync operations, the result will directly be shown on the prompt after entering required inputs.
   - For async operations, result will be accessed using 5th option in menu.
 
