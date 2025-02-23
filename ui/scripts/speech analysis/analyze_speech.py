import json
import os
import sys
import wave

from scipy.signal import resample_poly

import flow_analysis as flow
from pydub import AudioSegment

import numpy as np


# def resample_wav(input_filepath, output_filepath, target_rate=48000):
#     """
#     Resamples a WAV file from 24kHz to 48kHz (or to a specified target rate).
#
#     Args:
#         input_filepath (str): Path to the input WAV file (24kHz).
#         output_filepath (str): Path to save the resampled WAV file (48kHz or target_rate).
#         target_rate (int, optional): The target sampling rate in Hz. Defaults to 48000 (48kHz).
#
#     Returns:
#         bool: True if resampling and saving were successful, False otherwise.
#     """
#     try:
#         # Open the input WAV file
#         with wave.open(input_filepath, 'rb') as wav_in:
#             # Get parameters of the input WAV file
#             frame_rate_in = wav_in.getframerate()
#             num_channels = wav_in.getnchannels()
#             sample_width = wav_in.getsampwidth()
#             num_frames_in = wav_in.getnframes()
#
#             # Read audio data as bytes
#             audio_data_bytes = wav_in.readframes(num_frames_in)
#
#             # Convert byte data to a NumPy array
#             audio_array_in = np.frombuffer(audio_data_bytes, dtype=np.int16) # Assuming 16-bit WAV
#             if sample_width == 1:
#                 audio_array_in = np.frombuffer(audio_data_bytes, dtype=np.int8)
#             elif sample_width == 2:
#                 audio_array_in = np.frombuffer(audio_data_bytes, dtype=np.int16)
#             elif sample_width == 4:
#                 audio_array_in = np.frombuffer(audio_data_bytes, dtype=np.int32)
#             else:
#                 raise ValueError(f"Unsupported sample width: {sample_width} bytes")
#
#             # Reshape to (num_frames, num_channels) if multi-channel
#             if num_channels > 1:
#                 audio_array_in = audio_array_in.reshape(-1, num_channels)
#
#             # Calculate resampling ratio
#             if frame_rate_in == 0:
#                 print("Warning: Input WAV file has invalid frame rate (0 Hz). Assuming 24kHz for resampling.")
#                 frame_rate_in = 24000 # Assume 24kHz if invalid rate.
#             resample_ratio = target_rate / frame_rate_in
#
#             # Resample using scipy.signal.resample_poly (polyphase resampling for better quality)
#             if resample_ratio != 1.0: # Only resample if rates are different
#                 if resample_ratio > 1.0:
#                     up_factor = int(resample_ratio * 100) # Use integers for up and down factors
#                     down_factor = 100
#                 else:
#                     up_factor = 100
#                     down_factor = int((1/resample_ratio) * 100)
#
#                 if num_channels > 1: # Resample each channel independently if multi-channel
#                     audio_array_out = np.zeros((int(len(audio_array_in) * resample_ratio), num_channels), dtype=audio_array_in.dtype)
#                     for channel in range(num_channels):
#                         audio_array_out[:, channel] = resample_poly(audio_array_in[:, channel], up=up_factor, down=down_factor)
#                 else:
#                     audio_array_out = resample_poly(audio_array_in, up=up_factor, down=down_factor)
#             else:
#                 audio_array_out = audio_array_in # No resampling needed
#
#
#             # Convert the resampled NumPy array back to bytes
#             if sample_width == 1:
#                 audio_data_out_bytes = (audio_array_out.astype(np.int8)).tobytes()
#             elif sample_width == 2:
#                 audio_data_out_bytes = (audio_array_out.astype(np.int16)).tobytes()
#             elif sample_width == 4:
#                 audio_data_out_bytes = (audio_array_out.astype(np.int32)).tobytes()
#             else:
#                 raise ValueError(f"Unsupported sample width: {sample_width} bytes (after resampling)")
#
#
#             # Open the output WAV file for writing
#             with wave.open(output_filepath, 'wb') as wav_out:
#                 # Set parameters for the output WAV file
#                 wav_out.setnchannels(num_channels)
#                 wav_out.setsampwidth(sample_width)
#                 wav_out.setframerate(target_rate)
#                 wav_out.setnframes(len(audio_array_out) if num_channels == 1 else len(audio_array_out) // num_channels) # Correct frame count
#                 wav_out.setcomptype('NONE', 'not compressed')
#
#                 # Write the resampled audio data to the output WAV file
#                 wav_out.writeframes(audio_data_out_bytes)
#
#         return True
#
#     except FileNotFoundError:
#         print(f"Error: Input file not found: {input_filepath}")
#         return False
#     except wave.Error as e:
#         print(f"Error processing WAV file: {e}")
#         return False
#     except ValueError as ve:
#         print(f"ValueError: {ve}")
#         return False
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")
#         return False
#
# def segment_wav_file(input_wav_path, output_wav_path, segments):
#     try:
#         audio = AudioSegment.from_wav(input_wav_path)
#         combined_segment = AudioSegment.empty()
#
#         for start_time, end_time in segments:
#             start_ms = int(start_time * 1000)
#             end_ms = int(end_time * 1000)
#             segment = audio[start_ms:end_ms]
#
#             combined_segment += segment
#
#         combined_segment.export(
#             output_wav_path,
#             format="wav"
#         )
#         print(f"Segmented audio saved to: {output_wav_path}")
#
#     except FileNotFoundError:
#         print(f"Error: Input WAV file not found at '{input_wav_path}'")
#     except Exception as e:
#         print(f"An error occurred during segmentation: {e}")

def str_to_tuple_array(input_str):
    try:
        list_of_lists = json.loads(input_str)
        tuple_array = [tuple(inner_list) for inner_list in list_of_lists]
        return tuple_array
    except json.JSONDecodeError:
        print("Error: Invalid JSON string input")
        return False

def resample_wav(input_filepath, output_filepath, target_rate=48000):
    try:
        with wave.open(input_filepath, 'rb') as wav_in:
            frame_rate_in = wav_in.getframerate()
            num_channels = wav_in.getnchannels()
            sample_width = wav_in.getsampwidth()
            num_frames_in = wav_in.getnframes()
            audio_data_bytes = wav_in.readframes(num_frames_in)

            if sample_width == 1:
                audio_array_in = np.frombuffer(audio_data_bytes, dtype=np.int8)
            elif sample_width == 2:
                audio_array_in = np.frombuffer(audio_data_bytes, dtype=np.int16)
            elif sample_width == 4:
                audio_array_in = np.frombuffer(audio_data_bytes, dtype=np.int32)
            else:
                raise ValueError(f"Unsupported sample width: {sample_width} bytes")

            if num_channels > 1:
                audio_array_in = audio_array_in.reshape(-1, num_channels)

            if frame_rate_in == 0:
                print("Warning: Input WAV file has invalid frame rate (0 Hz). Assuming 24kHz for resampling.")
                frame_rate_in = 24000
            resample_ratio = target_rate / frame_rate_in

            if resample_ratio != 1.0:
                if resample_ratio > 1.0:
                    up_factor = int(resample_ratio * 100)
                    down_factor = 100
                else:
                    up_factor = 100
                    down_factor = int((1/resample_ratio) * 100)

                if num_channels > 1:
                    audio_array_out = np.zeros((int(len(audio_array_in) * resample_ratio), num_channels), dtype=audio_array_in.dtype)
                    for channel in range(num_channels):
                        audio_array_out[:, channel] = resample_poly(audio_array_in[:, channel], up=up_factor, down=down_factor)
                else:
                    audio_array_out = resample_poly(audio_array_in, up=up_factor, down=down_factor)
            else:
                audio_array_out = audio_array_in

            if sample_width == 1:
                audio_data_out_bytes = (audio_array_out.astype(np.int8)).tobytes()
            elif sample_width == 2:
                audio_data_out_bytes = (audio_array_out.astype(np.int16)).tobytes()
            elif sample_width == 4:
                audio_data_out_bytes = (audio_array_out.astype(np.int32)).tobytes()
            else:
                raise ValueError(f"Unsupported sample width: {sample_width} bytes (after resampling)")

            with wave.open(output_filepath, 'wb') as wav_out:
                wav_out.setnchannels(num_channels)
                wav_out.setsampwidth(sample_width)
                wav_out.setframerate(target_rate)
                wav_out.setnframes(len(audio_array_out) if num_channels == 1 else len(audio_array_out) // num_channels)
                wav_out.setcomptype('NONE', 'not compressed')
                wav_out.writeframes(audio_data_out_bytes)

        return True

    except FileNotFoundError:
        print(f"Error: Input file not found: {input_filepath}")
        return False
    except wave.Error as e:
        print(f"Error processing WAV file: {e}")
        return False
    except ValueError as ve:
        print(f"ValueError: {ve}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False


def segment_wav_file_numpy(input_wav_path, output_wav_path, segments):
    try:
        with wave.open(input_wav_path, 'rb') as wav_in:
            frame_rate = wav_in.getframerate()
            num_channels = wav_in.getnchannels()
            sample_width = wav_in.getsampwidth()
            num_frames = wav_in.getnframes()
            audio_data_bytes = wav_in.readframes(num_frames)

            if sample_width == 1:
                audio_array = np.frombuffer(audio_data_bytes, dtype=np.int8)
            elif sample_width == 2:
                audio_array = np.frombuffer(audio_data_bytes, dtype=np.int16)
            elif sample_width == 4:
                audio_array = np.frombuffer(audio_data_bytes, dtype=np.int32)
            else:
                raise ValueError(f"Unsupported sample width: {sample_width} bytes")

            if num_channels > 1:
                audio_array = audio_array.reshape(-1, num_channels)

            combined_segment_array = np.array([], dtype=audio_array.dtype)

            for start_time, end_time in segments:
                start_frame = int(start_time * frame_rate)
                end_frame = int(end_time * frame_rate)
                segment = audio_array[start_frame:end_frame]
                combined_segment_array = np.concatenate((combined_segment_array, segment))

            combined_segment_bytes = combined_segment_array.tobytes()

        with wave.open(output_wav_path, 'wb') as wav_out:
            wav_out.setnchannels(num_channels)
            wav_out.setsampwidth(sample_width)
            wav_out.setframerate(frame_rate)
            wav_out.setnframes(len(combined_segment_array) // num_channels if num_channels > 1 else len(combined_segment_array))
            wav_out.setcomptype('NONE', 'not compressed')
            wav_out.writeframes(combined_segment_bytes)

        # print(f"Segmented audio saved to: {output_wav_path}")

    except FileNotFoundError:
        print(f"Error: Input WAV file not found at '{input_wav_path}'")
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except wave.Error as e:
        print(f"Error processing WAV file: {e}")
    except Exception as e:
        print(f"An error occurred during segmentation: {e}")


def resample_and_segment_wav(input_24k_wav_path, output_48k_segmented_wav_path, segments, temp_48k_wav_path="temp_48kHz.wav"):
    try:
        # 1. Resample to 48kHz to a temporary file
        if not resample_wav(input_24k_wav_path, temp_48k_wav_path, target_rate=48000):
            print("Resampling failed. Segmentation aborted.")
            return False

        # 2. Segment the resampled 48kHz file
        segment_wav_file_numpy(temp_48k_wav_path, output_48k_segmented_wav_path, segments)

        # 3. Remove the temporary 48kHz file
        os.remove(temp_48k_wav_path)
        # print(f"Temporary resampled file '{temp_48k_wav_path}' removed.")

        return True

    except Exception as e:
        print(f"Error in resample_and_segment_wav: {e}")
        return False


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python analyze_speech.py <audio.wav> <segments>")
        sys.exit(1)

    flowdir = os.path.dirname(os.path.realpath(__file__)) + "/flow_analysis"
    filename = sys.argv[1]
    segments = str_to_tuple_array(sys.argv[2])

    # print("WAV File:", filename)
    # print("Segments:", segments)
    resample_and_segment_wav(flowdir+"/dataset/wav_files/"+filename+".wav", flowdir+"/dataset/wav_files/"+filename+"_segmented.wav", segments)

    try:
        with open(flowdir+"/dataset/wav_files/"+filename+"_segmented.wav", 'r') as file:
            # print(f"Found file '{filename}'")
            print(flow.getPauses(filename+"_segmented", flowdir))
            print(flow.getRateOfSpeech(filename+"_segmented", flowdir))
            print(flow.getRateOfArticulation(filename+"_segmented", flowdir))
            print(round(flow.getPronunciationPercentageCorrect(filename+"_segmented", flowdir)))

    except FileNotFoundError:
        print(f"Error: Could not find file '{filename}'")
    except Exception as e:
        print(f"An error occurred: {e}")