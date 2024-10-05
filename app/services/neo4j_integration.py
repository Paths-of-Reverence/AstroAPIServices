from neo4j import GraphDatabase

class Neo4jHandler:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
    
    def close(self):
        self.driver.close()
    
    def save_chart(self, chart_id, positions, aspects):
        with self.driver.session() as session:
            session.write_transaction(self._create_and_link_nodes, chart_id, positions, aspects)
    
    @staticmethod
    def _create_and_link_nodes(tx, chart_id, positions, aspects):
        # Create and link nodes in Neo4j
        for position in positions:
            tx.run("CREATE (p:Position {chart_id: $chart_id, planet: $planet, sign: $sign, degree: $degree})",
                   chart_id=chart_id, planet=position['planet'], sign=position['sign'], degree=position['degree'])
        
        for aspect in aspects:
            tx.run("MATCH (p1:Position {chart_id: $chart_id, planet: $planet1}), (p2:Position {chart_id: $chart_id, planet: $planet2}) "
                   "CREATE (p1)-[:ASPECT {type: $aspect, orb: $orb}]->(p2)",
                   chart_id=chart_id, planet1=aspect['planet1'], planet2=aspect['planet2'], aspect=aspect['aspect'], orb=aspect['orb'])