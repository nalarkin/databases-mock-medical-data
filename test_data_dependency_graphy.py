"""Verifies the foregin key constraints of mock generated data."""

import unittest
from data_dependency_graph import DirectedGraph


class DependencyGraphTest(unittest.TestCase):
    def test_simple_graph(self):
        graph = DirectedGraph()
        edges = [["A", "B"], ["B", "C"], ["A", "C"]]
        for prerequisite, dependent in edges:
            graph.add_edge(prerequisite, dependent)
        nodes = set("ABC")
        order = list(graph.topological_sort())
        indices = {n: idx for idx, n in enumerate(order)}
        for prerequisite, dependent in edges:
            with self.subTest(prerequisite=prerequisite, dependent=dependent):
                self.assertTrue(indices[prerequisite] < indices[dependent])
        self.assertEqual(len(nodes), len(order))

    def test_graph_a(self):
        graph = DirectedGraph()
        edges = [["A", "B"], ["B", "C"], ["A", "C"], ["D", "B"], ["D", "A"]]
        for prerequisite, dependent in edges:
            graph.add_edge(prerequisite, dependent)
        nodes = set("ABCD")
        order = list(graph.topological_sort())
        indices = {n: idx for idx, n in enumerate(order)}
        for prerequisite, dependent in edges:
            with self.subTest(prerequisite=prerequisite, dependent=dependent):
                self.assertTrue(indices[prerequisite] < indices[dependent])
        self.assertEqual(len(nodes), len(order))

    def test_basic_cycle(self):
        graph = DirectedGraph()
        edges = [["A", "B"], ["B", "C"], ["C", "A"]]
        for prerequisite, dependent in edges:
            graph.add_edge(prerequisite, dependent)
        with self.assertRaises(ValueError):
            graph.topological_sort()

    def test_graph_a_cycle(self):
        graph = DirectedGraph()
        edges = [["A", "B"], ["B", "C"], ["A", "C"], ["D", "B"], ["D", "A"], ["B", "D"]]
        for prerequisite, dependent in edges:
            graph.add_edge(prerequisite, dependent)
        with self.assertRaises(ValueError):
            graph.topological_sort()

    def test_allow_self_dependency(self):
        """Self dependencies are allowed when inserting all values at once"""
        graph = DirectedGraph()
        edges = [["A", "B"], ["B", "C"], ["A", "C"], ["A", "A"]]
        for prerequisite, dependent in edges:
            graph.add_edge(prerequisite, dependent)
        nodes = set("ABC")
        order = list(graph.topological_sort())
        indices = {n: idx for idx, n in enumerate(order)}
        for prerequisite, dependent in edges:
            with self.subTest(prerequisite=prerequisite, dependent=dependent):
                self.assertTrue(indices[prerequisite] <= indices[dependent])
        self.assertEqual(len(nodes), len(order))

    def test_allow_isolated_node(self):
        graph = DirectedGraph()
        edges = [["A", "B"], ["B", "C"], ["A", "C"], ["D", "D"]]
        for prerequisite, dependent in edges:
            graph.add_edge(prerequisite, dependent)
        nodes = set("ABCD")
        order = list(graph.topological_sort())
        indices = {n: idx for idx, n in enumerate(order)}
        for prerequisite, dependent in edges:
            with self.subTest(prerequisite=prerequisite, dependent=dependent):
                self.assertTrue(indices[prerequisite] <= indices[dependent])
        self.assertEqual(len(nodes), len(order))


if __name__ == "__main__":
    unittest.main()
