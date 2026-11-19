#!/usr/bin/env python3
"""
ES³ SML Framework — MkDocs Generator from Master JSON (v2)
==========================================================
Generates/synchronizes MkDocs documentation pages (docs/dimensions/*.md)
directly from the master `sml_data.json` file.

Matches the exact schema:
- Root: { "SML <N> <Title>": { "dimension_title", "dimension_desc", "objectives": [ ... ] } }
- Objectives: { "id", "title", "sovereignty_contribution", "controls": [ ... ] }
- Controls: { "id", "desc", "control_scope", "service_type", "question", "requirements": { ... } }
"""

import sys
import os
import re
import json
import argparse
from pathlib import Path

DIMENSION_SLUG_MAP = {
    "SML 1": "sml1-strategic.md",
    "SML 2": "sml2-legal.md",
    "SML 3": "sml3-data.md",
    "SML 4": "sml4-operational.md",
    "SML 5": "sml5-supply-chain.md",
    "SML 6": "sml6-technology.md",
    "SML 7": "sml7-security.md",
    "SML 8": "sml8-environmental.md",
    "SML 9": "sml9-ai.md",
}

def parse_control_id_and_level(raw_id: str):
    """
    Extracts the clean Control ID and Implementation Level.
    Example: 'SML 1.CO 1.C 1 (Governance and Operations)'
             -> ('SML 1.CO 1.C 1', 'Governance & Operations')
    """
    raw_id = raw_id.strip()
    match = re.search(r'^(.*?)\s*\((.*?)\)$', raw_id)
    if match:
        cid = match.group(1).strip()
        lvl = match.group(2).strip().replace(" and ", " & ")
        return cid, lvl
    return raw_id, "N/A"

def format_requirements_badges(requirements: dict) -> str:
    """Formats maturity level indicators (Initial, Managed, Advanced, Future-Proof)."""
    if not isinstance(requirements, dict):
        return ""
    
    levels = [
        ("initial", "Initial"),
        ("managed", "Managed"),
        ("advanced", "Advanced"),
        ("future_proof", "Future-Proof")
    ]
    
    active_levels = [label for key, label in levels if requirements.get(key)]
    if not active_levels:
        return ""
    
    badges = " ".join([f"`{lvl}`" for lvl in active_levels])
    return f"**Maturity Levels:** {badges}"

def format_objective_header(obj_id: str, obj_title: str):
    """
    Cleans up objective title and separates Target State if included.
    Example: 'Governance Authority (SML 1.CO 1) - To ensure that...'
             -> ('Governance Authority', 'To ensure that...')
    """
    cleaned = obj_title.strip()
    # Remove redundant (SML X.CO Y) if present
    if obj_id:
        cleaned = re.sub(r'\s*\(' + re.escape(obj_id) + r'\)', '', cleaned).strip()
    
    if " - " in cleaned:
        parts = cleaned.split(" - ", 1)
        name = parts[0].strip()
        target_state = parts[1].strip()
        return name, target_state
    return cleaned, ""

def generate_docs(json_path: Path, docs_dir: Path, check_only: bool = False) -> bool:
    if not json_path.exists():
        print(f"❌ Error: Master JSON file not found at: {json_path}")
        return False

    print(f"📖 Reading Master JSON from: {json_path}...")
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    target_dir = docs_dir / "dimensions"
    target_dir.mkdir(parents=True, exist_ok=True)

    all_synced = True

    for dim_key, dim_data in data.items():
        if not isinstance(dim_data, dict):
            continue

        # Extract dimension identifier (e.g. 'SML 1')
        dim_prefix_match = re.search(r'(SML\s*\d)', dim_key, re.IGNORECASE)
        prefix = dim_prefix_match.group(1).upper() if dim_prefix_match else dim_key[:5].strip()
        filename = DIMENSION_SLUG_MAP.get(prefix, f"{prefix.lower().replace(' ', '-')}.md")
        target_file = target_dir / filename

        dim_desc = dim_data.get("dimension_desc", "")

        md = []
        md.append(f"# {dim_key}")
        md.append("")
        if dim_desc:
            md.append(f"*{dim_desc}*")
            md.append("")
        md.append("---")
        md.append("")
        md.append("## Control Objectives & Controls")
        md.append("")

        for obj in dim_data.get("objectives", []):
            obj_id = obj.get("id", "").strip()
            obj_title = obj.get("title", "").strip()
            sovereignty_contrib = obj.get("sovereignty_contribution", "").strip()

            obj_name, target_state = format_objective_header(obj_id, obj_title)

            if target_state:
                md.append(f"### {obj_id}: {obj_name}")
                md.append(f"**Target State:** {target_state}\n")
            else:
                md.append(f"### {obj_id}: {obj_name}\n")

            if sovereignty_contrib:
                md.append(f"> **Sovereignty Contribution:** {sovereignty_contrib}\n")

            for ctrl in obj.get("controls", []):
                raw_cid = ctrl.get("id", "")
                cid, level = parse_control_id_and_level(raw_cid)
                scope = ctrl.get("control_scope", "All")
                stype = ctrl.get("service_type", "All")
                desc = ctrl.get("desc", "").strip()
                question = ctrl.get("question", "").strip()
                requirements = ctrl.get("requirements", {})

                md.append(f"* **{cid}** | Level: *{level}* | Scope: *{scope}* | Service Type: *{stype}*  ")
                md.append(f"  {desc}  ")
                md.append(f"  * **Audit Question:** {question}")
                
                req_badges = format_requirements_badges(requirements)
                if req_badges:
                    md.append(f"  * {req_badges}")
                md.append("")

            md.append("---")
            md.append("")

        rendered_content = "\n".join(md)

        if check_only:
            if not target_file.exists():
                print(f"❌ Missing file: {target_file}")
                all_synced = False
            elif target_file.read_text(encoding="utf-8") != rendered_content:
                print(f"❌ Out of sync: {target_file}")
                all_synced = False
            else:
                print(f"✅ In sync: {target_file}")
        else:
            target_file.write_text(rendered_content, encoding="utf-8")
            print(f"  ✓ Rendered: {target_file}")

    if check_only:
        if all_synced:
            print("🎉 Success: All MkDocs dimension pages match the master JSON!")
        return all_synced
    else:
        print(f"\n✨ Generation Complete! All dimension pages synchronized from JSON in '{target_dir}'.")
        return True

def main():
    parser = argparse.ArgumentParser(description="Generate MkDocs Markdown files from ES3 sml_data.json.")
    parser.add_argument("--input", "-i", default="docs/sml_data.json", help="Path to input master sml_data.json")
    parser.add_argument("--docs-dir", "-d", default="docs", help="Path to MkDocs docs directory")
    parser.add_argument("--check", action="store_true", help="Check synchronization without writing files")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        if Path("sml_data.json").exists():
            input_path = Path("sml_data.json")

    docs_path = Path(args.docs_dir)
    success = generate_docs(input_path, docs_path, check_only=args.check)
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()
