import pytest
from your_module import func, ifwin  # replace 'your_module' with the filename without .py

def test_ifwin_rows():
    # Winning by first row
    done = ["00", "01", "02"]
    assert ifwin(done) == True
    # Not enough moves
    done = ["00", "01"]
    assert ifwin(done) == False

def test_ifwin_columns():
    # Winning by first column
    done = ["00", "10", "20"]
    assert ifwin(done) == True
    # Winning by second column
    done = ["01", "11", "21"]
    assert ifwin(done) == True

def test_ifwin_diagonals():
    # Main diagonal
    done = ["00", "11", "22"]
    assert ifwin(done) == True
    # Anti-diagonal
    done = ["02", "11", "20"]
    assert ifwin(done) == True

def test_func_modifies_board(capsys):
    val = ["00","01","02","10","11","12","20","21","22"]
    choice = "00"
    func(val, choice, "X")
    captured = capsys.readouterr()
    # func prints the board; check the first element is replaced
    assert val[0] == "X"
    # Check printed output contains X in first row
    assert "X" in captured.out
