"""Idempotency guard for a local single-process demo; persistent store pending."""
from threading import Lock
_lock=Lock();_results={}

def run_idempotent(buyer:str,key:str,fingerprint:str,create):
    """Return prior result for identical replay, reject key reuse with changed payload."""
    if not buyer or not key or not fingerprint:raise ValueError("Idempotency scope required")
    with _lock:
        scope=(buyer,key)
        if scope in _results:
            old_fp,result=_results[scope]
            if old_fp!=fingerprint:raise ValueError("Idempotency conflict")
            return result
        result=create()
        _results[scope]=(fingerprint,result)
        return result
