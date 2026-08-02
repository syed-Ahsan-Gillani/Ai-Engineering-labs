sentence=input("enter the text : ")
sentences=sentence.lower()
newsentences=sentence.upper()
a=input("choose upper case or lower case")

if a=="upper case":
    print(newsentences)
elif a=="lower case":
    print(sentences)
else:
    print("spelling mistake in choosing upper or lower case")
    
    
list_sentence=['My name Is Syed AHSan ali Gillani',
               'Who are YOU?',
               'the CaT is slEEping ON The maT']
lower_sentence_list=[x.lower() for x in list_sentence]
print(lower_sentence_list)

