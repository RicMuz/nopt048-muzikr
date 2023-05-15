# nopt048-muzikr
Linear programming repository

- Both generators are written in python, thus they do not have to be compiled
- It's necessary to have python installed on computer
- Both generators contains shebang, hence can be executed like (if you're in coresponding dir):
```bash
./main.py inputs/vstup-s0.txt
``` 
or
```bash
./main <inputs/vstup-s0.txt
```
- On Windows user have to specify the language:
```bash
python main.py inputs/vstup-s0.txt
```

## Directed graph without short cycles (#1)

Program firstly generates necessary sets and parameters:

- param N := maximum number of vertex (number of verticies as specified in input file - 1)
- set Verticies := labels of verticies (not used in this) 
- set Edges := oriented edges loaded from the file

Then the linear program itself is generated:

- For every edge we generate binary variable (1 if we use the edge in graph, else 0) => integer
- We maximize the weight of the edges, that will remain in the graph
- condition_edge_triangles: For every triangle in the graph, we will let stay max two edges
- condition_edge_squares: For every 4 cycle in the graph, we will let stay max three edges

At the end we specify, what the output is:

- We add together the weights of the edges, that won't stay in the graph and print them
- Then we print the edges that we deleted and their weights

## Clique cover

The program is similar to vertex coloring of the graph. Clique cover is coloring on complement of the graph.

Program firstly generates necessary sets and parameters:

- param N := maximum number of vertex (number of verticies as specified in input file - 1)
- set Verticies := labels of verticies
- set Edges := edges loaded from the file
- set Complement := edges that are not in the original graph (we use that we know that edges have the smaller vertex on left in the inputs)

Then the linear program itself is generated:

- For every vertex with every color we generate binary variable (x_v,i = 1 if we use the color i for vertex v, else 0) => integer
- Variable z is the number of maximum used color (maximally we will need as many colors as there are verticies) => integer
- We manimize the z variable (the number of needed colors)
- condition_vertex: For every vertex, we want just one color
- condition_edge: For every edge, we want different colors on the ends of the edge
- condition_color: We want just to use colors 0-z (otherwise trivial solution)

At the end we specify, what the output is:

- We print the number of color used
- Then we print which vertex is in which clique