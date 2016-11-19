from signals import InputSignals, OutputSignals

class States:
   
    def __init__(self):
        pass


    @classmethod
    def start(self, input_signal):
        """
        START
        """
        #ukazka
        if(InputSignals.HL1 == input_signal):
            return States.filling_low_water, [OutputSignals.ZN]

        elif(InputSignals.HL2 == input_signal):
            #musi se dodelat
            return States.filling_low_water, [OutputSignals.ZN]

        elif(InputSignals.HL3 == input_signal):
            #musi se dodelat
            return States.filling_low_water, [OutputSignals.ZN]

        else:
            return States.start, None


    @classmethod
    def filling_low_water(self, input_signal):
        """
        napouští, málo vody
        """
        #musi se dodelat
        return None


    @classmethod
    def filling_heating(self, input_signal):
        """
        topí, napouští
        """
        #musi se dodelat
        return None


    @classmethod
    def heating(self, input_signal):
        """
        topí
        """
        #musi se dodelat
        return None


    @classmethod
    def nevim_jak_pojemnovat1(self, input_signal):
        """
        plná nádrž, netopí se, nenapouští se
        """
        #musi se dodelat
        return None


    @classmethod
    def nevim_jak_pojemnovat2(self, input_signal):
        """
        teplota a hladina OK
        """
        #musi se dodelat
        return None
        

    @classmethod
    def nevim_jak_pojemnovat3(self, input_signal):
        """
        napouštění dost vody na topení, ale netopí se
        """
        #musi se dodelat
        return None
        

    @classmethod
    def inactivity(self, input_signal):
        """
        nečinnost
        """
        #musi se dodelat
        return None  