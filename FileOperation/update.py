def update_server_config(file_path,key,value):
    with open(file_path,"r") as file:
        lines=file.readlines()
       # print(lines)

    with open(file_path,"w") as file:
        for line in lines:
            if key in line:
                file.write(key+"="+value+"\n")
            else:
                file.write(line)
    
    with open(file_path,"r") as file:
        lines=file.readlines()
        for line in lines:
            if  key in line:
                print(line)

    # Path to the server configuration file
server_config_file = 'server.conf'

# Key and new value for updating the server configuration
key_to_update = 'MAX_CONNECTIONS'
new_value = '800'  # New maximum connections allowed

# Update the server configuration file
update_server_config(server_config_file, key_to_update, new_value)
