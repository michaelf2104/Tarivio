// Pfad: frontend/src/components/GptChat.tsx
import React, { useState, useRef, useEffect } from "react";
import { askFreeQuestion } from "../services/api";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import "./ChatInterface.css"; // falls du die Styles dort zentral nutzt

/**
 * Component for sending free-form questions to the GPT API
 * and displaying the conversation in a chat-like format.
 * 
 * @returns JSX.Element
 */
function GptChat() {
  const [question, setQuestion] = useState("");
  const [gptMessages, setGptMessages] = useState<{ type: "user" | "bot"; content: string }[]>([]);
  const bottomRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [gptMessages]);


   /**
   * Handles user input submission and sends it to the GPT API.
   * Adds both user question and bot response to the message list.
   */
  async function handleSubmit() {
    if (!question.trim()) return;

    setGptMessages((prev) => [...prev, { type: "user", content: question }]);

    try {
      const response = await askFreeQuestion(question);
      setGptMessages((prev) => [...prev, { type: "bot", content: response }]);
    } catch {
      setGptMessages((prev) => [...prev, { type: "bot", content: "Antwort konnte nicht geladen werden." }]);
    }

    setQuestion("");
  }

  return (
    <div className="chat-container">
      <div className="chat-messages gpt-response">
        {gptMessages.map((msg, index) => (
          <div key={index} className={`chat-bubble ${msg.type}`}>
            <ReactMarkdown remarkPlugins={[remarkGfm]}>
              {msg.content}
            </ReactMarkdown>
          </div>
        ))}
        <div ref={bottomRef} />
      </div>

      <div className="chat-input">
        <div className="input-group">
          <input
            type="text"
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            placeholder="Stelle deine eigene Frage..."
          />
          <button onClick={handleSubmit}>Frage stellen</button>
        </div>
      </div>
    </div>
  );
}

export default GptChat;
