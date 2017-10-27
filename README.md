# bathtubs-and-rainbows
(Qualitative Reasoning) - Modeling the behaviors in container systems like bathtubs and sinks

### Output
`git clone` or download the project as zip. The project can be run either using 
1. python3. Dependencies - Jupyter notebook, graphviz
2. javascript (index.html, main.js). Requires latest verion of node.js to be installed


### Assumptions
`In causal ordering, exogenous functions are viewed as the start of causal chains`

Two exogenous functions are considered for the inflow of water into the container system (say, bathtub) - Random and Linear. 

### The following details are considered

#### Quantities
1. Inflow (of water into the container)
2. Outflow (of water out of the container)
3. Volume (of the water in the container)
4. Height (of the water in the container)
5. Pressure (exerted by the water at the mouth of the container)

#### Quantity spaces
1. Inflow: [0, +]
2. Outflow, Volume, Height, Pressure: [0, +, max]

#### Dependencies
1. I+(Inflow, Volume) - The amount of inflow increases the volume
2. I-(Outflow, Volume) - The amount of outflow decreases the volume
3. P+(Pressure, Outflow) - Outflow changes are proportional to pressure changes
4. P+(Volume, Height) - Increase in volume increases the Height
5. P+(Height, Pressure) - Increase in
6. VC(Volume(max), Outflow(max)) - The outflow is at its highest value (max), when the volume is at its highest value (also max).
7. VC(Volume(0), Outflow(0)) - There is no outflow, when there is no volume.
8. VC(Height(0), Pressure(0)) - There is no pressure, when height is 0.
7. VC(Height(max), Pressure(max)) - Pressure is maximum when height of the water in the container is maximum.
7. VC(Pressure(0), Outflow(0)) - There is no outflow, when there is no pressure.
7. VC(Pressure(max), Outflow(max)) - The outflow is at its highest value (max), when the pressure is at its highest value.
