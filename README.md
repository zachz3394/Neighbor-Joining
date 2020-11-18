# Neighbor-Joining Script

A short script to perform the intermediate calculations of the neighbor-joining algorithm used to create phylogenetic trees. 

## Usage
`python3 neighbor.py /PATH/TO/INPUT.txt /PATH/TO/OUTPUT.txt`

### Input
Takes a txt file containing the distance matrix from which to perform neighbor-joining calculations. 
See attached example file for formatting. The top-left entry is an X to facilitate formatting.

### Output
Calculates and prints to console:
* S(X) for each taxa X
* M(I)(J) for each of the taxa pairs (I,J)
* The minimum M(I)(J) among the taxa pairs
* S(I)(U) and S(J)(U), the distances for the newly created node U

In output file, writes the updated distance matrix after joining the node U.
