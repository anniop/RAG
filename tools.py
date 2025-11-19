# tools.py
import os
import requests
from typing import Dict, Any

# ---------------- calculator tool ----------------
def calculator_tool(expr: str) -> Dict[str, Any]:
    """
    Safe math evaluator. Supports numbers, + - * / **, parentheses, and math functions.
    Returns dict with success/result or success/error.
    """
    import ast
    import math as _math

    allowed_names = {k: getattr(_math, k) for k in dir(_math) if not k.startswith("__")}
    allowed_names.update({"abs": abs, "round": round})

    node = ast.parse(expr, mode="eval")

    def _eval(n):
        import ast
        if isinstance(n, ast.Expression):
            return _eval(n.body)
        if isinstance(n, ast.Constant):  # Python 3.8+: Constant for numbers/strings
            return n.value
        if isinstance(n, ast.Num):
            return n.n
        if isinstance(n, ast.BinOp):
            left = _eval(n.left)
            right = _eval(n.right)
            if isinstance(n.op, ast.Add):
                return left + right
            if isinstance(n.op, ast.Sub):
                return left - right
            if isinstance(n.op, ast.Mult):
                return left * right
            if isinstance(n.op, ast.Div):
                return left / right
            if isinstance(n.op, ast.Pow):
                return left ** right
            if isinstance(n.op, ast.Mod):
                return left % right
            raise ValueError("Unsupported binary op")
        if isinstance(n, ast.UnaryOp):
            if isinstance(n.op, ast.UAdd):
                return +_eval(n.operand)
            if isinstance(n.op, ast.USub):
                return -_eval(n.operand)
        if isinstance(n, ast.Call):
            if isinstance(n.func, ast.Name):
                fn = n.func.id
                if fn in allowed_names:
                    args = [_eval(a) for a in n.args]
                    return allowed_names[fn](*args)
            raise ValueError("Function not allowed or unsupported call")
        if isinstance(n, ast.Name):
            if n.id in allowed_names:
                return allowed_names[n.id]
            raise ValueError("Name not allowed")
        raise ValueError("Unsupported expression")

    try:
        result = _eval(node)
        return {"success": True, "result": result}
    except Exception as e:
        return {"success": False, "error": str(e)}


# ---------------- web_search tool ----------------
def web_search_tool(query: str) -> Dict[str, Any]:
    """
    Uses SerpAPI if SERPAPI_API_KEY present, otherwise DuckDuckGo Instant Answer.
    Returns a small JSON-friendly dict.
    """
    serp_key = os.getenv("SERPAPI_API_KEY")
    if serp_key:
        try:
            resp = requests.get("https://serpapi.com/search.json", params={"q": query, "api_key": serp_key}, timeout=10)
            data = resp.json()
            results = []
            for r in data.get("organic_results", [])[:5]:
                results.append({"title": r.get("title"), "link": r.get("link"), "snippet": r.get("snippet")})
            return {"success": True, "source": "serpapi", "results": results}
        except Exception as e:
            return {"success": False, "error": str(e)}
    else:
        try:
            resp = requests.get("https://api.duckduckgo.com/", params={"q": query, "format": "json"}, timeout=10)
            data = resp.json()
            abstract = data.get("AbstractText") or data.get("AbstractURL") or ""
            related = data.get("RelatedTopics", [])[:5]
            return {"success": True, "source": "duckduckgo", "abstract": abstract, "related": related}
        except Exception as e:
            return {"success": False, "error": str(e)}


# ---------------- email_sender tool (mock) ----------------
def email_sender_tool(recipient: str, subject: str, body: str) -> Dict[str, Any]:
    """
    Mock email sender for demo. For production integrate SendGrid/SMTP and secure keys.
    """
    # For demo, log to console and return success
    print(f"[MOCK EMAIL] To: {recipient} | Subject: {subject} | Body (first 200 chars): {body[:200]}")
    return {"success": True, "message": "Email queued (mock)"}
