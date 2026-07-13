from client import AgentSemanticCacheManagerClient
client = AgentSemanticCacheManagerClient()
print(client.lookup("hello world"))