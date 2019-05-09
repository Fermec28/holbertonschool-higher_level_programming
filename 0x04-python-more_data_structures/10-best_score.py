#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary != None:
        aux = {}
        aux["key"] = list(a_dictionary.keys())[0]
        aux["val"] = a_dictionary[aux["key"]]
        for key in a_dictionary.keys():
            if a_dictionary[key] > aux["val"]:
                aux["key"] = key
                aux["val"] = a_dictionary[key]
        return aux["key"]
    else:
        return None
