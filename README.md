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

## Current Project Structure

```text
ai-browser-agent/
│
├── assignments/
│   ├── week1/
│   │   ├── main.py
│   │   └── user.json
│   │
│   └── week2/
│       ├── navigator.py
│       ├── form_filler.py
│       ├── tab_manager.py
│       ├── user_data.json
│       ├── articles.json
│       ├── navigator_screenshot.png
│       └── form_filled.png
│
├── screenshots/
│
├── notes/
│
├── requirements.txt
├── README.md
└── .gitignore
```

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

## Progress

### Learning Phase

* [x] Week 1 — Python Foundations
* [x] Week 2 — Playwright Browser Automation
* [ ] Week 3 — LLMs, APIs & Prompt Engineering
* [ ] Week 4 — Agent Design & LangChain
* [ ] Week 5 — FastAPI, Databases & WebSockets
* [ ] Week 6 — React Frontend
* [ ] Stretch Topics — Memory, Embeddings & Multi-Agent Systems

---

## Future Goals

* Integrate Large Language Models
* Enable natural language browser control
* Add memory and context retention
* Support Gmail and Calendar automation
* Build a FastAPI backend
* Create a React-based interface
* Implement multi-agent workflows
* Deploy a fully autonomous browser assistant

```
```
