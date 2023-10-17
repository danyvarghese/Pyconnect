# Pyconnect - Bridging MIL/ILP Approaches with Robotic Simulations

## Overview

**Pyconnect** is an integral solution crafted to bridge the gap between **MIL/ILP approaches**, typically grounded in the **Prolog** programming language, and r**obotics simulations**, predominantly designed using **Python**. Pyconnect is the key that makes it possible for the abstract intelligence from MIL/ILP to work with the practical simulation features of modern robotic systems.



## Why Pyconnect?

Pyconnect emerges as a solution to these challenges. It offers:

1. A unified interface to synergize Prolog-based logic planning with Python-driven robotic simulations
2. Smooth interoperability, reducing the complexity of integration
3. A platform to harness the power of intuitive machine learning in real-world robotic scenarios

## Requirents

1. [Python 3](https://www.python.org/download/releases/3.0/)
2. [survey-simulation](https://github.com/aoat20/survey-simulation)

## Getting Started
To begin exploring this integrated solution:

1. Familiarize yourself with the surrey_bath [surrey_bath](https://github.com/stassa/surrey_bath) repository to understand the workings of the autonomous agent.
2. Dive into the [survey-simulation](https://github.com/aoat20/survey-simulation) repository for insights into the robotics simulator.
3. Follow the integration instructions (to be provided or linked) to set up the combined environment


## Usage
Import the package and initialise a sim object with mode, param file location and save location:
```python 
import pyconnect
plan = 'plan(actions([action(actionId(3),actionType(move),actionName(move_south_west),actionParams([x(160.0),y(50.0)])),
action(actionId(2),actionType(move),actionName(move_south_west),actionParams([x(170.0),y(60.0)]))]),count(2))'
action_list = pyconnect.extract_actions(plan) 
```

The _action_list_ will now hold the following list of rules:

```python 
action_list =  ['move(170.0,60.0)', 'move(160.0,50.0)']
```

We can also extract the _actionName_ and _actionParams_ from each rule using the following commands:

```python 
action_1 =  'move(170.0,60.0)'
actionName = Clause(action_1).predicate # move
actionParams = Clause(action_1).args() # ['170.0', '60.0']
```


