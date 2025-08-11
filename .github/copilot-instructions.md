# Copilot Instructions

<!-- Use this file to provide workspace-specific custom instructions to Copilot. For more details, visit https://code.visualstudio.com/docs/copilot/copilot-customization#_use-a-githubcopilotinstructionsmd-file -->

This is a Python FastAPI project for GLPI API communication with the following characteristics:

## Project Structure
- FastAPI application with route separation
- Token-based authentication system with permanent tokens
- Routes for tickets/chamados management
- Health check endpoint
- Modular architecture with routers

## Key Features
- **Authentication**: Uses a unique token that doesn't expire
- **Chamados Route**: Handles ticket-related operations
- **Health Check**: Simple health monitoring endpoint
- **Modular Design**: Separated routers for better organization

## Development Guidelines
- Follow FastAPI best practices
- Use proper HTTP status codes
- Implement proper error handling
- Keep routes organized in separate modules
- Use dependency injection for authentication
