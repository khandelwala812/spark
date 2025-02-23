const { spawn } = require('child_process');

async function runPythonAnalysis(filename) {
    return new Promise((resolve, reject) => {
        const pythonProcess = spawn('C:/Users/Lyc/IdeaProjects/VoiceAnalysis/.venv/Scripts/python.exe', ['../speech analysis/analyze_speech.py', filename]);
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
                resolve(outputLines);
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

async function main() {
    const filename = 'good';

    try {
        const outputLines = await runPythonAnalysis(filename);
        console.log('Python script output:');
        outputLines.forEach(line => {
            console.log(line);
        });
    } catch (error) {
        console.error('Error running Python analysis:', error.message);
    }
}

main();