import sys
from graphviz import Digraph
import re

def parse_nq_line(line):
    # Simple regex to extract <subject> <predicate> <object> <graph> .
    match = re.match(r'<([^>]+)> <([^>]+)> <([^>]+)> <([^>]+)> \.', line.strip())
    if match:
        return match.groups()
    return None

def nq_to_graphviz(nq_file, output_png):
    dot = Digraph(comment='RDF Graph from NQ')
    with open(nq_file, 'r') as f:
        for line in f:
            parsed = parse_nq_line(line)
            if parsed:
                subj, pred, obj, _ = parsed
                dot.edge(subj, obj, label=pred)
    dot.render(output_png, format='png', cleanup=True)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python nq_to_png.py <input.nq> <output>")
        sys.exit(1)
    nq_file = sys.argv[1]
    output_png = sys.argv[2]
    nq_to_graphviz(nq_file, output_png)
