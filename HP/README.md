# Tamil Animeverse - Flask Backend

A Flask-based anime streaming platform with dynamic search, video upload, and episode management for Tamil anime dubs.

## Features ✨

- 🔍 **Dynamic Search**: Real-time search across anime titles and genres
- ⬆️ **Video Upload**: Upload MP4/MKV/AVI/WebM video files with season/episode metadata
- 📺 **Episode Management**: Organize episodes by season
- 💾 **Persistent Storage**: JSON-based data persistence
- 🎨 **Beautiful UI**: Animated particle background with smooth transitions
- 📱 **Responsive Design**: Mobile-friendly layout

## Project Structure

```
HP/
├── app.py                    # Flask backend with all routes
├── requirements.txt          # Python dependencies
├── anime_data.json          # Anime data storage (auto-created)
├── templates/
│   └── Ani_updated.html     # Main HTML template
├── static/
│   ├── Logo.jpeg            # Favicon and branding
│   ├── ani.js              # Particle animation + search
│   ├── *.jpg, *.jpeg, etc.  # Anime cover images
│   └── uploads/            # Uploaded video files
```

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Copy Anime Images to Assets Folder

Copy all anime cover images from `../assets/` to `static/assets/`:

**On Windows (PowerShell):**
```powershell
Copy-Item ..\assets\*.{jpg,jpeg,webp,png} .\static\assets\ -Force
```

**On Mac/Linux:**
```bash
cp ../assets/* ./static/assets/
```

**Or manually copy these files:**
- `Logo.jpeg`
- `Naruto.jpg`
- `Dragon Ball.jpeg`
- `One piece.jpeg`
- `Pokemon.jpg`
- `AOT.webp`

### 3. Run the Flask App

```bash
python app.py
```

The server will start at `http://localhost:5000`

## API Endpoints

### 🔍 Search Anime
```
GET /api/search?q=dragon
```
Returns anime matching the query.

### 📺 Get All Anime
```
GET /api/anime
```
Returns complete list with seasons/episodes.

### ▶️ Get Anime Details
```
GET /api/anime/<id>
```
Returns specific anime with all seasons/episodes.

### 📊 Get Episodes for Season
```
GET /api/anime/<id>/season/<season_name>
```
Returns episodes for a specific season.

### ⬆️ Upload Video
```
POST /api/upload
Content-Type: multipart/form-data

Form data:
- title: "Dragon Ball" (required)
- season: "Season 1" (required)
- episode: "1" (required)
- video: <file> (required - mp4/mkv/avi/webm/mov)
```

**Example with curl:**
```bash
curl -X POST http://localhost:5000/api/upload \
  -F "title=Dragon Ball" \
  -F "season=Season 1" \
  -F "episode=3" \
  -F "video=@episode.mp4"
```

### ❌ Delete Episode
```
DELETE /api/anime/<id>/episode/<season>/<episode_num>
```

## File Upload Example (HTML Form)

```html
<form id="uploadForm">
  <input type="text" name="title" placeholder="Anime Title" required>
  <input type="text" name="season" placeholder="Season 1" required>
  <input type="number" name="episode" placeholder="1" required>
  <input type="file" name="video" accept=".mp4,.mkv,.avi,.webm,.mov" required>
  <button type="submit">Upload</button>
</form>

<script>
document.getElementById('uploadForm').addEventListener('submit', async (e) => {
  e.preventDefault();
  const formData = new FormData(e.target);
  const response = await fetch('/api/upload', { method: 'POST', body: formData });
  const data = await response.json();
  console.log(data.message);
});
</script>
```

## Data Structure

Each anime object contains:
```json
{
  "id": 1,
  "title": "Dragon Ball",
  "genre": "Action, Adventure, Fantasy",
  "image": "Dragon Ball.jpeg",
  "seasons": {
    "Season 1": [
      {"episode": 1, "file": "dragon-ball-s1e1.mp4"},
      {"episode": 2, "file": "dragon-ball-s1e2.mp4"}
    ],
    "Season 2": [...]
  }
}
```

## Configuration

Edit `app.py` to customize:

- **Max file size**: Line 14 - `app.config['MAX_CONTENT_LENGTH']`
- **Allowed formats**: Line 15 - `app.config['ALLOWED_EXTENSIONS']`
- **Upload folder**: Line 13 - `app.config['UPLOAD_FOLDER']`
- **Port**: Line 209 - `app.run(debug=True, host='0.0.0.0', port=5000)`

## Database

Data persists in `anime_data.json`. To reset:
1. Delete `anime_data.json`
2. Restart the app (it will recreate with default data)

## Deployment

### Using Gunicorn (Production)

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Using Docker

```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
```

## Troubleshooting

**Import errors?** Install Flask and Werkzeug:
```bash
pip install Flask Werkzeug
```

**Files not found?** Make sure anime images are in `static/` folder and properly named.

**Upload failing?** Check file size (max 500MB) and format (mp4/mkv/avi/webm/mov).

## License

Tamil Animeverse © 2025

---

Happy streaming! 🎬📺
