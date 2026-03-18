#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 18:44:26 2026

@author: jathinmadineni
"""



import csv
import heapq


def load_graph(filename):
    graph = {}

    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            src = row["Source"]
            dest = row["Destination"]
            dist = int(row["Distance"])

            # create entries if not present
            if src not in graph:
                graph[src] = []
            if dest not in graph:
                graph[dest] = []

            # add edges (undirected graph)
            graph[src].append((dest, dist))
            graph[dest].append((src, dist))

    return graph


def dijkstra(graph, start):
    pq = [(0, start)]   # priority queue
    dist = {city: float('inf') for city in graph}
    dist[start] = 0

    while pq:
        current_dist, current_city = heapq.heappop(pq)

        for neighbor, weight in graph[current_city]:
            new_dist = current_dist + weight

            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    return dist


if __name__ == "__main__":
    
    filename = "cities.csv"  
    graph = load_graph(filename)

    start_city = input("Enter starting city: ")

    if start_city not in graph:
        print("City not found in dataset!")
    else:
        result = dijkstra(graph, start_city)

        print("\nShortest distances from", start_city)
        
        for city in sorted(result):
            print(f"{city:15} -> {result[city]} km")