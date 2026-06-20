#!/usr/bin/env python3
"""
Career Signal Automation System
Converts raw project data into structured career narratives.

Part of: AI HOLDINGS OS 2026
Author: Shinnosuke Mori (Iizuka City, Fukuoka)
"""

from typing import Any


def process_career_data(data: dict[str, Any]) -> dict[str, Any]:
    """
    Main pipeline: raw project data → structured career signal.

    Args:
        data: dict with keys: title, description, tools, outcome

    Returns:
        Structured dict with skills, projects, impact narratives
    """
    return {
        "skills": extract_skills(data),
        "projects": map_projects(data),
        "impact": evaluate_impact(data),
    }


def extract_skills(data: dict[str, Any]) -> list[str]:
    """Extract skill signals from project data (tool use → capability proof)."""
    tools = data.get("tools", [])
    skill_map = {
        "github_actions": "CI/CD pipeline design",
        "python": "automation scripting",
        "notion": "structured knowledge systems",
        "zapier": "no-code workflow automation",
        "n8n": "self-hosted automation infrastructure",
        "cloudflare": "DevOps / edge deployment",
        "linkedin_api": "professional network automation",
    }
    return list({skill_map[t.lower()] for t in tools if t.lower() in skill_map})


def map_projects(data: dict[str, Any]) -> dict[str, str]:
    """Map project data into Problem / Solution / Impact structure."""
    return {
        "problem": data.get("problem", ""),
        "solution": data.get("title", "") + ": " + data.get("description", ""),
        "impact": data.get("outcome", "Structured output — see case studies"),
        "github_path": data.get("repo_path", ""),
    }


def evaluate_impact(data: dict[str, Any]) -> str:
    """
    Generate impact statement even without hard metrics.

    Impact types:
    - Time reduction: 'Reduced X from Y minutes to Z'
    - Structure: 'Converted ad-hoc process into repeatable system'
    - Reproducibility: 'Framework now reusable across N contexts'
    """
    outcome = data.get("outcome", "")
    if not outcome:
        return (
            "Converted unstructured workflow into documented, "
            "reproducible system — reducing future setup time."
        )
    return outcome


if __name__ == "__main__":
    sample_project = {
        "title": "LinkedIn × GitHub Integration Layer",
        "description": "Bidirectional career signal system connecting profile and code",
        "tools": ["github_actions", "python", "notion", "zapier"],
        "problem": "Professional identity fragmented across platforms",
        "outcome": "Unified career signal reduces recruiter evaluation friction",
        "repo_path": "career-signal-system/",
    }

    result = process_career_data(sample_project)
    print("=== Career Signal Output ===")
    for key, value in result.items():
        print(f"\n{key.upper()}:\n  {value}")
