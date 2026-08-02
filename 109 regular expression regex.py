# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 18:56:11 2026

@author: Inspector
"""
def fun(name):
    print(f"Aslam o alikum {name}")
fun(input("Enter you name : "))

import re
result_search=re.search("pattren", r"the pattren is good")
print(result_search)

#re.sub() search for a specific text with in a string and replaces it with a new content
#first the text or expressin you want to find re.sub("old text,)
#second the text that will take its place re.sub("old text","new text")
#third the sting in which string is preformed re.sub("old text","new text","the string")

string=r"My name is Sye Ahsan Ali Gillani"
print(string)
string_new=re.sub("Sye","Syed",string)
print(string_new)

a=r"user:\desktop\notes" #the r used at the start of the string ignore \n as a next line command
print(a)

customer_review=['This product is good',
                 'the cachier was very rude to me sarah',
                 'amazing work from sadeen',
                 'lucky such a greate addition to my collections',
                 'sarah was able to helped me finding the items',
                 'that is very nice of you']
sarahs_review=[]
pattren_to_find=r"sarah?"
for string in customer_review:
    if(re.search(pattren_to_find,string)):
        sarahs_review.append(string)
print(sarahs_review)

amag_review=[]
a_to_find="sadeen"
for string in customer_review:
    if(re.search(a_to_find,string)):
        amag_review.append(string)
print(amag_review)

b_review=[]
b_to_find="^T"
for string in customer_review:
    if(re.search(b_to_find,string)):
        b_review.append(string)
print(b_review)

c_review=[]
c_to_find="sarah | sadeen"
for string in customer_review:
    if(re.search(c_to_find,string)):
        c_review.append(string)
print(c_review)

d_review=[]
d_to_find="s$"
for string in customer_review:
    if(re.search(d_to_find, string)):
        d_review.append(string)
print(d_review)

e_review=[]
e_to_find="(greate | help)ed"
for string in customer_review:
    if(re.search(e_to_find, string)):
        e_review.append(string)
print(e_review)

#easy modren way

e_review=[
    string
    for string in customer_review
    if(re.search("items", string))
        
    ]
print(e_review)

f_review=[
    string
    for string in customer_review
    if(re.match(r"This", string))
    
    ]
print(f_review)

refin_review=[
    string
    for string in customer_review
    if(re.findall("is | was", string))
    ]
print(refin_review)

text='python is my favourit i love python'
m=[

   re.sub('python','java', text)
   ]
print(m)
    
string_1=['java is my favourit',
          'i love using java',
          'the syntax of java is very good']
result=[
        re.sub('java','python',string,)
        for string in string_1]
print(string_1,"\n",
      result)