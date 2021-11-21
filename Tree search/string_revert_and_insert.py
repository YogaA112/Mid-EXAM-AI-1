!#/bin/python

def string_revert_and_insert(string, p, l):
    temp_string = string[p:p+l]
    reverted_string = ""

    for item in temp_string:
        reverted_string = item + reverted_string

    result_string = string[:p] + reverted_string + string[p:]
    print result_string


string_revert_and_insert("ababababjsjsjs", 10, 5)
