from kt_pullback import cli
from click.testing import CliRunner


runner = CliRunner()


def test_exibe_retracoes_da_perna():
    res = runner.invoke(cli.cli, ["100.0", "10.0"])
    assert res.output == "70.00\n55.00\n40.00\n"
    assert res.exit_code == 0
