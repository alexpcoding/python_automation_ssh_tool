# python SSH automation tool in linux
This is an app developed in python that tests connections for multiple linux servers and then extracts information ( similar to Ansible concept ).
The app uses subprocess module for ssh, no modules are required to install. There are specific modules for ssh that can be used ( like paramiko ), but the script was made to emphasize capabilities of subprocess module.



Application overview:  
* level 3 network connection test
* port 22 test
* ssh password and key connection test
* extract linux server information , ex: memory, space, etc..
* multiple remote hosts targeted  
* options/arguments driven app  

Prerequisites and guidelines
  
1. **sshpass** must be installed on main server ( the password will be given from command line )  
2. SSH connections must be available with the servers, either with a **user** and password or a **key** ( same credentials for all servers ). Example:
`./python_ssh_tool.py -p` or `./python_ssh_tool.py -k /some/key`. The script will run only with one of these 2 formats ( by design ).  
3. **hosts.txt** file must be populated:  
![Capture3](https://user-images.githubusercontent.com/95858490/159157280-eefd7fd3-12d7-4165-96fe-ae85a0e0ad83.PNG)  
4. you can use optional argument **-l (--limit)** : `./python_ssh_tool.py -p -l 192.168.0.5 ` - this will ignore hosts.txt file and use only that specific host 
5. use **-h (--help)** for app usage :  
![Capture4](https://user-images.githubusercontent.com/95858490/159233164-c281ed55-35ed-403d-ade5-e81b69146d45.PNG)  


Python version : 3.10  
Editor version: Pycharm 2021.3  
Linux: Ubuntu 20.04.3 LTS  
  
## Examples  
![Capture](https://user-images.githubusercontent.com/95858490/159234151-1edcfd36-fa93-4c08-8275-2ace6828e6dd.PNG)!![Capture1](https://user-images.githubusercontent.com/95858490/159234530-9ed0e44f-60e3-4581-8039-5b98f1cc81a7.PNG)![Capture2](https://user-images.githubusercontent.com/95858490/159234608-6f07f3f5-418d-44eb-835b-a1dad5665c61.PNG)




