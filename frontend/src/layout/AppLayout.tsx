// Pfad: frontend/src/layout/AppLayout.tsx
import React, { useState } from "react";
import Sidebar from "../components/Sidebar";
import InfoPanel from "../components/InfoPanel";
import "../layout/AppLayout.css";
import ChatTabs from "../components/ChatTabs";

type ChildWithInfoProps = {
  onShowInfo: (title: string, text: string) => void;
};

type AppLayoutProps = {
  children: React.ReactElement<ChildWithInfoProps>;
};

function AppLayout() {
  const [infoPanelData, setInfoPanelData] = useState<{
    title: string;
    text: string;
  } | null>(null);

  const handleShowInfo = (title: string, text: string) => {
    setInfoPanelData({ title, text });
  };

  return (
    <div className="app-layout">
      <div className="sidebar-container">
        <Sidebar />
      </div>

      <div className="main-content">
        <ChatTabs onShowInfo={handleShowInfo} />
      </div>

      <div className="info-panel-container">
        {infoPanelData && (
          <InfoPanel
            title={infoPanelData.title}
            text={infoPanelData.text}
            onClose={() => setInfoPanelData(null)}
          />
        )}
      </div>
    </div>
  );
}

export default AppLayout;

