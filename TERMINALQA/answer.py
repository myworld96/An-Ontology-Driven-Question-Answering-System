import re
import os
from owlready2 import *
onto = get_ontology("file:///home/akshay/Pictures/LEGALUPDATE.owl").load() 
filename ='SRL.txt'
with open(filename) as f:
    data = f.read()
m = re.search('A0: (.+?)\n', data)
if m:
    found = m.group(1)
#print(found)
print("\n")
fname ='SENT.txt'
with open(fname) as f:
    val = f.read()
st=str(val)
st1=st.replace(found,"")
st1=st1.lstrip()
st2=st1.replace(" ","_")
st3=st2.replace(".","")
#print(st3)
app="LEGALUPDATE."
new=app + st3
t=found +" "+ st1
t=t.replace(".","")
#print(t)
Individuals=onto.individuals()
for item in Individuals:
 st=str(item)
# print(st)
 i=0
 if st == new:
   Penality=item.Penality
   for val in Penality:
    i=i+1
    if i>1:
     print("Penality (if repeated again) for  " +t +" is ₹", val)
    else:
     print("Penality for " +t +" is ₹", val)
#print(new.Penality)
print("\n")
text =input("\nDo you wish to ask any other question?\n")
if text =='Y' or text=='y':
 cmd = 'python Search.py'
 os.system(cmd)
else:
 exit(0)
