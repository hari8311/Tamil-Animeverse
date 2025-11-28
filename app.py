from flask import Flask, render_template, send_from_directory, request
import os
from datetime import date

app = Flask(__name__, static_folder='docs/static', template_folder='docs/templates')

# Route for the homepage
@app.route('/')
def home():
    return render_template('Ani_updated.html')

# Route to serve video files
@app.route('/play/<anime>/<episode>')
def play_video(anime, episode):
    video_folder = f'docs/static/video/{anime}'
    return send_from_directory(video_folder, episode)

# Route to render the video playback page
@app.route('/video_player')
def video_player():
    anime = request.args.get('anime')
    episode = request.args.get('episode')
    upload_date = date.today().isoformat()
    return render_template('video_player.html', anime=anime, episode=episode, upload_date=upload_date)

# Route to fetch episodes for a given anime
@app.route('/api/episodes')
def get_episodes():
    anime = request.args.get('anime')
    video_folder = f'docs/static/video/{anime}'

    if not os.path.exists(video_folder):
        print(f"Directory not found: {video_folder}")
        return {"error": "Anime not found"}, 404

    episodes = [f for f in os.listdir(video_folder) if os.path.isfile(os.path.join(video_folder, f))]

    if not episodes:
        print(f"No files found in directory: {video_folder}")
        return {"error": "No episodes available"}, 404

    print(f"Episodes found: {episodes}")
    return {"episodes": episodes}, 200

# Route to search anime
@app.route('/api/search')
def search_anime():
    query = request.args.get('q', '').lower()
    
    # Define your anime library
    anime_library = [
        {"title": "Naruto", "genre": "Action, Adventure", "image": "Naruto.jpg"},
        {"title": "One Piece", "genre": "Action, Adventure", "image": "One piece.jpeg"},
        {"title": "Dragon Ball", "genre": "Action, Martial Arts", "image": "Dragon Ball.jpeg"},
        {"title": "Pokemon", "genre": "Adventure, Fantasy", "image": "Pokemon.jpg"},
        {"title": "AOT", "genre": "Action, Dark Fantasy", "image": "AOT.webp"},
        {"title": "Jujutsu Kaisen", "genre": "Action, Supernatural", "image": "jujutsu kaisen.jpeg"}
    ]
    
    # Filter based on query
    if query:
        filtered = [anime for anime in anime_library 
                   if query in anime['title'].lower() or query in anime['genre'].lower()]
    else:
        filtered = anime_library
    
    return {"results": filtered}, 200

# SEO files: robots.txt and sitemap.xml
@app.route('/robots.txt')
def robots_txt():
    return send_from_directory('.', 'robots.txt')

@app.route('/sitemap.xml')
def sitemap_xml():
    return send_from_directory('.', 'sitemap.xml')

# Google Search Console HTML file verification
@app.route('/googlea891d11fb35a233a.html')
def gsc_verification_file():
    return send_from_directory('.', 'googlea891d11fb35a233a.html')

# Run the app
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))  # Render sets PORT env variable
    app.run(host='0.0.0.0', port=port)