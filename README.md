# 📧 Email Assistant OpenEnv Environment

A reinforcement learning environment for training AI agents to classify and reply to emails, built using the [OpenEnv](https://github.com/meta-pytorch/OpenEnv) framework by Meta PyTorch.

## 🚀 Live Demo
🤗 [Hugging Face Space](https://huggingface.co/spaces/sanproster/email-env-assistant)

---

## 📌 Environment Details

| Property | Value |
|----------|-------|
| **Task** | Email classification & reply generation |
| **Actions** | `classify` or `reply` |
| **Labels** | `spam`, `work`, `personal` |
| **Reward Range** | `0.0` to `1.0` |
| **Framework** | OpenEnv (Meta PyTorch) |

---

## 📁 File Structure

| File | Description |
|------|-------------|
| `app.py` | FastAPI server with reset/step/state endpoints |
| `env.py` | Core RL environment logic |
| `models.py` | Pydantic models for Action, Observation, Reward |
| `Dockerfile` | Container configuration for HF Spaces |
| `requirements.txt` | Python dependencies |

---

## 🔌 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Health check |
| `/reset` | POST | Start a new episode |
| `/step` | POST | Take an action |
| `/state` | GET | Get current episode state |

---

## 🧪 Example Usage

```python
import requests

BASE_URL = "https://sanproster-email-env-assistant.hf.space"

# Reset environment
obs = requests.post(f"{BASE_URL}/reset").json()
print(obs)
# Output: {"email_text": "Win a free iPhone now!!!", "expected_label": "spam"}

# Classify action
action = {"action_type": "classify", "content": "spam"}
result = requests.post(f"{BASE_URL}/step", json=action).json()
print(result)
# Output: {"observation": {...}, "reward": {"value": 1.0}, "done": true, "info": {...}}

# Reply action
action = {"action_type": "reply", "content": "I will send the report by tomorrow morning."}
result = requests.post(f"{BASE_URL}/step", json=action).json()
print(result)
```

---

## 🏆 Reward Structure

### Classification Task
| Prediction | Reward |
|------------|--------|
| Correct label | `1.0` |
| Wrong but valid label | `0.4` |
| Invalid response | `0.0` |

### Reply Task
| Reply Quality | Reward |
|---------------|--------|
| Too short (< 5 chars) | `0.0` |
| Contextually relevant | `1.0` |
| Decent length (> 15 chars) | `0.7` |
| Short but valid | `0.3` |

---

## 🛠️ Built With

- [OpenEnv](https://github.com/meta-pytorch/OpenEnv) - Meta PyTorch RL Environment Framework
- [FastAPI](https://fastapi.tiangolo.com/) - Web framework
- [Pydantic](https://docs.pydantic.dev/) - Data validation
- [Docker](https://www.docker.com/) - Containerization

---

## 👤 Author

**Aditya** - [@adityalakeshri6](https://github.com/adityalakeshri6)
