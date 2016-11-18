from states import States


class FiniteAutomata:
    
    def __init__(self):
        pass

    def start(self):
       self.loop()


    def loop(self):
        state = States.start

        while(True):
            state = self.state_base(state)
            #nevim kdy zastavit automat
            if(state is None):
                break



    def state_base(self,state):
        print("Stav: {0}".format(state.__doc__))

        input_signal = input("Zadejte vstupní signál: ")
       
        state, output_signals = state(input_signal)

        if(output_signals is not None):
            str_output_signals = ', '.join(output_signals)
            print("Výstupní signal: {0}".format(str_output_signals))

        return state
