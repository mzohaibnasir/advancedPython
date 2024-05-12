"""
ENUM:

"""

from enum import Enum, auto


# class State(Enum):
#     PLAYING = auto()
#     PAUSED = auto()
#     GAME_OVER = auto()


class State(Enum):
    PLAYING = 0
    PAUSED = 1
    GAME_OVER = 2


# print(State.PLAYING)
# print(State.PAUSED)
# print(State.GAME_OVER)


state = State.PLAYING

# print(f"current state: {state}, {state.value}")


print(State(0))
print(State(1))
print(State(2))


# example
