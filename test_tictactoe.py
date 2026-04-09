import pytest
from tictactoe_logic import func, ifwin

def test_ifwin_rows():
    assert ifwin(["00","01","02"]) == True
    assert ifwin(["10","11","12"]) == True
    assert ifwin(["20","21","22"]) == True
    assert ifwin(["00","01"]) == False

def test_ifwin_columns():
    assert ifwin(["00","10","20"]) == True
    assert ifwin(["01","11","21"]) == True
    assert ifwin(["02","12","22"]) == True

def test_ifwin_diagonals():
    assert ifwin(["00","11","22"]) == True
    assert ifwin(["02","11","20"]) == True

def test_func_modifies_board():
    val = ["00","01","02","10","11","12","20","21","22"]
    board = func(val, "00", "X")
    assert board[0][0] == "X"
    board = func(val, "11", "O")
    assert board[1][1] == "O"
