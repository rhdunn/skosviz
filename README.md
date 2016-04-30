# SKOS Visualization

- [Dependencies](#dependencies)
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

## License

The `skosviz` project is released under the GPL version 3 or later license.

Copyright (C) 2011-2016 Reece H. Dunn
