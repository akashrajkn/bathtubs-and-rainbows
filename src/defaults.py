{
    'dependency': [
        {
            'effect': 'influence',
            'type': '+',
            'from': 'inflow',
            'to': 'volume'
        },
        {
            'effect': 'influence',
            'type': '-',
            'from': 'outflow',
            'to': 'volume'
        },
        {
            'effect': 'proportional',
            'type': '+',
            'from': 'volume',
            'to': 'outflow'
        },
        {
            'effect': 'VC',
            'type': 'max',
            'from': 'volume',
            'to': 'outflow'
        },
        {
            'effect': 'VC',
            'type': '0',
            'from': 'volume',
            'to': 'outflow'
        }
    ],
    # Define quantity spaces
    'qspace_inflow': ['0', '+'],
    'qspace_outflow': ['0', '+', 'max'],
    'qspace_volume': ['0', '+', 'max'],
    'derivatives': ['+', '0', '-'],
    'initial_state': {
        'id': 0,
        'previous_state': [-1],
        'inflow': ['0', '0'],
        'volume': ['0', '0'],
        'outflow': ['0', '0']
    }
}
