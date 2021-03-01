# Accounts

Accounts extends the custom user model of django's projects.

## Quick start

1. Clone this project with:

```bash
git clone https://github.com/sgelias/django-reusable-custom-user-model.git
```

3. Install from tar.gz source file:

```bash
pip install dist/accounts-manager-0.0.1.tar.gz
```

4. Add "accounts" to your INSTALLED_APPS to setting.py:

```python
INSTALLED_APPS = [
    ...
    'account-owner',
]
```

5. Also include the AUTH_USER_MODEL variable indicating the custom user model setting.py

```python
AUTH_USER_MODEL = 'accounts.User'
```

6. Include the accounts URLconf in your project urls.py:

```python
path('accounts/', include('accounts.urls')),
```

7. Run ``python manage.py migrate`` to create the polls models.

8. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

9. Visit http://127.0.0.1:8000/accounts/ to check the app.
