import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# Sender's email credentials
sender_email = 'Abhi1931480@gmail.com'
sender_password = 'zvhb pohs phcz obxz'

# Email content
subject = 'Looking for Data Engineer Role - Abhishek Tiwari'
body = """
Hi Team,

I hope this message finds you well. I am writing to express my interest in the Data Engineer position. With three years of industry experience in data engineering, I am confident in my ability to contribute effectively to your team and help drive data-driven solutions.

------------------------------------------------------------------------------------------------------------
Professional Highlights:

Cloud Services and Data Warehousing: I have successfully managed various Cloud Services, specializing in AWS and Azure. My proficiency in AWS technologies, including IAM, Lambda, EC2, S3, Glue, RDS, EMR, VPC, Secret Manager, CloudWatch, Lambda, and Amazon Kinesis, along with expertise in Azure services such as Data Factory, Synapse Analytics, Azure SQL, Database Azure, Blob Storage, Data Lake Store, and Data Warehouse, positions me as a versatile data engineer capable of navigating diverse cloud environments.

Programming Expertise: I am adept in multiple programming languages, including Python, Shell Script, and Spark. This proficiency extends to numerical data analysis and AI frameworks such as NumPy and Pandas. My programming skills enable me to develop robust applications for seamless data processing.

Database Management: I excel in working with databases like MySQL and SQL Server, ensuring optimal data storage and retrieval. My experience includes handling SQL, CSV, and Parquet file formats for diverse data integration needs.

Tool Proficiency: I have honed my skills with essential tools such as Databricks, Tableau, Jenkins, Bitbucket, Jira, and Terraform. This proficiency ensures smooth project execution and successful outcomes in data engineering projects.
---------------------------------------------------------------------------------------------------------

I am enthusiastic about the opportunity to contribute my skills and industry. My commitment to delivering efficient and innovative data solutions aligns with your organization's goals, and I am eager to bring my expertise to your esteemed team.

Thank you for considering my application. I am looking forward to the possibility of discussing how my skills can benefit.

Best Regards,
Abhishek Tiwari
91 8960077051
"""

# Path to your resume file
resume_path = 'path/to/your/resume.pdf'

# List of recipient email addresses
recipients = ['email1@example.com', 'email2@example.com']

def send_email(to_email):
    # Create the MIME object
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = to_email
    message['Subject'] = subject

    # Attach the body to the email
    message.attach(MIMEText(body, 'plain'))

    # Attach the resume as a PDF file
    with open(resume_path, 'rb') as resume_file:
        resume_attachment = MIMEApplication(resume_file.read(), _subtype="pdf")
        resume_attachment.add_header('Content-Disposition', f'attachment; filename={resume_path}')
        message.attach(resume_attachment)

    # Connect to the SMTP server
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, to_email, message.as_string())

if __name__ == "__main__":
    for recipient in recipients:
        send_email(recipient)

print("Emails sent successfully.")
