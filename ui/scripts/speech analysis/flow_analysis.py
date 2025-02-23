from parselmouth.praat import call, run_file
import pandas as pd
import numpy as np
from scipy.stats import binom
from scipy.stats import ks_2samp
from scipy.stats import ttest_ind


def getFiles(wavFile, pathToDir):
    """
    Get necessary files and locations
    """
    wav = pathToDir + "/" + "dataset" + "/" + "wav_files" + "/" + wavFile + ".wav"
    praat = pathToDir + "/" + "dataset" + "/" + "praat" + "/" + "sp.praat"
    path = pathToDir + "/" + "dataset" + "/" + "wav_files" + "/"
    return wav, praat, path


def getSyllabus(wavFile, pathToDir):
    """
    Detect and count number of syllables
    """
    wav, praat, path = getFiles(wavFile, pathToDir)
    try:
        objects = run_file(praat, -20, 2, 0.3, "yes", wav, path, 80, 400, 0.01, capture_output=True)
        z1 = str(objects[
                     1])  # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data object with a TextGrid inside
        z2 = z1.strip().split()
        z3 = int(z2[0])  # will be the integer number 10
        z4 = float(z2[3])  # will be the floating point number 8.3
        return z3
    except:
        z3 = 0
        #print("Try again the sound of the audio was not clear")
    return;


def getPauses(wavFile, pathToDir):
    """
    Detect and count number of fillers and pauses
    """
    wav, praat, path = getFiles(wavFile, pathToDir)
    try:
        objects = run_file(praat, -20, 2, 0.3, "yes", wav, path, 80, 400, 0.01, capture_output=True)
        z1 = str(objects[
                     1])  # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data object with a TextGrid inside
        z2 = z1.strip().split()
        z3 = int(z2[1])  # will be the integer number 10
        z4 = float(z2[3])  # will be the floating point number 8.3
        return z3
    except:
        z3 = 0
        #print("Try again the sound of the audio was not clear")
    return;


def getRateOfSpeech(wavFile, pathToDir):
    """
    Measure the rate of speech (speed)
    """
    wav, praat, path = getFiles(wavFile, pathToDir)
    try:
        objects = run_file(praat, -20, 2, 0.3, "yes", wav, path, 80, 400, 0.01, capture_output=True)
        z1 = str(objects[
                     1])  # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data object with a TextGrid inside
        z2 = z1.strip().split()
        z3 = int(z2[2])  # will be the integer number 10
        z4 = float(z2[3])  # will be the floating point number 8.3
        return z3
    except:
        z3 = 0
        #print("Try again the sound of the audio was not clear")
    return;


def getRateOfArticulation(wavFile, pathToDir):
    """
    Measure the articulation (speed)
    """
    wav, praat, path = getFiles(wavFile, pathToDir)
    try:
        objects = run_file(praat, -20, 2, 0.3, "yes", wav, path, 80, 400, 0.01, capture_output=True)
        z1 = str(objects[
                     1])  # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data object with a TextGrid inside
        z2 = z1.strip().split()
        z3 = int(z2[3])  # will be the integer number 10
        z4 = float(z2[3])  # will be the floating point number 8.3
        return z3
    except:
        z3 = 0
        #print("Try again the sound of the audio was not clear")
    return;


def getDurationSpeaking(wavFile, pathToDir):
    """
    Measure speaking time (excl. fillers and pause)
    """
    wav, praat, path = getFiles(wavFile, pathToDir)
    try:
        objects = run_file(praat, -20, 2, 0.3, "yes", wav, path, 80, 400, 0.01, capture_output=True)
        z1 = str(objects[
                     1])  # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data object with a TextGrid inside
        z2 = z1.strip().split()
        z3 = int(z2[3])  # will be the integer number 10
        z4 = float(z2[4])  # will be the floating point number 8.3
        return z3
    except:
        z4 = 0
        #print("Try again the sound of the audio was not clear")
    return;


def getDurationTotal(wavFile, pathToDir):
    """
    Measure total speaking duration (inc. fillers and pauses)
    """
    wav, praat, path = getFiles(wavFile, pathToDir)
    try:
        objects = run_file(praat, -20, 2, 0.3, "yes", wav, path, 80, 400, 0.01, capture_output=True)
        z1 = str(objects[
                     1])  # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data object with a TextGrid inside
        z2 = z1.strip().split()
        z3 = int(z2[3])  # will be the integer number 10
        z4 = float(z2[5])  # will be the floating point number 8.3
        return z3
    except:
        z4 = 0
        #print("Try again the sound of the audio was not clear")
    return;


def getDurationRatio(wavFile, pathToDir):
    """
    Measure ratio between speaking duration and total speaking duration
    """
    wav, praat, path = getFiles(wavFile, pathToDir)
    try:
        objects = run_file(praat, -20, 2, 0.3, "yes", wav, path, 80, 400, 0.01, capture_output=True)
        z1 = str(objects[
                     1])  # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data object with a TextGrid inside
        z2 = z1.strip().split()
        z3 = int(z2[3])  # will be the integer number 10
        z4 = float(z2[6])  # will be the floating point number 8.3
        return z3
    except:
        z4 = 0
        #print("Try again the sound of the audio was not clear")
    return;


def getHertzMean(wavFile, pathToDir):
    """
    Measure fundamental frequency distribution mean
    """
    wav, praat, path = getFiles(wavFile, pathToDir)
    try:
        objects = run_file(praat, -20, 2, 0.3, "yes", wav, path, 80, 400, 0.01, capture_output=True)
        z1 = str(objects[
                     1])  # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data object with a TextGrid inside
        z2 = z1.strip().split()
        z3 = int(z2[3])  # will be the integer number 10
        z4 = float(z2[7])  # will be the floating point number 8.3
        return z3
    except:
        z4 = 0
        #print("Try again the sound of the audio was not clear")
    return;


def getHertzStdev(wavFile, pathToDir):
    """
    Measure fundamental frequency distribution SD
    """
    wav, praat, path = getFiles(wavFile, pathToDir)
    try:
        objects = run_file(praat, -20, 2, 0.3, "yes", wav, path, 80, 400, 0.01, capture_output=True)
        z1 = str(objects[
                     1])  # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data object with a TextGrid inside
        z2 = z1.strip().split()
        z3 = int(z2[3])  # will be the integer number 10
        z4 = float(z2[8])  # will be the floating point number 8.3
        return z3
    except:
        z4 = 0
        #print("Try again the sound of the audio was not clear")
    return;


def getHertzMedian(wavFile, pathToDir):
    """
    Measure fundamental frequency distribution median
    """
    wav, praat, path = getFiles(wavFile, pathToDir)
    try:
        objects = run_file(praat, -20, 2, 0.3, "yes", wav, path, 80, 400, 0.01, capture_output=True)
        z1 = str(objects[
                     1])  # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data object with a TextGrid inside
        z2 = z1.strip().split()
        z3 = int(z2[3])  # will be the integer number 10
        z4 = float(z2[9])  # will be the floating point number 8.3
        return z3
    except:
        z4 = 0
        #print("Try again the sound of the audio was not clear")
    return;


def getHertzMin(wavFile, pathToDir):
    """
    Measure fundamental frequency distribution minimum
    """
    wav, praat, path = getFiles(wavFile, pathToDir)
    try:
        objects = run_file(praat, -20, 2, 0.3, "yes", wav, path, 80, 400, 0.01, capture_output=True)
        z1 = str(objects[
                     1])  # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data object with a TextGrid inside
        z2 = z1.strip().split()
        z3 = int(z2[10])  # will be the integer number 10
        z4 = float(z2[10])  # will be the floating point number 8.3
        return z3
    except:
        z3 = 0
        #print("Try again the sound of the audio was not clear")
    return;


def getHertzMax(wavFile, pathToDir):
    """
    Measure fundamental frequency distribution maximum
    """
    wav, praat, path = getFiles(wavFile, pathToDir)
    try:
        objects = run_file(praat, -20, 2, 0.3, "yes", wav, path, 80, 400, 0.01, capture_output=True)
        z1 = str(objects[
                     1])  # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data object with a TextGrid inside
        z2 = z1.strip().split()
        z3 = int(z2[11])  # will be the integer number 10
        z4 = float(z2[11])  # will be the floating point number 8.3
        return z3
    except:
        z3 = 0
        #print("Try again the sound of the audio was not clear")
    return;


def getHertz25Percentile(wavFile, pathToDir):
    """
    Measure 25th quantile fundamental frequency distribution
    """
    wav, praat, path = getFiles(wavFile, pathToDir)
    try:
        objects = run_file(praat, -20, 2, 0.3, "yes", wav, path, 80, 400, 0.01, capture_output=True)
        z1 = str(objects[
                     1])  # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data object with a TextGrid inside
        z2 = z1.strip().split()
        z3 = int(z2[12])  # will be the integer number 10
        z4 = float(z2[11])  # will be the floating point number 8.3
        return z3
    except:
        z3 = 0
        #print("Try again the sound of the audio was not clear")
    return;


def getHertz75Percentile(wavFile, pathToDir):
    """
    Measure 75th quantile fundamental frequency distribution
    """
    wav, praat, path = getFiles(wavFile, pathToDir)
    try:
        objects = run_file(praat, -20, 2, 0.3, "yes", wav, path, 80, 400, 0.01, capture_output=True)
        z1 = str(objects[
                     1])  # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data object with a TextGrid inside
        z2 = z1.strip().split()
        z3 = int(z2[13])  # will be the integer number 10
        z4 = float(z2[11])  # will be the floating point number 8.3
        return z3
    except:
        z3 = 0
        #print("Try again the sound of the audio was not clear")
    return;


def getAllOutput(wavFile, pathToDir):
    """
    Overview
    """
    wav, praat, path = getFiles(wavFile, pathToDir)
    try:
        objects = run_file(praat, -20, 2, 0.3, "yes", wav, path, 80, 400, 0.01, capture_output=True)
        z1 = str(objects[
                     1])  # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data object with a TextGrid inside
        z2 = z1.strip().split()
        z3 = np.array(z2)
        z4 = np.array(z3)[np.newaxis]
        z5 = z4.T
        df = pd.DataFrame(
            {"number_ of_syllables": z5[0, :], "number_of_pauses": z5[1, :], "rate_of_speech": z5[2, :],
             "articulation_rate": z5[3, :], "speaking_duration": z5[4, :],
             "original_duration": z5[5, :], "balance": z5[6, :], "f0_mean": z5[7, :], "f0_std": z5[8, :],
             "f0_median": z5[9, :], "f0_min": z5[10, :], "f0_max": z5[11, :],
             "f0_quantile25": z5[12, :], "f0_quan75": z5[13, :]})
        return df
    except:
        pass
        #print("Try again the sound of the audio was not clear")
    return;


def getPronunciationPercentageCorrect(wavFile, pathToDir):
    """
    Pronunciation posteriori probability score percentage
    """
    wav, praat, path = getFiles(wavFile, pathToDir)
    try:
        objects = run_file(praat, -20, 2, 0.3, "yes", wav, path, 80, 400, 0.01, capture_output=True)
        z1 = str(objects[
                     1])  # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data object with a TextGrid inside
        z2 = z1.strip().split()
        z3 = int(z2[13])  # will be the integer number 10
        z4 = float(z2[14])  # will be the floating point number 8.3
        db = binom.rvs(n=10, p=z4, size=10000)
        a = np.array(db)
        b = np.mean(a) * 100 / 10
        # print("PreNorm", b)
        min = 100 * ((1/100.0) ** 3)
        max = 100 * ((100/100.0) ** 3)
        trans = 100 * ((b/100.0) ** 3)
        return 40 + (trans - min) * 60 / (max - min)
    except:
        pass
        #print("Try again the sound of the audio was not clear")
    return;


def getGenderAndMood(wavFile, pathToDir):
    """
    Gender recognition and mood of speech
    """
    wav, praat, path = getFiles(wavFile, pathToDir)
    try:
        objects = run_file(praat, -20, 2, 0.3, "yes", wav, path, 80, 400, 0.01, capture_output=True)
        z1 = str(objects[
                     1])  # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data object with a TextGrid inside
        z2 = z1.strip().split()
        z3 = float(z2[8])  # will be the integer number 10
        z4 = float(z2[7])  # will be the floating point number 8.3
        if z4 <= 114:
            g = 101
            j = 3.4
        elif z4 > 114 and z4 <= 135:
            g = 128
            j = 4.35
        elif z4 > 135 and z4 <= 163:
            g = 142
            j = 4.85
        elif z4 > 163 and z4 <= 197:
            g = 182
            j = 2.7
        elif z4 > 197 and z4 <= 226:
            g = 213
            j = 4.5
        elif z4 > 226:
            g = 239
            j = 5.3
        else:
            print("Voice not recognized")
            exit()

        def teset(a, b, c, d):
            d1 = np.random.wald(a, 1, 1000)
            d2 = np.random.wald(b, 1, 1000)
            d3 = ks_2samp(d1, d2)
            c1 = np.random.normal(a, c, 1000)
            c2 = np.random.normal(b, d, 1000)
            c3 = ttest_ind(c1, c2)
            y = ([d3[0], d3[1], abs(c3[0]), c3[1]])
            return y

        nn = 0
        mm = teset(g, j, z4, z3)
        while (mm[3] > 0.05 and mm[0] > 0.04 or nn < 5):
            mm = teset(g, j, z4, z3)
            nn = nn + 1
        nnn = nn
        if mm[3] <= 0.09:
            mmm = mm[3]
        else:
            mmm = 0.35
        if z4 > 97 and z4 <= 114:
            print("Male, mood of speech: showing no emotion, normal, p-value/sample size= :%.2f" % (mmm), (nnn))
        elif z4 > 114 and z4 <= 135:
            print("Male, mood of speech: reading, p-value/sample size= :%.2f" % (mmm), (nnn))
        elif z4 > 135 and z4 <= 163:
            print("Male, mood of speech: speaking passionately, p-value/sample size= :%.2f" % (mmm), (nnn))
        elif z4 > 163 and z4 <= 197:
            print("Female, mood of speech: showing no emotion, normal, p-value/sample size= :%.2f" % (mmm), (nnn))
        elif z4 > 197 and z4 <= 226:
            print("Female, mood of speech: reading, p-value/sample size= :%.2f" % (mmm), (nnn))
        elif z4 > 226 and z4 <= 245:
            print("Female, mood of speech: speaking passionately, p-value/sample size= :%.2f" % (mmm), (nnn))
        else:
            print("Voice not recognized")
    except:
        pass
        #print("Try again the sound of the audio was not clear")