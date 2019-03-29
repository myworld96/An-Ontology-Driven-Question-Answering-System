import re
import os
from owlready2 import *
import owlready2.rdflib_store

onto = get_ontology("file:///home/akshay/Pictures/LEGALUPDATE.owl").load() 
filename ='SRL.txt'
found=""
with open(filename) as f:
    data = f.read()
m = re.search('A0: (.+?)\n', data)
with open('Penalty.txt', 'w') as f:
    f.write(" ")
if m:
    found = m.group(1)
#print(found)
print("\n")
fname ='SENT.txt'
class SparqlQueries:
    def __init__(self):
        my_world = World()
        my_world.get_ontology(
            "file:///home/akshay/Pictures/LEGALUPDATE.owl").load()  # path to the owl file is given here
        # sync_reasoner(my_world)  #reasoner is started and synchronized here
        self.graph = my_world.as_rdflib_graph()

    def search(self):
        # Search query is given here
        # Base URL of your ontology has to be given here
        query = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>" \
                "PREFIX owl: <http://www.w3.org/2002/07/owl#>" \
                "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>" \
                "PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>" \
                "SELECT distinct ?value " \
                "WHERE { " \
                "<http://www.semanticweb.org/akshay/ontologies/2018/11/LEGALUPDATE#" + st3 + "> ?property  ?value." \
                                                                                             "filter ( ?property not in ( rdf:type ) ) . " \
                                                                                             "}"

        # query is being run
        resultsList = self.graph.query(query)

        # creating json object
        response = []
        i = 0
        with open('Penalty.txt', 'w') as f:
            for item in resultsList:
                o = int(item['value'].toPython())
                i = i + 1
                if i > 1:
                    f.write("Penality (if repeated again) for  " + str(t) + " is ₹" + str(o) + ".")
                else:
                    f.write("Penality for " + str(t) + " is ₹" + str(o) + ".")
                    # print(o)


if found:
    with open(fname) as f:
        val = f.read()
    st=str(val)
    st1=st.replace(found,"")
    st1=st1.lstrip()
    st2=st1.replace(" ","_")
    st3=st2.replace(".","")
    #print(st3)
    t = found + " " + st1
    t = t.replace(".", "")
    runQuery = SparqlQueries()
    runQuery.search()
    print("\n")
else:
    with open('Penalty.txt', 'w') as f:
     f.write(" OFFENSE NOT FOUND")
