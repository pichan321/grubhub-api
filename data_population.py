class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex in self.vertices: return
        self.vertices[vertex] = []

    def add_edge(self, src, dest):
        self.add_vertex(src)
        self.add_vertex(dest)

        self.vertices[src].append(dest)
    
    def topological_sort(self):
        indegree = {k: 0 for k, _ in self.vertices.items()}
        
        for k, v in self.vertices.items():
            for node in v:
                indegree[node] += 1
        
        q = []
        for k, v in indegree.items():
            if v == 0: q.append(k)
        
        ordering = []
   
        while q:
            current = q.pop(0)
            ordering.append(current)

            for node in self.vertices[current]:
                indegree[node] -= 1

                if indegree[node] == 0: q.append(node)
        
        return ordering



def produce_population_ordering():
    g = Graph()
    # g.add_edge("accounts", "subscription")
# 
    # g.add_edge("choice_groups", "menu_items")
    # g.add_edge("choice_groups", "option_type")
    # g.add_edge("choice_groups", "choice_status")
# 
    # g.add_edge("choice_items", "choice_groups")
    # g.add_edge("choice_items", "choice_status")
# 
    # g.add_edge("menu_categories", "restaurants")
# 
    # g.add_edge("menu_items", "menu_categories")
# 
    # g.add_edge("order_details", "orders")
    # g.add_edge("order_details", "choice_items")
    # g.add_edge("order_details", "menu_items")
# 
    # g.add_vertex("order_status")
# 
    # g.add_vertex("order_type")
# 
    # g.add_edge("orders", "accounts")
    # g.add_edge("orders", "order_type")
    # g.add_edge("orders", "order_status")
# 
    # g.add_vertex("restaurant_categories")
# 
    # g.add_edge("restaurant_to_category", "restaurant_categories")
    # g.add_edge("restaurant_to_category", "restaurants")
# 
    # g.add_vertex("restaurants")
# 
    # g.add_vertex("subscription")
    g.add_edge("subscription", "accounts")

    g.add_edge("menu_items"    , "choice_groups") 
    g.add_edge("option_type"   , "choice_groups")
    g.add_edge("choice_status" , "choice_groups")

    g.add_edge("choice_groups", "choice_items" )
    g.add_edge("choice_status", "choice_items" )

    g.add_edge("restaurants", "menu_categories")

    g.add_edge("menu_categories", "menu_items")

    g.add_edge("orders"      , "order_details")
    g.add_edge("choice_items", "order_details")
    g.add_edge("menu_items"  , "order_details")  

    g.add_vertex("order_status")

    g.add_vertex("order_type")

    g.add_edge( "accounts"    , "orders")
    g.add_edge( "order_type"  , "orders")
    g.add_edge( "order_status", "orders")

    g.add_vertex("restaurant_categories")

    g.add_edge("restaurant_categories", "restaurant_to_category")
    g.add_edge("restaurants"          , "restaurant_to_category")

    g.add_vertex("restaurants")

    g.add_vertex("subscription")

    l = g.topological_sort()
    print(l)

produce_population_ordering()