
# Automated Job Application Email Sender

This Python script automates the process of sending job application emails with your resume attached. It uses the `smtplib` library to connect to Gmail's SMTP server and sends personalized emails to a list of recipients. The email includes a cover letter and attaches your resume in PDF format.

## Features

- Sends job application emails to multiple recipients in one go.
- Automatically attaches your resume to each email.
- Customizes each email with your message expressing interest in a Data Engineer role.
- Secure email login with TLS encryption to protect your credentials.

## Prerequisites

- **Python 3.6+**
- Required Libraries:
  - `smtplib`
  - `email` (MIME components: `MIMEText`, `MIMEMultipart`, `MIMEApplication`)

## How to Use

1. Clone or download the repository.
2. Install the necessary Python libraries if not already installed.
3. Update the `sender_email`, `sender_password`, `resume_path`, and `attachment_name` fields in the script.
4. Modify the list of recipients as needed.
5. Run the script to send emails to all recipients with your cover letter and attached resume.

## Instructions

1. **Email Subject & Body**: 
   - The email subject and body content are predefined in the script, expressing your interest in Data Engineering roles.
   
2. **Resume Attachment**: 
   - Ensure your resume is available at the specified file path (`resume_path`). The script will send this file as a PDF attachment.

3. **Running the Script**: 
   - Run the script in your terminal or Python environment:  
     ```bash
     python send_email.py
     ```

4. **Security**: 
   - Use an app-specific password from Gmail for secure login. Do **NOT** hardcode your Gmail password directly.

## Important Notes

- The script uses Gmail's SMTP server for sending emails, but can be modified to work with other email services.
- Gmail might block the sign-in attempt if you're using a less secure method, so ensure you've enabled app-specific passwords in your Google Account settings.
  
## Disclaimer

Use this script responsibly, and ensure you have consent to send emails to all listed recipients. Misuse of email services could result in your account being temporarily blocked or flagged.
