import pytest
from classes.Score import Score
from classes.Ball import Ball
from classes.Block import Block
from classes.Game import Game
from classes.Paddle import Paddle
from components.BlocksArray import blocks

def test_block_destroy():
    block = Block([100, 80], 50, 20)
    block.destroy()
    assert block.status == "destroyed"

def test_score_increase():
    score = Score(0)
    score.increase()
    assert score.score == 1

def test_game_over():
    game = Game([800, 600])
    game.ball.position = [100, 700]  # Set ball position below screen height
    assert game.check_game_over() == True


def test_game_over_blocks():
    game = Game([800, 600])
    for block in blocks:
        block.destroy()
    assert game.check_game_over() == True

if __name__ == "__main__":
    pytest.main()

