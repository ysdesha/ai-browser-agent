# AI Browser Agent

An end-to-end Agentic AI Browser Assistant being built from scratch using Python, Playwright, FastAPI, LLMs, LangChain, and React.

The goal of this project is to develop an autonomous browser agent capable of navigating websites, extracting information, filling forms, managing tabs, interacting with external APIs, maintaining memory, and eventually executing complex multi-step tasks from natural language instructions.

---

## Project Roadmap

### Week 1 — Python Foundations & Web Basics

Topics Covered:

* Async / Await
* JSON Handling
* Exception Handling
* Virtual Environments
* Dataclasses
* HTML Structure
* DOM Fundamentals
* CSS Selectors
* Forms and Inputs

Assignment Completed:

* Created Python virtual environment
* Installed and managed dependencies
* Built an async JSON reader
* Implemented exception handling
* Practiced CSS selectors using browser DevTools
* Completed foundational Python exercises

---

### Week 2 — Browser Automation with Playwright

Topics Covered:

* Async Playwright
* Browser / Context / Page Architecture
* Locators
* Fill, Click and Input Actions
* Screenshots
* Wait Strategies
* Multiple Tabs
* JSON Integration
* Error Handling

Assignments Completed:

#### Script 1 — Navigator

Features:

* Opens Hacker News
* Extracts top 5 article titles
* Saves results to JSON
* Handles page load timeouts
* Handles missing elements
* Captures screenshots

Output:

```text
articles.json
navigator_screenshot.png
```

---

#### Script 2 — Form Filler

Features:

* Reads user information from JSON
* Opens DemoQA Practice Form
* Automatically fills form fields
* Selects gender option
* Captures screenshot before submission
* Handles page load and element errors

Output:

```text
user_data.json
form_filled.png
```

---

#### Script 3 — Tab Manager

Features:

* Opens 5 browser tabs in parallel
* Navigates to multiple websites
* Captures page titles
* Closes all tabs except the first
* Handles navigation and title retrieval errors

---

## Technologies Used

* Python 3.10+
* Playwright
* AsyncIO
* JSON
* Git
* GitHub

---

## Setup

Clone the repository:

```bash
git clone <repository-url>
cd ai-browser-agent
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install Playwright browsers:

```bash
playwright install
```

---
### Week 3 — LLMs, APIs & Prompt Engineering

Topics Covered:

* Large Language Models (LLMs)
* Gemini API Integration
* Prompt Engineering
* Few-Shot Prompting
* Structured Outputs
* JSON-Based Action Planning
* Function Calling Concepts
* API Authentication
* Natural Language Understanding

Assignment Completed:

#### Intent Parser Prototype

Features:

* Integrated Gemini API for natural language understanding
* Built a reusable `parse_intent()` function
* Converts natural language commands into structured JSON action plans
* Designed a consistent action schema
* Implemented few-shot prompting through a system prompt
* Added clarification handling for ambiguous commands
* Tested the parser with multiple browser-assistant commands
* Added error handling for API failures and rate limits

Schema Used:

```json
{
  "action": "",
  "target_url": "",
  "data": {},
  "steps": []
}
```

Supported Actions:

* navigate
* fill_form
* click
* email
* summarize
* tab_management

Example:

Input:

```text
apply to this job
```

Output:

```json
{
  "action": "fill_form",
  "target_url": "",
  "data": {},
  "steps": [
    "fill out application",
    "submit application"
  ]
}
```

Files Created:

```text
week3/
│
├── intent_parser.py
├── test_commands.py
├── sample_outputs.txt
├── .env
│
└── prompts/
    └── system_prompt.txt
```

Technologies Used:

* Gemini API
* Google GenAI SDK
* Python Dotenv
* JSON
* Prompt Engineering
* Few-Shot Learning

---

### Week 4 — Agentic AI Design & LangChain

Topics Covered:

* Agentic AI Concepts
* ReAct Pattern
* Tool-Based Reasoning
* LangChain Fundamentals
* Custom Tools
* Agent Workflows
* Conversation Memory
* User Profile Storage
* Planning and Execution Loops

Assignment Completed:

#### LangChain Agent with Browser Tools

Features:

* Created browser interaction tools
* Built a simple agent architecture using Gemini
* Added user profile memory using JSON
* Implemented tool discovery and action planning
* Simulated agent reasoning and execution flow
* Connected natural language commands to browser actions
* Demonstrated the complete agent workflow

Custom Tools:

* `navigate_to(url)`
* `click_element(selector)`
* `type_text(text)`

User Profile Store:

```json
{
  "name": "Esha",
  "email": "ysdesha@gmail.com",
  "resume_path": "resume.pdf"
}
```

Example Workflow:

```text
User Command
      ↓
Agent Reasoning
      ↓
Tool Selection
      ↓
Tool Execution
      ↓
Observation
      ↓
Final Result
```

Example Task:

```text
Go to google.com and search for AI news
```

Generated Plan:

```python
navigate_to("https://www.google.com")
type_text("AI news")
```

Files Created:

```text
week4/
│
├── agent.py
├── browser_tools.py
├── memory_store.py
├── test_agent.py
└── user_profile.json
```

Technologies Used:

* LangChain
* Gemini API
* Python Dotenv
* JSON
* Custom Tool Design
* ReAct Agent Pattern

## Progress

### Learning Phase

* [x] Week 1 — Python Foundations
* [x] Week 2 — Playwright Browser Automation
* [x] Week 3 — LLMs, APIs & Prompt Engineering
* [x] Week 4 — Agent Design & LangChain
* [ ] Week 5 — FastAPI, Databases & WebSockets
* [ ] Week 6 — React Frontend
* [ ] Stretch Topics — Memory, Embeddings & Multi-Agent Systems

---

## Future Goals

* Support Gmail and Calendar automation
* Build a FastAPI backend
* Create a React-based interface
* Implement multi-agent workflows
* Deploy a fully autonomous browser assistant

```
```
