import pyaudio
import wave

# Audio configuration
FORMAT = pyaudio.paInt24     # Use 24-bit resolution
CHANNELS = 1                 # Mono audio (adjust to 2 for stereo)
RATE = 48000                 # Sample rate (48 kHz)
CHUNK = 1024                 # Number of frames per buffer
RECORD_SECONDS = 15          # Total duration of recording
OUTPUT_FILENAME = "Recording.wav"  # Output file name

# Initialize PyAudio
p = pyaudio.PyAudio()

# Open the audio stream for recording
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("Recording...")

frames = []

# Record audio in chunks for the specified duration
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("Finished recording.")

# Stop and close the stream, and terminate PyAudio
stream.stop_stream()
stream.close()
p.terminate()

# Saving the recorded frames as a WAV file
wf = wave.open(OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()
