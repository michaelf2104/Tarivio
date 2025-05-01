// Pfad: frontend/src/components/ChatTabs.tsx
import React, { useState } from "react";
import ChatInterface from "./ChatInterface";
import GptChat from "./GptChat";
import "./ChatTabs.css";
import ProgressBar from "./ProgressBar";
import { questionFlow } from "../data/questions";

type ChatTabsProps = {
  onShowInfo: (title: string, text: string) => void;
};


/**
 * Component that displays two chat tabs: one for the PKV chatbot and one for GPT-based answers.
 * Also shows a progress bar tracking answered questions.
 */
function ChatTabs({ onShowInfo }: ChatTabsProps) {
  const [activeTab, setActiveTab] = useState<"pkv" | "gpt">("pkv");
  const [answeredCount, setAnsweredCount] = useState(0); 

  const totalSteps = questionFlow.length + 2;

  return (
    <div className="chat-tabs-wrapper">
      {/* progress bar */}
      <div className="progress-header">
        <h2>Fortschritt</h2>
      </div>
      <ProgressBar currentStep={answeredCount} totalSteps={totalSteps} />

      {/* tabs */}
      <div className="tab-header">
        <button
          className={activeTab === "pkv" ? "active" : ""}
          onClick={() => setActiveTab("pkv")}
        >
          PKV-Chat
        </button>
        <button
          className={activeTab === "gpt" ? "active" : ""}
          onClick={() => setActiveTab("gpt")}
        >
          GPT-Antworten
        </button>
      </div>

      <div className="tab-content">
        <div style={{ display: activeTab === "pkv" ? "block" : "none" }}>
          <ChatInterface onShowInfo={onShowInfo} onAnsweredUpdate={setAnsweredCount} />
        </div>
        <div style={{ display: activeTab === "gpt" ? "block" : "none" }}>
          <GptChat />
        </div>
      </div>
    </div>
  );
}

export default ChatTabs;
