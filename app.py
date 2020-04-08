from logging import basicConfig, INFO
from libsm import Value, SM
from libsm.func import single

# set logging level
basicConfig(level=INFO)


# fi: init function
#     init function returns a set (Value) of initial state
#     the only initial state in this example is `{}`

@single
def fi():
    return Value()

# fn: next function
#     next function returns a set (Value) of next state
#     the only next state in this example `{}` whatever the previous state is


@single
def fn(value):
    return Value()


sm = SM(fi, fn)
states, transitions = sm.result()

print(states)
print(transitions)
