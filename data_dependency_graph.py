"""
This sorts the table names by dependencies, in an order where we
can insert data in order from left to right, and prevent foreign key constraint errors.

See the following link for more: https://en.wikipedia.org/wiki/Topological_sorting
"""
from collections import defaultdict
from collections import deque
from typing import Deque

UNVISITED = "<UNVISITED>"
VISITING = "<SEARCHING>"
VISITED = "<VISITED>"


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.nodes = {}
        # self.visited = dict()

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.nodes[u] = UNVISITED
        self.nodes[v] = UNVISITED

    def dfs(self, node: str, queue: Deque):
        self.nodes[node] = VISITING
        for destination in self.graph[node]:
            if self.nodes[destination] == VISITING:
                raise ValueError(
                    "Graph contains a cycle, unable to perform topological sort"
                )
            if self.nodes[destination] == UNVISITED:
                self.dfs(destination, queue)
        self.nodes[node] = VISITED
        queue.appendleft(node)

    def topological_sort(self) -> Deque:
        queue = deque()
        for node in self.nodes:
            if self.nodes[node] == UNVISITED:
                self.dfs(node, queue)
        return queue


outgoing_edges = [
    [
        "appointments",
        [
            "appointment_employees",
            "appointment_medical_conditions",
            "diagnoses",
            "exams",
            "lab_reports",
        ],
    ],
    ["archived_files", ["lab_reports"]],
    [
        "employees",
        [
            "appointment_employees",
            "archived_files",
            "diagnoses",
            "immunized_employees",
            "prescriptions",
            "referrals",
        ],
    ],
    ["exams", ["administered_vaccines", "blood_exams", "covid_exams"]],
    ["immunizations", ["immunized_employees", "immunized_patients"]],
    ["insurance_providers", ["insurance_covers"]],
    ["lab_reports", ["exams", "report_creators"]],
    [
        "medical_conditions",
        ["appointment_medical_conditions", "diagnoses", "relative_conditions"],
    ],
    [
        "patients",
        [
            "appointments",
            "archived_files",
            "diagnoses",
            "immunized_patients",
            "insurance_covers",
            "prescriptions",
            "relatives",
            "referrals",
        ],
    ],
    ["pharmacies", ["prescriptions"]],
    ["referrable_doctors", ["referrals"]],
    ["relatives", ["relative_conditions"]],
    ["specialized_labs", ["accepted_tests", "report_creators"]],
    ["tests", ["accepted_tests"]],
]


def build_topological_sor() -> Deque:
    g = Graph()
    for origin, destinations in outgoing_edges:
        for destination in destinations:
            g.add_edge(origin, destination)
    return g.topological_sort()


def print_topological_sort():
    print("Topological Sort")
    print(" --> ".join(build_topological_sor()))


if __name__ == "__main__":
    print_topological_sort()
