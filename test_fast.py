import pytest
import fast

@pytest.mark.parametrize("numero, esperado", [
    (4, True),
    (2, True),
])
def test_es_primo(numero, esperado):
    assert fast.es_primo(numero) == esperado