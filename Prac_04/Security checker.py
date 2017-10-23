
def username_check(username_list,username):
    if username in username_list:
        return True


def main():
    username_list = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole',
'InterpreterInterface', 'StartServer', 'bob']
    username = 0
    username = str(input("What is your username?"))

    if username_check(username_list, username) == True:
        print ("Access granted")

main()