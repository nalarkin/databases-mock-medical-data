"""
This sorts the table names by dependencies, in an order where we
can insert data in order from left to right, and prevent foreign key constraint errors.

See the following link for more: https://en.wikipedia.org/wiki/Topological_sorting
"""
from collections import defaultdict
from collections import deque
from pprint import pprint
from typing import Deque, Iterable

UNVISITED = "<UNVISITED>"
VISITING = "<SEARCHING>"
VISITED = "<VISITED>"


class DirectedGraph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.nodes = {}

    def add_edge(self, origin, destination):
        if origin != destination:
            self.graph[origin].append(destination)
            self.nodes[destination] = UNVISITED
        self.nodes[origin] = UNVISITED

    def _dfs(self, node: str, queue: Deque):
        self.nodes[node] = VISITING
        for destination in self.graph[node]:
            if self.nodes[destination] == VISITING:
                raise ValueError(
                    "Graph contains a cycle, unable to perform topological sort"
                )
            if self.nodes[destination] == UNVISITED:
                self._dfs(destination, queue)
        self.nodes[node] = VISITED
        queue.appendleft(node)

    def topological_sort(self) -> Iterable:
        queue = deque()
        for node, search_status in self.nodes.items():
            if search_status == UNVISITED:
                self._dfs(node, queue)
        return iter(queue)


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


def build_topological_sort() -> Deque:
    graph = DirectedGraph()
    for dependency, dependents in outgoing_edges:
        for dependent in dependents:
            graph.add_edge(dependency, dependent)
    return graph.topological_sort()


def build_reverse_topological_sort() -> Deque:
    """Used for deleting tables"""
    graph = DirectedGraph()
    for dependency, dependents in outgoing_edges:
        for dependent in dependents:
            graph.add_edge(dependent, dependency)
    return graph.topological_sort()


def print_topological_sort():
    print("Topological Sort")
    print(" --> ".join(build_topological_sort()))


if __name__ == "__main__":
    print_topological_sort()
