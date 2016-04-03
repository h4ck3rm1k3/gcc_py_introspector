def parse_command():
    r=undef
    command_to_execute=undef
    need_here_doc = 0
    run_pending_traps ()
    if (interactive and bash_input.type != st_string):
        command_to_execute = get_string_value ("PROMPT_COMMAND")
        if (command_to_execute):
            execute_variable_command (command_to_execute, "PROMPT_COMMAND")
        if (running_under_emacs == 2):
            send_pwd_to_eterm ()
    current_command_line_count = 0
    r = yyparse ()
    if (need_here_doc):
        gather_here_documents ()
    return (r);

