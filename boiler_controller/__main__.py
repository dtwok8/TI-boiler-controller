from finite_automata import FiniteAutomata
import argparse
import sys

def execute(): 
    args = args_parse()

    print("Spuštění automatu")
    finite_automata = FiniteAutomata()
    finite_automata.start()


def args_parse():
    parser = argparse.ArgumentParser(prog='boiler_controller',description='Simulace boileru, pomocí konečného automatu')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s (version 0.7dev)')
  
    return parser.parse_args()
    

if __name__ == "__main__":
    execute()
