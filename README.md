# Enterprise AI Agent Platform

## Overview

Enterprise AI Agent Platform is a multi-agent AI system built using FastAPI and Azure OpenAI.

The platform routes user requests to specialized AI agents that provide domain-specific responses.

Current agents include:

* Knowledge Agent
* CloudOps Agent
* DevOps Agent
* Documentation Agent

The platform also supports tool integration and retrieval workflows.

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

Response

---

## Features

### Multi-Agent Routing

Automatically routes requests to the most appropriate agent.

### Azure OpenAI Integration

Uses Azure OpenAI GPT-4o-mini for AI-powered responses.

### Tool-Augmented Agents

Agents can use tools to enrich responses.

Implemented tools:

* GitHub Tool
* Azure DevOps Tool
* Search Tool

### Retrieval Workflow

Knowledge Agent can retrieve contextual information before generating responses.

### Production API Design

REST API built with FastAPI.

Endpoint:

POST /agent/chat

Example Request:

{
"question": "How do I optimize Azure costs?"
}

---

## Project Structure

agents/

api/

app/

models/

orchestrator/

services/

services/tools/

tests/

---

## Technology Stack

* Python
* FastAPI
* Azure OpenAI
* GPT-4o-mini
* Pydantic
* REST APIs

---

## Roadmap

### Completed

* Multi-Agent Platform
* Azure OpenAI Integration
* Tool Layer
* Tool Service
* Retrieval Workflow

### Planned

* GitHub API Integration
* Azure DevOps API Integration
* Azure AI Search RAG
* Agent Orchestration
* Conversation Memory
* Observability

---

## Author

Amboj Kumar

