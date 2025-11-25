from flask import Flask, render_template, send_from_directory, request
import os

app = Flask(__name__, static_folder='HP/static', template_folder='HP/templates')

# Route for the homepage
@app.route('/')
def home():
    return render_template('Ani_updated.html')

# Route to serve video files
@app.route('/play/<anime>/<episode>')
def play_video(anime, episode):
    video_folder = f'HP/static/video/{anime}'
    return send_from_directory(video_folder, episode)

# Route to render the video playback page
@app.route('/video_player')
def video_player():
    anime = request.args.get('anime')
    episode = request.args.get('episode')
    return render_template('video_player.html', anime=anime, episode=episode)

# Route to fetch episodes for a given anime
@app.route('/api/episodes')
def get_episodes():
    anime = request.args.get('anime')
    video_folder = f'HP/static/video/{anime}'

    if not os.path.exists(video_folder):
        print(f"Directory not found: {video_folder}")
        return {"error": "Anime not found"}, 404

    episodes = [f for f in os.listdir(video_folder) if os.path.isfile(os.path.join(video_folder, f))]

    if not episodes:
        print(f"No files found in directory: {video_folder}")
        return {"error": "No episodes available"}, 404

    print(f"Episodes found: {episodes}")
    return {"episodes": episodes}, 200

# Run the app
if __name__ == '__main__':
    app.run(debug=True)