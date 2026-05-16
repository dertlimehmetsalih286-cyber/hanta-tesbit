# -*- coding: utf-8 -*-
"""
Created on Sat May 16 14:31:55 2026

@author: Dell
"""
import { useState } from "react";
import "./SymptomsStep.css";

export default function SymptomsStep({ onSubmit, onBack }) {
  const [symptoms, setSymptoms] = useState({
    fever: false,
    headache: false,
    muscleAche: false,
    fatigue: false,
    nausea: false,
    feverDegree: 38,
    duration: "1-2",
  });

  const [loading, setLoading] = useState(false);

  const handleCheckboxChange = (key) => {
    setSymptoms((prev) => ({
      ...prev,
      [key]: !prev[key],
    }));
  };

  const handleInputChange = (key, value) => {
    setSymptoms((prev) => ({
      ...prev,
      [key]: value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    await new Promise((resolve) => setTimeout(resolve, 800));
    onSubmit(symptoms);
  };

  return (
    <div className="symptoms-container">
      <div className="symptoms-card">
        <div className="symptoms-header">
          <h2>Semptom Değerlendirmesi</h2>
          <p>Lütfen yaşadığınız semptomları seçin</p>
        </div>

        <form onSubmit={handleSubmit} className="symptoms-form">
          <div className="symptom-group">
            <h3>Temel Semptomlar</h3>

            <label className="checkbox-label">
              <input
                type="checkbox"
                checked={symptoms.fever}
                onChange={() => handleCheckboxChange("fever")}
                disabled={loading}
              />
              <span>Yüksek ateş (38°C üstü)</span>
            </label>

            {symptoms.fever && (
              <div className="slider-container">
                <label>Ateş Derecesi: {symptoms.feverDegree}°C</label>
                <input
                  type="range"
                  min="36"
                  max="41"
                  step="0.1"
                  value={symptoms.feverDegree}
                  onChange={(e) => handleInputChange("feverDegree", parseFloat(e.target.value))}
                  disabled={loading}
                  className="slider"
                />
              </div>
            )}

            <label className="checkbox-label">
              <input
                type="checkbox"
                checked={symptoms.headache}
                onChange={() => handleCheckboxChange("headache")}
                disabled={loading}
              />
              <span>Şiddetli baş ağrısı</span>
            </label>

            <label className="checkbox-label">
              <input
                type="checkbox"
                checked={symptoms.muscleAche}
                onChange={() => handleCheckboxChange("muscleAche")}
                disabled={loading}
              />
              <span>Kas ve eklem ağrıları (sırt, kalça, bacaklar)</span>
            </label>

            <label className="checkbox-label">
              <input
                type="checkbox"
                checked={symptoms.fatigue}
                onChange={() => handleCheckboxChange("fatigue")}
                disabled={loading}
              />
              <span>Aşırı halsizlik ve yorgunluk</span>
            </label>

            <label className="checkbox-label">
              <input
                type="checkbox"
                checked={symptoms.nausea}
                onChange={() => handleCheckboxChange("nausea")}
                disabled={loading}
              />
              <span>Mide bulantısı, kusma veya karın ağrısı</span>
            </label>
          </div>

          <div className="symptom-group">
            <label htmlFor="duration" className="form-label">
              Semptom Süresi
            </label>
            <select
              id="duration"
              value={symptoms.duration}
              onChange={(e) => handleInputChange("duration", e.target.value)}
              disabled={loading}
              className="select-input"
            >
              <option value="1-2">1-2 gün</option>
              <option value="3-5">3-5 gün</option>
              <option value="5+">5 günden fazla</option>
            </select>
          </div>

          <div className="form-actions">
            <button
              type="button"
              onClick={onBack}
              disabled={loading}
              className="btn btn-secondary"
            >
              Geri
            </button>
            <button
              type="submit"
              disabled={loading}
              className="btn btn-primary"
            >
              {loading ? "Analiz Ediliyor..." : "Sonuçları Gör"}
            </button>
          </div>
        </form>

        <div className="warning-box">
          <strong>⚠️ Önemli:</strong> Bu sistem eğitim amaçlıdır. Tıbbi teşhis için lütfen
          doktora danışın.
        </div>
      </div>
    </div>
  );
}

