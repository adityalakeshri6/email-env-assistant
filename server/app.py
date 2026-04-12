from fastapi import FastAPI
from env import EmailAssistantEnv
from models import Action

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
