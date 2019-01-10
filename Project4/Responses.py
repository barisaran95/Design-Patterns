
class Responses:
    def __init__(self, desiredResponse):
        self.desiredResponse = desiredResponse
        self.cheers = ["Yaay", "Woo", "Heey", "HeHeHey", "Victory is OURS!", "Go Home"]
        self.barks = ["Boo", "Noo", "Grr", "Big BOOO", "NOOO", "I bet this match, damn!"]
    
    def response_context(self):
        return self.desiredResponse.response_interface()
        
class Strategy:
    def __init__(self):
        pass
        
    def response_interface(self):
        pass
        
class PositiveAudienceStrategy(Strategy):
    def response_interface(self):
        return ["p_hit", "p_crit_hit", "p_dodge", "p_killed", "n_crit_damaged"]
    
class NegativeAudienceStrategy(Strategy):
    def response_interface(self):
        return ["n_damaged", "n_crit_damaged", "n_dodgedby", "n_died", "p_crit_hit"]
    
class HybridStrategy(Strategy):
    def response_interface(self):
        return ["p_hit", "n_dodgedby", "p_killed", "n_crit_damaged"]