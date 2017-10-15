# bathtubs-and-rainbows
(Qualitative Reasoning) - Modeling the behaviors in container systems like bathtubs and sinks

### Assumptions
`In causal ordering, exogenous functions are viewed as the start of causal chains`

Two exogenous functions are considered for the inflow of water into the container system (say, bathtub) - Sinusoidal and Linear. A combination of the two will be considered (i.e., a sinusoid which increases until the water level in the bathtub is maximum, then decreases)

### The following details are considered

#### Quantities
1. Inflow (of water into the container)
2. Outflow (of water out of the container)
3. Volume (of the water in the container)

#### Quantity spaces
1. Inflow: [0, +]
2. Outflow and Volume: [0, +, max]

#### Dependencies
1. I+(Inflow, Volume) - The amount of inflow increases the volume
2. I-(Outflow, Volume) - The amount of outflow decreases the volume
3. P+(Volume, Outflow) - Outflow changes are proportional to volume changes
4. VC(Volume(max), Outflow(max)) - The outflow is at its highest value (max), when the volume is at its highest value (also max).
5. VC(Volume(0), Outflow(0)) - There is no outflow, when there is no volume.

