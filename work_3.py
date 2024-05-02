class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory 
       
    @property
    def cpu(self):
        return self.__cpu
        
    @property
    def memory(self):
        return self.__memory
        
    def __make_computions(self):
         print(f""" Результат сложения: {self.cpu+self.memory},\nРезультат вычитания: {self.cpu-self.memory},\nРезультат умножения: {self.cpu*self.memory},\nРезультат деления: {self.cpu/self.memory}""")
        

    @property
    def make_computions(self):
        return self.__make_computions
   
         
comp_1 = Computer(5, 256)
comp_2 = Computer(7, 128)
comp_3 = Computer(6, 256)

comp_1.make_computions()
comp_2.make_computions()
comp_3.make_computions()

class Laptop(Computer):
    def __init__(self, cpu, memory, memory_kard):
        super().__init__(cpu, memory)
        self._memory_kard = memory_kard

    @property
    def memory_kard(self):
        return self._memory_kard

    def info(self):
        print(f"CPU - {self.cpu},  MEMORY - {self.memory}, MEMORY_KARD - {self.memory_kard} ")
 


laptop_1= Laptop(5, 256, 128)
laptop_2 = Laptop(6, 256, 256)
laptop_3 = Laptop(10, 128, 256)

print(laptop_1.cpu)
print(laptop_1.memory)
laptop_1.info()
print(laptop_2.cpu)
print(laptop_2.memory)
laptop_2.info()
print(laptop_3.cpu)
print(laptop_3.memory)
laptop_3.info()




   

