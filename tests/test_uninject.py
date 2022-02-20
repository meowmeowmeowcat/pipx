from helpers import run_pipx_cli


def test_uninject_simple(pipx_temp_env, capsys):
    assert not run_pipx_cli(["install", "pycowsay"])
    assert not run_pipx_cli(["inject", "pycowsay", "black"])
    assert not run_pipx_cli(["uninject", "pycowsay", "black"])


def test_uninject_include_apps(pipx_temp_env, capsys):
    assert not run_pipx_cli(["install", "pycowsay"])
    assert not run_pipx_cli(
        ["inject", "pycowsay", "black", "--include-deps", "--include-apps"]
    )
    assert not run_pipx_cli(["uninject", "pycowsay", "black"])
