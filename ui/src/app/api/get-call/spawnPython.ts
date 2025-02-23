import { spawn } from 'child_process';
import { getStartAndEndSegments } from './callParser';
import fs from 'node:fs'
import fetch from 'node-fetch'

function generateRandomString(length) {
    const characters = 'abcdefghijklmnopqrstuvwxyz';
    let randomString = '';

    for (let i = 0; i < length; i++) {
        const randomIndex = Math.floor(Math.random() * characters.length);
        randomString += characters.charAt(randomIndex);
    }

    return randomString;
}


async function downloadWavFile(recordingUrl) {
    if (!recordingUrl) {
        console.error("Error: 'recording_url' property not found in the JSON object.");
        return;
    }
    try {
        const response = await fetch(recordingUrl);

        if (!response.ok) {
            throw new Error(`HTTP error, status: ${response.status}`);
        }

        const arrayBuffer = await response.arrayBuffer();
        const buffer = Buffer.from(arrayBuffer);
        const name = "recording_" + generateRandomString(5)

        fs.writeFileSync(`C:/Users/avikw/Coding/projects/MockInt/ui/scripts/speech analysis/flow_analysis/dataset/wav_files/${name}.wav`, buffer);
        console.log(`Successfully downloaded and saved WAV file: ${name}`);

        return name;
    } catch (error) {
        console.error("Error downloading or saving WAV file:", error);
    }
}

export async function runPythonAnalysis(callObject) {
    const filename = await downloadWavFile(callObject.recording_url);

    return new Promise((resolve, reject) => {
        const pythonProcess = spawn('C:/Users/avikw/anaconda3/python.exe', ['C:/Users/avikw/Coding/projects/MockInt/ui/scripts/speech analysis/analyze_speech.py', filename, JSON.stringify(getStartAndEndSegments(callObject))]);
        const stdoutData = [];

        // Capture stdout
        pythonProcess.stdout.on('data', (data) => {
            stdoutData.push(data.toString()); // Convert Buffer to string and add to array
        });

        // Capture stderr
        pythonProcess.stderr.on('data', (data) => {
            console.error(`stderr: ${data}`); // Log stderr to console, or handle as needed
        });

        // Handle process exit
        pythonProcess.on('close', (code) => {
            if (code === 0) {
                // Process exited successfully
                const combinedOutput = stdoutData.join(''); // Combine all chunks of stdout
                const outputLines = combinedOutput.trim().split('\n'); // Split into lines
                if (outputLines.length === 4) {
                  resolve(outputLines)
                } else {
                    reject(new Error(`Python has catastrophically failed!`));
                }
            } else {
                // Process exited with an error code
                reject(new Error(`Python process exited with code ${code}`));
            }
        });

        // Handle errors during process spawning
        pythonProcess.on('error', (err) => {
            reject(new Error(`Failed to spawn python process: ${err}`));
        });
    });
}
