
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory store to mirror the ACEest Fitness 'workouts' concept
workouts = []

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/workouts")
def get_workouts():
    return jsonify(workouts)

@app.post("/workouts")
def add_workout():
    data = request.get_json(silent=True) or {}
    workout = (data.get("workout") or "").strip()
    duration = data.get("duration")

    if not workout or duration is None:
        return jsonify({"error": "workout and duration required"}), 400

    try:
        duration = int(duration)
    except (ValueError, TypeError):
        return jsonify({"error": "duration must be an integer"}), 400

    if duration <= 0:
        return jsonify({"error": "duration must be positive"}), 400

    entry = {"workout": workout, "duration": duration}
    workouts.append(entry)
    return jsonify({"message": "added", "entry": entry}), 201

if __name__ == "__main__":
    # For local runs (not production)
    app.run(host="0.0.0.0", port=5000, debug=True)
