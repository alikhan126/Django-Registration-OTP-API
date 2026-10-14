# Django-Registration-OTP-API

A Django REST Framework API (2019) for user accounts with phone verification:
registration, email verification, token login, password reset, and phone number
verification with a one-time code sent by SMS through Twilio.

## Endpoints

Endpoints marked 🔒 need the header `Authorization: Token <token>` (get the token from login).

| Method | Endpoint | Body | Notes |
|---|---|---|---|
| POST | `/api/accounts/register/` | `username`, `email`, `password`, `password_2`, `first_name`, `last_name`, `invite_code` (optional) | Creates the user and emails a verification link |
| GET | `/api/accounts/verify/<verification_key>/` | – | Email verification link |
| POST | `/api/accounts/login/` | `email` or `username`, `password` | Returns `{ "token": "<token>" }` |
| POST | `/api/accounts/password_reset/` | `email` | Emails a password-reset link |
| POST | `/api/accounts/reset/<uidb64>/<token>/` | `new_password`, `new_password_2` | Sets the new password |
| GET 🔒 | `/api/accounts/user-profile/` | – | `user` (email, first/last name) + `has_email_verified` |
| POST 🔒 | `/api/verification/send_otp/` | `country_code`, `phone_number` (digits only, e.g. `1`, `5551234567`) | Texts a 6-character code to the number |
| POST 🔒 | `/api/verification/verify_otp/` | `otp` | Marks the phone number verified if the code matches |

## Layout

```
accounts/   users, registration, email verification, login, password reset, profile
otp/        PhoneVerification model + send/verify OTP endpoints (Twilio)
base/       shared model/utils
i2x_demo/   Django project settings and URLs
templates/  email subject/body templates
```

## Running it locally

Written for Python 3.6 and Django 2.1. Uses SQLite by default.

```
pip install -r requirements.txt   # mysqlclient needs MySQL client libs; remove it if you stick with SQLite
python manage.py migrate
python manage.py runserver
```

### Configuration (environment variables)

| Variable | Used for |
|---|---|
| `DJANGO_SECRET_KEY` | Django secret key (falls back to an insecure dev-only value) |
| `TWILIO_ACCOUNT_SID` | Twilio account for sending the OTP SMS |
| `TWILIO_AUTH_TOKEN` | Twilio auth token |
| `TWILIO_FROM_NUMBER` | Your Twilio sending number, e.g. `+15550001111` |

Email settings (`EMAIL_HOST_USER` / `EMAIL_HOST_PASSWORD`) are placeholders in
`i2x_demo/settings.py`. Set real values in a `local_settings.py` (git-ignored, and
loaded automatically if present) to actually send the verification and reset emails.

## Status

Unmaintained demo, kept for reference. Not production-ready: `DEBUG = True`, and
OTPs never expire and have no attempt limit.
