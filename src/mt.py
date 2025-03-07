from functools import partial

class maquina_de_turing:
    type estado = str
    type simbolo = str
    type accion = partial
    estados : list[estado] = None 
    alfabeto : list[simbolo] = None
    estado_final : estado = None 
    lista_instrucciones : dict[(estado, simbolo), (accion,estado)] = None
    estado_inicial : estado = None
    estado_actual : estado = None
    cinta : list[simbolo]= None
    pos_cabezal :int = None
    log : str = None

    def __init__(self, estados : list[estado], alfabeto : list[simbolo], 
                 instrucciones : dict[(estado, simbolo), (accion,estado)], 
                 e_inicial : estado, e_final : estado, cinta : list[simbolo], asserts = True, log = False):
        
        self.alfabeto = alfabeto
        self.alfabeto.append('b')
        if asserts:
            assert e_inicial in estados, 'El estado inicial debe pertener a los estados de la Máquina de Turing.'
            assert e_final in estados, 'El estado final debe pertenecer a los estados de la Máquina de Turing.'
            for clave, valor in instrucciones.items():
                estado = clave[0]
                simbolo = clave[1]
                accion = valor[0]
                prox_estado = valor[1]
                assert estado in estados, f'Hay una instrucción para el estado {estado} que no está en el autómata.'
                assert simbolo in self.alfabeto, f'Hay una instrucción para el símbolo {simbolo} y no está en el alfabeto del autómata'
                # TODO agregar un assert para cada accion en la lista de instrucciones
                assert prox_estado in estados, f'Hay una instrucción,{prox_estado}, que lleva a la Máquina de Turing a un estado que no posee.'

        self.estados = estados
        
        self.instrucciones = instrucciones
        self.estado_inicial = e_inicial
        self.estado_final = e_final
        self.cinta = list(cinta)
        self.pos_cabezal = len(cinta)-1 # El cabezal arranca "lo más a la derecha"
        self.log = ''
        
    
    def paso(self):
        lectura_cabezal = self.leer_cabezal()
        accion, prox_estado = self.instrucciones[self.estado_actual,
                                        lectura_cabezal]
        self.log += f'Estado actual: {self.estado_actual}. Cabezal en {self.get_pos_cabezal()}: {lectura_cabezal}.\nAcción de la MT: {getattr(
                                                                                                                                            getattr(accion,'func',accion),
                                                                                                                                            '__name__',
                                                                                                                                            None)}. Próximo estado: {prox_estado}.\n'
        self.log += F'Antes de la acción: \n{"".join(self.cinta)}\nDespués:\n'
        accion(self)
        
        self.estado_actual = prox_estado
        self.log += "".join(self.cinta) + f"\n +++++++++++++++++++++++++ \n" 


    def computar(self):
        self.log += f'Cómputo de la cinta {"".join(self.cinta)}.\nEstado inicial: {self.estado_inicial}.\n \n'
        self.estado_actual = self.estado_inicial
        while self.estado_actual != self.estado_final:
            self.paso()
        if self.log:
            print(self.log)
        return self.get_cinta()

        
    def instrucciones(self, estado, simbolo_cabezal):
        return self.lista_instrucciones[(estado, simbolo_cabezal)]
    
    def leer_cabezal(self):
        return self.cinta[self.get_pos_cabezal()]

    def get_cinta(self):
        return self.cinta
    def set_cinta(self, cinta):
        self.cinta = cinta
    def get_pos_cabezal(self):
        return self.pos_cabezal
    def set_pos_cabezal(self,i):
        self.pos_cabezal = i    

    class acciones:
        agregado = 2
        def mover_derecha(maquina : 'maquina_de_turing'):
            cinta = maquina.get_cinta()
            pos_cabezal = maquina.get_pos_cabezal()
            if pos_cabezal == len(cinta) - 1:
                cinta = cinta + ['b'] * maquina_de_turing.acciones.agregado
                maquina.set_cinta(cinta)
            maquina.set_pos_cabezal(pos_cabezal + 1)
        def mover_izquierda(maquina : 'maquina_de_turing'):
            cinta = maquina.get_cinta()
            pos_cabezal = maquina.get_pos_cabezal()
            if pos_cabezal > 0: 
                maquina.set_pos_cabezal(pos_cabezal - 1)  
            else:
                cinta = (['b'] * maquina_de_turing.acciones.agregado) + cinta  
                maquina.set_pos_cabezal(maquina_de_turing.acciones.agregado)
                maquina.set_cinta(cinta)
        def escribir_cinta(maquina : 'maquina_de_turing',simbolo = 'b'):
            simbolo = str(simbolo)
            cinta = maquina.get_cinta()
            pos_cabezal = maquina.get_pos_cabezal()
            cinta[pos_cabezal] = simbolo
            maquina.set_cinta(cinta)