def run(state):
    """Get human verification for low/medium severity alerts"""
    severity = state["severity"].strip().lower()

    if severity in ["low", "medium"]:
        print("\n" + "="*50)
        print(f"Low/Medium severity alert for {state['city']} requires human approval:")
        print(f"Disaster Type: {state['disaster_type']}")
        print(f"Current Weather: {state['weather_data']['weather']}")
        print(f"Temperature: {state['weather_data']['temperature']}°C")
        print(f"Wind Speed: {state['weather_data']['wind_speed']} m/s")
        print(f"Severity: {state['severity']}")
        print(f"Response Plan: {state['response']}")
        print("\nType 'y' to approve sending alert or 'n' to reject (waiting for input):")
        print("="*50)

        # Block and wait for input
        while True:
            try:
                user_input = input().lower().strip()
                if user_input in ['y', 'n']:
                    approved = user_input == 'y'
                    print(f"Human verification result: {'Approved' if approved else 'Rejected'}")
                    break
                else:
                    print("Please enter 'y' for yes or 'n' for no:")
            except Exception as e:
                print(f"Error reading input: {str(e)}")
                print("Please try again with 'y' or 'n':")

        return {
            **state,
            "human_approved": approved,
            "messages": state["messages"] + [
                SystemMessage(content=f"Human verification: {'Approved' if approved else 'Rejected'}")
            ]
        }
    else:
        # Auto-approve for high/critical severity
        return {
            **state,
            "human_approved": True,
            "messages": state["messages"] + [
                SystemMessage(content=f"Auto-approved {severity} severity alert")
            ]
        }