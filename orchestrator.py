import json
from typing import TypedDict, List
from langgraph.graph import StateGraph, END
import ollama

# 1. Define the unified State
class AgentState(TypedDict):
    raw_data: str
    analysis: str
    sanitized_output: str
    xai_report: str 

# --- AGENT 1: The Analyst ---
def analyst_node(state: AgentState):
    print("--- [Agent] Analyst is processing data ---")
    data = state['raw_data']
    # Simulated insight - in real world, this would process the 'data' variable
    analysis = f"Statistical Summary: Found 3 transactions above €5000 for client in Berlin. Risk level: Moderate."
    return {"analysis": analysis}

# --- AGENT 2: The Privacy Auditor ---
def privacy_auditor_node(state: AgentState):
    print("--- [Agent] Privacy Auditor Redacting ---")
    
    # We provide an example (Few-Shot) to guide the model
    prompt = f"""
    ROLE: You are an automated GDPR Redaction Engine for a Private Bank. 
    TASK: Replace Names, Addresses, and exact Amounts with [REDACTED].
    
    ### EXAMPLE ###
    INPUT: "Transaction for John Doe of 500 Euro in Paris."
    OUTPUT: "Transaction for [REDACTED] of [REDACTED] in [REDACTED]."
    
    ### YOUR TASK ###
    INPUT: "{state['analysis']}"
    OUTPUT:
    """
    
    response = ollama.chat(model='llama3.2', messages=[{'role': 'user', 'content': prompt}])
    return {"sanitized_output": response['message']['content']}

# --- AGENT 3: The XAI Explainer ---
def xai_explainer_node(state: AgentState):
    print("--- [Agent] XAI Explainer Justifying ---")
    prompt = f"""
    ROLE: High-Risk AI Transparency Officer.
    TASK: Explain the legal basis (GDPR Article 5) for why the previous agent redacted PII in this text.
    TEXT: {state['sanitized_output']}
    """
    response = ollama.chat(model='llama3.2', messages=[{'role': 'user', 'content': prompt}])
    return {"xai_report": response['message']['content']}

# --- BUILD THE GRAPH ---
workflow = StateGraph(AgentState)

workflow.add_node("analyst", analyst_node)
workflow.add_node("auditor", privacy_auditor_node)
workflow.add_node("xai_explainer", xai_explainer_node)

workflow.set_entry_point("analyst")
workflow.add_edge("analyst", "auditor")
workflow.add_edge("auditor", "xai_explainer")
workflow.add_edge("xai_explainer", END)

app = workflow.compile()