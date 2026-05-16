# -*- coding: utf-8 -*-
"""
Created on Sat May 16 14:29:32 2026

@author: Dell
"""
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  font-size: 16px;
}

body {
  font-family: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
  min-height: 100vh;
  color: #1a1a1a;
  line-height: 1.5;
}

#root {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 1rem;
}

button {
  font-family: inherit;
  cursor: pointer;
  border: none;
  transition: all 0.3s ease;
}

input[type="file"],
textarea,
select {
  font-family: inherit;
}

@media (max-width: 768px) {
  html {
    font-size: 14px;
  }
}

