# Expense Tracker with Azure AD Authentication

This Django application demonstrates how to integrate Microsoft Azure AD (Entra ID) authentication into a simple expense tracking web application.

## Features

- Azure AD authentication for user login
- Display user's name and email upon successful login
- Logout functionality

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- An Azure account with an active subscription
- An Azure AD tenant and the ability to create app registrations

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/Moshood-Wale/azure-auth.git
   cd azure-auth
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up Azure AD:
   - Go to the Azure Portal (https://portal.azure.com)
   - Navigate to Azure Active Directory > App registrations
   - Click on "New registration"
   - Name your application and select "Accounts in any organizational directory (Any Azure AD directory - Multitenant)"
   - Set the redirect URI to `http://localhost:8000/complete/azuread-oauth2/`
   - After creation, note down the Application (client) ID and create a new client secret

5. Create a `.env` file in the project root and add your Azure AD credentials:
   ```
   SECRET_KEY=SECRET_KEY
   SOCIAL_AUTH_AZUREAD_OAUTH2_KEY=your-client-id
   SOCIAL_AUTH_AZUREAD_OAUTH2_SECRET=your-client-secret
   ```

6. Run migrations:
   ```
   python manage.py migrate
   ```

## Running the Application

1. Start the Django development server:
   ```
   python manage.py runserver
   ```

2. Open a web browser and navigate to `http://localhost:8000`

3. Click on the "Login with Azure AD" button to authenticate

## Troubleshooting

If you encounter any issues:

1. Check the console for error messages and logs
2. Verify that your Azure AD app registration settings match your Django settings
3. Ensure you've cleared your browser cache and cookies after making changes
4. Double-check that all required settings are correctly added to your `settings.py` file
