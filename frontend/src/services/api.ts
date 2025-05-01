const BASE_URL = process.env.REACT_APP_BACKEND_URL || "http://localhost:8000";
const TESTING_USER_UUID = "a44b47af-ef73-4176-a692-e7638d4cb453"

// CHANGE TESTING_USER_UUID WITH "userId" before deployment

export async function submitAnswer(userId: string, question_key: string, answer_text: string) {
    await fetch(`${BASE_URL}/api/answers`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ 
        user_id: TESTING_USER_UUID, 
        question_key: question_key,
        answer_text: answer_text
      }),
    });
  }
  
export async function fetchSummary(userId: string): Promise<string>{
  const response = await fetch(`${BASE_URL}/api/summary/${TESTING_USER_UUID}`);
  if (!response.ok) {
    throw new Error("Failed to fetch answers");
  }

  const data = await response.json()
  return data.summary;
}

export async function askFreeQuestion(question: string): Promise<string> {
  console.log("▶️ Sending free question to backend:", question); // Log im Frontend

  const response = await fetch(`${BASE_URL}/api/question`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ question }),
  });

  const data = await response.json();

  if (!response.ok) {
    console.error("❌ API Error:", data.error);
    throw new Error(data.error || "KI-Antwort konnte nicht geladen werden");
  }

  return data.answer;
}
