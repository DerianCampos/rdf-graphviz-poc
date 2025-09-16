import sys
from graphviz import Digraph
import re

def parse_nt_line(line):
    # Simple regex to extract <subject> <predicate> <object> .
    match = re.match(r'<([^>]+)> <([^>]+)> <([^>]+)> \.', line.strip())
    if match:
        return match.groups()
    return None

def nt_to_graphviz(nt_file, output_png):
    dot = Digraph(comment='RDF Graph from NT')
    with open(nt_file, 'r') as f:
        for line in f:
            parsed = parse_nt_line(line)
            if parsed:
                subj, pred, obj = parsed
                dot.edge(subj, obj, label=pred)
    dot.render(output_png, format='png', cleanup=True)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python nt_to_png.py <input.nt> <output>")
        sys.exit(1)
    nt_file = sys.argv[1]
    output_png = sys.argv[2]
    nt_to_graphviz(nt_file, output_png)
