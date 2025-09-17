import sys
import re
import html

def parse_nq_line(line):
    match = re.match(r'<([^>]+)> <([^>]+)> <([^>]+)> <([^>]+)> \.', line.strip())
    if match:
        return match.groups()
    return None

def nq_to_drawio_xml(nq_file, xml_file):
    nodes = set()
    edges = []
    with open(nq_file, 'r') as infile:
        for line in infile:
            parsed = parse_nq_line(line)
            if parsed:
                subj, pred, obj, _ = parsed
                subj = html.escape(subj)
                pred = html.escape(pred)
                obj = html.escape(obj)
                nodes.add(subj)
                nodes.add(obj)
                edges.append((subj, obj, pred))
    node_ids = {node: str(i+2) for i, node in enumerate(nodes)}
    xml = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<mxfile host="app.diagrams.net">',
           '  <diagram id="graph1" name="Graph">',
           '    <mxGraphModel dx="1000" dy="1000" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="850" pageHeight="1100" math="0" shadow="0">',
           '      <root>',
           '        <mxCell id="0" />',
           '        <mxCell id="1" parent="0" />']
    x, y = 100, 100
    for node, node_id in node_ids.items():
        xml.append(f'        <mxCell id="{node_id}" value="{node}" style="ellipse;whiteSpace=wrap;html=1;" vertex="1" parent="1">')
        xml.append(f'          <mxGeometry x="{x}" y="{y}" width="120" height="40" as="geometry" />')
        xml.append('        </mxCell>')
        x += 350  # Increased horizontal spacing
        if x > 2500:  # Increased wrap threshold for more columns
            x = 100
            y += 250  # Increased vertical spacing
    edge_id = len(nodes) + 2
    for subj, obj, pred in edges:
        xml.append(f'        <mxCell id="{edge_id}" value="{pred}" style="endArrow=block;html=1;" edge="1" parent="1" source="{node_ids[subj]}" target="{node_ids[obj]}">')
        xml.append('          <mxGeometry relative="1" as="geometry" />')
        xml.append('        </mxCell>')
        edge_id += 1
    xml.append('      </root>')
    xml.append('    </mxGraphModel>')
    xml.append('  </diagram>')
    xml.append('</mxfile>')
    with open(xml_file, 'w') as out:
        out.write('\n'.join(xml))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python nq_to_drawio_xml.py <input.nq> <output.xml>")
        sys.exit(1)
    nq_file = sys.argv[1]
    xml_file = sys.argv[2]
    nq_to_drawio_xml(nq_file, xml_file)