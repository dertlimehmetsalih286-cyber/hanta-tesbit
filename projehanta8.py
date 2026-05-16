# -*- coding: utf-8 -*-
"""
Created on Sat May 16 14:29:35 2026

@author: Dell
"""

import "jsr:@supabase/functions-js/edge-runtime.d.ts";
import { Anthropic } from "npm:@anthropic-ai/sdk@0.9.0";

const corsHeaders = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type, Authorization, X-Client-Info, Apikey",
};

interface AnalysisRequest {
  imageData: string;
  imageMediaType: "image/jpeg" | "image/png" | "image/gif" | "image/webp";
}

Deno.serve(async (req: Request) => {
  if (req.method === "OPTIONS") {
    return new Response(null, {
      status: 200,
      headers: corsHeaders,
    });
  }

  try {
    const { imageData, imageMediaType }: AnalysisRequest = await req.json();

    const client = new Anthropic({
      apiKey: Deno.env.get("ANTHROPIC_API_KEY"),
    });

    const message = await client.messages.create({
      model: "claude-3-5-sonnet-20241022",
      max_tokens: 1024,
      messages: [
        {
          role: "user",
          content: [
            {
              type: "image",
              source: {
                type: "base64",
                media_type: imageMediaType,
                data: imageData,
              },
            },
            {
              type: "text",
              text: "This is a medical image for Hanta virus detection analysis. Please analyze this image for any signs, markers, or indicators that might suggest Hanta virus infection. Look for medical test results, lab markers, or clinical indicators. Provide a JSON response with: 1) findings (list of observations), 2) confidence_level (0-100), 3) hanta_indicators (list of Hanta-specific findings if any), 4) recommendation (what to do next). Be objective and clinical in your analysis.",
            },
          ],
        },
      ],
    });

    const responseText =
      message.content[0].type === "text" ? message.content[0].text : "";

    const jsonMatch = responseText.match(/\{[\s\S]*\}/);
    const analysis = jsonMatch
      ? JSON.parse(jsonMatch[0])
      : {
          findings: [responseText],
          confidence_level: 0,
          hanta_indicators: [],
          recommendation: "Unable to determine from image",
        };

    return new Response(JSON.stringify(analysis), {
      headers: {
        ...corsHeaders,
        "Content-Type": "application/json",
      },
    });
  } catch (error) {
    return new Response(
      JSON.stringify({
        error: error instanceof Error ? error.message : "Unknown error",
      }),
      {
        status: 500,
        headers: {
          ...corsHeaders,
          "Content-Type": "application/json",
        },
      }
    );
  }
});
