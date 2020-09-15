from A.solution import main
from tester import test_solution

test_solution(main, ["1", "2"], ["3"])
test_solution(main, ["10", "2"], ["12"])
test_solution(main, ["2", "2"], ["5"])

