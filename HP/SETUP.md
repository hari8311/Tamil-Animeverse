# Tamil Animeverse - Full Setup Guide

## 🚀 Quick Start

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Copy Images to Assets
Copy all anime images to `static/assets/`:
```powershell
Copy-Item ..\assets\* .\static\assets\ -Force
```

### Step 3: Replace Flask App
Rename the new enhanced app:
```powershell
Remove-Item app.py
Rename-Item app_new.py app.py
```

### Step 4: Replace HTML Template
```powershell
Remove-Item .\templates\Ani_updated.html
Rename-Item .\templates\Ani_updated_v2.html .\templates\Ani_updated.html
```

### Step 5: Run the App
```bash
python app.py
```

Visit: **http://localhost:5000**

---

## ✨ Features Implemented

### ✅ User Authentication
- **Register** with name, email, password
- **Login** with email/password
- **Logout** functionality
- **User Profile** page showing name, email, wishlist count

### ✅ Wishlist System
- Add/remove anime from personal wishlist
- View all wishlisted anime
- Persistent storage (saved in `users_data.json`)

### ✅ Anime Details Modal
- Click any anime image → slide animation opens
- Shows anime title, genre, description
- Season selector dropdown
- Episode selection (shows available episodes)
- **Video player** for uploaded videos
- Add/Remove from wishlist button

### ✅ Video Player
- Click episode number → video plays
- Supports uploaded videos (MP4, MKV, AVI, WebM, MOV)
- Full controls (play, pause, seek, fullscreen)
- Shows current season/episode info

### ✅ Search Functionality
- Real-time search by anime title
- Search by genre
- Live results update

### ✅ Upload System
Upload videos with this format:

**Using curl:**
```bash
curl -X POST http://localhost:5000/api/upload \
  -F "title=Dragon Ball" \
  -F "season=Season 1" \
  -F "episode=1" \
  -F "video=@dragon-ball-s1e1.mp4"
```

**Result:** Video appears in modal with playable episode

---

## 📁 File Structure

```
HP/
├── app.py                      # Enhanced Flask backend (rename from app_new.py)
├── app_new.py                  # New enhanced version (use this)
├── requirements.txt            # Python dependencies
├── anime_data.json            # Anime database (auto-created)
├── users_data.json            # User accounts & wishlist (auto-created)
├── templates/
│   ├── Ani_updated.html       # Old version (backup)
│   └── Ani_updated_v2.html    # New enhanced version (rename to Ani_updated.html)
├── static/
│   ├── ani.js                 # Particle animation
│   ├── uploads/               # Uploaded videos
│   └── assets/
│       ├── Logo.jpeg
│       ├── Naruto.jpg
│       ├── Dragon Ball.jpeg
│       ├── One piece.jpeg
│       ├── Pokemon.jpg
│       └── AOT.webp
```

---

## 🎯 How to Use

### Uploading a Video

1. **Prepare your video:**
   - Format: MP4, MKV, AVI, WebM, or MOV
   - Example: `dragon-ball-season-1-ep1.mp4`

2. **Upload via curl:**
```bash
curl -X POST http://localhost:5000/api/upload \
  -F "title=Dragon Ball" \
  -F "season=Season 1" \
  -F "episode=1" \
  -F "video=@your-video.mp4"
```

3. **In website:**
   - Click Dragon Ball anime card → Modal opens
   - Select "Season 1" from dropdown
   - Click "Ep 1" → Video plays!

### Registering & Creating Profile

1. Click **"Register"** button
2. Enter: Name, Email, Password
3. Click **"Register"**
4. Profile automatically created!
5. Click profile dropdown to:
   - View profile info
   - See wishlist
   - Logout

### Using Wishlist

1. Click anime image → Modal opens
2. Click **"♡ Add to Wishlist"** button
3. Button changes to **"♥ In Wishlist"**
4. Click profile → **"My Wishlist"** to see all saved anime

### Searching

1. Type in search bar at top
2. Results update in real-time
3. Click any result to open details modal

---

## 📊 API Endpoints

### Authentication
- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - Login user
- `POST /api/auth/logout` - Logout
- `GET /api/auth/profile` - Get current user profile

### Wishlist
- `POST /api/wishlist/add/<anime_id>` - Add to wishlist
- `POST /api/wishlist/remove/<anime_id>` - Remove from wishlist
- `GET /api/wishlist` - Get user's wishlist

### Anime
- `GET /api/anime` - Get all anime
- `GET /api/search?q=dragon` - Search anime
- `GET /api/anime/<id>` - Get anime details
- `GET /api/anime/<id>/seasons` - Get seasons list
- `GET /api/anime/<id>/season/<season_name>` - Get episodes

### Upload
- `POST /api/upload` - Upload video

---

## 🔧 Troubleshooting

### Images not showing?
✅ Copy images to `static/assets/` folder
✅ Ensure filenames match: Logo.jpeg, Naruto.jpg, Dragon Ball.jpeg, etc.

### Videos not playing?
✅ Check video is in `static/uploads/` folder
✅ Upload name format: `dragon-ball-season-1-ep1.mp4`
✅ Use correct video format (MP4, MKV, AVI, WebM, MOV)

### Login not working?
✅ Restart Flask app: `python app.py`
✅ Check `users_data.json` was created

### Search not working?
✅ Type in search box at header
✅ Should filter anime by title or genre

---

## 🚀 Production Deployment

### Using Gunicorn
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

---

## 📝 Notes

- Change `app.secret_key` in production!
- All data stored in JSON files (SQLite recommended for production)
- Max upload: 500MB per file
- Session expires on browser close (use cookies for persistence)

---

**Happy Streaming! 🎬📺**
