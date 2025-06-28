import random

class RandomNumberButton:
    WEB_DIRECTORY = "js"
    CATEGORY = "Agent Assist"
    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("random_number",)
    FUNCTION = "generate_random"

    @classmethod
    def INPUT_TYPES(s):
        # No standard inputs are needed for this node's function.
        # The button is handled by Javascript triggering a workflow queue.
        return {"required": {}}

    def generate_random(self):
        """Generates a random integer between 0 and 1000."""
        number = random.randint(0, 1000)
        # print(f"Generated random number: {number}") # Optional: for debugging
        return (number,)
# ====================================================================================================
# DO NOT TOUCH THIS SECTION, IT IS REQUIRED FOR THE NODE TO WORK IN COMFYUI
# ====================================================================================================
NODE_CLASS_MAPPINGS = {
    "RandomNumberButton": RandomNumberButton
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "RandomNumberButton": "Random Number Button"
}
