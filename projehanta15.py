# -*- coding: utf-8 -*-
"""
Created on Sat May 16 14:31:55 2026

@author: Dell
"""
import { useState } from "react";
import "./UploadStep.css";

export default function UploadStep({ onImageSelected }) {
  const [preview, setPreview] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    if (!file) return;

    setLoading(true);
    const reader = new FileReader();

    reader.onload = (event) => {
      const imageData = event.target.result.split(",")[1];
      const mediaType = file.type || "image/jpeg";

      setPreview(event.target.result);
      setLoading(false);

      setTimeout(() => {
        onImageSelected({ imageData, mediaType });
      }, 500);
    };

    reader.readAsDataURL(file);
  };

  return (
    <div className="upload-container">
      <div className="upload-card">
        <div className="upload-header">
          <h1>Hanta Virüsü Teşhis Sistemi</h1>
          <p>Tıbbi fotoğraf veya test sonucunu yükleyin</p>
        </div>

        <div className="upload-box">
          {preview ? (
            <div className="preview-container">
              <img src={preview} alt="Preview" />
              {loading && <div className="loading-overlay">İşleniyor...</div>}
            </div>
          ) : (
            <>
              <svg
                className="upload-icon"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={2}
                  d="M12 4v16m8-8H4"
                />
              </svg>
              <p className="upload-text">
                <strong>Fotoğraf yüklemek için tıklayın</strong>
              </p>
              <p className="upload-subtext">veya sürükleyip bırakın</p>
            </>
          )}
          <input
            type="file"
            accept="image/*"
            onChange={handleFileChange}
            className="file-input"
            disabled={loading}
          />
        </div>

        <div className="info-section">
          <h3>Desteklenen Dosya Türleri:</h3>
          <ul>
            <li>Kan testi sonuçları</li>
            <li>İdrar analizi</li>
            <li>Pıhtı testleri</li>
            <li>Tıbbi raporlar</li>
          </ul>
        </div>
      </div>
    </div>
  );
}

