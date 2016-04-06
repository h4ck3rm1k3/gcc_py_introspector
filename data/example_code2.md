  211 /* Call the YACC-generated parser and return the status of the parse.
  212    Input is read from the current input stream (bash_input).  yyparse
  213    leaves the parsed command in the global variable GLOBAL_COMMAND.
  214    This is where PROMPT_COMMAND is executed. */
  215 int
  216 parse_command ()
  217 {
  218   int r;
  219   char *command_to_execute;
  220
  221   need_here_doc = 0;
  222   run_pending_traps ();
  223
  224   /* Allow the execution of a random command just before the printing
  225      of each primary prompt.  If the shell variable PROMPT_COMMAND
  226      is set then the value of it is the command to execute. */
  227   if (interactive && bash_input.type != st_string)
  228     {
  229       command_to_execute = get_string_value ("PROMPT_COMMAND");
  230       if (command_to_execute)
  231     execute_variable_command (command_to_execute, "PROMPT_COMMAND");
  232
  233       if (running_under_emacs == 2)
  234     send_pwd_to_eterm ();   /* Yuck */
  235     }
  236
  237   current_command_line_count = 0;
  238   r = yyparse ();
  239
  240   if (need_here_doc)
  241     gather_here_documents ();
  242
  243   return (r);
  244 }