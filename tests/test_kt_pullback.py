from kt_pullback import __version__
from kt_pullback import kt_pullback


def test_version():
    assert __version__ == "0.1.0"


def test_tamanho_da_perna():
    assert kt_pullback.tamanho_perna(100.00, 10.00) == 90.0


def test_metade_da_perna():
    assert kt_pullback.metade_perna(90.00) == 45.0


def test_terco_da_perna():
    assert kt_pullback.terco_perna(90.00) == 30.0


def test_retracao_de_um_terco():
    assert kt_pullback.retracao_um_terco(100.00, 30.00) == 70.00


def test_retracao_da_metade():
    assert kt_pullback.retracao_metade(100.00, 45.00) == 55.00


def test_retracao_de_dois_tercos():
    assert kt_pullback.retracao_dois_tercos(100.00, 30.00) == 40.00
