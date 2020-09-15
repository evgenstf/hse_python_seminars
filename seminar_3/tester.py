import sys

class MockIO:
    def __init__(self, input):
        self.input = input
        self.input_index = 0
        self.output = []

    def readline(self):
        line = self.input[self.input_index]
        self.input_index += 1
        return line

    def flush(self):
        pass

    def write(self, line):
        line = line.strip()
        if line:
            self.output.append(line)

def test_solution(solution, input, expected_output):
    original_stdin = sys.stdin
    original_stdout = sys.stdout

    mock_io = MockIO(input)
    sys.stdin = mock_io
    sys.stdout = mock_io

    solution()

    sys.stdin = original_stdin
    sys.stdout = original_stdout

    if mock_io.output != expected_output:
        print("failed on input:", input)
        print("received output:", mock_io.output)
        print("expected output:", expected_output)
    else:
        print("ok on input:", input)
    print()