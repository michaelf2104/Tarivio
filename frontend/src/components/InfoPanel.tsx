import React from "react";
import "./InfoPanel.css";

type InfoPanelProps = {
  title: string;
  text: string;
  onClose: () => void;
};

function InfoPanel({ title, text, onClose }: InfoPanelProps) {
  return (
    <div className="info-panel">
      <div className="info-panel-header">
        <h3>{title}</h3>
        <button onClick={onClose} className="close-button">×</button>
      </div>
      <p>{text}</p>
    </div>
  );
}

export default InfoPanel;
