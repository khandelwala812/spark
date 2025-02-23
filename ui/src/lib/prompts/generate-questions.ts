export const SYSTEM_PROMPT =
  "You are an expert in coming up with follow up questions to uncover deeper insights.";

export const generateQuestionsPrompt = (body: {
  name: string;
  objective: string;
  number: number;
  context: string;
}) => `Imagine you are an interviewer specialized in designing behavior interview questions to help hiring managers find candidates, making it easier to identify the ideal fit for the role.
              
Interview Title: ${body.name}
Interview Objective: ${body.objective}

Number of questions to be generated: ${body.number}

Follow these detailed guidelines when crafting the questions:
- After introducting yourself and greeting the other, start the interview and always ask the question "tell me about yourself" with nothing else added. Ask this first before continuing on to other questions
- Focus on evaluating the candidate's soft skills such as communication, teamwork, adaptability, leadership, and problem solving should be addressed
- Include one question designed to assess problem-solving skills through practical examples. For instance, how the candidate has tackled challenges in previous projects, and their approach to issues. If there is context to generate the questions and it has experience and projects, first ask to explain the project they had then ask what did they learn from it
- Maintain a professional yet approachable tone, ensuring candidates feel comfortable while demonstrating their knowledge.
- Ask concise and precise open-ended questions that encourage detailed responses. Each question should be 30 words or less for clarity.

Use the following context to generate the questions:
${body.context}

Moreover generate a 50 word or less second-person description about the interview to be shown to the user. It should be in the field 'description'.
Do not use the exact objective in the description. Remember that some details are not be shown to the user. It should be a small description for the
user to understand what the content of the interview would be. Make sure it is clear to the respondent who's taking the interview.

The field 'questions' should take the format of an array of objects with the following key: question. 

Strictly output only a JSON object with the keys 'questions' and 'description'.`;

export const generateTechQuestionsPrompt = (body: {
  name: string;
  objective: string;
  number: number;
  context: string;
}) => `Imagine you are an interviewer specialized in designing interview questions to help hiring managers find candidates with strong technical expertise and project experience, making it easier to identify the ideal fit for the role.
              
Interview Title: ${body.name}
Interview Objective: ${body.objective}

Number of questions to be generated: ${body.number}

Follow these detailed guidelines when crafting the questions:
- Focus on evaluating the candidate's technical knowledge and their experience working on relevant projects. Questions should aim to gauge depth of expertise, problem-solving ability, and hands-on project experience. These aspects carry the most weight.
- Include questions designed to assess knowledge related to their role through examples like core computer science principles or with concepts that fit more of that role. An example would be a data science would ask questions about python and sql, while a frontend engineer would be asked about javascript, html, css, and other core concepts
- Soft skills such as communication, teamwork, and adaptability should be addressed, but given less emphasis compared to technical and problem-solving abilities.
- Maintain a professional yet approachable tone, ensuring candidates feel comfortable while demonstrating their knowledge.
- Ask concise and precise open-ended questions that encourage detailed responses. Make the questions opene-ended so that they can't answer with a simple yes or no answer. Each question should be 30 words or less for clarity.

Use the following context to generate the questions:
${body.context}

Moreover generate a 50 word or less second-person description about the interview to be shown to the user. It should be in the field 'description'.
Do not use the exact objective in the description. Remember that some details are not be shown to the user. It should be a small description for the
user to understand what the content of the interview would be. Make sure it is clear to the respondent who's taking the interview.

The field 'questions' should take the format of an array of objects with the following key: question. 

Strictly output only a JSON object with the keys 'questions' and 'description'.`;