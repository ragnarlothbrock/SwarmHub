def run(state):
    """Executes the generated test script with the use of Pytest and stores its output."""
    
    print("Evaluating the generated test with PyTest.")
    
    exec(state["script"], globals())

    nest_asyncio.apply()

    from contextlib import redirect_stdout
    output = io.StringIO()
    with redirect_stdout(output):
        ipytest.run()

    output.getvalue()

    return {
        **state,
        "test_evaluation_output": output.getvalue()
    }