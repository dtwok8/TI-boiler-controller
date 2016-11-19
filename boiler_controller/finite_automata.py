from states import States
from signals import InputSignals

class FiniteAutomata:
    
    def __init__(self):
        pass


    def start(self):
       self.loop()


    def loop(self):
        state = States.start

        while(True):
            state = self.state_base(state)
            if(state is None):
                print("Ukončení pro neplatný vstupní signál")
                break


    def state_base(self,state):
        print("Stav: {0}".format(state.__doc__))

        input_signal = input("Zadejte vstupní signál: ")
       
        if(input_signal in InputSignals.__members__):
            input_signal = InputSignals(input_signal)
        else:
            return None

        state, output_signals = state(input_signal)

        if(output_signals is not None):
            str_output_signals = ', '.join(str(x) for x in output_signals)
            print("Výstupní signal: {0}".format(str_output_signals))

        return state