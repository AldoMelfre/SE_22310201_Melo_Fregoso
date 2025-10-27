import heapq
import networkx as nx
import matplotlib.pyplot as plt

def prim_mst(graph, start):
    visited = set()
    mst_edges = []
    edges = [(0, None, start)]
    while edges:
        weight, u, v = heapq.heappop(edges)
        if v in visited:
            continue
        visited.add(v)
        if u is not None:
            mst_edges.append((u, v, weight))
        for w, w_weight in graph[v].items():
            if w not in visited:
                heapq.heappush(edges, (w_weight, v, w))
    return mst_edges

# Grafo ampliado de actividades diarias de un freelancer
actividades = {
    'Despertar': {'Gimnasio': 1, 'Desayuno': 0.5, 'Meditar': 0.3},
    'Meditar': {'Despertar': 0.3, 'Gimnasio': 0.2},
    'Gimnasio': {'Despertar': 1, 'Desayuno': 0.5, 'Meditar': 0.2, 'Ducha': 0.3},
    'Ducha': {'Gimnasio': 0.3, 'Desayuno': 0.2},
    'Desayuno': {'Despertar': 0.5, 'Gimnasio': 0.5, 'Ducha': 0.2, 'Trabajo': 0.5},
    'Trabajo': {'Desayuno': 0.5, 'Lectura': 1, 'Autodidacta': 2, 'Ver Novia': 2, 'Comida': 1},
    'Comida': {'Trabajo': 1, 'Lectura': 0.5},
    'Lectura': {'Trabajo': 1, 'Autodidacta': 1, 'Comida': 0.5},
    'Autodidacta': {'Trabajo': 2, 'Lectura': 1, 'Ver Novia': 1.5, 'Proyecto Personal': 2},
    'Proyecto Personal': {'Autodidacta': 2, 'Ver Novia': 2},
    'Ver Novia': {'Trabajo': 2, 'Autodidacta': 1.5, 'Proyecto Personal': 2, 'Cena': 1},
    'Cena': {'Ver Novia': 1, 'Dormir': 0.5},
    'Dormir': {'Cena': 0.5}
}

# Dependencias (actividad: [predecesores])
dependencias = {
    'Despertar': [],
    'Meditar': ['Despertar'],
    'Gimnasio': ['Despertar', 'Meditar'],
    'Ducha': ['Gimnasio'],
    'Desayuno': ['Despertar', 'Gimnasio', 'Ducha'],
    'Trabajo': ['Desayuno'],
    'Comida': ['Trabajo'],
    'Lectura': ['Trabajo'],
    'Autodidacta': ['Trabajo', 'Lectura'],
    'Proyecto Personal': ['Autodidacta'],
    'Ver Novia': ['Trabajo', 'Autodidacta', 'Proyecto Personal'],
    'Cena': ['Ver Novia'],
    'Dormir': ['Cena']
}

mst = prim_mst(actividades, 'Despertar')

def mostrar_grafo_interactivo(actividades, mst, dependencias):
    G = nx.Graph()
    for u, v, w in mst:
        G.add_edge(u, v, weight=w)
    pos = nx.spring_layout(G, seed=42)

    completadas = set(['Despertar'])  # Solo puedes empezar por 'Despertar'

    fig, ax = plt.subplots(figsize=(12, 8))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=1200, font_size=10, ax=ax)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, ax=ax)
    plt.title("Haz clic en la siguiente actividad permitida")

    node_positions = {nodo: pos[nodo] for nodo in G.nodes}

    def actividad_permitida(nodo):
        return all(dep in completadas for dep in dependencias.get(nodo, []))

    def on_click(event):
        for nodo, (x, y) in node_positions.items():
            if (event.xdata is not None and event.ydata is not None and
                (abs(event.xdata - x) < 0.05 and abs(event.ydata - y) < 0.05)):
                if not actividad_permitida(nodo):
                    print(f"No puedes hacer '{nodo}' antes de completar: {dependencias[nodo]}")
                    plt.title(f"Primero completa: {', '.join(dep for dep in dependencias[nodo] if dep not in completadas)}")
                    fig.canvas.draw()
                    break
                completadas.add(nodo)
                ax.clear()
                nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=1200, font_size=10, ax=ax)
                nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, ax=ax)
                nx.draw_networkx_nodes(G, pos, nodelist=list(completadas), node_color='orange', node_size=1400, ax=ax)
                plt.title(f"Actividad completada: {nodo}")
                fig.canvas.draw()
                print(f"Actividad: {nodo}")
                print(f"Conexiones: {actividades[nodo]}")
                break

    fig.canvas.mpl_connect('button_press_event', on_click)
    plt.show()

mostrar_grafo_interactivo(actividades, mst, dependencias)