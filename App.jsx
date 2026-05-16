# -*- coding: utf-8 -*-
"""
Created on Sat May 16 14:27:52 2026

@author: Dell
"""

import { useState } from "react";
import UploadStep from "./components/UploadStep";
import SymptomsStep from "./components/SymptomsStep";
import ResultStep from "./components/ResultStep";
import "./App.css";

export default function App() {
  const [step, setStep] = useState("upload");
  const [imageData, setImageData] = useState(null);
  const [analysis, setAnalysis] = useState(null);
  const [symptoms, setSymptoms] = useState({
    fever: false,
    headache: false,
    muscleAche: false,
    fatigue: false,
    nausea: false,
    feverDegree: 38,
    duration: "1-2",
  });

  const handleImageSelected = (data) => {
    setImageData(data);
    setStep("symptoms");
  };

  const handleSymptomsSubmit = async (symptomData) => {
    setSymptoms(symptomData);

    const riskFactors = [
      symptomData.fever ? 20 : 0,
      symptomData.feverDegree > 39 ? 10 : (symptomData.feverDegree > 38 ? 5 : 0),
      symptomData.headache ? 15 : 0,
      symptomData.muscleAche ? 15 : 0,
      symptomData.fatigue ? 10 : 0,
      symptomData.nausea ? 10 : 0,
      symptomData.duration === "3-5" ? 10 : (symptomData.duration === "5+" ? 15 : 0),
    ];

    const riskScore = Math.min(100, riskFactors.reduce((a, b) => a + b, 0));

    let riskLevel = "Düşük";
    let recommendation = "";

    if (riskScore < 25) {
      riskLevel = "Düşük Risk";
      recommendation = "Semptomlara devam etmek için gözlemleyin. Durum kötüleşirse tıbbi yardım alın.";
    } else if (riskScore < 50) {
      riskLevel = "Orta Risk";
      recommendation = "Yakın zamanda bir doktor ile görüşmeyi tavsiye ederiz. Test yaptırın.";
    } else if (riskScore < 75) {
      riskLevel = "Yüksek Risk";
      recommendation = "Hemen bir tıbbi profesyonelle iletişime geçin. Test yaptırılması gerekli.";
    } else {
      riskLevel = "Kritik";
      recommendation = "ACİL: Hemen hastaneye başvurun. Yoğun tıbbi değerlendirme gerekli.";
    }

    // Fotoğraf analizi simülasyonu
    const imageAnalysisResult = {
      findings: ["Görüntü analiz edildi"],
      confidence_level: Math.floor(Math.random() * 40 + 40),
      hanta_indicators: [],
      recommendation: "Klinik değerlendirme önerilir",
    };

    setAnalysis({
      riskScore,
      riskLevel,
      recommendation,
      imageAnalysis: imageAnalysisResult,
      symptoms: symptomData,
    });

    setStep("result");
  };

  return (
    <div className="app-container">
      {step === "upload" && <UploadStep onImageSelected={handleImageSelected} />}
      {step === "symptoms" && (
        <SymptomsStep onSubmit={handleSymptomsSubmit} onBack={() => setStep("upload")} />
      )}
      {step === "result" && (
        <ResultStep analysis={analysis} onReset={() => setStep("upload")} />
      )}
    </div>
  );
}
