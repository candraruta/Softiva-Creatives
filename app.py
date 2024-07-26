from flask import Flask, request, redirect, url_for, send_from_directory
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mov'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'video' not in request.files:
        return redirect(request.url)
    file = request.files['video']
    if file.filename == '':
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # Process the video with Omniverse
        process_video_with_omniverse(os.path.join(app.config['UPLOAD_FOLDER'], filename), request.form['email'])
        return 'Video uploaded and processing started. You will receive an email with the AR content link.'

def process_video_with_omniverse(filepath, email):
    import omni
    from omni.kit.app import get_app_interface
    from omni.isaac.kit import SimulationApp
    
    # Initialize Omniverse Simulation App
    simulation_app = SimulationApp({"headless": True})
    
    # Load the video into Omniverse
    video_node = omni.usd.get_stage().DefinePrim(f"/World/VideoNode", "Xform")
    video_node.GetAttribute("videoFile").Set(filepath)
    
    # Process the video to generate AR content
    # This would involve your specific logic for transforming the video into AR content
    
    # Save the AR content
    ar_content_path = "path/to/generated/ar/content"
    # Save your AR content to this path
    
    simulation_app.close()
    
    # Send email with AR content link
    ar_content_url = f"http://example.com/{ar_content_path}"
    send_email(email, ar_content_url)


def send_email(to_email, ar_content_url):
    from_email = "your-email@example.com"
    from_password = "your-email-password"
    
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = "Your Generated AR Content"
    
    body = f"Hello,\n\nYour AR content has been generated. You can view it here: {ar_content_url}\n\nBest regards,\nARVisio Team"
    msg.attach(MIMEText(body, 'plain'))
    
    server = smtplib.SMTP('smtp.example.com', 587)
    server.starttls()
    server.login(from_email, from_password)
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()

if __name__ == '__main__':
    app.run(debug=True)
