from signals import InputSignals, OutputSignals

class States:
   
    def __init__(self):
        pass


    @classmethod
    def start(self, input_signal):
        """
        START
        """

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
    def filling_low_water():
        """
        napouští, málo vody
        """
        #musi se dodelat
        return None

    @classmethod
    def filling_heating():
        """
        topí, napouští
        """
        #musi se dodelat
        return None


    @classmethod
    def heating():
        """
        topí
        """
        #musi se dodelat
        return None

    @classmethod
    def w():
        """
        plná nádrž, netopí se, nenapouští se
        """
        #musi se dodelat
        return None

    @classmethod
    def q():
        """
        teplota a hladina OK
        """
        #musi se dodelat
        return None
        

    @classmethod
    def a():
        """
        napouštění dost vody na topení, ale netopí se
        """
        #musi se dodelat
        return None
        

    @classmethod
    def inactivity():
        """
        nečinnost
        """
        #musi se dodelat
        return None  