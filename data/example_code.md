Here is an example from the bash source code and it's representation in an experimental yaml syntax.

## C Code

```
196 /* Send an escape sequence to emacs term mode to tell it the
197 current working directory. */
198 static void
199 send_pwd_to_eterm ()
200 {
201 char *pwd, *f;
202
203 f = 0;
204 pwd = get_string_value ("PWD");
205 if (pwd == 0)
206 f = pwd = get_working_directory ("eterm");
207 fprintf (stderr, "\032/%s\n", pwd);
208 free (f);
209 }
```


## Yaml Representation

```
function:
  name: send_pwd_to_eterm
  link: static
  srcp: eval.c:199
  body:
    bind:
      body:
      - [f, '=', '0']
      - - pwd
	- '='
	- call: {E0: '"PWD"', fn: null}
      - cond_expr:
	  OP0: [pwd, ==, '0']
	  OP1:
	  - f
	  - '='
	  - - pwd
	    - '='
	    - call: {E0: '"eterm"', fn: null}
      - call: {E0: stderr, E1: '"&#xfffd;/%s"', E2: pwd, fn: null}
      - call: {E0: f, E1: '"../eval.c"', E2: '208', fn: null}
      vars: pwd

```


## Json format

```
{
    "function": {
        "body": {
            "bind": {
                "body": [
                    [
                        "f",
                        "=",
                        "0"
                    ],
                    [
                        "pwd",
                        "=",
                        {
                            "call": {
                                "E0": "\"PWD\"",
                                "fn": null
                            }
                        }
                    ],
                    {
                        "cond_expr": {
                            "OP0": [
                                "pwd",
                                "==",
                                "0"
                            ],
                            "OP1": [
                                "f",
                                "=",
                                [
                                    "pwd",
                                    "=",
                                    {
                                        "call": {
                                            "E0": "\"eterm\"",
                                            "fn": null
                                        }
                                    }
                                ]
                            ]
                        }
                    },
                    {
                        "call": {
                            "E0": "stderr",
                            "E1": "\"&#xfffd;/%s\"",
                            "E2": "pwd",
                            "fn": null
                        }
                    },
                    {
                        "call": {
                            "E0": "f",
                            "E1": "\"../eval.c\"",
                            "E2": "208",
                            "fn": null
                        }
                    }
                ],
                "vars": "pwd"
            }
        },
        "link": "static",
        "name": "send_pwd_to_eterm",
        "srcp": "eval.c:199"
    }
}
```