export function getFillerWordsWithTimestamp(call) {
  const transcriptObject = call.transcript_object;
  const stored = new Map();
  const expletive = /\b(u+m+|u+h+|e+r+|a+h+|like|so|well|actually|basically|just)\b/gi;

  if (!transcriptObject || !Array.isArray(transcriptObject)) {
      console.log("Missing transcript_object");
      return;
  }

  for (const item of transcriptObject) {
      if (item.role === 'user') {
          if (item.words) {
              for (const word of item.words) {
                  if (word.word.match(expletive)) {
                      if (stored.has(word)) stored.set(word.word, stored.get(word.word).push(word.start));
                      else stored.set(word.word, [word.start])
                  }
              }
          } else {
              console.log("Words array missing from user object '" + item + "'");
          }
      }
  }

  console.log("Node Fillers: " + stored);
  return stored;
}

export function getStartAndEndSegments(call) {
  const transcriptObject = call.transcript_object;
  const segments = []
  for (const item of transcriptObject) {
      if (item.role === 'user') {
          if (item.words) {
              const seg = [(item.words[0].start), (item.words[item.words.length - 1].end)];
              segments.push(seg);
          }
      }
  }

  console.log("Node Segments: " + segments)
  return segments;
}
