# 🧠 AI Orchestrator with Containers

This project is a mini "AI Orchestrator" that uses LLM (Large Language Model) integration and containerized microservices to dynamically perform tasks based on high-level user instructions.

## 🚀 Overview

Users provide a high-level request like:
- "Clean this dataset"
- "Analyze sentiment in this text"

The orchestrator:
1. Sends the prompt to an LLM agent.
2. Determines which containerized tasks to run.
3. Spins up Docker containers in sequence.
4. Returns the final result to the user via CLI.

## 🧩 Architecture

- **LLM Agent**: Parses user requests and maps them to specific tasks.
- **Docker Containers**: Each service (e.g., data cleaning, sentiment analysis) is containerized.
- **Orchestrator (Python)**: Receives the input, interacts with LLM, manages containers, and returns output.
- **CLI**: Simple command-line interface for input/output.

### 🖼️ Architecture Diagram

```text
[User Input] --> [LLM Agent] --> [Orchestrator]
                                 |--> [Container A]
                                 |--> [Container B]
                                 --> [Final Output]
