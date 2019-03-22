from owlready2 import *
onto_path.append("/home/akshay/Pictures")
onto = get_ontology("file:///home/akshay/Pictures/test.owl").load()
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
test_pizza = onto.Person(st3)
onto.save()
with open('Check.txt', 'w') as f:
    f.write("ONTOLOGY SAVED SUCCESSFULLY!!!!!")