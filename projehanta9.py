# -*- coding: utf-8 -*-
"""
Created on Sat May 16 14:31:54 2026

@author: Dell
"""
# Create Hanta Virus Detection Database

  1. New Tables
    - `hanta_analyses`
      - `id` (uuid, primary key)
      - `user_id` (text, for session tracking)
      - `image_url` (text)
      - `image_analysis` (jsonb, Claude Vision analysis results)
      - `symptoms` (jsonb, user symptom responses)
      - `risk_score` (numeric, 0-100)
      - `risk_level` (text, Low/Medium/High/Critical)
      - `recommendation` (text)
      - `created_at` (timestamp)

  2. Security
    - Enable RLS on `hanta_analyses` table
    - Add policy for users to read their own data
*/

CREATE TABLE IF NOT EXISTS hanta_analyses (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id text NOT NULL,
  image_url text,
  image_analysis jsonb,
  symptoms jsonb,
  risk_score numeric DEFAULT 0,
  risk_level text DEFAULT 'Low',
  recommendation text,
  created_at timestamptz DEFAULT now()
);

ALTER TABLE hanta_analyses ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Users can read own analyses"
  ON hanta_analyses FOR SELECT
  TO public
  USING (user_id = current_setting('app.current_user_id', true));

CREATE POLICY "Users can create analyses"
  ON hanta_analyses FOR INSERT
  TO public
  WITH CHECK (user_id = current_setting('app.current_user_id', true));

CREATE INDEX idx_hanta_analyses_user_id ON hanta_analyses(user_id);
CREATE INDEX idx_hanta_analyses_created_at ON hanta_analyses(created_at);

