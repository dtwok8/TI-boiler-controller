from states import States
from signals import InputSignals

class FiniteAutomata:
    
    def __init__(self):
        pass


    def start(self):
       self.loop()


    def loop(self):
        state = States.inactivity

        while(True):
            state = self.state_base(state)
            if(state is None):
                break


    def state_base(self,state):
        print("Stav: {0}".format(state.__doc__))

        if(state.__code__.co_argcount <= 1):
            return None

        print("Zadejte vstupní signál: ", end="")
        input_signal = input().strip().upper()
       
        if(input_signal in InputSignals.__members__):
            input_signal = InputSignals(input_signal)      
        else:
            input_signal = None

        state, output_signals = state(input_signal)

        if(output_signals is not None):
            str_output_signals = ', '.join(str(x) for x in output_signals)
            print("Výstupní signály: {0}".format(str_output_signals))

        return state