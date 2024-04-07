# test_cafeteria.py

import pytest

from cafeteria import validar_bebida

@pytest.mark.parametrize("bebida, resultado_esperado", [
    ("cafe,12,16,20", True),("Ca3ri,12,16,20", False),("a,1,2,3,4",False),("CaféLatteConCremaBatida,12,16,20",False), ("MokaLatte,0,16,20",False),
    ("Latte,12.5,16,20",False),("Latte,12.5,16,20",False),("CafeLatteMoka,12,16,20",True),("Moka,20,3,71", False),("moka,1,2,3,4",True),("Late,1,2,3,4,5,6",False),
    ("Latte,1,2,3,4,5", True), ("290,1,2,3,4,5",False), ("MokaLate,1,23,4,5",False),("Cafe,12,16,20,24,30",True),("Moka Latte,2,3,4,6",True),
    # Agrega más casos de prueba aquí si es necesario
])
def test_validar_bebida(bebida, resultado_esperado):
    resultado = validar_bebida(bebida)
    assert resultado == resultado_esperado, f"El resultado esperado para {bebida} debería ser {resultado_esperado}"

# Si ejecutas este archivo como un script (__main__), se ejecutarán todas las pruebas
if __name__ == "__main__":
    pytest.main()
