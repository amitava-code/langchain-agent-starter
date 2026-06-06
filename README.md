# 🤖 LangChain AI Agent with Real-Time Web Search

## 📌 Overview

This project demonstrates the development of an AI agent using **LangChain**, integrated with a real-time internet search tool powered by **Tavily** and **Google Gemini (2.5 Flash)**.

The goal of this project was not just to build a working agent, but to deeply understand how agents:

* Decide when to use tools
* Process external data
* Generate reliable, grounded responses

---

## 🚀 Key Features

* 🔍 Real-time internet search using Tavily API
* 🧠 LLM-powered reasoning with Gemini 2.5 Flash
* 🛠️ Custom tool integration using LangChain
* ⚙️ Agent-based architecture for dynamic decision-making
* 📡 Ability to answer time-sensitive queries

---

## 🧩 Tech Stack

* **Python**
* **LangChain**
* **Google Generative AI (Gemini 2.5 Flash)**
* **Tavily API**
* **python-dotenv**

---

## 🏗️ Project Workflow

### 1. Environment Setup

* API keys are securely managed using `.env`
* `python-dotenv` loads environment variables at runtime

```python
from dotenv import load_dotenv
load_dotenv()
```

---

### 2. Tool Creation (Internet Search)

A custom tool is created using LangChain’s `@tool` decorator.

#### Purpose:

To fetch real-time information from the web.

```python
@tool
def surfInternet(query: str):
    result = tavily_client.search(query=query)
    return "\n\n".join([
        r.get("content", "")
        for r in result.get("results", [])
    ])
```

#### Key Insight:

Instead of returning raw JSON, the output is **cleaned and structured**, making it easier for the LLM to interpret.

---

### 3. Model Initialization

The agent uses Gemini 2.5 Flash for fast and efficient responses.

```python
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
```

---

### 4. Agent Creation

The agent is created by combining:

* The LLM (reasoning engine)
* The tool (external capability)

```python
agent = create_agent(
    model=model,
    tools=[surfInternet],
    system_prompt="""
    You are an AI agent.
    Always use tools for real-time information.
    Do not rely on internal knowledge for current events.
    """
)
```

---

### 5. Execution Flow

#### Step-by-step:

1. User sends a query
2. Agent decides whether to use the tool
3. Tool fetches real-time data
4. Data is passed back to the LLM
5. LLM generates the final response

```python
response = agent.invoke({
    "messages": [
        HumanMessage("Who is the current president of the United States?")
    ]
})
```

---

## ⚠️ Challenges & Learnings

### ❌ Initial Issues

* Agent ignored the tool and answered from outdated knowledge
* Incorrect answers for real-time queries
* Poor interpretation of raw tool outputs

---

### ✅ Solutions Implemented

* Structured tool output (instead of raw JSON)
* Strong system prompts to enforce tool usage
* Improved query design for clarity
* Reduced ambiguity in retrieved data

---

## 🧠 Key Takeaways

* Tool access ≠ correct answers
* Output formatting significantly impacts LLM reasoning
* Agents require **control, not just capability**
* Reliability is the biggest challenge in AI agent systems


---

## 🤝 Contributing / Feedback

Feedback, suggestions, and discussions are welcome.
Feel free to open an issue or connect!

---

## ⭐ Final Note

This project is a foundational step toward building reliable AI agents — focusing not just on functionality, but on **correctness and control**.
