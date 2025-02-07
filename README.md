# article-manager

Overview

This is a Django-based REST API for managing articles, including AI-powered summarization using Google Gemini API. The API supports CRUD operations and allows summarizing article content using an LLM.

Features

1. Create, Retrieve, Update, and Delete Articles
2. AI-powered content summarization using Google Gemini API

Requirements

1. Python 3.9+
2. Django 
3. Django REST Framework
4. Google-genai

Endpoints
1. GET /api/articles/
2. POST /api/articles/
3. GET /api/articles/<id>/ 
4. PUT/PATCH /api/articles/<id>/
5. DELETE /api/articles/<id>/
6. GET /api/articles/<id>/summary/

