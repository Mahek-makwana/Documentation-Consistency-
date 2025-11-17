# src/models/llm_suggester.py

def suggest_doc_fix(missing_functions):
    """Mock LLM — generate simple docstrings for missing functions."""
    if not missing_functions:
        return "✅ All functions are documented!"

    result = ""
    for f in missing_functions:
        result += f"def {f}():\n    '''Auto-generated docstring for {f}'''\n\n"
    return result

if __name__ == "__main__":
    example = ["load_data", "analyze_results"]
    print(suggest_doc_fix(example))

