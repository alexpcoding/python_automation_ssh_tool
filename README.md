# python SSH automation tool in linux
This is an app developed in python that tests connections for multiple linux servers and then extracts information ( similar to Ansible concept ).
The app uses subprocess module for ssh, no modules are required to install. There are specific modules for ssh that can be used ( like paramiko ), but the script was made to emphasize capabilities of subprocess module.



Application options included:
* op1
* op2
* op3
* op4

Prerequisites and guidelines
  
1. **sshpass** must be installed on main server ( the password will be given from command line )  
2. SSH connections must be available with the the servers, either with a **user** and password or a **key** ( same credentials for all servers ). Example:
`./python_ssh_tool.py -p` or `./python_ssh_tool.py -k /some/key`. The script will run only with one of these 2 formats ( by design ).  
3. **hosts.txt** file must be populated:  
![Capture3](https://user-images.githubusercontent.com/95858490/159157280-eefd7fd3-12d7-4165-96fe-ae85a0e0ad83.PNG)  
4. you can use optional argument **-l (--limit)** : `./python_ssh_tool.py -p -l 192.168.0.5 ` - this will ignore hosts.txt file and use only that specific host 
5. use **-h (--help)** for app usage :  
![Capture4](https://user-images.githubusercontent.com/95858490/159233164-c281ed55-35ed-403d-ade5-e81b69146d45.PNG)  

7. do not forget to add execution permissions on file : `chmod a+x file`  

Python version : 3.10  
Editor version: Pycharm 2021.3  

## Examples  
![Capture](https://user-images.githubusercontent.com/95858490/159234151-1edcfd36-fa93-4c08-8275-2ace6828e6dd.PNG)!


