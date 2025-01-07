import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageFilter
import cv2
import librosa
import librosa.display
import scipy.signal
import soundfile as sf

# Part 1: Image Data Processing
def load_image(file_path):
    # Load and display an image
    img = Image.open(file_path)
    img.show(title="Main Image")
    return img

def resize_image(img, size=(200, 200)):
    # Resize the image
    resized_img = img.resize(size)
    resized_img.show(title="Resized Image")
    
    return resized_img

# The "L" mode stands for 8-bit pixels, black and white.
def grayscale_image(img):
    # Convert the image to grayscale
    gray_img = img.convert("L")
    gray_img.show(title="Grayscale Image")
    return gray_img

def apply_gaussian_blur(img, radius=2):
    # Apply Gaussian Blur to the image
    blurred_img = img.filter(ImageFilter.GaussianBlur(radius))
    blurred_img.show(title="Gaussian Blur Image")
    return blurred_img

# This function converts the image to a NumPy array and applies cv2.Canny() for edge detection. The Canny edge detection algorithm detects areas where pixel intensity changes sharply. Edge detection is useful for identifying objects, boundaries, and shapes in an image, especially for object recognition or analysis tasks.
def edge_detection(img):
    # Apply edge detection to the image
    img_cv = np.array(img)
    edges = cv2.Canny(img_cv, 100, 200)
    plt.imshow(edges, cmap='gray')
    plt.title("Edge Detection")
    plt.show()
    return edges

# This function calculates and plots the histogram for each of the RGB channels (blue, green, red) calcHist().Histograms help analyze the distribution of pixel intensities in an image. This is useful for adjusting brightness, contrast, and understanding image properties.
def histogram_analysis(img):
    # Display histogram for different color channels.
    img_array = np.array(img)
    color = ('b', 'g', 'r')
    for i, col in enumerate(color):
        hist = cv2.calcHist([img_array], [i], None, [256], [0, 256])
        plt.plot(hist, color=col)
        plt.xlim([0, 256])
    plt.title("Histogram Analysis")
    plt.show()

# Part 2: Audio Data Processing
def load_audio(file_path):
    # Load and display the waveform of an audio file
    audio, sr = librosa.load(file_path, sr=None)
    plt.figure(figsize=(10, 4))
    librosa.display.waveshow(audio, sr=sr)
    plt.title("Audio Waveform")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.show()
    return audio, sr


    # Change playback speed of the audio
    # Correct call to time_stretch
    return librosa.effects.time_stretch(audio, rate)
def change_playback_speed(audio, rate=1.5):
    # Change playback speed of the audio using resampling
    # Use scipy to resample the audio
    new_length = int(len(audio) / rate)
    sped_up_audio = scipy.signal.resample(audio, new_length)
    return sped_up_audio

def apply_reverb(audio, sr, reverb_amount=0.3):
    # Apply a reverb effect to the audio
    reverb = audio + reverb_amount * np.roll(audio, sr // 2)
    return reverb

def trim_audio(audio, start_time, end_time, sr):
    # Trim the audio between start_time and end_time
    start_sample = int(start_time * sr)
    end_sample = int(end_time * sr)
    trimmed_audio = audio[start_sample:end_sample]
    return trimmed_audio

def add_noise(audio, noise_factor=0.02):
    # Add white noise to the audio
    noise = noise_factor * np.random.randn(len(audio))
    noisy_audio = audio + noise
    return noisy_audio

def spectral_analysis(audio, sr):
    # Display the spectrogram of the audio
    plt.figure(figsize=(10, 4))
    D = librosa.amplitude_to_db(np.abs(librosa.stft(audio)), ref=np.max)
    # Converts the amplitude (magnitude) of the STFT to decibels (dB), 
    # Computes the Short-Time Fourier Transform (STFT) of the audio signal. STFT splits the audio into overlapping segments and transforms each segment into the frequency domain. 
    librosa.display.specshow(D, sr=sr, x_axis='time', y_axis='log')
    plt.colorbar(format='%+2.0f dB')
    plt.title("Spectrogram")
    plt.show()

# Testing the functions
if __name__ == "__main__":
    # Image Processing
    img_file_path = 'Image.jpg'  # Replace with actual image path
    img = load_image(img_file_path)
    resized_img = resize_image(img)
    gray_img = grayscale_image(img)
    blurred_img = apply_gaussian_blur(img)
    edges = edge_detection(img)
    histogram_analysis(img)

    # Audio Processing
    audio_file_path = 'audio.mp3'  # Replace with actual audio path
    audio, sr = load_audio(audio_file_path)
    sped_up_audio = change_playback_speed(audio, rate=1.5)
    reverb_audio = apply_reverb(audio, sr)
    trimmed_audio = trim_audio(audio, start_time=5, end_time=15, sr=sr)
    noisy_audio = add_noise(audio)
    spectral_analysis(audio, sr)

    # Save processed audio files (optional)
    sf.write('sped_up_audio.wav', sped_up_audio, sr)
    sf.write('reverb_audio.wav', reverb_audio, sr)
    sf.write('trimmed_audio.wav', trimmed_audio, sr)
    sf.write('noisy_audio.wav', noisy_audio, sr)
