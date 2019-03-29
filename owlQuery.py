from owlready2 import *
import owlready2.rdflib_store
class SparqlQueries:
    def __init__(self):
        my_world = World()
        my_world.get_ontology("file:///home/akshay/Pictures/LEGALUPDATE.owl").load() #path to the owl file is given here
        #sync_reasoner(my_world)  #reasoner is started and synchronized here
        self.graph = my_world.as_rdflib_graph()

    def search(self):
        #Search query is given here
        #Base URL of your ontology has to be given here
        query = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>"\
		"PREFIX owl: <http://www.w3.org/2002/07/owl#>"\
		"PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>"\
		"PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>"\
                "SELECT distinct ?value " \
                "WHERE { " \
                "<http://www.semanticweb.org/akshay/ontologies/2018/11/LEGALUPDATE#using_sub-standard_articles_or_process> ?property  ?value." \
		"filter ( ?property not in ( rdf:type ) ) . "\
                "}"

        #query is being run
        resultsList = self.graph.query(query)

        #creating json object
        response = []
        for item in resultsList:
           
            o = int(item['value'].toPython())
            print(o)
       

        #print(response) #just to show the output
        #return response


runQuery = SparqlQueries()
runQuery.search()
