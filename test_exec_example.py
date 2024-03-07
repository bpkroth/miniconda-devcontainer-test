import os.path
from subprocess import run

def test_exec_example():
    env = {}
    env["PATH"] = os.environ["PATH"]
    env["foo"] = "bar"
    result = run(["./example.py"],
        capture_output=True,
        text=True,
        check=False,
        env=env,
        cwd=os.path.realpath(os.path.dirname(__file__))
    )
    result.check_returncode()