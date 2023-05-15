#!/usr/bin/env python3

import sys

class Generator:
    def __init__(self) -> None:
        pass

    def parse_edge_line(self, line: str) -> tuple:
        line = line.strip()
        line = line.strip(")")
        line_parts = line.split()
        return (int(line_parts[0]),int(line_parts[2]),int(line_parts[4]))
    
    def parse_first_line(self, line: str) -> tuple:
        line = line.strip()
        line = line.strip(":")
        line_parts = line.split()
        return (int(line_parts[2]),int(line_parts[3]))
    
    def create_output(self, number_of_verticies_and_edges: int, edges: list) -> None:
        # Create the sets we work with 
        print(f"# Orientovany graf bez kratkych orientovanych cyklu")
        print(f"param N := {number_of_verticies_and_edges[0]};")
        print("set Verticies := (1..N);")
        print(f"set Edges := { {*edges} };")

        # The linear program
        print("var x{(u,v,c) in Edges}, >= 0, <= 1, integer;")
        print("maximize obj: sum{(u,v,c) in Edges} x[u,v,c]*c;")
        print("condition_edge_triangles{(u,v,c) in Edges,(v,w,d) in Edges ,(w,u,e) in Edges}: x[u,v,c] + x[v,w,d] + x[w,u,e] <= 2;")
        print("condition_edge_squares{(u,v,c) in Edges,(v,w,d) in Edges ,(w,y,e) in Edges,(y,u,f) in Edges}: x[u,v,c] + x[v,w,d] + x[w,y,e] + x[y,u,f] <= 3;")
        print("solve;")

        # Formating output
        print("printf \"#OUTPUT: W %d\\n\", sum{(u,v,c) in Edges} abs(x[u,v,c]-1)*c;")
        print("printf {(u,v,c) in Edges} (if x[u,v,c] == 0 then \"%d --> %d with weight %d\\n\" else \"\"), u, v, c;")
        print("printf \"#OUTPUT END \\n\";")
        print("end;")

        
    def run(self, func) -> None:
        line = func()
        number_of_verticies_and_edges = self.parse_first_line(line)
        line = func()
        edges = []
        while line:
            edges.append(self.parse_edge_line(line))
            line = func()
        self.create_output(number_of_verticies_and_edges, edges)
        

def main() -> None:
    generator = Generator()
    exit_code = 0
    if len(sys.argv) == 1:
        generator.run(sys.stdin.readline)
    elif len(sys.argv) == 2:
        with open(sys.argv[1],'r') as f:   
            generator.run(f.readline)
    else:
        print("Error: wrong number of parameters", file=sys.stderr)
        exit_code = 1
    sys.exit(exit_code)

if __name__ == "__main__":
    main()

