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
            return States.error, []

        elif(InputSignals.VK == input_signal):
            return States.inactivity, []

        elif(InputSignals.HL1 == input_signal):
            return States.filling_low_water, [OutputSignals.ZN]

        elif(InputSignals.HL2 == input_signal):
            return States.water_on_heating, [OutputSignals.ZN]

        elif(InputSignals.HL3 == input_signal):
            return States.full_water_not_heating, []

        else: #ostatni signaly -> nazpatek do stavu
            return States.start, None


    @classmethod
    def filling_low_water(self, input_signal):
        """
        Napouští, málo vody
        """
        if(input_signal == None):
            return States.error, [OutputSignals.VN]

        elif(InputSignals.VK == input_signal):
            return States.inactivity, [OutputSignals.VN]

        elif(InputSignals.HL2 == input_signal):
            return States.water_on_heating, []

        else:
            return States.filling_low_water, None


    @classmethod
    def filling_heating(self, input_signal):
        """
        Topí, Napouští
        """
        if(input_signal == None):
            return States.error, [OutputSignals.VN, OutputSignals.VT]

        elif(InputSignals.VK == input_signal):
            return States.inactivity, [OutputSignals.VN, OutputSignals.VT]

        elif(InputSignals.TP2 == input_signal):
            return States.water_on_heating, [OutputSignals.VT]

        elif(InputSignals.HL1 == input_signal):
            return States.filling_low_water, [OutputSignals.VT]

        elif(InputSignals.HL3 == input_signal):
            return States.heating, [OutputSignals.VN]
        
        else:
            return States.filling_heating, None


    @classmethod
    def heating(self, input_signal):
        """
        Topí
        """
        if(input_signal == None):
            return States.error, [OutputSignals.VT]

        elif(InputSignals.VK == input_signal):
            return States.inactivity, [OutputSignals.VT]

        elif(InputSignals.TP2 == input_signal):
            return States.temperature_water_ok, [OutputSignals.VT]

        elif(InputSignals.HL3 == input_signal):
            return States.filling_heating, [OutputSignals.ZN]

        elif(InputSignals.HL1 == input_signal):
            return States.error, [OutputSignals.VT]

        else:
            return States.heating, None


    @classmethod
    def full_water_not_heating(self, input_signal):
        """
        Plná nádrž, Netopí se, Nenapouští se
        """
        if(input_signal == None):
            return States.error, []
        
        elif(InputSignals.VK == input_signal):
            return States.inactivity, []

        elif(InputSignals.TP1 == input_signal):
            return States.heating, [OutputSignals.ZT]

        elif(InputSignals.TP2 == input_signal):
            return States.temperature_water_ok, []

        elif(InputSignals.HL2 == input_signal):
            return States.water_on_heating, [OutputSignals.ZN]

        elif(InputSignals.HL1 == input_signal):
            return States.error, []

        else:
            return States.full_water_not_heating, None


    @classmethod
    def temperature_water_ok(self, input_signal):
        """
        Teplota OK, Hladina OK
        """
        if(input_signal == None):
            return States.error, []
        
        elif(InputSignals.VK == input_signal):
            return States.inactivity, []

        elif(InputSignals.TP1 == input_signal):
            return States.heating, [OutputSignals.ZT]

        elif(InputSignals.HL2 == input_signal):
            return States.water_on_heating, [OutputSignals.ZN]

        elif(InputSignals.HL1 == input_signal):
            return States.error, []

        else:
            return States.temperature_water_ok, None


    @classmethod
    def water_on_heating(self, input_signal):
        """
        Napouštění, dost vody na topení, ale netopí se
        """
        if(input_signal == None):
            return States.error, [OutputSignals.VN]
        
        elif(InputSignals.VK == input_signal):
            return States.inactivity, [OutputSignals.VN]

        elif(InputSignals.HL3 == input_signal):
            return States.temperature_water_ok, [OutputSignals.VN]

        elif(InputSignals.TP1 == input_signal):
            return States.filling_heating, [OutputSignals.ZT]

        else:
            return States.water_on_heating, None


    @classmethod
    def inactivity(self, input_signal):
        """
        NEČINNOST
        """
        if(input_signal == None):
            return States.error, []
        
        elif(InputSignals.ZK == input_signal):
            return States.start, []

        else:
            return States.inactivity, None


    @classmethod
    def error(self):
        """
        CHYBA
        """     
        return None, []   