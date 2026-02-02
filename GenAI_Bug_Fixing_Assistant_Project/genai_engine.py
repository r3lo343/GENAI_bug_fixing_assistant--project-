
    def genai_fix(code):
        # Simulated LLM reasoning (college demo friendly)
        if "==" in code and "=" in code:
            explanation = (
                "The AI model detected a common logical bug. "
                "You may be using assignment '=' instead of comparison '=='."
            )
            fixed_code = code.replace("=", "==", 1)
            return explanation, fixed_code

        if "NullPointerException" in code or "null" in code:
            explanation = (
                "The GenAI model predicts a null reference issue. "
                "Objects should be initialized before usage."
            )
            fixed_code = "// Initialize object before use
" + code
            return explanation, fixed_code

        explanation = (
            "The GenAI model analyzed your code. "
            "No syntax-level bug found, but logical validation is advised."
        )
        fixed_code = code
        return explanation, fixed_code
