# -*- coding: utf-8 -*-
"""
Created on Sat May 16 14:31:55 2026

@author: Dell
"""
.upload-container {
  width: 100%;
}

.upload-card {
  background: white;
  border-radius: 12px;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
  padding: 2rem;
  animation: slideUp 0.5s ease;
}

@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.upload-header {
  text-align: center;
  margin-bottom: 2rem;
}

.upload-header h1 {
  font-size: 1.75rem;
  font-weight: 700;
  color: #1a1a1a;
  margin-bottom: 0.5rem;
}

.upload-header p {
  font-size: 1rem;
  color: #666;
}

.upload-box {
  position: relative;
  border: 2px dashed #0066cc;
  border-radius: 8px;
  padding: 3rem 2rem;
  text-align: center;
  background: #f9f9f9;
  transition: all 0.3s ease;
  cursor: pointer;
  min-height: 250px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin-bottom: 1.5rem;
}

.upload-box:hover {
  border-color: #0052a3;
  background: #f0f5ff;
}

.file-input {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  opacity: 0;
  cursor: pointer;
}

.file-input:disabled {
  cursor: not-allowed;
}

.upload-icon {
  width: 3rem;
  height: 3rem;
  color: #0066cc;
  margin-bottom: 1rem;
}

.upload-text {
  font-size: 1.1rem;
  color: #1a1a1a;
  margin-bottom: 0.5rem;
}

.upload-subtext {
  font-size: 0.9rem;
  color: #999;
}

.preview-container {
  position: relative;
  width: 100%;
  height: 250px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.preview-container img {
  max-width: 100%;
  max-height: 100%;
  border-radius: 4px;
  object-fit: contain;
}

.loading-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  border-radius: 4px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: 600;
  animation: fadeIn 0.3s ease;
}

.info-section {
  background: #f0f5ff;
  border-left: 4px solid #0066cc;
  padding: 1rem;
  border-radius: 4px;
}

.info-section h3 {
  font-size: 0.9rem;
  color: #1a1a1a;
  margin-bottom: 0.5rem;
  font-weight: 600;
}

.info-section ul {
  list-style: none;
  font-size: 0.85rem;
  color: #555;
}

.info-section li {
  padding: 0.25rem 0;
  padding-left: 1.5rem;
  position: relative;
}

.info-section li:before {
  content: "✓";
  position: absolute;
  left: 0;
  color: #0066cc;
  font-weight: bold;
}

@media (max-width: 768px) {
  .upload-card {
    padding: 1.5rem;
  }

  .upload-header h1 {
    font-size: 1.5rem;
  }

  .upload-box {
    padding: 2rem 1rem;
    min-height: 200px;
  }
}

