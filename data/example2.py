def send_pwd_to_eterm ():
    pwd=''    
    f = 0;
    pwd = get_string_value ("PWD");
    if (pwd == 0) :
        f = pwd = get_working_directory ("eterm");
        
    fprintf (stderr, "\032/%s\n", pwd);
    free (f);

