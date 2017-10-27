import copy

import defaults


def proportional(source, dest, sign):
    pass


def influence(source, dest, sign):
    pass


def get_current_state():
    pass


def get_next_state(t_value, current):
    '''
    Given the t_value (tap), and the current state, get the next state
    '''
    inflow = current['inflow'].copy()

    if t_value == '+':
        if inflow[0] == '0' and inflow[1] == '0':
            inflow[1] = '+'
        elif inflow[0] == '0' and inflow[1] == '+':
            inflow[0] = '+'
        elif inflow[0] == '+' and inflow[1] == '+':
            pass
    elif t_value == '0':
        pass
    else:
        pass


def get_previous_state():
    pass


def exogenous():
    '''
    Input assumption
    '''
    return ['+', '0', '-']


def simulate():
    generated_graph = []

    # Get initial state
    initial_state = defaults['initial_state'].copy()
    generated_states.append(initial_state)
    tap = exogenous()

    current = initial_state.copy()
    for t in tap:
        current = get_next_state(t, current)

        if is_unique_state(current, generated_graph):
            generated_graph.append(current)

    # TODO: pretty print the graph

if __name__ == '__main__':
    simulate()
