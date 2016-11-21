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
        if(input_signal == None): #spatny vstup -> chybovy stav
            return States.error, [OutputSignals.VN, OutputSignals.VT]

        elif(InputSignals.HL1 == input_signal):
            return States.filling_low_water, [OutputSignals.ZN]

        elif(InputSignals.HL2 == input_signal):
            #musi se dodelat
            return States.filling_low_water, [OutputSignals.ZN]

        elif(InputSignals.HL3 == input_signal):
            #musi se dodelat
            return States.filling_low_water, [OutputSignals.ZN]

        else: #ostatni signaly -> nazpatek do stavu
            return States.start, None


    @classmethod
    def filling_low_water(self, input_signal):
        """
        napouští, málo vody
        """
        if(input_signal == None):
            return States.error, [OutputSignals.VN, OutputSignals.VT]

        else:
            return States.filling_low_water, None


    @classmethod
    def filling_heating(self, input_signal):
        """
        topí, napouští
        """
        if(input_signal == None):
            return States.error, [OutputSignals.VN, OutputSignals.VT]
        
        else:
            return States.filling_heating, None


    @classmethod
    def heating(self, input_signal):
        """
        topí
        """
        if(input_signal == None):
            return States.error, [OutputSignals.VN, OutputSignals.VT]

        else:
            return States.heating, None


    @classmethod
    def nevim_jak_pojemnovat1(self, input_signal):
        """
        plná nádrž, netopí se, nenapouští se
        """
        if(input_signal == None):
            return States.error, [OutputSignals.VN, OutputSignals.VT]
        
        else:
            return States.nevim_jak_pojemnovat1, None


    @classmethod
    def nevim_jak_pojemnovat2(self, input_signal):
        """
        teplota a hladina OK
        """
        if(input_signal == None):
            return States.error, [OutputSignals.VN, OutputSignals.VT]
        
        else:
            return States.nevim_jak_pojemnovat2, None


    @classmethod
    def nevim_jak_pojemnovat3(self, input_signal):
        """
        napouštění dost vody na topení, ale netopí se
        """
        if(input_signal == None):
            return States.error, [OutputSignals.VN, OutputSignals.VT]
        
        else:
            return States.nevim_jak_pojemnovat3, None


    @classmethod
    def inactivity(self, input_signal):
        """
        nečinnost
        """
        if(input_signal == None):
            return States.error, [OutputSignals.VN, OutputSignals.VT]
        
        else:
            return States.inactivity, None


    @classmethod
    def error(self):
        """
        chybový stav
        """     
        return None, []   