# Exercise to make simple program, which would make a print in interesting way - as cascade.

import time

text = input("Please provide text to be printed in cool way: ")
alfhabet = " 123456789AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuWwVvXxYyZz-"
to_be_printed = ""

for txt_letter in text:
    for alf_letter in alfhabet:
        if alf_letter != txt_letter:
            to_be_printed += alf_letter
            print(to_be_printed)
            to_be_printed = to_be_printed[:-1]
            time.sleep(0.1)
        else:
            to_be_printed += alf_letter
            print(to_be_printed)
            time.sleep(0.1)
            break
            
    
