Information and data regarding the preliminary and extended evaluation of the SStaRM Ontology Design Pattern by PhD candidate Mousouris Spiridon and Professors Kavakli Evangelia and Kotis Konstantinos form the Department of Cultural Technology and Communication, University of the Aegean, Greece.

This repo details the summarization of SStaRM ODP evaluation presented in

- the paper “Defining Axioms to Address the Cultural Snapshot Phenomenon: Introducing the Spatiotemporal States Reference Model (SStaRM)”, presented in the MTSR 2025 Conference
- the article “Definition and Evaluation of the Spatiotemporal States Reference Model (SStaRM) Ontology Design Pattern”

# Preliminary Evaluation

**For paper “Defining Axioms to Address the Cultural Snapshot Phenomenon: Introducing the Spatiotemporal States Reference Model (SStaRM)” - MTSR 2025**

**Using FoKo Ontology individuals** [**https://foko-project.eu/#/de**](https://foko-project.eu/#/de)

**_inside ‘preliminary’ folder_**

## Data selection process 

Since FoKo contains multiple categories of buildings and structures, we can test the ability of our axioms to produce knowledge with SOIs of different classes. To ensure diversity in the categories of our data, we gathered all the distinct instances of foko:Object_Classification_Appellation in English, classifying  Objects, ie FoKo points of interest. Then,  from those original 159, we kept only classes describing buildings, constructions or part of buildings that are tangible, three dimensional and not movable. This gave us a list of 98 classes. Using that list, we wrote a query that gathers a max of 10 FoKo objects per class. This process gave us a random and diverse dataset, representative of all the categories, with 214894 triples originally. After adding ontology prefixes, imports and definitions of SStaRM-rekated classes and relations, necessary for axioms execution , the original dataset has 243883 triples.

For details, see the file : _preliminary_foko_categories_and_data_selection.xlsx_  

The initial file is : _preliminary_foko_all_foko_combined_extended.ttl_

## Usage of SPARQL CONSTRUCT queries

While translating the axioms to SWRL rules, we observed that some axioms require multiple aggregations per a combination of classes, in order to have multiple triples with common classes in different space and time. For example, for axiom 4 “SOIs actualize Cultural Subjects via the Events connected to the latter” multiple Actualizes class individuals of the same Cultural Subject must be produced, for different objects (ie SOIs), spaces and timespans, to answer detailed questions such as “when and where this particular Cultural Subject was actualized? ”. Grouping per Cultural Subject and then also by object, location and timespan is needed. This cannot be achieved with SWRL because it’s a deterministic rule language with limited abilities in complex aggregation, grouping or iteration. Its functions and relations are strictly binary (swrlx:makeOWLThing). For example, swrlx:makeOWLThing(?actualizes, ?culturalSubject) can produce a new Actualizes individual per Cultural Subject, but creating different Actualizes individuals for the same Cultural Subject and different objects, spaces and times is impossible. Thus, FOL rules are expressed as SPARQL CONSTRUCT queries, where grouping and aggregation is achieved. Results of each query are introduced to the dataset, making it the basis to run the next query and allowing us to measure new knowledge and individuals produced, at each step. 

## Execution of SPARQL CONSTRUCT queries

- File _preliminary_foko_all_foko_combined_extended.ttl_ was imported to Apache Jena Fuseki 5.3.0
- After executing the first SPARQL CONSTRUCT query for axioms 1 and 2, the results we got are in the file

_preliminary_foko_results-rule1-1-modification.rdf_ and

_preliminary_foko_results-rule1-2-production.rdf_

All of those combined are in the file

_preliminary_foko_all_foko_combined_extended_rule_1_2.ttl._

- That file is imported into Apache Jena Fuseki 5.3.0 again, as a new dataset and we execute SPARQL CONSTRUCT query for axiom 3, the results we got are in file

_preliminary_foko_results-rule-3.rdf._

- All of those combined are in the file

_preliminary_foko_all_foko_combined_extended_rule_3.ttl_ 

All the queries, number of triples, precision, recall and F1 score per axiom are detailed in the file :

_preliminary_foko_construct_queries_f1_score_MTSR_2025.xlsx_

# SStaRM ODP Evaluation – FoKo use case

**For article “Definition and Evaluation of the Spatiotemporal States Reference Model (SStaRM) Ontology Design Pattern”**

**Using FoKo Ontology individuals** [**https://foko-project.eu/#/de**](https://foko-project.eu/#/de)

**_inside ‘foko’ folder_**

## Data selection process

To ensure diversity in the categories of our data, we gathered all the distinct instances of foko:Object_Classification_Appellation in English, classifying  Objects, ie FoKo points of interest.

_SELECT DISTINCT ?classification_note WHERE {_

_?classification a foko:Object_Classification_Appellation ;_

_ecrm:P3_has_note ?classification_note ;_

_ecrm:P72_has_language ?language ._

_?language ecrm:P1_is_identified_by ?lang_id ._

_?lang_id ecrm:P3_has_note "EN" ._

_} ORDER BY ?classification_note_

Then, from those original 159, we kept only classes describing buildings, constructions or part of buildings that are tangible, three dimensional and not movable. This gave us a list of 98 classes. Using that list, we wrote a query that gathers a max of 10 FoKo objects per class.

_SELECT DISTINCT ?object WHERE {_

_?object a foko:Object ;_

_ecrm:P2_has_type ?classification ._

_?classification a foko:Object_Classification ;_

_ecrm:P149_is_identified_by ?appellation ._

_?appellation a foko:Object_Classification_Appellation ;_

_ecrm:P3_has_note "bridges (built works)"^^xsd:string ;_

_ecrm:P72_has_language ?language ._

_?language a ecrm:E56_Language ;_

_ecrm:P1_is_identified_by ?lang_id ._

_?lang_id a foko:Language_ID ;_

_ecrm:P3_has_note "EN"^^xsd:string ._

_} LIMIT 10_

This process gave us a random and diverse dataset, representative of all the categories, with 214894 triples originally. After adding ontology prefixes, imports and definitions of SStaRM-related classes and relations, the original dataset has 243883 triples.

For details, see the file : _foko_categories_and_data_selection.xlsx_  

The initial file is : _foko_all_foko_combined_extended.ttl_

## Execution of SPARQL CONSTRUCT queries

The process is that we execute a SPARQL CONSTRUCT query, combine the results to a new file, that is used as a base to execute the next query by importing to Apache Jena Fuseki 5.3.0 again, so a new SPARQL CONSTRUCT query is executed and so on.

- File _foko_all_foko_combined_extended.ttl_ was imported to Apache Jena Fuseki 5.3.0
- After executing the first SPARQL CONSTRUCT query for axioms 1 and 2, the results we got are combined in the file

_foko_all_foko_combined_extended_rule_1_2.ttl_

- That file is imported into Apache Jena Fuseki 5.3.0 again, as a new dataset and we execute SPARQL CONSTRUCT query for axiom 3, the results we got are combined in file

_foko_all_foko_combined_extended_rule_3.ttl_

- That file is imported into Apache Jena Fuseki 5.3.0 again, as a new dataset and we execute SPARQL CONSTRUCT query for axiom 4, the results we got are combined in file

_foko_all_foko_combined_extended_rule_4.ttl_

- That file is imported into Apache Jena Fuseki 5.3.0 again, as a new dataset and we execute SPARQL CONSTRUCT query for axiom 5, the results we got are combined in file

_foko_all_foko_combined_extended_rule_5.ttl_

- That file is imported into Apache Jena Fuseki 5.3.0 again, as a new dataset and we execute SPARQL CONSTRUCT query for axiom 8, the results we got are combined in file

_foko_all_foko_combined_extended_rule_8.ttl_

All the queries, results and number of triples are detailed in the file :

_foko_construct_queries_and_triples.xlsx_

# SStaRM ODP Evaluation – ArCo use case

**For article “Definition and Evaluation of the Spatiotemporal States Reference Model (SStaRM) Ontology Design Pattern”**

**Using ArCo Ontology individuals** [**https://dati.beniculturali.it/arco/index.php?lang=en**](https://dati.beniculturali.it/arco/index.php?lang=en)

**_inside ‘arco’ folder_**

## Data selection process

### SOIs

After examining the classes in the documentation, (https://dati.beniculturali.it/arco/primer-guide-v1.0-en.html ) the classes closer to a SOI are the ‘arco:ArchitecturalOrLandscapeHeritage’, particularly the ‘arco:ImmovableCulturalProperty’ and the ‘arco:Construction’

Using a SPARQL query to get the location of each of those classes

PREFIX arco-arco: &lt;https://w3id.org/arco/ontology/arco/&gt;

PREFIX arco-location: &lt;https://w3id.org/arco/ontology/location/&gt;

PREFIX CLV: &lt;https://w3id.org/italia/onto/CLV/&gt;

PREFIX arco-dd: &lt;https://w3id.org/arco/ontology/denotative-description/&gt;

PREFIX ns5: &lt;https://w3id.org/arco/ontology/immovable-property/&gt;

_select distinct ?typeValues_

_WHERE {_

_?constr rdf:type arco:ImmovableCulturalProperty ;_

_a-loc:hasTimeIndexedTypedLocation ?indexLocation._

_?indexLocation a-loc:hasLocationType ?typeValues ._

_}_

_limit 2000_

(replace arco:ImmovableCulturalProperty with ‘arco:ArchitecturalOrLandscapeHeritage’ and ‘ns5:Construction’)

It seems like that all SOIs are described by a ‘CurrentPhysicalLocation’. Probably all constructions in general are considered immovable, so they only have one “current” location. To examine if those ‘CurrentPhysicalLocation’ are maybe dynamic, having any differences in time, a query is necessary to gather all their timespans

_PREFIX arco-arco: &lt;https://w3id.org/arco/ontology/arco/&gt;_

_PREFIX arco-location: &lt;https://w3id.org/arco/ontology/location/&gt;_

_PREFIX CLV: &lt;https://w3id.org/italia/onto/CLV/&gt;_

_PREFIX arco-dd: &lt;https://w3id.org/arco/ontology/denotative-description/&gt;_

_PREFIX ns5: &lt;https://w3id.org/arco/ontology/immovable-property/&gt;_

_select distinct ?timeInerval_

_WHERE {_

_?constr rdf:type ns5:Construction;_

_a-loc:hasTimeIndexedTypedLocation ?indexLocation._

_?indexLocation tiapit:atTime ?timeInerval_

_}_

(replace ‘Construction’ with ‘arco:ArchitecturalOrLandscapeHeritage’ and arco:ImmovableCulturalProperty)

For all types of SOIs, this returns empty, so they don’t change over time. A SPARQL query is necessary to gather all the geometry types describing SOIs. Using

_PREFIX arco-arco: &lt;https://w3id.org/arco/ontology/arco/&gt;_

_PREFIX arco-location: &lt;https://w3id.org/arco/ontology/location/&gt;_

_PREFIX clv: &lt;https://w3id.org/italia/onto/CLV/&gt;_

_PREFIX clvapit: &lt;https://w3id.org/italia/onto/CLV/&gt;_

_PREFIX arco-dd: &lt;https://w3id.org/arco/ontology/denotative-description/&gt;_

_PREFIX ns5: &lt;https://w3id.org/arco/ontology/immovable-property/&gt;_

_select distinct ?geotype_

_where {_

_?s rdf:type ? ns5:Construction;_

_clvapit:hasGeometry ?geo._

_?geo clv:hasGeometryType ?geotype._

_}_

(replace ‘Construction’ with ‘arco:ArchitecturalOrLandscapeHeritage’ and arco:ImmovableCulturalProperty)

All geometry types of SOIs have

- https://w3id.org/italia/onto/CLV/Point
- https://w3id.org/italia/onto/CLV/Polygon
- https://w3id.org/italia/onto/CLV/Line

and ‘ArchitecturalOrLandscapeHeritage’ also has

- https://w3id.org/arco/resource/GeometryType/georeferenziazione-multiareale

this means that, contrary to FoKo, the spatiotemporal calculations of axioms are possible in ArCo, because the geometry types have formalized values with spatial meaning.

### Events

According to the documentation, the ArCo ‘cis:CulturalEvent’ class may be close to SStaRM ODP Events. Upon inspecting the distinct ‘dc:type’ values of ‘cis:CulturalEvent’ , using the following query

_PREFIX cis: &lt;http://dati.beniculturali.it/cis/&gt;_

_SELECT distinct ?evtype_

_WHERE {_

_?ev a cis:CulturalEvent;_

_dc:type ?evtype._

_}_

it seems like the types of those events regard social happenings and occasional activities. They are not Events that affect or change a SOI or its cultural attributes (like its use or architecture). This detail highlights the importance of examining the semantic definition of a class during SStaRM ODP mapping, because the despite their name, some ontology classes may have a different meaning. So, ArCo Events cannot be utilized by SStaRM ODP

### Cultural Subject

According to the documentation, the general class ‘a-dd:CulturalPropertyType’ that characterizes all ‘arco:CulturalProperty’ is suitable to express a general category or type.

### Actor

The general class of ‘I0:Agent’ can be used to express an Actor in general. But the ‘I0:Agent’ is connected to Cultural Properties using the ‘a-cd:hasCommission‘ property. Using the following query

_PREFIX ns5: &lt;https://w3id.org/arco/ontology/immovable-property/&gt;_

_SELECT ?cultpro (COUNT(?commission) AS ?commissionCount)_

_WHERE {_

_?cultpro a-cd:hasCommission ?commission ;_

_rdf:type ns5:Construction ._

_}_

_GROUP BY ?cultpro_

_HAVING (COUNT(?commission) > 1)_

_ORDER BY DESC(?commissionCount)_

(replace ‘Construction’ with ‘arco:ArchitecturalOrLandscapeHeritage’ and arco:ImmovableCulturalProperty)

Looks like SOIs in general are not related to an Actor via the a-cd:hasCommission property, because the query returns 0.

### States

According to the documentation, the class a-dd:DesignationInTime could be considered a State, because according to its definition in https://dati.beniculturali.it/lodview-arco/ontology/denotative-description/DesignationInTime.html , ‘This class represents a certain cultural property's designation/denomination attested over time.’

Despite ArCo containing a class that expresses a State, continuing with the application of SStaRM ODP axioms will showcase their flexibility to adjust and inference missing data: in the case of ArCo, Events are not defined, but can be inferenced, inversing its flexible logic, to allow further usage of axioms. Axioms will then produce knowledge regarding interconnecting States and SOIs. Additionally, since the SOIs of ArCo have a detailed description of their geospatial attributes, combined with standardized values, axioms that demand geospatial calculations can be executed and evaluated.

### Acquiring Data

After the clarification of ArCo’s structure, the next step involved to decide to select, use and download a representative smaller subset. This is due to the size of the ArCo dataset that limits the execution of complex queries without a LIMIT in the online SPARQL endpoint. We randomly chose the region of ‘Lombardia’ to select all the SOIs with that region in their ‘CLV:hasRegion’ property. We then downloaded all the SOIs with their accompanying relations and classes, using a DESCRIBE SPARQL query

_PREFIX arco-arco: &lt;https://w3id.org/arco/ontology/arco/&gt;_

_PREFIX arco-location: &lt;https://w3id.org/arco/ontology/location/&gt;_

_PREFIX CLV: &lt;https://w3id.org/italia/onto/CLV/&gt;_

_PREFIX arco-dd: &lt;https://w3id.org/arco/ontology/denotative-description/&gt;_

_PREFIX ns5: &lt;https://w3id.org/arco/ontology/immovable-property/&gt;_

_describe ?cultpro_

_WHERE {_

_?cultpro a ?typeValues_

_VALUES ?typeValues{_

_ns5:Construction_

_arco-arco:ArchitecturalOrLandscapeHeritage_

_arco:ImmovableCulturalProperty_

_}_

_?cultpro arco-location:hasCulturalPropertyAddress ?address._

_?address CLV:hasRegion ?region._

_?region rdfs:label ?regNome._

_FILTER regex(?regNome, "Lombardia", "i")_

_}_

The results where formatted as ‘Turtle’ and saved in a ‘.ttl’ file. Then that file was edited in protégé 5.6.5, to add prefixes, import ontologies and define the classes of State and Event.

See file

_arco_lombardia.ttl_

The above query efficiently describes the SOIs of a certain type, in a certain region, but the accompanying details of their geometry are not well described. Particularly, the additional triples of the property ‘hasGeometry’ are not included in the results because of the traversal depth limitation the DESCRIBE queries have and they only describe the triples immediate to the described resource, in this case the SOI. So, as a next step, to get the geometries per SOI, in detail, a new query lists them all

_PREFIX arco-arco: &lt;https://w3id.org/arco/ontology/arco/&gt;_

_PREFIX arco-location: &lt;https://w3id.org/arco/ontology/location/&gt;_

_PREFIX CLV: &lt;https://w3id.org/italia/onto/CLV/&gt;_

_PREFIX arco-dd: &lt;https://w3id.org/arco/ontology/denotative-description/&gt;_

_PREFIX ns5: &lt;https://w3id.org/arco/ontology/immovable-property/&gt;_

_select distinct ?cultpro_

_WHERE {_

_?cultpro_

_a ?typeValues._

_VALUES ?typeValues{_

_ns5:Construction_

_arco-arco:ArchitecturalOrLandscapeHeritage_

_arco:ImmovableCulturalProperty_

_}_

_?cultpro arco-location:hasCulturalPropertyAddress ?address._

_?address CLV:hasRegion ?region._

_?region rdfs:label ?regNome._

_FILTER regex(?regNome, "Lombardia", "i")_

_}_

And then a python script gets each SOI URL from the above list and uses inside the query below, it to get its geometry

&nbsp;   _CONSTRUCT {{_

&nbsp;       _?geo ?p ?o ._

&nbsp;       _?coords ?cp ?co._

&nbsp;   _}}_

&nbsp;   _WHERE {{_

&nbsp;       _VALUES ?cultpro {{ {class_URL} }}_

&nbsp;       _?cultpro clvapit:hasGeometry ?geo ._

&nbsp;       _?geo ?p ?o ._

&nbsp;       _?geo a-loc:hasCoordinates ?coords._

&nbsp;       _?coords ?cp ?co._

&nbsp;   _}}_

See python file _arco_get_geometries.py_

All the new triples are combined in a new ‘.ttl’ file and added in the original dataset.

See file

_arco_lombardia4geo.ttl_

## Execution of SPARQL CONSTRUCT queries

The process is that we execute a SPARQL CONSTRUCT query, combine the results to a new file, that is used as a base to execute the next query by importing to Apache Jena Fuseki 5.6.5 again, so a new SPARQL CONSTRUCT query is executed and so on.

- File _arco_lombardia4geo.ttl_ was imported to Apache Jena Fuseki 5.6.5
- After executing the first SPARQL CONSTRUCT query for axioms 1 and 2, regarding States, the results we got are combined in the file

_arco_rule-1-2-states-lombardia-geo.ttl_

- That file is imported into Apache Jena Fuseki 5.6.5 again and another SPARQL CONSTRUCT query for axioms 1 and 2 is executed, regarding Events. The results we got are combined in file

_arco_rule-1-2-events-lombardia-geo.ttl_

- In that file, new definitions regarding ‘Actualizes’ and ‘Cultural Subjects’ classes and properties are defined and the file

_arco_rule-4-prepare-lombardia-geo.ttl_

is created

- That file is imported into Apache Jena Fuseki 5.6.5 again and a SPARQL CONSTRUCT query for axiom 4 executed. The results we got are combined in file

_arco_rule-4 -lombardia-geo.ttl_

- In that file, new definitions regarding the ‘Cultural Subject Connection’ classes and properties are defined and the file

_arco_rule-5-prepare-lombardia-geo.ttl_

is created

- That file is imported into Apache Jena Fuseki 5.6.5 again and a SPARQL CONSTRUCT query for axiom 5 executed. The results we got are combined in file

_arco_rule-5-lombardia-geo.ttl_

- Since the geospatial properties of constructions in ArCo are detailed and their values are standardized, we can utilize axiom 6 to further investigate if there are SOIs included in a CS area and consequently, if they do, to further examine if they have any States missing. Before that, some processing of the values is required, for the filters and geospatial functions to work. The values of points is in a geo:wktLiteral format like “POINT(10 45)”^^ ogcgs:wktLiteral. But polygons have a set of coordinate individuals, each one looking like &lt;https://w3id.org/arco/resource/Coordinates/0300103953-geometry-polygon-1-coordinates-10&gt;. The number at the end is the order of coordinate and each one is essentially a point. A Python script takes all the lon/lat values from those points and serializes them as a Polygon ‘ogcgs:asWKT’ literal. This harmonizes all the values for all geometry types, in a format that GeoSPARQL queriy functions can work with. That Python script uses the RDFlib package to handle the graph and the triples https://rdflib.readthedocs.io/en/stable/ . It also imports the GeoSPARQL namespace as well as the Location and CLV namespaces from ArCo.

_See Python file arco_serialize_polygons.py_

- The output of that script with the new serialized values is re-introduced in the file arco_rule-5-lombardia-geo.ttl and so file

_arco_rule-6-prepare-lombardia-geo.ttl_

is defined

- The execution of axiom 6 does not have any results, so in the same file _arco_rule-6-prepare-lombardia-geo.ttl_ a property relating States to Cultural Subjects is defined and the file

_arco_rule-7-prepare-lombardia-geo.ttl_

is created

- That file is imported into Apache Jena Fuseki 5.6.5 again and a SPARQL CONSTRUCT query for axiom 7 executed. The results we got are combined in file

_arco_rule-7 -lombardia-geo.ttl_

All the queries, results and number of triples are detailed in the file :

_arco_construct_queries_and_triples.xlsx_