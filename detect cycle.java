class Graph {
    private int vertices;
    private Map<Integer, List<Integer>> adjList;
    private Set<Integer> grey, black, white; //grey for vertices under exploration , white unvisited, black visited
    Graph(int v) {
        vertices = v;
        adjList = new HashMap<Integer, List<Integer>>();
        grey = new HashSet<Integer>();
        black = new HashSet<Integer>();
        white = new HashSet<Integer>();
        for(int i=0;i<v;i++) {
        	white.add(i+1);
        }
    }
    
    public void addEdge(int u,int v) {
        if(adjList.containsKey(u)) {
        	adjList.get(u).add(v);
        } else {
        	adjList.put(u, new ArrayList<Integer>(Arrays.asList(v)));
        }
    }
    
    public int dfs(int u) {
        moveSet(white, grey, u);
    	if(adjList.get(u) != null) {
    	
    	for(int vertex: adjList.get(u)) {
    	    if(black.contains(vertex)) {
    	        continue;
    	    }
    		if(grey.contains(vertex)) {
    			return 1;
		    }
    		if(dfs(vertex) == 1) {
    			return 1;
    		}

	    }
	    
        }
	    moveSet(grey,black,u);
	    return 0;
    }
    
    
    public int detectCycle() {
    	while(!white.isEmpty()) {
    		int u = white.iterator().next();
    		if(dfs(u)==1) {
    			return 1;
    		}
    	}
    	return 0;
    	
    }
    
    public void moveSet(Set<Integer> source, Set<Integer> target, int v ) {
    	source.remove(v);
    	target.add(v);
    }
    
}
