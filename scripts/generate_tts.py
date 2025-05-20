import os
import requests
from pathlib import Path

def ensure_dir(directory):
    """Ensure directory exists, create if it doesn't."""
    Path(directory).mkdir(parents=True, exist_ok=True)

def generate_tts(text, output_path, server_url="http://localhost:5002"):
    """Generate TTS audio for given text using the TTS server API."""
    try:
        # Make request to TTS server
        response = requests.get(
            f"{server_url}/api/tts",
            params={"text": text}
        )
        
        # Check if request was successful
        if response.status_code == 200:
            # Save the audio file
            with open(output_path, 'wb') as f:
                f.write(response.content)
            print(f"Successfully generated audio for: {text}")
            return True
        else:
            print(f"Failed to generate audio for: {text}")
            print(f"Status code: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"Error generating audio for {text}: {str(e)}")
        return False

def process_text_list(text_list, output_dir="output/ja"):
    """Process a list of texts and generate TTS audio files."""
    # Ensure output directory exists
    ensure_dir(output_dir)
    
    # Process each text
    for i, text in enumerate(text_list):
        # Create filename from text (truncate if too long)
        safe_text = "".join(c for c in text if c.isalnum() or c in (' ', '-', '_'))[:50]
        output_path = os.path.join(output_dir, f"{i+1:03d}_{safe_text}.wav")
        
        # Generate TTS audio
        generate_tts(text, output_path)

def main():
    # Example text list - replace with your actual text list
    text_list = [
        "こんにちは",
        "おはようございます",
        "さようなら",
        "ありがとうございます"
    ]
    
    # Process the text list
    process_text_list(text_list)

if __name__ == "__main__":
    main() 