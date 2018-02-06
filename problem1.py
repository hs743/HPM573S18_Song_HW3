# Master class
class Patient:

    def __init__(self, name):
        """

        :param name: name of patient

        """
        self.name = name

    def discharge(self):

        """Abstract method which to be overridden in derived classes"""

        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")

class EmergencyPatient(Patient):

    def __init__(self, name):
       Patient.__init__(self, name)
       self.expectedcost = 1000

    def discharge(self):
        print(self.name + " " + "EmergencyPatient")

class HospitalizedPatient(Patient):

    def __init__(self, name):
        Patient.__init__(self, name)
        self.expectedcost = 2000

    def discharge(self):
        print(self.name + " " + "HospitalizedPatient")

# Hospital class
class Hospital:

    def __init__(self):
        self.cost = 0
        self.Patients = []

    def admit(self, patients):
        self.Patients.append(patients)
    # add patient to the list of Patients one by one

    def discharge_all(self):

        for patients in self.Patients:
            patients.discharge()
            self.cost += patients.expectedcost

    def get_total_cost(self):

        return self.cost

# Creating variables

P1 = HospitalizedPatient("a")
P2 = HospitalizedPatient("b")
P3 = EmergencyPatient("c")
P4 = EmergencyPatient("d")
P5 = EmergencyPatient("e")

SimulationHospital = Hospital()


SimulationHospital.admit(P1)
SimulationHospital.admit(P2)
SimulationHospital.admit(P3)
SimulationHospital.admit(P4)
SimulationHospital.admit(P5)

SimulationHospital.discharge_all()

print(SimulationHospital.get_total_cost())
























