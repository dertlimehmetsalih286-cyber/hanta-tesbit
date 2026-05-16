
import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App.jsx"; // Doğrudan yanındaki App.jsx'i görmesi için yolu netleştirdik
import "./index.css";

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
