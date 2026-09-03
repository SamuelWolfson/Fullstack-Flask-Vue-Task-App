from flask_mailman import EmailMessage


def send_reset_email(user, reset_token):
    reset_url = f"http://localhost:5173/reset-password?token={reset_token}"
    msg = EmailMessage(
        subject="Password Reset Request",
        body=(
            f"Hello,\n\n"
            "You requested a password reset. Click the link below to set a new password:\n\n"
            f"{reset_url}\n\n"
            "This link will expire in 15 minutes.\n\n"
            "If you did not request this, please ignore this email."
        ),
        to=[user.email],
    )
    msg.send()