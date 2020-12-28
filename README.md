# Accounts

Accounts extends the custom user model of django's projects.

## Quick start

1. Clone this project with:

```bash
git clone https://github.com/sgelias/django-reusable-custom-user-model.git
```

3. Install from tar.gz source file:

```bash
pip install ../accounts-manager/dist/accounts-manager-0.0.1.tar.gz
```

4. Add "accounts" to your INSTALLED_APPS setting like this:

```python
INSTALLED_APPS = [
    ...
    'accounts',
]
```

5. Include the accounts URLconf in your project urls.py:

```python
path('accounts/', include('accounts.urls')),
```

6. Run ``python manage.py migrate`` to create the polls models.

7. Start the development server and visit `http://127.0.0.1:8000/admin/`
   to create a poll (you'll need the Admin app enabled).

8. Visit `http://127.0.0.1:8000/accounts/` to check the app.
