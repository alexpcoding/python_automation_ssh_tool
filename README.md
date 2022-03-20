# python SSH automation tool in linux
This is a app developed in python that tests connections for multiple linux servers and then extracts information ( similar to Ansible concept ).
The app uses subprocess module for ssh, no modules are required to install. There are specific modules for ssh that can be used ( like paramiko ), but the script was made to empphasize capabilities of subprocess module



Application options included:
* op1
* op2
* op3
* op4

Prerequisites and guidelines
  
1.) sshpass must be installaed on main server ( the password will be given from command line )  
2.) SSH connections must be available with the the servers, either with a user and password or a key ( same credentials for all servers ). Example:
`./python_ssh_tool.py -p` or `./python_ssh_tool.py -k /some/key`. The script will run only with one of these 2 formats ( by desgin ).  
3.) hosts.txt file must be populated:
![Capture3](https://user-images.githubusercontent.com/95858490/159157280-eefd7fd3-12d7-4165-96fe-ae85a0e0ad83.PNG)

4.) do not forget to add execution permissions on file : `chmod a+x file`  

Python version
Editor
## Examples
