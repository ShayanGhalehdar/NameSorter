from pathlib import Path
import pytest
from name_sorter import main


def test_cli_end_to_end(tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture):
    # 1. Arrange input and pre-existing output files in a temporary sandbox
    input_file = tmp_path / "unsorted-names-list.txt"
    input_file.write_text(
        "Shayan Reza Ghalehdar\nMarin Alvarez\nShayan Ghalehdar\n",
        encoding="utf-8",
    )

    output_file = tmp_path / "sorted-names-list.txt"
    output_file.write_text("old stale contents\n", encoding="utf-8")

    # Set working directory to the temporary path and simulate CLI arguments
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr("sys.argv", ["name-sorter", str(input_file)])

    # 2. Act
    main()

    # 3. Assert console output
    captured = capsys.readouterr()
    expected_output = "Marin Alvarez\nShayan Ghalehdar\nShayan Reza Ghalehdar\n"
    assert captured.out == expected_output

    # 4. Assert file output was written and replaced the old content
    assert output_file.read_text(encoding="utf-8") == expected_output


def test_cli_missing_file_error(tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture):
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr("sys.argv", ["name-sorter", "non_existent.txt"])

    with pytest.raises(SystemExit) as exc_info:
        main()

    assert exc_info.value.code == 1
    captured = capsys.readouterr()
    assert "Error:" in captured.err


def test_cli_invalid_name_error(tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture):
    bad_file = tmp_path / "bad.txt"
    bad_file.write_text("Madonna\n", encoding="utf-8")

    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr("sys.argv", ["name-sorter", str(bad_file)])

    with pytest.raises(SystemExit) as exc_info:
        main()

    assert exc_info.value.code == 1
    captured = capsys.readouterr()
    assert "Error: 'Madonna' must have at least 1 given name." in captured.err