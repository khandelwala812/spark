import sys
import flow_analysis as flow

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python analyze_speech.py <audio.wav>")
        sys.exit(1)

    flowdir = r"C:\Voice\flow_analysis"
    filename = sys.argv[1]

    try:
        print(flowdir+"/dataset/wav_files/"+filename)
        with open(flowdir+"/dataset/wav_files/"+filename+".wav", 'r') as file:
            print(f"Found file '{filename}'")
            print("Number of Pauses:", flow.getPauses(filename, flowdir))
            print("Rate of Speech:", flow.getRateOfSpeech(filename, flowdir))
            print("Rate of Articulation:", flow.getRateOfArticulation(filename, flowdir))
            print("Pronunciation Correctness Percentage:", flow.getPronunciationPercentageCorrect(filename, flowdir))




    except FileNotFoundError:
        print(f"Error: Could not find file '{filename}'")
    except Exception as e:
        print(f"An error occurred: {e}")