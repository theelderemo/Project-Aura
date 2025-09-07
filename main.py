from aura_agent import Aura

if __name__ == "__main__":
    # Create an instance of the Aura agent.
    aura_instance = Aura()
    
    # Start the main cognitive loop. This will run until the user quits.
    aura_instance.run_cognitive_loop()