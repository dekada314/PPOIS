from Entities.citizens import Citizens
from Entities.economy import Economy
from Entities.parliament import Parliament
from Entities.state import State

state = State("Belarus")
# citizens = Citizens(500000, 50, 1000)
# print(citizens.mean_salary)


state.add_organ('parliament', Parliament())
print(state)
# print(state.organs)

