# ARVisio AI

ARVisio AI is an advanced tool designed to transform video content into immersive AR (Augmented Reality) experiences. This project utilizes the NVIDIA Omniverse SDK to process video files, generating realistic 3D models and AR elements based on the video content. Users can upload their video files through a web interface, and the AI will generate the AR content and send a link to the user's email address.


├── app.py
├── omniverse_processing.py
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
├── templates/
│   └── index.html


## Features

- **Automated Content Generation**: Utilizes AI to generate realistic 3D models, textures, and environments for AR/VR experiences.
- **Performance Optimization**: Optimizes AR/VR applications for better performance and user experience using AI-driven analytics.
- **Personalized User Experiences**: Implements AI to create personalized AR/VR experiences based on user preferences and behavior.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Flask
- NVIDIA Omniverse SDK
- dotenv

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/arvisio-ai.git
    cd arvisio-ai
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  
    ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    Create a `.env` file in the root directory and add the following:
    ```env
    EMAIL_USER=your-email@example.com
    EMAIL_PASS=your-email-password
    SMTP_SERVER=smtp.example.com
    SMTP_PORT=587
    ```

### Usage

1. **Run the Flask application**:
    ```bash
    python app.py
    ```

2. **Access the web interface**:
    Open your browser and go to `http://127.0.0.1:5000`.

3. **Upload a video file**:
    - Select a video file from your local machine.
    - Enter your email address.
    - Click the "Upload and Generate AR Content" button.

4. **Receive the AR content**:
    - The AI will process the video and generate AR content.
    - You will receive an email with a link to the AR content.




