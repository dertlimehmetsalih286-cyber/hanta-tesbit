# -*- coding: utf-8 -*-
"""
Created on Sat May 16 14:29:35 2026

@author: Dell
"""
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,
  },
});

