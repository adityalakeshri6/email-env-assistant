from openenv.core.env_server import Environment
from models import Action, Observation, Reward
import random

class EmailAssistantEnv(Environment):
    def __init__(self):
        super().__init__()
        self.tasks = [
            {"text": "Win a free iPhone now!!! Click here", "label": "spam", "difficulty": "easy"},
            {"text": "Limited time offer, claim reward now", "label": "spam", "difficulty": "easy"},
            {"text": "Project meeting at 3 PM tomorrow", "label": "work", "difficulty": "medium"},
            {"text": "Please review the attached document", "label": "work", "difficulty": "medium"},
            {"text": "Client feedback received, need changes", "label": "work", "difficulty": "medium"},
            {"text": "Let's go for dinner tonight", "label": "personal", "difficulty": "medium"},
            {"text": "Happy birthday! Wish you success", "label": "personal", "difficulty": "medium"},
            {"text": "Can you send the report by tomorrow?", "label": "work", "difficulty": "hard"},
            {"text": "Please schedule a meeting with the client", "label": "work", "difficulty": "hard"},
            {"text": "We need urgent support for this issue", "label": "work", "difficulty": "hard"}
        ]
        self.current = None
        self.steps = 0

    def reset(self):
        self.current = random.choice(self.tasks)
        self.steps = 0
        return Observation(
            email_text=self.current["text"],
            expected_label=self.current["label"]
        )

    def step(self, action: Action):
        self.steps += 1
        reward = 0.0
        done = True
        info = {"difficulty": self.current["difficulty"]}
        text = self.current["text"].lower()
        label = self.current["label"]

        if action.action_type == "classify":
            pred = action.content.lower()
            if pred == label:
                reward = 1.0
            elif pred in ["spam", "work", "personal"]:
                reward = 0.4
            else:
                reward = 0.0
            obs = Observation(
                email_text=self.current["text"],
                agent_output=action.content
            )

        elif action.action_type == "reply":
            reply = action.content.lower()
            if len(reply) < 5:
                reward = 0.0
            elif "report" in text and ("send" in reply or "will" in reply):
                reward = 1.0
            elif "meeting" in text and ("schedule" in reply or "available" in reply):
                reward = 1.0
            elif "urgent" in text and ("resolve" in reply or "working" in reply):
                reward = 1.0
            elif len(reply) > 15:
                reward = 0.7
            else:
                reward = 0.3
            obs = Observation(
                email_text=self.current["text"],
                agent_output=action.content
            )

        else:
            obs = Observation(email_text=self.current["text"])

        return obs, Reward(value=reward), done, info

    def state(self):
        return {
            "steps": self.steps,
            "current_task": self.current
        }
