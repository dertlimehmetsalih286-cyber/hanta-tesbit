# -*- coding: utf-8 -*-
"""
Created on Sat May 16 14:31:55 2026

@author: Dell
"""
import "./ResultStep.css";

export default function ResultStep({ analysis, onReset }) {
  const getRiskColor = (level) => {
    if (level.includes("Düşük")) return "low";
    if (level.includes("Orta")) return "medium";
    if (level.includes("Yüksek")) return "high";
    return "critical";
  };

  const getEmoji = (level) => {
    if (level.includes("Düşük")) return "✓";
    if (level.includes("Orta")) return "⚠";
    if (level.includes("Yüksek")) return "⚠";
    return "🚨";
  };

  return (
    <div className="result-container">
      <div className="result-card">
        <div className={`risk-header risk-${getRiskColor(analysis.riskLevel)}`}>
          <div className="risk-emoji">{getEmoji(analysis.riskLevel)}</div>
          <div className="risk-content">
            <h2>Risk Değerlendirmesi</h2>
            <p className="risk-level">{analysis.riskLevel}</p>
          </div>
        </div>

        <div className="risk-score">
          <div className="score-label">Risk Puanı</div>
          <div className={`score-bar risk-${getRiskColor(analysis.riskLevel)}`}>
            <div
              className="score-fill"
              style={{ width: `${analysis.riskScore}%` }}
            />
          </div>
          <div className="score-value">{Math.round(analysis.riskScore)}/100</div>
        </div>

        <div className="recommendation-box">
          <h3>Tavsiye</h3>
          <p>{analysis.recommendation}</p>
        </div>

        <div className="details-section">
          <h3>Değerlendirilen Semptomlar</h3>
          <div className="symptoms-list">
            {analysis.symptoms.fever && (
              <div className="symptom-item">
                <span className="symptom-check">✓</span>
                <div>
                  <strong>Yüksek ateş</strong>
                  <p>{analysis.symptoms.feverDegree}°C</p>
                </div>
              </div>
            )}
            {analysis.symptoms.headache && (
              <div className="symptom-item">
                <span className="symptom-check">✓</span>
                <strong>Şiddetli baş ağrısı</strong>
              </div>
            )}
            {analysis.symptoms.muscleAche && (
              <div className="symptom-item">
                <span className="symptom-check">✓</span>
                <strong>Kas ve eklem ağrıları</strong>
              </div>
            )}
            {analysis.symptoms.fatigue && (
              <div className="symptom-item">
                <span className="symptom-check">✓</span>
                <strong>Aşırı halsizlik ve yorgunluk</strong>
              </div>
            )}
            {analysis.symptoms.nausea && (
              <div className="symptom-item">
                <span className="symptom-check">✓</span>
                <strong>Mide bulantısı / kusma</strong>
              </div>
            )}
          </div>
        </div>

        <div className="medical-note">
          <h3>Önemli Not</h3>
          <p>
            Bu sistem eğitim ve ön tarama amaçlı olup, tıbbi teşhis koymaz. Kesin
            teşhis için lütfen bir sağlık profesyoneli ile iletişime geçin.
          </p>
        </div>

        <button onClick={onReset} className="btn-reset">
          Yeni Değerlendirme
        </button>
      </div>
    </div>
  );
}

