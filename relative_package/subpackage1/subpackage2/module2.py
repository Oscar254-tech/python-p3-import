# Relative import from the same package
from .module1 import function1

# Relative import from parent package  
from .. import module3

def run_demo():
    function1()
    module3.function1()

if __name__ == "__main__":
    run_demo()