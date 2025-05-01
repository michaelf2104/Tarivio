import React from "react";
import "./ProgressBar.css";

type ProgressBarProps = {
  currentStep: number;
  totalSteps: number;
};

function ProgressBar({ currentStep, totalSteps }: ProgressBarProps) {
  const percentage = Math.min((currentStep / totalSteps) * 100, 100);

  return (
    <div className="progress-bar-wrapper">
      <div className="progress-bar">
        <div className="progress-bar-fill" style={{ width:`${percentage}%` }} />
      </div>
    </div>
  );
}

export default ProgressBar;
