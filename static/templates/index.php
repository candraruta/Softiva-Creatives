<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ARVisio - Upload Video</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <form id="upload-form" action="/upload" method="post" enctype="multipart/form-data" style="max-width: 500px; margin: auto; padding: 20px; border: 1px solid #ccc; border-radius: 10px; background-color: #f9f9f9;">
        <label for="file-upload" class="custom-file-upload" style="display: block; margin-bottom: 10px; font-weight: bold; font-size: 16px; color: #333;">
            Select Video File
        </label>
        <input id="file-upload" type="file" name="video" accept="video/*" required style="display: block; width: 100%; padding: 10px; margin-bottom: 20px; border: 1px solid #ccc; border-radius: 5px;">
      
        <label for="email" style="display: block; margin-bottom: 10px; font-weight: bold; font-size: 16px; color: #333;">Your Email (to receive the AR content link):</label>
        <input type="email" id="email" name="email" placeholder="Enter your email" required style="display: block; width: 100%; padding: 10px; margin-bottom: 20px; border: 1px solid #ccc; border-radius: 5px;">
      
        <button type="submit" style="display: block; width: 100%; padding: 10px; background-color: #4CAF50; color: white; font-size: 16px; border: none; border-radius: 5px; cursor: pointer;">
            Upload and Generate AR Content
        </button>
    </form>

    <script src="{{ url_for('static', filename='js/script.js') }}"></script>
</body>
</html>
