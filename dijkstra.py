#!/usr/bin/env python
# coding: utf-8

# In[50]:


flights = {
    
'LAX':{'SFO':3, 'SEA': 6,'CHI':10},
'SFO':{'SEA':2, 'ATL':7},
'SEA':{'ATL':10, 'CHI':5},
'CHI':{'NYC':4,'MIA':3},
'NYC':{'MIA':3,'PHO':2},
'ATL':{'NYC':2,'PHO':5},
'MIA':{'PHO':4},
'PHO':{'MIA':4}
    
}


# In[51]:


flights['SFO']


# In[52]:


def dijkstra(flights, start, destination):
    
    #initialize our required parameters
    shortest_flight = {}
    previous_flight = {}
    unseenNodes = flights
    infinity = float('inf')
    track_path = []
    
    # we create sentinels to ensure we are always looking for shorter total paths
    for node in unseenNodes:
        shortest_flight[node] = infinity
        
    # distance or hours at destination will be 0    
    shortest_flight[start] = 0
    
    # scanning through possible locations
    while unseenNodes:
        
        
        min_distance_node = None
        
        for node in unseenNodes:
            
            # verifying condition & then selecting a possibility
            if min_distance_node is None:
                min_distance_node = node
                
            # we swap the shortest flight for whichever is closer    
            elif shortest_flight[node] < shortest_flight[min_distance_node]:
                min_distance_node = node
            
        #this opens up all possibilities    
        path_options = flights[min_distance_node].items()
        
        # now we will use possible destinations and the hours it takes to get to them
        for child_node, hours in path_options:
            
            # comparisons to check the shortest route
            if hours + shortest_flight[min_distance_node] < shortest_flight[child_node]:
                shortest_flight[child_node] = hours+shortest_flight[min_distance_node]
                previous_flight[child_node] = min_distance_node
                
        unseenNodes.pop(min_distance_node)

    # what to do once we have the final spot
    currentNode = destination
    while currentNode != start:
        try:
            track_path.insert(0, currentNode)
            currentNode = previous_flight[currentNode]
            
        # In some cases, some cities will not be interconnected depending on our input
        except KeyError:
            print("Destination is not reachable")
            break
            
        
    track_path.insert(0,start)
    
    # otherwise, we print out the shortest flight combo and cities we must go through
    if shortest_flight[destination] != infinity:
        print("Shortest Flight Available is " + str(shortest_flight[destination]), "Hours Long")
        print("Optimal path is" + str(track_path))
        
        
dijkstra(flights, "SEA", "NYC")


# In[ ]:




