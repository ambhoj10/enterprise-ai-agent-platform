# Enterprise AI Agent Platform

## Overview

Enterprise AI Agent Platform is a multi-agent AI system built using FastAPI and Azure OpenAI.

The platform routes user requests to specialized AI agents that provide domain-specific responses. Agents can leverage enterprise tools and retrieval workflows to generate contextual and actionable responses.

Current agents include:

* Knowledge Agent
* CloudOps Agent
* DevOps Agent
* Documentation Agent

---

## Architecture

User Request

↓

FastAPI API Gateway

↓

Agent Router

↓

Selected Agent

* Knowledge Agent
* CloudOps Agent
* DevOps Agent
* Documentation Agent

↓

Tool Service

* GitHub Tool
* Azure DevOps Tool
* Search Tool

↓

Azure OpenAI (GPT-4o-mini)

↓

AI Response

---

## Features

### Multi-Agent Routing

Automatically routes requests to the most appropriate AI agent based on user intent.

### Azure OpenAI Integration

Uses Azure OpenAI GPT-4o-mini for enterprise-grade AI responses.

### Tool-Augmented Agents

Agents can access tools and external systems to enrich responses.

Implemented tools:

* GitHub Tool
* Azure DevOps Tool
* Search Tool

### Retrieval Workflow

Knowledge Agent can retrieve contextual information before generating responses.

### GitHub Repository Intelligence

The DevOps Agent can retrieve live repository information directly from GitHub.

Capabilities:

* Repository Metadata
* Open Issues Analysis
* Pull Request Analysis
* GitHub Best Practices
* AI-Powered DevOps Recommendations

### Production API Design

REST API built with FastAPI.

Endpoint:

POST /agent/chat

Example Request:

```json
{
  "question": "Summarize my GitHub repository"
}
```

---

## Example Questions

### Knowledge Agent

* What is Retrieval Augmented Generation?
* Explain vector databases.
* What are AI agent architectures?

### CloudOps Agent

* How do I optimize Azure costs?
* Explain Azure monitoring best practices.
* How should I design a scalable cloud architecture?

### DevOps Agent

* Summarize my GitHub repository.
* Show open issues in my repository.
* What pull requests are currently open?
* Give me DevOps recommendations for my repository.

### Documentation Agent

* Create a deployment runbook.
* Generate architecture documentation.
* Create an operational procedure.

---

## Project Structure

```text
agents/

api/

app/

docs/

models/

orchestrator/

services/

services/tools/

tests/
```

---

## Technology Stack

* Python
* FastAPI
* Azure OpenAI
* GPT-4o-mini
* Requests
* Pydantic
* REST APIs

---

## Current Status

### Completed

#### Week 13 – Multi-Agent Platform

* Agent Router
* Knowledge Agent
* CloudOps Agent
* DevOps Agent
* Documentation Agent
* FastAPI Gateway
* Azure OpenAI Integration

#### Week 14 – Tool Layer

* GitHub Tool
* Azure DevOps Tool
* Search Tool
* Tool Service
* Retrieval Workflow

#### Week 15 – GitHub API Integration

* GitHub Personal Access Token Integration
* GitHub Service
* Repository Metadata Retrieval
* Open Issues Retrieval
* Pull Request Retrieval
* GitHub Tool Integration
* DevOps Agent Integration
* Live Repository Intelligence

---

## Roadmap

### Next Milestones

* GitHub Actions Workflow Intelligence
* Azure DevOps API Integration
* Azure AI Search Integration
* Retrieval Augmented Generation (RAG)
* Agent Orchestration
* Conversation Memory
* Observability
* Production Monitoring

---

## Version

Current Version: **1.1**

---

## Author

Amboj Kumar

