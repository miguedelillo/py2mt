from mt import maquina_de_turing
# from acciones_mt import acciones_turing
#def test_suma():
#    assert 2 + 2 == 4



def crear_turing():
    return maquina_de_turing(estados=[],
                        alfabeto=[],
                        e_final=[],
                        e_inicial=[],
                        instrucciones={},
                        asserts=False
)
cabezal_0 = 3
cinta_0 = list('bbbbbb')

def test_cinta_vacia():
    turing = crear_turing()
    assert turing.get_cinta() == cinta_0

def test_cabezal():
    turing = crear_turing()
    assert turing.get_pos_cabezal() == cabezal_0

def test_escribir_1():
    turing = crear_turing()
    maquina_de_turing.acciones.escribir_cinta(turing, 1)
    assert turing.get_cinta() == list('bbb1bb')

def test_mover_uno_derecha():
    turing = crear_turing()
    maquina_de_turing.acciones.mover_derecha(turing)
    assert turing.get_pos_cabezal() == cabezal_0 + 1

def test_mover_limite_derecha():
    turing = crear_turing()
    len_cinta_original = len(turing.get_cinta())
    turing.set_pos_cabezal(len_cinta_original - 1)
    assert turing.get_pos_cabezal() == 5
    maquina_de_turing.acciones.mover_derecha(turing)
    assert turing.get_pos_cabezal() == 6
    assert turing.get_cinta() == list('bbbbbbbb')

def test_mover_izquierda():
    turing = crear_turing()
    maquina_de_turing.acciones.mover_izquierda(turing)
    assert turing.get_pos_cabezal() == cabezal_0 - 1

def test_mover_limite_izquierda():
    turing = crear_turing()
    turing.set_pos_cabezal(0)
    maquina_de_turing.acciones.mover_izquierda(turing)
    assert turing.get_pos_cabezal() == 2
    assert turing.get_cinta() == list('bbbbbbbb')

def test_escribir_unos_derecha():
    turing = crear_turing()
    maquina_de_turing.acciones.escribir_cinta(turing, '1')
    maquina_de_turing.acciones.mover_derecha(turing)
    maquina_de_turing.acciones.escribir_cinta(turing, '1')
    maquina_de_turing.acciones.mover_derecha(turing)
    maquina_de_turing.acciones.escribir_cinta(turing, '1')
    maquina_de_turing.acciones.mover_derecha(turing)
    maquina_de_turing.acciones.escribir_cinta(turing, '1')
    maquina_de_turing.acciones.mover_derecha(turing)
    assert turing.get_cinta() == list('bbb1111b')

def test_escribir_unos_izquierda():
    turing = crear_turing()
    maquina_de_turing.acciones.escribir_cinta(turing, '1')
    maquina_de_turing.acciones.mover_izquierda(turing)
    maquina_de_turing.acciones.escribir_cinta(turing, '1')
    maquina_de_turing.acciones.mover_izquierda(turing)
    maquina_de_turing.acciones.escribir_cinta(turing, '1')
    maquina_de_turing.acciones.mover_izquierda(turing)
    maquina_de_turing.acciones.escribir_cinta(turing, '1')
    assert turing.get_cinta() == list('1111bb')
    assert turing.get_pos_cabezal() == 0