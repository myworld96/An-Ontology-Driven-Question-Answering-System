from practnlptools.tools import Annotator
from nltk.tokenize import sent_tokenize
annotator=Annotator()
filename ='test.txt'
with open(filename) as f:
    data = f.read()
#data = "He sent her a letter. Mary loves him."
sent=sent_tokenize(data,language='english')
print sent
i=0
for data in sent:
   s=annotator.getAnnotations(data)['srl']
   # print(s)
   with open('your_file.txt', 'a+') as f:
		   for item in s:
		    st=str(item)
		    st1=st.replace("{","")
		    st2=st1.replace("'","")
		    st3=st2.replace("}","")
		    st4=st3.replace(" "," ")
		    st5=st4.replace(",","\n")
		    f.write("\n%s\n" %st5)
		    print(st5)
		    print("\n")

