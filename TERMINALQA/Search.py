from practnlptools.tools import Annotator
from nltk.tokenize import sent_tokenize
import re
import os
annotator=Annotator()
print("******************************************************************************************")
text =raw_input("Ask me for Penality rate for an offense in MVD\n")
#text="Driver not having license."
s=annotator.getAnnotations(text)['srl']
with open('SENT.txt', 'w') as f:
 f.write("%s" %text)
st5=""
with open('SRL.txt', 'w') as f:
	for item in s:
	   st=str(item)
	   st1=st.replace("{","")
	   st2=st1.replace("'","")
	   st3=st2.replace("}","")
	   st4=st3.replace(" "," ")
	   st5=st4.replace(",","\n")
	   f.write("%s" %st5)
	   print(st5)
	   print("\n")
cmd = 'python3 answer.py'
os.system(cmd)

