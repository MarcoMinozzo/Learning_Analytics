# Social Network Analysis with Agent-Based Modeling (ABM)

An agent-based model, often referred to as agent-based modeling (ABM), is a class of computer simulations that mimic the interactions of autonomous agents (individuals, entities, or groups) to evaluate their effects on the system as a whole. These models are used to simulate and study the complex dynamics of systems in a variety of fields, such as economics, biology, social sciences, engineering, and more.

## Main Features

- **Autonomous Agents**: Each agent is a distinct entity with its own set of characteristics and rules of behavior. Agents can represent people, animals, cells, organizations, vehicles, etc.
- **Local Interactions**: Agents interact with each other and their environment, which can lead to complex system-level behaviors.
- **Heterogeneity**: Agents can be heterogeneous, reflecting the diversity found in real systems.
- **Adaptation**: Agents can learn and adapt their behavior based on experiences and environmental changes.
- **Environment**: The environment can influence or be influenced by the actions of agents.

## Applications

- **Economics and Financial Markets**: Simulate markets and study economic policies.
- **Ecology and Evolution**: Model ecosystems and population dynamics.
- **Sociology and Political Science**: Explore social dynamics and public opinion.
- **Public Health**: Model disease spread and evaluate intervention strategies.
- **Urban Engineering and Planning**: Simulate traffic flow and city layouts.
- **Multi-Agent Systems in AI**: Explore intelligent agent interactions in solving complex problems.

## Mathematical Theory

While ABMs don't rely on a single mathematical theory, they use a variety of concepts:

- **Cellular Automata**: Discrete systems with rules governing the states of cells, useful for modeling local interactions.
- **Graphs and Networks**: Represent interactions between agents and analyze network structures.
- **Game Theory**: Model agents' decisions and strategies.
- **Stochastic Processes**: Capture randomness in agent behaviors or environmental events.
- **Dynamical and Differential Systems**: Describe continuous state changes and system dynamics.
- **Monte Carlo Simulations**: Analyze ABMs with stochastic components through repeated simulations.

## Tools

Several platforms support ABM, including **NetLogo**, **AnyLogic**, **Mesa (Python)**, and **Repast**.

### Mesa Library

The **Mesa** library is a flexible Python framework for agent-based modeling, with features like:

- **Agent-Based Modeling**: Define agents with individual behaviors.
- **Spatial Environments**: Support for various spatial structures.
- **Data Collection**: Tools to collect and analyze simulation data.
- **Visualization**: Web-based interface for visualizing simulations.
- **Scalability and Flexibility**: Support for building models from simple to highly complex.

### Propagation of Opinions on Social Networks

Let's explore an example of ABM applied to opinion propagation within a social network using Python.

#### Social Network Opinion Propagation Model (Business Rules)

1. **Initial Opinions**: Agents are initialized with positive, negative, or neutral sentiments.
2. **One-Way Positive Propagation**: Positive agents influence neighbors, converting them to positive.
3. **Differentiated Influence**: 
    - 10% chance to convert a negative agent to positive.
    - 30% chance to convert a neutral agent to positive.
4. **No Negative/Neutral Propagation**: Negative and neutral sentiments do not spread.
5. **Fixed Social Network**: Modeled as an Erdős-Rényi graph, with a fixed network structure.
6. **Sentiment Data Collection**: Track the number of agents in each sentiment state over time.
7. **Temporal Dynamics**: Simulation progresses in discrete steps, with actions taken at each step.

This model emphasizes the unidirectional spread of positive influence, leading to the eventual predominance of positive sentiments in the network.

[ABM Code](learning-analytics-ml/abm.py)

We can see in the graph how opinion formation evolves over the course of interactions between agents and the number of interactions necessary to achieve satisfactory goals.

![image](https://github.com/user-attachments/assets/660a3a8a-e541-4363-9272-fd5d900c6373)


This example is a basic introduction to agent-based modeling and shows how you can start simulating complex systems with local interactions between agents. The table offers many more functionalities, including the ability to create web-based visualizations of the simulations, which can significantly aid in understanding the dynamics of the model.

Note: In this article I preferred to use the term social networks instead of social media because the model works in all types of social networks including the case of social media.
