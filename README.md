# Table of Contents

- [Features](#features)
- [Folder Structure](#folder-structure)
- [Usage](#usage)
- [Requirements](#requirements)
- [License](#license)
# RDF Graphviz PoC

This project demonstrates how to visualize RDF data using Graphviz. It provides scripts to convert RDF data in N-Quads (`.nq`) and N-Triples (`.nt`) formats into PNG images representing the graph structure.

## Features
- Convert `.nq` (N-Quads) files to PNG using `nq_to_png.py`
- Convert `.nt` (N-Triples) files to PNG using `nt_to_png.py`
- Example RDF data included

## Folder Structure


```
.
├── app/
│   ├── nq_app/
│   │   ├── nq_to_png.py
│   │   └── nq_to_xml.py
│   └── nt_app/
│       └── nt_to_png.py
├── data/
│   ├── nq/
│   │   └── nq_metal_example.nq
│   └── nt/
│       └── nt_metal_example.nt
├── models/
│   ├── nq/
│   │   └── nq_metal_model.png
│   ├── nt/
│   │   └── nt_metal_model.png
│   ├── png/
│   │   └── nq_metal_model.png
│   └── xml/
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
├── venv/
```

### Description
- `app/nq_app/` and `app/nt_app/`: Application scripts or modules for N-Quads and N-Triples
- `app/nq_app/nq_to_xml.py`: Script to convert N-Quads to XML
- `data/nq/` and `data/nt/`: Example RDF data in N-Quads and N-Triples formats
- `models/nq/`, `models/nt/`, `models/png/`: Output PNG files generated from the converters
- `models/xml/`: Output XML files generated from the converters (currently empty)
- `requirements.txt`: Python dependencies
- `README.md`: Project information and usage instructions
- `LICENSE`: License information
- `.gitignore`: Git ignore rules
- `venv/`: Python virtual environment (not tracked in git)


## Usage

### Convert N-Quads to PNG
```sh
python app/nq_app/nq_to_png.py data/nq/nq_metal_example.nq models/nq/nq_metal_model
```
This will generate a PNG file at `models/nq/nq_metal_model.png` visualizing the RDF graph.

### Convert N-Triples to PNG
```sh
python app/nt_app/nt_to_png.py data/nt/nt_metal_example.nt models/nt/nt_metal_model
```
This will generate a PNG file at `models/nt/nt_metal_model.png` visualizing the RDF graph.

### Convert N-Quads to XML
```sh
python app/nq_app/nq_to_xml.py data/nq/nq_metal_example.nq models/xml/nq_metal_model.xml
```
This will generate an XML file at `models/xml/nq_metal_model.xml` from the N-Quads data.

## Requirements
- Python 3.x
- Graphviz (for rendering PNGs)
- Python packages listed in `requirements.txt`

To install the required Python packages, run:
```sh
pip install -r requirements.txt
```

## License
See `LICENSE` file for details.