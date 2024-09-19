from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import NetworkGrid
from mesa.datacollection import DataCollector
import networkx as nx
import random
import matplotlib.pyplot as plt

class Person(Agent):
    def __init__(self, unique_id, model, sentiment):
        super().__init__(unique_id, model)
        self.sentiment = sentiment  # Correto: Sentiment is now a parameter

    def step(self):
        if self.sentiment == "positive":
            # Corrigido: de self.mail para self.pos para obter a posição atual do agente
            neighbors_nodes = self.model.grid.get_neighbors(self.pos, include_center=False)
            if neighbors_nodes:
                other = random.choice(neighbors_nodes)
                if other.sentiment == "negative" and random.random() < 0.1:
                    other.sentiment = "positive"
                elif other.sentiment == "neutral" and random.random() < 0.3:
                    other.sentiment = "positive"

class SentimentModel(Model):
    def __init__(self, N, p_edge, num_positive, num_negative):
        super().__init__()
        self.num_agents = N
        self.p_edge = p_edge
        # Corrigido: de Self. G e self. G para self.G
        self.G = nx.erdos_renyi_graph(n=self.num_agents, p=self.p_edge)
        self.grid = NetworkGrid(self.G)
        self.schedule = RandomActivation(self)

        num_neutral = self.num_agents - (num_positive + num_negative)

        for i, node in enumerate(self.G.nodes()):
            if i < num_positive:
                sentiment = "positive"
            elif i < num_positive + num_negative:  # Corrigido: de 'to' para 'i'
                sentiment = "negative"
            else:
                sentiment = "neutral"
            a = Person(i, self, sentiment)
            self.schedule.add(a)
            self.grid.place_agent(a, node)

        self.datacollector = DataCollector(
            {"Positive": lambda m: sum([1 for a in m.schedule.agents if a.sentiment == "positive"]),
             "Negative": lambda m: sum([1 for a in m.schedule.agents if a.sentiment == "negative"]),
             "Neutral": lambda m: sum([1 for a in m.schedule.agents if a.sentiment == "neutral"])})

    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()

model = SentimentModel(N=500, p_edge=0.023, num_positive=40, num_negative=300)
for i in range(40):
    model.step()

results = model.datacollector.get_model_vars_dataframe()
results["Positive %"] = (results["Positive"] / model.num_agents) * 100
results["Negative %"] = (results["Negative"] / model.num_agents) * 100
results["Neutral %"] = (results["Neutral"] / model.num_agents) * 100

plt.figure(figsize=(10, 6))
plt.plot(results.index, results["Positive %"], label='Positive %', color='green')
plt.plot(results.index, results["Negative %"], label='Negative %', color='red')
plt.plot(results.index, results["Neutral %"], label='Neutral %', color='blue')
plt.title('Percentage of Agents by Sentiment over Time')
plt.xlabel('Number of Interactions')
plt.ylabel('Percentage')
plt.legend()
plt.show()
