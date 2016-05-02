# SKOS Visualization

- [Dependencies](#dependencies)
- [SKOS Core Support](#skos-core-support)
  - [Classes](#classes)
  - [Properties](#properties)
- [License](#license)

----------

The `skosviz` tool is a simple Python program for visualising SKOS-based RDF metadata.

## Dependencies

| Library | Required? | Description |
|---------|-----------|-------------|
| [rdflib](https://pypi.python.org/pypi/rdflib/) | Yes | Used for SKOS-based metadata parsing. |
| [rdflib-jsonld](https://pypi.python.org/pypi/rdflib-jsonld/) | No | Used for JSON-LD format support metadata parser. |

To install these libraries on Debian-based machines (including Ubuntu and Mint), you can run:

	sudo apt-get install python-LIBRARY

On other operating systems, you can run:

	sudo pip install LIBRARY

This will install the `LIBRARY` python package.

## SKOS Core Support

### Classes

| Class                                                                      | Supported |
|----------------------------------------------------------------------------|-----------|
| [Collection](http://www.w3.org/2004/02/skos/core#Collection)               | No        |
| [Concept](http://www.w3.org/2004/02/skos/core#Concept)                     | Yes       |
| [ConceptScheme](http://www.w3.org/2004/02/skos/core#ConceptScheme)         | Yes       |
| [OrderedCollection](http://www.w3.org/2004/02/skos/core#OrderedCollection) | No        |

### Properties

| Properties                                                                   | Supported |
|------------------------------------------------------------------------------|-----------|
| [altLabel](http://www.w3.org/2004/02/skos/core#altLabel)                     | Yes       |
| [broadMatch](http://www.w3.org/2004/02/skos/core#broadMatch)                 | Yes       |
| [broader](http://www.w3.org/2004/02/skos/core#broader)                       | Yes       |
| [broaderTransitive](http://www.w3.org/2004/02/skos/core#broaderTransitive)   | Yes       |
| [changeNote](http://www.w3.org/2004/02/skos/core#changeNote)                 | No        |
| [closeMatch](http://www.w3.org/2004/02/skos/core#closeMatch)                 | Yes       |
| [definition](http://www.w3.org/2004/02/skos/core#definition)                 | No        |
| [editorialNote](http://www.w3.org/2004/02/skos/core#editorialNote)           | No        |
| [exactMatch](http://www.w3.org/2004/02/skos/core#exactMatch)                 | Yes       |
| [example](http://www.w3.org/2004/02/skos/core#example)                       | No        |
| [hasTopConcept](http://www.w3.org/2004/02/skos/core#hasTopConcept)           | Yes       |
| [hiddenLabel](http://www.w3.org/2004/02/skos/core#hiddenLabel)               | No        |
| [historyNote](http://www.w3.org/2004/02/skos/core#historyNote)               | No        |
| [inScheme](http://www.w3.org/2004/02/skos/core#inScheme)                     | No        |
| [mappingRelation](http://www.w3.org/2004/02/skos/core#mappingRelation)       | No        |
| [member](http://www.w3.org/2004/02/skos/core#member)                         | No        |
| [memberList](http://www.w3.org/2004/02/skos/core#memberList)                 | No        |
| [narrowMatch](http://www.w3.org/2004/02/skos/core#narrowMatch)               | Yes       |
| [narrower](http://www.w3.org/2004/02/skos/core#narrower)                     | Yes       |
| [narrowerTransitive](http://www.w3.org/2004/02/skos/core#narrowerTransitive) | Yes       |
| [notation](http://www.w3.org/2004/02/skos/core#notation)                     | Yes       |
| [note](http://www.w3.org/2004/02/skos/core#note)                             | No        |
| [prefLabel](http://www.w3.org/2004/02/skos/core#prefLabel)                   | Yes       |
| [related](http://www.w3.org/2004/02/skos/core#related)                       | Yes       |
| [relatedMatch](http://www.w3.org/2004/02/skos/core#relatedMatch)             | Yes       |
| [scopeNote](http://www.w3.org/2004/02/skos/core#scopeNote)                   | No        |
| [semanticRelation](http://www.w3.org/2004/02/skos/core#semanticRelation)     | No        |
| [topConceptOf](http://www.w3.org/2004/02/skos/core#topConceptOf)             | No        |

## License

The `skosviz` project is released under the GPL version 3 or later license.

Copyright (C) 2011-2016 Reece H. Dunn
