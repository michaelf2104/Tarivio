import React from "react";
import "../components/Sidebar.css";
import logo from "../assets/PKVBotLogo.png";

/**
 * sidebar component containing navigation buttons and logo
 */
function Sidebar() {
  return (
    <div className="sidebar">
      <div className="sidebar-logo">
        <img src={logo} alt="PKV Chatbot Logo" />
      </div>

      <nav className="sidebar-nav">
        <button className="sidebar-link">🏠 Home</button>
        <hr className="sidebar-divider" />
        <button className="sidebar-link">🧑‍💼 Profil</button>
        <hr className="sidebar-divider" />
        <button className="sidebar-link">❓ Support</button>
      </nav>
    </div>
  );
}

export default Sidebar;