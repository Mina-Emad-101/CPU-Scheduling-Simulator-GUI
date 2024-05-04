import unittest
from GanttChart import Process, GanttChart


class TestGanttChart(unittest.TestCase):

    def test_getGanttChartList(self):
        testList = [
            (
                [
                    Process(1, 0, 3, 2),
                    Process(2, 1, 2, 1),
                    Process(3, 3, 4, 3),
                ],
                "122113333"
            ),
            (
                [
                    Process(1, 0, 3, 1),
                    Process(2, 1, 2, 2),
                    Process(3, 3, 4, 3),
                ],
                "111223333"
            ),
            (
                [
                    Process(1, 0, 3, 2),
                    Process(2, 1, 2, 1),
                    Process(3, 5, 4, 3),
                ],
                "122113333"
            ),
            (
                [
                    Process(1, 0, 3, 2),
                    Process(2, 1, 2, 1),
                    Process(3, 7, 4, 3),
                ],
                "12211--3333"
            ),
            (
                [
                    Process(1, 0, 3, 2),
                    Process(2, 1, 2, 1),
                    Process(3, 10, 4, 3),
                ],
                "12211-----3333"
            ),
            (
                [
                    Process(1, 0, 10, 3),
                    Process(2, 1, 1, 1),
                    Process(3, 2, 2, 4),
                    Process(4, 3, 3, 2),
                ],
                "1214441111111133"
            ),
        ]

        ganttChartList = [GanttChart(testTuple[0]) for testTuple in testList]
        ganttStrs = [ganttChart.getGanttChartString() for ganttChart in ganttChartList]

        for i in range(len(testList)):
            print(f"Test Case: {i + 1}")
            ganttStr = ganttStrs[i]
            self.assertEqual(ganttStr, testList[i][1])
            print("OK")


if __name__ == "__main__":
    unittest.main()

