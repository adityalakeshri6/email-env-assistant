from fastapi import FastAPI
from models import Action, Observation, Reward
from env import EmailAssistantEnv
import uvicorn

app = FastAPI()
env = EmailAssistantEnv()

@app.get("/")
def root():
    return {"status": "Email Assistant Env is running!"}

@app.post("/reset")
def reset():
    return env.reset()

@app.post("/step")
def step(action: Action):
    obs, reward, done, info = env.step(action)
    return {
        "observation": obs,
        "reward": reward,
        "done": done,
        "info": info
    }

@app.get("/state")
def state():
    return env.state()

def main():
    uvicorn.run(app, host="0.0.0.0", port=7860)

if __name__ == "__main__":
    main()
