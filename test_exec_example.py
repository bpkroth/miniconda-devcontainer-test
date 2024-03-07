import os.path
from subprocess import run

def test_exec_example():
    result = run(["./example.py"],
        capture_output=True,
        text=True,
        check=False,
        cwd=os.path.realpath(os.path.dirname(__file__))
    )
    result.check_returncode()