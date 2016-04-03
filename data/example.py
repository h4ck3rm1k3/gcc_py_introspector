def get_string_value (env):
    return 0
def get_working_directory(n):
    pass
def fprintf (*args):
    pass
stderr=None
def free(x):
    pass
    
def send_pwd_to_eterm ():
    pwd=''    
    f = 0;
    pwd = get_string_value ("PWD");
    if (pwd == 0) :
        f = pwd = get_working_directory ("eterm");
        
    fprintf (stderr, "\032/%s\n", pwd);
    free (f);

send_pwd_to_eterm ()    
