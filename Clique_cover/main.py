#!/usr/bin/env python3

import sys

class Generator:
    def __init__(self) -> None:
        pass

    def parse_edge_line(self, line: str) -> tuple:
        line = line.strip()
        line_parts = line.split()
        return (int(line_parts[0]),int(line_parts[2]))
    
    def parse_first_line(self, line: str) -> tuple:
        line = line.strip()
        line = line.strip(":")
        line_parts = line.split()
        return (int(line_parts[1]),int(line_parts[2]))
    
    def create_output(self, number_of_verticies_and_edges: int, edges: list) -> None:
        # Create the sets we work with 
        print(f"# Minimimalni pokryti klikami")
        print(f"param N := {number_of_verticies_and_edges[0]-1};")
        print("set Verticies := (0..N);")
        print(f"set Edges := { {*edges} };")
        print("set Complement := {(u,v) in Verticies cross Verticies: u < v && (u,v) !in Edges};")

        # The linear program
        print("var x{(i,j) in Verticies cross Verticies}, >= 0, <= 1, integer;")
        print("var z, >= 0, <= N, integer;")
        print("minimize obj: z;")
        print("condition_vertex{i in Verticies}: sum{j in Verticies} x[i,j] = 1;")
        print("condition_edge{(u,v) in Complement, i in Verticies}: x[u,i] + x[v,i] <= 1;")
        print("condition_color{v in Verticies, i in Verticies}: i * x[v,i]<=z;") 
        print("solve;")

        # Formating output
        print("printf \"#OUTPUT: %d\\n\", z+1;")
        print("printf {(v,i) in Verticies cross Verticies} (if x[v,i] == 1 then \"v_%d: %d\\n\" else \"\"), v, i;")
        print("printf \"#OUTPUT END \\n\";")
        print("end;")

        
    def run(self, func) -> None:
        line = func()
        number_of_verticies_and_edges = self.parse_first_line(line)
        line = func()
        edges = []
        while line:
            edge = self.parse_edge_line(line)
            edges.append(edge)
            #edges.append((edge[1],edge[0]))
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

