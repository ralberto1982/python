class Alarma:

    def __init__(self,sonar):
        self.sonar=sonar


    def postergar(self, minutos):
        self.minutos=minutos
        print(' la alarma has sido Propuesta {}'.format(self.minutos),'minutos')

miAlarma=Alarma('rinnnnnn')

miAlarma.postergar('3')