
import os
from pathlib import Path

from dotenv import load_dotenv
from magic_hour import Client

# Load secrets from a local .env file, if one exists.
# In Codespaces, we will use a repository secret instead.
load_dotenv()

API_KEY = os.getenv("MAGIC_HOUR_API_KEY")

OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

PROMPT = """
A cinematic mystery-action scene featuring ZERO, the same
masked vigilante throughout the series.

ZERO wears a matte black hood, a fitted black mask with a
subtle silver detail, black gloves and dark clothing.
His face remains concealed.

At night, ZERO stands in a rain-soaked urban alley.
He slowly turns toward an unseen sound, then takes two
controlled steps forward. The camera pushes in toward his
mask as distant lights flicker in the background.

Photorealistic live-action thriller, realistic human motion,
dramatic blue shadows, subtle red highlights, atmospheric
rain, carefully composed framing, smooth cinematic camera
movement, suspenseful mood.

Vertical portrait composition, subject centered.
No text, subtitles, logos, or watermarks added by the model.
"""

def main():
    if not API_KEY:
        raise SystemExit(
            "Missing MAGIC_HOUR_API_KEY. "
            "Add it to Codespaces Secrets and restart the terminal."
        )

    client = Client(token=API_KEY)

    print("Generating ZERO's first AI video...")
    print("Requested duration: 5 seconds")
    print("Requested format: vertical 9:16")

    try:
        result = client.v1.text_to_video.generate(
            end_seconds=5.0,
            aspect_ratio="9:16",
            style={"prompt": PROMPT},
            name="ZERO - First Contact",
            resolution="720p",
            wait_for_completion=True,
            download_outputs=True,
            download_directory=str(OUTPUT_DIR),
        )

        print("\nGeneration request completed.")
        print("Provider response:", result)
        print("Check the output folder for the generated video.")

    except Exception as exc:
        # Avoid printing environment variables or credentials.
        print(f"\nVideo generation failed: {type(exc).__name__}")
        print("Check your API access, free credits, model limits,")
        print("and the provider's current API documentation.")
        raise SystemExit(1) from None


if __name__ == "__main__":
    main()
  
