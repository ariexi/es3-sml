#!/usr/bin/env python3
"""
ES³ SML Framework — JSON to MkDocs Documentation Generator
==========================================================
Generates high-quality, standardized Markdown documentation pages for MkDocs
directly from the master Assessment Tool JSON (sml_data.json).

Features:
- Robust schema parser supporting both list- and dict-based JSON structures.
- Generates clean, Material-for-MkDocs compatible Markdown with proper tables and callouts.
- Supports CI validation mode (--check) to ensure docs stay in sync with JSON.
"""

import os
import sys
import json
import argparse
from pathlib import Path

DIMENSION_SLUGS = {
    "SML 1": "sml1-strategic",
    "SML 2": "sml2-legal",
    "SML 3": "sml3-data",
    "SML 4": "sml4-operational",
    "SML 5": "sml5-supply-chain",
    "SML 6": "sml6-technology",
    "SML 7": "sml7-security",
    "SML 8": "sml8-environmental",
    "SML 9": "sml9-ai",
}

def normalize_collection(item_or_coll):
    """Converts either a list of dicts or a dict-of-dicts into a uniform list of dicts."""
    if isinstance(item_or_coll, list):
        return item_or_coll
    elif isinstance(item_or_coll, dict):
        result = []
        for key, val in item_or_coll.items():
            if isinstance(val, dict):
                entry = dict(val)
                if "id" not in entry and "code" not in entry:
                    entry["id"] = key
                result.append(entry)
            else:
                result.append({"id": key, "value": val})
        return result
    return []

def extract_dimensions(catalog: dict):
    """Extracts dimensions from diverse JSON structures."""
    raw_dims = catalog.get("dimensions", [])
    dims = normalize_collection(raw_dims)
    
    parsed_dims = []
    for dim in dims:
        dim_id = dim.get("id") or dim.get("code") or ""
        dim_name = dim.get("name") or dim.get("title") or dim_id
        dim_desc = dim.get("description") or dim.get("desc") or ""
        
        raw_cos = dim.get("control_objectives") or dim.get("objectives") or []
        cos = normalize_collection(raw_cos)
        
        parsed_cos = []
        for co in cos:
            co_id = co.get("id") or co.get("code") or ""
            co_title = co.get("title") or co.get("name") or co_id
            co_obj = co.get("objective") or co.get("target_state") or co.get("description") or ""
            
            raw_ctrls = co.get("controls") or []
            ctrls = normalize_collection(raw_ctrls)
            
            parsed_ctrls = []
            for ctrl in ctrls:
                c_id = ctrl.get("id") or ctrl.get("code") or ""
                level = ctrl.get("level") or ctrl.get("implementation_level") or "Governance & Operations"
                scope = ctrl.get("scope") or ctrl.get("control_scope") or "Service Provider"
                service_type = ctrl.get("service_type") or ctrl.get("service_types") or "All"
                desc = ctrl.get("description") or ctrl.get("text") or ctrl.get("desc") or ""
                question = ctrl.get("question") or ctrl.get("audit_question") or ""
                q_id = ctrl.get("question_id") or ctrl.get("q_id") or (f"{c_id}.Q 1" if c_id else "Q 1")
                
                parsed_ctrls.append({
                    "id": c_id,
                    "level": level,
                    "scope": scope,
                    "service_type": service_type,
                    "description": desc,
                    "question": question,
                    "question_id": q_id
                })
                
            parsed_cos.append({
                "id": co_id,
                "title": co_title,
                "objective": co_obj,
                "controls": parsed_ctrls
            })
            
        parsed_dims.append({
            "id": dim_id,
            "name": dim_name,
            "description": dim_desc,
            "control_objectives": parsed_cos
        })
        
    return parsed_dims

def render_dimension_markdown(dim: dict) -> str:
    """Renders a single dimension into clean MkDocs-compatible Markdown."""
    lines = []
    lines.append(f"# {dim['name']}\n")
    if dim.get("description"):
        lines.append(f"*{dim['description']}*\n")
    lines.append("---\n")
    lines.append("## Control Objectives & Controls\n")
    
    for co in dim.get("control_objectives", []):
        lines.append(f"### {co['id']}: {co['title']}")
        if co.get("objective"):
            lines.append(f"**Target State:** {co['objective']}\n")
        else:
            lines.append("")
            
        for ctrl in co.get("controls", []):
            meta = f"| Level: *{ctrl['level']}* | Scope: *{ctrl['scope']}* | Service Type: *{ctrl['service_type']}*"
            lines.append(f"* **{ctrl['id']}** {meta}  ")
            lines.append(f"  {ctrl['description']}  ")
            q_label = ctrl['question_id']
            if not q_label.startswith(ctrl['id']):
                q_label = f"{ctrl['id']}.Q 1"
            lines.append(f"  * **Question {q_label}:** {ctrl['question']}\n")
            
        lines.append("---\n")
        
    return "\n".join(lines).strip() + "\n"

def main():
    parser = argparse.ArgumentParser(description="Generate MkDocs Markdown files from Assessment Tool JSON.")
    parser.add_argument("--input", "-i", default=None, help="Path to input sml_data.json")
    parser.add_argument("--docs-dir", "-d", default="docs", help="Path to MkDocs docs directory (default: docs)")
    parser.add_argument("--check", action="store_true", help="Check mode: verifies if docs are in sync without writing")
    args = parser.parse_args()

    # Candidate JSON paths if not explicitly provided
    candidate_paths = [
        args.input,
        "docs/sml_data.json"
    ]
    input_file = None
    for p in candidate_paths:
        if p and os.path.exists(p):
            input_file = Path(p)
            break
            
    if not input_file:
        searched = [p for p in candidate_paths if p]
        print(f"❌ Error: Master JSON file not found. Looked in: {', '.join(searched)}")
        print("Please provide the path using: python generate_docs_from_json.py --input <path_to_json>")
        sys.exit(1)

    print(f"📖 Reading Master JSON from: {input_file}...")
    try:
        with open(input_file, "r", encoding="utf-8") as f:
            catalog = json.load(f)
    except Exception as e:
        print(f"❌ Error parsing JSON file '{input_file}': {e}")
        sys.exit(1)

    dims = extract_dimensions(catalog)
    if not dims:
        print("❌ Error: No dimensions found in the JSON file.")
        sys.exit(1)

    print(f"✓ Found {len(dims)} dimensions.")
    docs_dir = Path(args.docs_dir)
    dim_out_dir = docs_dir / "dimensions"
    dim_out_dir.mkdir(parents=True, exist_ok=True)

    all_synced = True
    for dim in dims:
        dim_id = dim["id"]
        # Match ID to slug
        matched_slug = None
        for key, slug in DIMENSION_SLUGS.items():
            if dim_id.upper().startswith(key.upper()) or key.upper() in dim_id.upper():
                matched_slug = slug
                break
        if not matched_slug:
            matched_slug = dim_id.lower().replace(" ", "-").replace("_", "-")
            
        target_path = dim_out_dir / f"{matched_slug}.md"
        rendered_content = render_dimension_markdown(dim)

        if args.check:
            if not target_path.exists():
                print(f"❌ Out of sync: {target_path} does not exist.")
                all_synced = False
            else:
                existing = target_path.read_text(encoding="utf-8")
                if existing != rendered_content:
                    print(f"❌ Out of sync: {target_path} differs from JSON master.")
                    all_synced = False
                else:
                    print(f"✅ In sync: {target_path}")
        else:
            target_path.write_text(rendered_content, encoding="utf-8")
            print(f"  ✓ Rendered: {target_path}")

    if args.check:
        if all_synced:
            print("🎉 Success: All MkDocs dimension pages are perfectly in sync with the JSON master!")
            sys.exit(0)
        else:
            print("❌ Failure: MkDocs dimension pages are out of sync. Run 'python generate_docs_from_json.py' to update.")
            sys.exit(1)
    else:
        print(f"\n✨ Generation Complete! {len(dims)} dimension pages created/updated in '{dim_out_dir}'.")

if __name__ == "__main__":
    main()
