class AgentSemanticCacheManagerClient:
    def lookup(self, prompt: str) -> dict:
        return {"cache_hit": False, "cached_response": ""}