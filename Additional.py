import other_test

# Example usage with different models
if __name__ == "__main__":
    # Examples of models you could use:

    # Larger GPT-2 models
    # model = AdvancedPPL(model_id="gpt2-large")

    # Microsoft DialoGPT
    # model = AdvancedPPL(model_id="microsoft/DialoGPT-large")

    # GPT-Neo models
    # model = AdvancedPPL(model_id="EleutherAI/gpt-neo-1.3B")
    # model = AdvancedPPL(model_id="EleutherAI/gpt-neo-2.7B")

    # Llama models (if you have access)
    # model = AdvancedPPL(model_id="meta-llama/Llama-2-7b-hf")

    # Default to GPT-2
    model = AdvancedPPL(model_id="gpt2")

    test_text = """
    This is a sample text to test the perplexity calculation.
    It contains multiple sentences with varying complexity.
    The algorithm will analyze each sentence individually.
    """

    results, output = model(test_text)
    print("\nResults:", results)
    print("Output:", output)
