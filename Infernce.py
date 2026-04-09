import requests

BASE_URL = "https://sanproster-email-env-assistant.hf.space"

def reset():
    response = requests.post(f"{BASE_URL}/reset")
    return response.json()

def step(action_type: str, content: str):
    action = {
        "action_type": action_type,
        "content": content
    }
    response = requests.post(f"{BASE_URL}/step", json=action)
    return response.json()

def state():
    response = requests.get(f"{BASE_URL}/state")
    return response.json()

if __name__ == "__main__":
    print("=== Resetting Environment ===")
    obs = reset()
    print(obs)

    print("\n=== Classify Action ===")
    result = step("classify", "spam")
    print(result)

    print("\n=== Reply Action ===")
    result = step("reply", "I will send the report by tomorrow morning.")
    print(result)

    print("\n=== Current State ===")
    print(state())
