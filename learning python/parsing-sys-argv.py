#!/usr/bin/env python

"""
simple command line tool using argv 
"""

import sys

def say_it(greeting, name):
    message = f"{greeting} {name}"
    print(message)

if __name__ == '__main__':
    greeting = "hello"
    name = "John"

    if "--help" in sys.argv:
        help_message = f"Usage: {sys.argv[0]} --name <Name> --greeting <Greeting>"
        print(help_message)
        sys.exit()

    if "--name" in sys.argv:
        # get position after a name flag
        name_index = sys.argv.index("--name") + 1
        if name_index < len(sys.argv):
            name = sys.argv[name_index]

    if "--greeting" in sys.argv:
        greeting_index = sys.argv.index("--greeting") + 1
        if greeting_index < len(sys.argv):
            greeting = sys.argv[greeting_index]

    say_it(greeting, name)

