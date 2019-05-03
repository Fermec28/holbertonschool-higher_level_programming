#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for function in dir(hidden_4):
        if function[0] != '_' and function[1] != '_':
            print(function)
