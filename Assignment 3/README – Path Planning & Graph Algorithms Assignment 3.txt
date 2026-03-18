README – Path Planning & Graph Algorithms Assignment 3
Name: Naga Sai Jathin Madineni
Roll No: SE24UCSE015
________________


Overview
This project contains implementations of three important algorithms related to path finding and graph traversal:
1. Dijkstra’s Algorithm – to find shortest distances between Indian cities
2. Grid-based Path Planning (A*) – for navigating a robot in a grid with obstacles
3. Dynamic Grid Handling – ensuring a valid path exists using safe grid generation
The goal of this assignment is to understand how shortest path algorithms work in both real-world maps and simulated environments.
________________


1. Dijkstra’s Algorithm (Cities Dataset)
* A graph of Indian cities is created using a CSV file
* Each city is treated as a node, and distances between them are edges
* The algorithm finds the shortest distance from a given starting city to all other cities
Key Idea:
Always choose the node with the minimum distance using a priority queue.
________________


2. Grid-Based Path Planning (A* Algorithm)
* A 70×70 grid is generated
* Cells can either be:
   * Free space (0)
   * Obstacles (1)
* The A* algorithm finds the shortest path from the start (top-left) to the goal (bottom-right)
Why A*?
It is faster than BFS because it uses a heuristic (Manhattan distance) to guide the search.
________________


3. Safe Grid Generation (Improvement)
* Since random obstacles can sometimes block the path completely,
the grid is regenerated until a valid path is found
* This ensures the algorithm always produces a result during execution
________________
 Visualization
   * The grid is displayed using matplotlib for better understanding
   * Colors used:
   * White → Free space
   * Black → Obstacles
   * Red → Shortest path
   * Green → Start point
   * Blue → Goal point
This makes the output easy to interpret and suitable for screenshots.
________________


How to Run :
Make sure Python is installed
Install required libraries:
pip install matplotlib numpy
Run the Python file:
python filename.py


________________

Explanation of Outputs
1. Dijkstra’s Algorithm Output (Cities)
The output displays the shortest distance from the chosen starting city to all other cities in the dataset.
   * Each line shows:
City → Distance (in km)
   * The starting city will always have distance 0 km
   * Other cities show the minimum travel distance based on the available connections
Example Interpretation:
If it shows Mumbai → 710 km, it means the shortest route from the starting city to Mumbai is 710 km.
 This output proves that the algorithm correctly finds the minimum cost path in a weighted graph.
________________


2. Grid-Based Path Planning Output (A*)
The output consists of:
      * A message: “Path found!”
      * The number of steps required to reach the goal
      * A visual grid plot
In the visualization:
      * White cells → free space
      * Black cells → obstacles
      * Red path → shortest path taken
      * Green dot → starting point
      * Blue dot → goal point
The red path shows how the algorithm navigates around obstacles efficiently to reach the destination.
________________


3. Safe Grid Generation Output
This ensures that the program always produces a valid result.
      * If a randomly generated grid blocks all paths, it is discarded
      * A new grid is generated until a valid path is found
Final Output:
      * Always shows “Path found!”
      * Displays a valid path and its length
      * Avoids cases where “No path possible” is printed
This guarantees smooth execution during testing and demonstration.
________________


Overall Understanding
      * Dijkstra → Finds shortest distances in a city network
      * A* → Finds shortest path in a grid with obstacles
      * Safe generation → Ensures the algorithm always works on valid input
________________

Conclusion
This project demonstrates how shortest path algorithms can be applied in:
   * Navigation systems (like Google Maps)
   * Robotics path planning
   * Real-world problem solving using graphs
It also highlights the importance of efficient algorithms like Dijkstra and A* in handling large datasets and environments.

Final Note
The code is written in a simple and understandable way, focusing on clarity and practical implementation of concepts.
________________