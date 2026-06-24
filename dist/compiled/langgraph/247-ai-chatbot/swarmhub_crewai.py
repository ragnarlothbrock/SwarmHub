# ==========================================================================
# GENERATED AUTOMATICALLY BY SWARMHUB FOR AGENT SWARM: 247-ai-chatbot
# TARGET RUNTIME: CrewAI (Memory Layer: in_memory | Thread: test_1)
# ==========================================================================

import importlib
import os
import sys
import sqlite3
import json
import time
import uuid
from pydantic import BaseModel, Field
# === SWARMHUB METADATA SOURCE MAP (LOSSLESS ROUND-TRIP ASSURANCE) ===
# SWARMHUB_METADATA_START
# {
#   "version": "agentic.io/v1alpha1",
#   "kind": "UniversalAgent",
#   "name": "247-ai-chatbot",
#   "runtime": {
#     "provider": "langgraph_extracted",
#     "model": "extracted_model",
#     "temperature": 0.2,
#     "max_tokens": null
#   },
#   "memory": {
#     "storage_backend": "in_memory",
#     "thread_id": "test_1",
#     "connection_string": "data/categories.db"
#   },
#   "system_prompt": "Extracted automatically via SwarmHub static AST source-slicing.",
#   "interfaces": [],
#   "state_schema": {},
#   "topology": {
#     "type": "StateMachine",
#     "initial_node": "requirements_gathering",
#     "nodes": [
#       {
#         "id": "approach_analysis",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/approach_analysis.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_TASK_KNOWLEDGE_RETRIEVAL",
#             "target_node": "task_knowledge_retrieval"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "task_knowledge_retrieval",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/task_knowledge_retrieval.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_CUSTOMIZED_APPROACH_GENERATION",
#             "target_node": "customized_approach_generation"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "customized_approach_generation",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/customized_approach_generation.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_END",
#             "target_node": "END"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "melody_generator",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/melody_generator.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_HARMONY_CREATOR",
#             "target_node": "harmony_creator"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "harmony_creator",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/harmony_creator.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_RHYTHM_ANALYZER",
#             "target_node": "rhythm_analyzer"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "rhythm_analyzer",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/rhythm_analyzer.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_STYLE_ADAPTER",
#             "target_node": "style_adapter"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "style_adapter",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/style_adapter.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_MIDI_CONVERTER",
#             "target_node": "midi_converter"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "midi_converter",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/midi_converter.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_END",
#             "target_node": "END"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "triage",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/triage.py",
#         "transitions": [],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "response_agent",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/response_agent.py",
#         "transitions": [],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "triage",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/triage.py",
#         "transitions": [],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "response_agent",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/response_agent.py",
#         "transitions": [],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "code_execution_node",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/code_execution_node.py",
#         "transitions": [],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "code_update_node",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/code_update_node.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_CODE_PATCHING_NODE",
#             "target_node": "code_patching_node"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "code_patching_node",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/code_patching_node.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_CODE_EXECUTION_NODE",
#             "target_node": "code_execution_node"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "bug_report_node",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/bug_report_node.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_MEMORY_SEARCH_NODE",
#             "target_node": "memory_search_node"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "memory_search_node",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/memory_search_node.py",
#         "transitions": [],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "memory_filter_node",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/memory_filter_node.py",
#         "transitions": [],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "memory_modification_node",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/memory_modification_node.py",
#         "transitions": [],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "memory_generation_node",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/memory_generation_node.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_CODE_UPDATE_NODE",
#             "target_node": "code_update_node"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "input_city",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/input_city.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_INPUT_INTERESTS",
#             "target_node": "input_interests"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "input_interests",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/input_interests.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_CREATE_ITINERARY",
#             "target_node": "create_itinerary"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "create_itinerary",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/create_itinerary.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_END",
#             "target_node": "END"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "get_weather",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/get_weather.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_ANALYZE_DISASTER",
#             "target_node": "analyze_disaster"
#           },
#           {
#             "on_condition": "GOTO_SOCIAL_MEDIA_MONITORING",
#             "target_node": "social_media_monitoring"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "analyze_disaster",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/analyze_disaster.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_ASSESS_SEVERITY",
#             "target_node": "assess_severity"
#           },
#           {
#             "on_condition": "GOTO_ASSESS_SEVERITY",
#             "target_node": "assess_severity"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "assess_severity",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/assess_severity.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_DATA_LOGGING",
#             "target_node": "data_logging"
#           },
#           {
#             "on_condition": "GOTO_DATA_LOGGING",
#             "target_node": "data_logging"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "data_logging",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/data_logging.py",
#         "transitions": [],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "emergency_response",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/emergency_response.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_SEND_EMAIL_ALERT",
#             "target_node": "send_email_alert"
#           },
#           {
#             "on_condition": "GOTO_SEND_EMAIL_ALERT",
#             "target_node": "send_email_alert"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "civil_defense_response",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/civil_defense_response.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_GET_HUMAN_VERIFICATION",
#             "target_node": "get_human_verification"
#           },
#           {
#             "on_condition": "GOTO_GET_HUMAN_VERIFICATION",
#             "target_node": "get_human_verification"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "public_works_response",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/public_works_response.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_GET_HUMAN_VERIFICATION",
#             "target_node": "get_human_verification"
#           },
#           {
#             "on_condition": "GOTO_GET_HUMAN_VERIFICATION",
#             "target_node": "get_human_verification"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "get_human_verification",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/get_human_verification.py",
#         "transitions": [],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "send_email_alert",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/send_email_alert.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_END",
#             "target_node": "END"
#           },
#           {
#             "on_condition": "GOTO_END",
#             "target_node": "END"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "handle_no_approval",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/handle_no_approval.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_END",
#             "target_node": "END"
#           },
#           {
#             "on_condition": "GOTO_END",
#             "target_node": "END"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "get_weather",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/get_weather.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_ANALYZE_DISASTER",
#             "target_node": "analyze_disaster"
#           },
#           {
#             "on_condition": "GOTO_SOCIAL_MEDIA_MONITORING",
#             "target_node": "social_media_monitoring"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "social_media_monitoring",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/social_media_monitoring.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_ANALYZE_DISASTER",
#             "target_node": "analyze_disaster"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "analyze_disaster",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/analyze_disaster.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_ASSESS_SEVERITY",
#             "target_node": "assess_severity"
#           },
#           {
#             "on_condition": "GOTO_ASSESS_SEVERITY",
#             "target_node": "assess_severity"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "assess_severity",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/assess_severity.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_DATA_LOGGING",
#             "target_node": "data_logging"
#           },
#           {
#             "on_condition": "GOTO_DATA_LOGGING",
#             "target_node": "data_logging"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "data_logging",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/data_logging.py",
#         "transitions": [],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "emergency_response",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/emergency_response.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_SEND_EMAIL_ALERT",
#             "target_node": "send_email_alert"
#           },
#           {
#             "on_condition": "GOTO_SEND_EMAIL_ALERT",
#             "target_node": "send_email_alert"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "civil_defense_response",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/civil_defense_response.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_GET_HUMAN_VERIFICATION",
#             "target_node": "get_human_verification"
#           },
#           {
#             "on_condition": "GOTO_GET_HUMAN_VERIFICATION",
#             "target_node": "get_human_verification"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "public_works_response",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/public_works_response.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_GET_HUMAN_VERIFICATION",
#             "target_node": "get_human_verification"
#           },
#           {
#             "on_condition": "GOTO_GET_HUMAN_VERIFICATION",
#             "target_node": "get_human_verification"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "get_human_verification",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/get_human_verification.py",
#         "transitions": [],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "send_email_alert",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/send_email_alert.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_END",
#             "target_node": "END"
#           },
#           {
#             "on_condition": "GOTO_END",
#             "target_node": "END"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "handle_no_approval",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/handle_no_approval.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_END",
#             "target_node": "END"
#           },
#           {
#             "on_condition": "GOTO_END",
#             "target_node": "END"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "assistant",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/assistant.py",
#         "transitions": [],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "tools",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/tools.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_ASSISTANT",
#             "target_node": "assistant"
#           },
#           {
#             "on_condition": "GOTO_ASSISTANT",
#             "target_node": "assistant"
#           },
#           {
#             "on_condition": "GOTO_AGENT",
#             "target_node": "agent"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "generate_new_inputs",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/generate_new_inputs.py",
#         "transitions": [],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "static_test",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/static_test.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_GENERATE_NODE_DESCRIPTIONS",
#             "target_node": "generate_node_descriptions"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "generate_node_descriptions",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/generate_node_descriptions.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_GENERATE_TESTERS",
#             "target_node": "generate_testers"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "generate_testers",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/generate_testers.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_GENERATE_TEST_CASES",
#             "target_node": "generate_test_cases"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "generate_test_cases",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/generate_test_cases.py",
#         "transitions": [],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "run_test_cases",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/run_test_cases.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_ANALIZE_RESULTS",
#             "target_node": "analize_results"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "analize_results",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/analize_results.py",
#         "transitions": [],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "assistant",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/assistant.py",
#         "transitions": [],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "tools",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/tools.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_ASSISTANT",
#             "target_node": "assistant"
#           },
#           {
#             "on_condition": "GOTO_ASSISTANT",
#             "target_node": "assistant"
#           },
#           {
#             "on_condition": "GOTO_AGENT",
#             "target_node": "agent"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "process_input",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/process_input.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_PLANNER",
#             "target_node": "planner"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "planner",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/planner.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_RESEARCHER",
#             "target_node": "researcher"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "researcher",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/researcher.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_SEARCH_ARTICLES",
#             "target_node": "search_articles"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "search_articles",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/search_articles.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_ARTICLE_DECISIONS",
#             "target_node": "article_decisions"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "article_decisions",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/article_decisions.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_DOWNLOAD_ARTICLES",
#             "target_node": "download_articles"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "download_articles",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/download_articles.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_PAPER_ANALYZER",
#             "target_node": "paper_analyzer"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "paper_analyzer",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/paper_analyzer.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_WRITE_ABSTRACT",
#             "target_node": "write_abstract"
#           },
#           {
#             "on_condition": "GOTO_WRITE_INTRODUCTION",
#             "target_node": "write_introduction"
#           },
#           {
#             "on_condition": "GOTO_WRITE_METHODS",
#             "target_node": "write_methods"
#           },
#           {
#             "on_condition": "GOTO_WRITE_RESULTS",
#             "target_node": "write_results"
#           },
#           {
#             "on_condition": "GOTO_WRITE_CONCLUSION",
#             "target_node": "write_conclusion"
#           },
#           {
#             "on_condition": "GOTO_WRITE_REFERENCES",
#             "target_node": "write_references"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "write_abstract",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/write_abstract.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_AGGREGATE_PAPER",
#             "target_node": "aggregate_paper"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "write_introduction",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/write_introduction.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_AGGREGATE_PAPER",
#             "target_node": "aggregate_paper"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "write_methods",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/write_methods.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_AGGREGATE_PAPER",
#             "target_node": "aggregate_paper"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "write_results",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/write_results.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_AGGREGATE_PAPER",
#             "target_node": "aggregate_paper"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "write_conclusion",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/write_conclusion.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_AGGREGATE_PAPER",
#             "target_node": "aggregate_paper"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "write_references",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/write_references.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_AGGREGATE_PAPER",
#             "target_node": "aggregate_paper"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "aggregate_paper",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/aggregate_paper.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_CRITIQUE_PAPER",
#             "target_node": "critique_paper"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "critique_paper",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/critique_paper.py",
#         "transitions": [],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "revise_paper",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/revise_paper.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_CRITIQUE_PAPER",
#             "target_node": "critique_paper"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "final_draft",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/final_draft.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_END",
#             "target_node": "END"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "task_generation",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/task_generation.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_TASK_DEPENDENCIES",
#             "target_node": "task_dependencies"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "task_dependencies",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/task_dependencies.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_TASK_SCHEDULER",
#             "target_node": "task_scheduler"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "task_scheduler",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/task_scheduler.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_TASK_ALLOCATOR",
#             "target_node": "task_allocator"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "task_allocator",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/task_allocator.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_RISK_ASSESSOR",
#             "target_node": "risk_assessor"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "risk_assessor",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/risk_assessor.py",
#         "transitions": [],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "insight_generator",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/insight_generator.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_TASK_SCHEDULER",
#             "target_node": "task_scheduler"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "create_project_plan",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/create_project_plan.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_END",
#             "target_node": "END"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "requirements_gathering",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/requirements_gathering.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_GENERATE_JOB_DESC",
#             "target_node": "generate_job_desc"
#           },
#           {
#             "on_condition": "GOTO_GENERATE_JOB_DESC",
#             "target_node": "generate_job_desc"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "generate_job_desc",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/generate_job_desc.py",
#         "transitions": [],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "linkedin_process",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/linkedin_process.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_ANALYZE_CV",
#             "target_node": "analyze_cv"
#           },
#           {
#             "on_condition": "GOTO_ANALYZE_CV",
#             "target_node": "analyze_cv"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "analyze_cv",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/analyze_cv.py",
#         "transitions": [],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "prepare_interview",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/prepare_interview.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_END",
#             "target_node": "END"
#           },
#           {
#             "on_condition": "GOTO_END",
#             "target_node": "END"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "check_relevance",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/check_relevance.py",
#         "transitions": [],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "check_grammar",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/check_grammar.py",
#         "transitions": [],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "analyze_structure",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/analyze_structure.py",
#         "transitions": [],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "evaluate_depth",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/evaluate_depth.py",
#         "transitions": [],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "calculate_final_score",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/calculate_final_score.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_END",
#             "target_node": "END"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "generate_query",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/generate_query.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_SEARCH_WEB",
#             "target_node": "search_web"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "search_web",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/search_web.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_GENERATE_QUESTION",
#             "target_node": "generate_question"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "chunk_context",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/chunk_context.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_CONTEXT_VALIDATION",
#             "target_node": "context_validation"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "context_validation",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/context_validation.py",
#         "transitions": [],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "generate_checkpoints",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/generate_checkpoints.py",
#         "transitions": [],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "generate_question",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/generate_question.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_USER_ANSWER",
#             "target_node": "user_answer"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "next_checkpoint",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/next_checkpoint.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_GENERATE_QUESTION",
#             "target_node": "generate_question"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "user_answer",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/user_answer.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_VERIFY_ANSWER",
#             "target_node": "verify_answer"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "verify_answer",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/verify_answer.py",
#         "transitions": [],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "teach_concept",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/teach_concept.py",
#         "transitions": [],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "tour_introduction",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/tour_introduction.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_DISPLAY_ARTWORK",
#             "target_node": "display_artwork"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "display_artwork",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/display_artwork.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_DISCUSS",
#             "target_node": "discuss"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "get_next_artwork",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/get_next_artwork.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_DISPLAY_ARTWORK",
#             "target_node": "display_artwork"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "discuss",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/discuss.py",
#         "transitions": [],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "conclude_tour",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/conclude_tour.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_END",
#             "target_node": "END"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "character_introduction",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/character_introduction.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_ASK_QUESTION",
#             "target_node": "ask_question"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "ask_question",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/ask_question.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_HUMAN_DISCUSS",
#             "target_node": "human_discuss"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "answer_question",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/answer_question.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_ASK_QUESTION",
#             "target_node": "ask_question"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "create_characters",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/create_characters.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_CREATE_STORY",
#             "target_node": "create_story"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "create_story",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/create_story.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_NARRARTOR",
#             "target_node": "narrartor"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "narrartor",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/narrartor.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_SHERLOCK",
#             "target_node": "sherlock"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "sherlock",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/sherlock.py",
#         "transitions": [],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "guesser",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/guesser.py",
#         "transitions": [],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "conversation",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/conversation.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_SHERLOCK",
#             "target_node": "sherlock"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "summary_node",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/summary_node.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_RESEARCH_NODE",
#             "target_node": "research_node"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "research_node",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/research_node.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_INTENT_MATCHING_NODE",
#             "target_node": "intent_matching_node"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "intent_matching_node",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/intent_matching_node.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_INSTAGRAM",
#             "target_node": "instagram"
#           },
#           {
#             "on_condition": "GOTO_TWITTER",
#             "target_node": "twitter"
#           },
#           {
#             "on_condition": "GOTO_LINKEDIN",
#             "target_node": "linkedin"
#           },
#           {
#             "on_condition": "GOTO_BLOG",
#             "target_node": "blog"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "instagram",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/instagram.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_COMBINE_CONTENT",
#             "target_node": "combine_content"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "twitter",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/twitter.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_COMBINE_CONTENT",
#             "target_node": "combine_content"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "linkedin",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/linkedin.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_COMBINE_CONTENT",
#             "target_node": "combine_content"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "blog",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/blog.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_COMBINE_CONTENT",
#             "target_node": "combine_content"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "combine_content",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/combine_content.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_END",
#             "target_node": "END"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "generate_character_description",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/generate_character_description.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_GENERATE_PLOT",
#             "target_node": "generate_plot"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "generate_plot",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/generate_plot.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_GENERATE_IMAGE_PROMPTS",
#             "target_node": "generate_image_prompts"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "generate_image_prompts",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/generate_image_prompts.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_CREATE_IMAGES",
#             "target_node": "create_images"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "create_images",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/create_images.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_CREATE_GIF",
#             "target_node": "create_gif"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "create_gif",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/create_gif.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_END",
#             "target_node": "END"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "classify_content",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/classify_content.py",
#         "transitions": [],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "process_general",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/process_general.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_TEXT_TO_SPEECH",
#             "target_node": "text_to_speech"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "process_poem",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/process_poem.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_TEXT_TO_SPEECH",
#             "target_node": "text_to_speech"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "process_news",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/process_news.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_TEXT_TO_SPEECH",
#             "target_node": "text_to_speech"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "process_joke",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/process_joke.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_TEXT_TO_SPEECH",
#             "target_node": "text_to_speech"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "text_to_speech",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/text_to_speech.py",
#         "transitions": [],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "categorize",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/categorize.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_ANALYZE_SENTIMENT",
#             "target_node": "analyze_sentiment"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "handle_learning_resource",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/handle_learning_resource.py",
#         "transitions": [],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "handle_resume_making",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/handle_resume_making.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_END",
#             "target_node": "END"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "handle_interview_preparation",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/handle_interview_preparation.py",
#         "transitions": [],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "job_search",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/job_search.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_END",
#             "target_node": "END"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "mock_interview",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/mock_interview.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_END",
#             "target_node": "END"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "interview_topics_questions",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/interview_topics_questions.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_END",
#             "target_node": "END"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "tutorial_agent",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/tutorial_agent.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_END",
#             "target_node": "END"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "ask_query_bot",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/ask_query_bot.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_END",
#             "target_node": "END"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "calendar_analyzer",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/calendar_analyzer.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_TASK_ANALYZER",
#             "target_node": "task_analyzer"
#           },
#           {
#             "on_condition": "GOTO_TASK_ANALYZER",
#             "target_node": "task_analyzer"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "task_analyzer",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/task_analyzer.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_PLAN_GENERATOR",
#             "target_node": "plan_generator"
#           },
#           {
#             "on_condition": "GOTO_PLAN_GENERATOR",
#             "target_node": "plan_generator"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "plan_generator",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/plan_generator.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_EXECUTE",
#             "target_node": "execute"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "notewriter_analyze",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/notewriter_analyze.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_NOTEWRITER_GENERATE",
#             "target_node": "notewriter_generate"
#           },
#           {
#             "on_condition": "GOTO_NOTEWRITER_GENERATE",
#             "target_node": "notewriter_generate"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "notewriter_generate",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/notewriter_generate.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_END",
#             "target_node": "END"
#           },
#           {
#             "on_condition": "GOTO_EXECUTE",
#             "target_node": "execute"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "advisor_analyze",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/advisor_analyze.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_ADVISOR_GENERATE",
#             "target_node": "advisor_generate"
#           },
#           {
#             "on_condition": "GOTO_ADVISOR_GENERATE",
#             "target_node": "advisor_generate"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "advisor_generate",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/advisor_generate.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_END",
#             "target_node": "END"
#           },
#           {
#             "on_condition": "GOTO_EXECUTE",
#             "target_node": "execute"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "coordinator",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/coordinator.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_PROFILE_ANALYZER",
#             "target_node": "profile_analyzer"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "profile_analyzer",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/profile_analyzer.py",
#         "transitions": [],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "execute",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/execute.py",
#         "transitions": [],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "calendar_analyzer",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/calendar_analyzer.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_TASK_ANALYZER",
#             "target_node": "task_analyzer"
#           },
#           {
#             "on_condition": "GOTO_TASK_ANALYZER",
#             "target_node": "task_analyzer"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "task_analyzer",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/task_analyzer.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_PLAN_GENERATOR",
#             "target_node": "plan_generator"
#           },
#           {
#             "on_condition": "GOTO_PLAN_GENERATOR",
#             "target_node": "plan_generator"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "plan_generator",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/plan_generator.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_EXECUTE",
#             "target_node": "execute"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "notewriter_analyze",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/notewriter_analyze.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_NOTEWRITER_GENERATE",
#             "target_node": "notewriter_generate"
#           },
#           {
#             "on_condition": "GOTO_NOTEWRITER_GENERATE",
#             "target_node": "notewriter_generate"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "notewriter_generate",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/notewriter_generate.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_END",
#             "target_node": "END"
#           },
#           {
#             "on_condition": "GOTO_EXECUTE",
#             "target_node": "execute"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "advisor_analyze",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/advisor_analyze.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_ADVISOR_GENERATE",
#             "target_node": "advisor_generate"
#           },
#           {
#             "on_condition": "GOTO_ADVISOR_GENERATE",
#             "target_node": "advisor_generate"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "advisor_generate",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/advisor_generate.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_END",
#             "target_node": "END"
#           },
#           {
#             "on_condition": "GOTO_EXECUTE",
#             "target_node": "execute"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "convert_user_instruction_to_actions",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/convert_user_instruction_to_actions.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_GET_INITIAL_ACTION",
#             "target_node": "get_initial_action"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "get_initial_action",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/get_initial_action.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_GET_WEBSITE_STATE",
#             "target_node": "get_website_state"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "get_website_state",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/get_website_state.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_GENERATE_CODE_FOR_ACTION",
#             "target_node": "generate_code_for_action"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "generate_code_for_action",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/generate_code_for_action.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_VALIDATE_GENERATED_ACTION",
#             "target_node": "validate_generated_action"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "validate_generated_action",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/validate_generated_action.py",
#         "transitions": [],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "handle_generation_error",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/handle_generation_error.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_END",
#             "target_node": "END"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "post_process_script",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/post_process_script.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_EXECUTE_TEST_CASE",
#             "target_node": "execute_test_case"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "execute_test_case",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/execute_test_case.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_GENERATE_TEST_REPORT",
#             "target_node": "generate_test_report"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "generate_test_report",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/generate_test_report.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_END",
#             "target_node": "END"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "categorize",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/categorize.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_ANALYZE_SENTIMENT",
#             "target_node": "analyze_sentiment"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "analyze_sentiment",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/analyze_sentiment.py",
#         "transitions": [],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "handle_technical",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/handle_technical.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_END",
#             "target_node": "END"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "handle_billing",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/handle_billing.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_END",
#             "target_node": "END"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "handle_general",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/handle_general.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_END",
#             "target_node": "END"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "escalate",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/escalate.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_END",
#             "target_node": "END"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "get_website_content",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/get_website_content.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_ANALYZE_COMPANY",
#             "target_node": "analyze_company"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "analyze_company",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/analyze_company.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_GENERATE_CONCEPTS",
#             "target_node": "generate_concepts"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "generate_concepts",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/generate_concepts.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_SELECT_TEMPLATES",
#             "target_node": "select_templates"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "select_templates",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/select_templates.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_GENERATE_TEXT",
#             "target_node": "generate_text"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "generate_text",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/generate_text.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_CREATE_URL",
#             "target_node": "create_url"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "create_url",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/create_url.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_END",
#             "target_node": "END"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "tavily_search",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/tavily_search.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_SCHEMA_MAPPING",
#             "target_node": "schema_mapping"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "schema_mapping",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/schema_mapping.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_PRODUCT_COMPARISON",
#             "target_node": "product_comparison"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "product_comparison",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/product_comparison.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_YOUTUBE_REVIEW",
#             "target_node": "youtube_review"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "youtube_review",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/youtube_review.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_DISPLAY",
#             "target_node": "display"
#           },
#           {
#             "on_condition": "GOTO_SEND_EMAIL",
#             "target_node": "send_email"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "display",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/display.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_END",
#             "target_node": "END"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "send_email",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/send_email.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_END",
#             "target_node": "END"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "classify_input",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/classify_input.py",
#         "transitions": [],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "discover_database",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/discover_database.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_CREATE_PLAN",
#             "target_node": "create_plan"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "create_plan",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/create_plan.py",
#         "transitions": [],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "execute_plan",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/execute_plan.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_GENERATE_RESPONSE",
#             "target_node": "generate_response"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "generate_response",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/generate_response.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_END",
#             "target_node": "END"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "generate_newsapi_params",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/generate_newsapi_params.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_RETRIEVE_ARTICLES_METADATA",
#             "target_node": "retrieve_articles_metadata"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "retrieve_articles_metadata",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/retrieve_articles_metadata.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_RETRIEVE_ARTICLES_TEXT",
#             "target_node": "retrieve_articles_text"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "retrieve_articles_text",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/retrieve_articles_text.py",
#         "transitions": [],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "select_top_urls",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/select_top_urls.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_SUMMARIZE_ARTICLES_PARALLEL",
#             "target_node": "summarize_articles_parallel"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "summarize_articles_parallel",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/summarize_articles_parallel.py",
#         "transitions": [],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "format_results",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/format_results.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_END",
#             "target_node": "END"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "decision_making",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/decision_making.py",
#         "transitions": [],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "planning",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/planning.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_AGENT",
#             "target_node": "agent"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "tools",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/tools.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_ASSISTANT",
#             "target_node": "assistant"
#           },
#           {
#             "on_condition": "GOTO_ASSISTANT",
#             "target_node": "assistant"
#           },
#           {
#             "on_condition": "GOTO_AGENT",
#             "target_node": "agent"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "agent",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/agent.py",
#         "transitions": [],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "judge",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/judge.py",
#         "transitions": [],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "CATEGORY",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/CATEGORY.py",
#         "transitions": [],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "SUMMARY",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/SUMMARY.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_END",
#             "target_node": "END"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "FACT_CHECKING",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/FACT_CHECKING.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_END",
#             "target_node": "END"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "TONE_ANALYSIS",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/TONE_ANALYSIS.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_END",
#             "target_node": "END"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "QUOTE_EXTRACTION",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/QUOTE_EXTRACTION.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_END",
#             "target_node": "END"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "GRAMMAR_AND_BIAS_REVIEW",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/GRAMMAR_AND_BIAS_REVIEW.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_END",
#             "target_node": "END"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "web_download",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/web_download.py",
#         "transitions": [],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "embeddings_ner",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/embeddings_ner.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_PREPARE_TOPIC",
#             "target_node": "prepare_topic"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "main_assistant",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/main_assistant.py",
#         "transitions": [],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "main_assistant_tools",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/main_assistant_tools.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_UPDATE_STATE",
#             "target_node": "update_state"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "underwriting_assistant",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/underwriting_assistant.py",
#         "transitions": [],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "quote_assistant",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/quote_assistant.py",
#         "transitions": [],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "quote_assistant_tools",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/quote_assistant_tools.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_QUOTE_ASSISTANT",
#             "target_node": "quote_assistant"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "entry_quote_assistant",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/entry_quote_assistant.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_QUOTE_ASSISTANT",
#             "target_node": "quote_assistant"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "retrieve",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/retrieve.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_REASONING",
#             "target_node": "reasoning"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "reasoning",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/reasoning.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_CLASSIFICATION_GRADING",
#             "target_node": "classification_grading"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "classification_grading",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/classification_grading.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_PASS_FINAL_CLASSIFICATIONS",
#             "target_node": "pass_final_classifications"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "update_state",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/update_state.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_MAIN_ASSISTANT",
#             "target_node": "main_assistant"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "reroute",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/reroute.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_MAIN_ASSISTANT",
#             "target_node": "main_assistant"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "pass_tool_call_id",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/pass_tool_call_id.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_RETRIEVE",
#             "target_node": "retrieve"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "pass_final_classifications",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/pass_final_classifications.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_CREATE_TOOL_MESSAGE",
#             "target_node": "create_tool_message"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "create_tool_message",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/create_tool_message.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_UNDERWRITING_ASSISTANT",
#             "target_node": "underwriting_assistant"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "update_workflow_state",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/update_workflow_state.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_ENTRY_QUOTE_ASSISTANT",
#             "target_node": "entry_quote_assistant"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "ask_user_needs",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/ask_user_needs.py",
#         "transitions": [],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "build_filters",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/build_filters.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_SEARCH_LISTINGS",
#             "target_node": "search_listings"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "search_listings",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/search_listings.py",
#         "transitions": [],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "fetch_additional_info",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/fetch_additional_info.py",
#         "transitions": [],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "irrelevant",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/irrelevant.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_END",
#             "target_node": "END"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "classify_contract",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/classify_contract.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_RETRIEVE_CLAUSES",
#             "target_node": "retrieve_clauses"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "retrieve_clauses",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/retrieve_clauses.py",
#         "transitions": [],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "execute_step_clause",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/execute_step_clause.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_CREATE_REVIEW_PLAN",
#             "target_node": "create_review_plan"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "create_review_plan",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/create_review_plan.py",
#         "transitions": [],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "execute_step",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/execute_step.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_GENERATE_FINAL_REPORT",
#             "target_node": "generate_final_report"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "generate_final_report",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/generate_final_report.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_END",
#             "target_node": "END"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "search",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/search.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_SUMMARIZE",
#             "target_node": "summarize"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "summarize",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/summarize.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_PUBLISH",
#             "target_node": "publish"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "publish",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/publish.py",
#         "transitions": [],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "Keywords",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/Keywords.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_STRUCTURE",
#             "target_node": "Structure"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "Structure",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/Structure.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_END",
#             "target_node": "END"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "Host question",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/Host question.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_WEB RESEARCH",
#             "target_node": "Web research"
#           },
#           {
#             "on_condition": "GOTO_WIKI RESEARCH",
#             "target_node": "Wiki research"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "Web research",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/Web research.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_EXPERT ANSWER",
#             "target_node": "Expert answer"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "Wiki research",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/Wiki research.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_EXPERT ANSWER",
#             "target_node": "Expert answer"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "Expert answer",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/Expert answer.py",
#         "transitions": [],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "Save podcast",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/Save podcast.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_WRITE SCRIPT",
#             "target_node": "Write script"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "Write script",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/Write script.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_END",
#             "target_node": "END"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "Planing",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/Planing.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_START RESEARCH",
#             "target_node": "Start research"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "Start research",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/Start research.py",
#         "transitions": [],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "Create podcast",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/Create podcast.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_WRITE REPORT",
#             "target_node": "Write report"
#           },
#           {
#             "on_condition": "GOTO_WRITE INTRODUCTION",
#             "target_node": "Write introduction"
#           },
#           {
#             "on_condition": "GOTO_WRITE CONCLUSION",
#             "target_node": "Write conclusion"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "Write report",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/Write report.py",
#         "transitions": [],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "Write introduction",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/Write introduction.py",
#         "transitions": [],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "Write conclusion",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/Write conclusion.py",
#         "transitions": [],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "Finalize podcast",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/Finalize podcast.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_END",
#             "target_node": "END"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "requirements_gathering",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/requirements_gathering.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_GENERATE_JOB_DESC",
#             "target_node": "generate_job_desc"
#           },
#           {
#             "on_condition": "GOTO_GENERATE_JOB_DESC",
#             "target_node": "generate_job_desc"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "generate_job_desc",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/generate_job_desc.py",
#         "transitions": [],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "linkedin_process",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/linkedin_process.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_ANALYZE_CV",
#             "target_node": "analyze_cv"
#           },
#           {
#             "on_condition": "GOTO_ANALYZE_CV",
#             "target_node": "analyze_cv"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "analyze_cv",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/analyze_cv.py",
#         "transitions": [],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "prepare_interview",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/prepare_interview.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_END",
#             "target_node": "END"
#           },
#           {
#             "on_condition": "GOTO_END",
#             "target_node": "END"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "classification_node",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/classification_node.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_ENTITY_EXTRACTION",
#             "target_node": "entity_extraction"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "entity_extraction",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/entity_extraction.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_SUMMARIZATION",
#             "target_node": "summarization"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       },
#       {
#         "id": "summarization",
#         "executor_type": "opaque_blob",
#         "executor_reference": "blobs/summarization.py",
#         "transitions": [
#           {
#             "on_condition": "GOTO_END",
#             "target_node": "END"
#           }
#         ],
#         "tools": [
#           "ToQuoteAssistant"
#         ],
#         "interfaces": []
#       }
#     ]
#   }
# }
# SWARMHUB_METADATA_END

from crewai import Agent, Task, Crew, Process
from crewai.tools import tool

# 1. Patch Runtime Environment Paths to discover localized Code Blobs
sys.path.insert(0, os.getcwd())

# 2. Initialize Global Runtime Configurations
# Selected Provider Context: langgraph_extracted
# Selected Model Target: extracted_model

# 3. Define functional stubs for cross-compiled tools
@tool("ToQuoteAssistant")
def ToQuoteAssistant(*args, **kwargs):
    """Cross-compiled SwarmHub capability artifact: ToQuoteAssistant"""
    return "Tool execution fallback payload finished."

# 3.2 Initialize Registered Global MCP Capability Interface Targets
GLOBAL_INTERFACES_REGISTRY = {}

# 4. Define strict Data Contract Verification Model schemas
class SharedContextContract(BaseModel):
    pass

# 5. Define Autonomous Agent Personas dynamically from Topology
approach_analysis_agent = Agent(
    role="Approach Analysis",
    goal="Execute capabilities defined under the workspace node approach_analysis",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

task_knowledge_retrieval_agent = Agent(
    role="Task Knowledge Retrieval",
    goal="Execute capabilities defined under the workspace node task_knowledge_retrieval",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

customized_approach_generation_agent = Agent(
    role="Customized Approach Generation",
    goal="Execute capabilities defined under the workspace node customized_approach_generation",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

melody_generator_agent = Agent(
    role="Melody Generator",
    goal="Execute capabilities defined under the workspace node melody_generator",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

harmony_creator_agent = Agent(
    role="Harmony Creator",
    goal="Execute capabilities defined under the workspace node harmony_creator",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

rhythm_analyzer_agent = Agent(
    role="Rhythm Analyzer",
    goal="Execute capabilities defined under the workspace node rhythm_analyzer",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

style_adapter_agent = Agent(
    role="Style Adapter",
    goal="Execute capabilities defined under the workspace node style_adapter",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

midi_converter_agent = Agent(
    role="Midi Converter",
    goal="Execute capabilities defined under the workspace node midi_converter",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

triage_agent = Agent(
    role="Triage",
    goal="Execute capabilities defined under the workspace node triage",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

response_agent_agent = Agent(
    role="Response Agent",
    goal="Execute capabilities defined under the workspace node response_agent",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

triage_agent = Agent(
    role="Triage",
    goal="Execute capabilities defined under the workspace node triage",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

response_agent_agent = Agent(
    role="Response Agent",
    goal="Execute capabilities defined under the workspace node response_agent",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

code_execution_node_agent = Agent(
    role="Code Execution Node",
    goal="Execute capabilities defined under the workspace node code_execution_node",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

code_update_node_agent = Agent(
    role="Code Update Node",
    goal="Execute capabilities defined under the workspace node code_update_node",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

code_patching_node_agent = Agent(
    role="Code Patching Node",
    goal="Execute capabilities defined under the workspace node code_patching_node",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

bug_report_node_agent = Agent(
    role="Bug Report Node",
    goal="Execute capabilities defined under the workspace node bug_report_node",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

memory_search_node_agent = Agent(
    role="Memory Search Node",
    goal="Execute capabilities defined under the workspace node memory_search_node",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

memory_filter_node_agent = Agent(
    role="Memory Filter Node",
    goal="Execute capabilities defined under the workspace node memory_filter_node",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

memory_modification_node_agent = Agent(
    role="Memory Modification Node",
    goal="Execute capabilities defined under the workspace node memory_modification_node",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

memory_generation_node_agent = Agent(
    role="Memory Generation Node",
    goal="Execute capabilities defined under the workspace node memory_generation_node",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

input_city_agent = Agent(
    role="Input City",
    goal="Execute capabilities defined under the workspace node input_city",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

input_interests_agent = Agent(
    role="Input Interests",
    goal="Execute capabilities defined under the workspace node input_interests",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

create_itinerary_agent = Agent(
    role="Create Itinerary",
    goal="Execute capabilities defined under the workspace node create_itinerary",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

get_weather_agent = Agent(
    role="Get Weather",
    goal="Execute capabilities defined under the workspace node get_weather",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

analyze_disaster_agent = Agent(
    role="Analyze Disaster",
    goal="Execute capabilities defined under the workspace node analyze_disaster",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

assess_severity_agent = Agent(
    role="Assess Severity",
    goal="Execute capabilities defined under the workspace node assess_severity",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

data_logging_agent = Agent(
    role="Data Logging",
    goal="Execute capabilities defined under the workspace node data_logging",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

emergency_response_agent = Agent(
    role="Emergency Response",
    goal="Execute capabilities defined under the workspace node emergency_response",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

civil_defense_response_agent = Agent(
    role="Civil Defense Response",
    goal="Execute capabilities defined under the workspace node civil_defense_response",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

public_works_response_agent = Agent(
    role="Public Works Response",
    goal="Execute capabilities defined under the workspace node public_works_response",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

get_human_verification_agent = Agent(
    role="Get Human Verification",
    goal="Execute capabilities defined under the workspace node get_human_verification",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

send_email_alert_agent = Agent(
    role="Send Email Alert",
    goal="Execute capabilities defined under the workspace node send_email_alert",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

handle_no_approval_agent = Agent(
    role="Handle No Approval",
    goal="Execute capabilities defined under the workspace node handle_no_approval",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

get_weather_agent = Agent(
    role="Get Weather",
    goal="Execute capabilities defined under the workspace node get_weather",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

social_media_monitoring_agent = Agent(
    role="Social Media Monitoring",
    goal="Execute capabilities defined under the workspace node social_media_monitoring",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

analyze_disaster_agent = Agent(
    role="Analyze Disaster",
    goal="Execute capabilities defined under the workspace node analyze_disaster",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

assess_severity_agent = Agent(
    role="Assess Severity",
    goal="Execute capabilities defined under the workspace node assess_severity",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

data_logging_agent = Agent(
    role="Data Logging",
    goal="Execute capabilities defined under the workspace node data_logging",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

emergency_response_agent = Agent(
    role="Emergency Response",
    goal="Execute capabilities defined under the workspace node emergency_response",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

civil_defense_response_agent = Agent(
    role="Civil Defense Response",
    goal="Execute capabilities defined under the workspace node civil_defense_response",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

public_works_response_agent = Agent(
    role="Public Works Response",
    goal="Execute capabilities defined under the workspace node public_works_response",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

get_human_verification_agent = Agent(
    role="Get Human Verification",
    goal="Execute capabilities defined under the workspace node get_human_verification",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

send_email_alert_agent = Agent(
    role="Send Email Alert",
    goal="Execute capabilities defined under the workspace node send_email_alert",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

handle_no_approval_agent = Agent(
    role="Handle No Approval",
    goal="Execute capabilities defined under the workspace node handle_no_approval",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

assistant_agent = Agent(
    role="Assistant",
    goal="Execute capabilities defined under the workspace node assistant",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

tools_agent = Agent(
    role="Tools",
    goal="Execute capabilities defined under the workspace node tools",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

generate_new_inputs_agent = Agent(
    role="Generate New Inputs",
    goal="Execute capabilities defined under the workspace node generate_new_inputs",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

static_test_agent = Agent(
    role="Static Test",
    goal="Execute capabilities defined under the workspace node static_test",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

generate_node_descriptions_agent = Agent(
    role="Generate Node Descriptions",
    goal="Execute capabilities defined under the workspace node generate_node_descriptions",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

generate_testers_agent = Agent(
    role="Generate Testers",
    goal="Execute capabilities defined under the workspace node generate_testers",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

generate_test_cases_agent = Agent(
    role="Generate Test Cases",
    goal="Execute capabilities defined under the workspace node generate_test_cases",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

run_test_cases_agent = Agent(
    role="Run Test Cases",
    goal="Execute capabilities defined under the workspace node run_test_cases",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

analize_results_agent = Agent(
    role="Analize Results",
    goal="Execute capabilities defined under the workspace node analize_results",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

assistant_agent = Agent(
    role="Assistant",
    goal="Execute capabilities defined under the workspace node assistant",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

tools_agent = Agent(
    role="Tools",
    goal="Execute capabilities defined under the workspace node tools",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

process_input_agent = Agent(
    role="Process Input",
    goal="Execute capabilities defined under the workspace node process_input",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

planner_agent = Agent(
    role="Planner",
    goal="Execute capabilities defined under the workspace node planner",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

researcher_agent = Agent(
    role="Researcher",
    goal="Execute capabilities defined under the workspace node researcher",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

search_articles_agent = Agent(
    role="Search Articles",
    goal="Execute capabilities defined under the workspace node search_articles",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

article_decisions_agent = Agent(
    role="Article Decisions",
    goal="Execute capabilities defined under the workspace node article_decisions",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

download_articles_agent = Agent(
    role="Download Articles",
    goal="Execute capabilities defined under the workspace node download_articles",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

paper_analyzer_agent = Agent(
    role="Paper Analyzer",
    goal="Execute capabilities defined under the workspace node paper_analyzer",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

write_abstract_agent = Agent(
    role="Write Abstract",
    goal="Execute capabilities defined under the workspace node write_abstract",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

write_introduction_agent = Agent(
    role="Write Introduction",
    goal="Execute capabilities defined under the workspace node write_introduction",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

write_methods_agent = Agent(
    role="Write Methods",
    goal="Execute capabilities defined under the workspace node write_methods",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

write_results_agent = Agent(
    role="Write Results",
    goal="Execute capabilities defined under the workspace node write_results",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

write_conclusion_agent = Agent(
    role="Write Conclusion",
    goal="Execute capabilities defined under the workspace node write_conclusion",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

write_references_agent = Agent(
    role="Write References",
    goal="Execute capabilities defined under the workspace node write_references",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

aggregate_paper_agent = Agent(
    role="Aggregate Paper",
    goal="Execute capabilities defined under the workspace node aggregate_paper",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

critique_paper_agent = Agent(
    role="Critique Paper",
    goal="Execute capabilities defined under the workspace node critique_paper",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

revise_paper_agent = Agent(
    role="Revise Paper",
    goal="Execute capabilities defined under the workspace node revise_paper",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

final_draft_agent = Agent(
    role="Final Draft",
    goal="Execute capabilities defined under the workspace node final_draft",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

task_generation_agent = Agent(
    role="Task Generation",
    goal="Execute capabilities defined under the workspace node task_generation",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

task_dependencies_agent = Agent(
    role="Task Dependencies",
    goal="Execute capabilities defined under the workspace node task_dependencies",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

task_scheduler_agent = Agent(
    role="Task Scheduler",
    goal="Execute capabilities defined under the workspace node task_scheduler",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

task_allocator_agent = Agent(
    role="Task Allocator",
    goal="Execute capabilities defined under the workspace node task_allocator",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

risk_assessor_agent = Agent(
    role="Risk Assessor",
    goal="Execute capabilities defined under the workspace node risk_assessor",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

insight_generator_agent = Agent(
    role="Insight Generator",
    goal="Execute capabilities defined under the workspace node insight_generator",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

create_project_plan_agent = Agent(
    role="Create Project Plan",
    goal="Execute capabilities defined under the workspace node create_project_plan",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

requirements_gathering_agent = Agent(
    role="Requirements Gathering",
    goal="Execute capabilities defined under the workspace node requirements_gathering",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

generate_job_desc_agent = Agent(
    role="Generate Job Desc",
    goal="Execute capabilities defined under the workspace node generate_job_desc",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

linkedin_process_agent = Agent(
    role="Linkedin Process",
    goal="Execute capabilities defined under the workspace node linkedin_process",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

analyze_cv_agent = Agent(
    role="Analyze Cv",
    goal="Execute capabilities defined under the workspace node analyze_cv",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

prepare_interview_agent = Agent(
    role="Prepare Interview",
    goal="Execute capabilities defined under the workspace node prepare_interview",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

check_relevance_agent = Agent(
    role="Check Relevance",
    goal="Execute capabilities defined under the workspace node check_relevance",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

check_grammar_agent = Agent(
    role="Check Grammar",
    goal="Execute capabilities defined under the workspace node check_grammar",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

analyze_structure_agent = Agent(
    role="Analyze Structure",
    goal="Execute capabilities defined under the workspace node analyze_structure",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

evaluate_depth_agent = Agent(
    role="Evaluate Depth",
    goal="Execute capabilities defined under the workspace node evaluate_depth",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

calculate_final_score_agent = Agent(
    role="Calculate Final Score",
    goal="Execute capabilities defined under the workspace node calculate_final_score",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

generate_query_agent = Agent(
    role="Generate Query",
    goal="Execute capabilities defined under the workspace node generate_query",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

search_web_agent = Agent(
    role="Search Web",
    goal="Execute capabilities defined under the workspace node search_web",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

chunk_context_agent = Agent(
    role="Chunk Context",
    goal="Execute capabilities defined under the workspace node chunk_context",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

context_validation_agent = Agent(
    role="Context Validation",
    goal="Execute capabilities defined under the workspace node context_validation",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

generate_checkpoints_agent = Agent(
    role="Generate Checkpoints",
    goal="Execute capabilities defined under the workspace node generate_checkpoints",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

generate_question_agent = Agent(
    role="Generate Question",
    goal="Execute capabilities defined under the workspace node generate_question",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

next_checkpoint_agent = Agent(
    role="Next Checkpoint",
    goal="Execute capabilities defined under the workspace node next_checkpoint",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

user_answer_agent = Agent(
    role="User Answer",
    goal="Execute capabilities defined under the workspace node user_answer",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

verify_answer_agent = Agent(
    role="Verify Answer",
    goal="Execute capabilities defined under the workspace node verify_answer",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

teach_concept_agent = Agent(
    role="Teach Concept",
    goal="Execute capabilities defined under the workspace node teach_concept",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

tour_introduction_agent = Agent(
    role="Tour Introduction",
    goal="Execute capabilities defined under the workspace node tour_introduction",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

display_artwork_agent = Agent(
    role="Display Artwork",
    goal="Execute capabilities defined under the workspace node display_artwork",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

get_next_artwork_agent = Agent(
    role="Get Next Artwork",
    goal="Execute capabilities defined under the workspace node get_next_artwork",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

discuss_agent = Agent(
    role="Discuss",
    goal="Execute capabilities defined under the workspace node discuss",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

conclude_tour_agent = Agent(
    role="Conclude Tour",
    goal="Execute capabilities defined under the workspace node conclude_tour",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

character_introduction_agent = Agent(
    role="Character Introduction",
    goal="Execute capabilities defined under the workspace node character_introduction",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

ask_question_agent = Agent(
    role="Ask Question",
    goal="Execute capabilities defined under the workspace node ask_question",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

answer_question_agent = Agent(
    role="Answer Question",
    goal="Execute capabilities defined under the workspace node answer_question",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

create_characters_agent = Agent(
    role="Create Characters",
    goal="Execute capabilities defined under the workspace node create_characters",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

create_story_agent = Agent(
    role="Create Story",
    goal="Execute capabilities defined under the workspace node create_story",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

narrartor_agent = Agent(
    role="Narrartor",
    goal="Execute capabilities defined under the workspace node narrartor",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

sherlock_agent = Agent(
    role="Sherlock",
    goal="Execute capabilities defined under the workspace node sherlock",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

guesser_agent = Agent(
    role="Guesser",
    goal="Execute capabilities defined under the workspace node guesser",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

conversation_agent = Agent(
    role="Conversation",
    goal="Execute capabilities defined under the workspace node conversation",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

summary_node_agent = Agent(
    role="Summary Node",
    goal="Execute capabilities defined under the workspace node summary_node",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

research_node_agent = Agent(
    role="Research Node",
    goal="Execute capabilities defined under the workspace node research_node",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

intent_matching_node_agent = Agent(
    role="Intent Matching Node",
    goal="Execute capabilities defined under the workspace node intent_matching_node",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

instagram_agent = Agent(
    role="Instagram",
    goal="Execute capabilities defined under the workspace node instagram",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

twitter_agent = Agent(
    role="Twitter",
    goal="Execute capabilities defined under the workspace node twitter",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

linkedin_agent = Agent(
    role="Linkedin",
    goal="Execute capabilities defined under the workspace node linkedin",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

blog_agent = Agent(
    role="Blog",
    goal="Execute capabilities defined under the workspace node blog",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

combine_content_agent = Agent(
    role="Combine Content",
    goal="Execute capabilities defined under the workspace node combine_content",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

generate_character_description_agent = Agent(
    role="Generate Character Description",
    goal="Execute capabilities defined under the workspace node generate_character_description",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

generate_plot_agent = Agent(
    role="Generate Plot",
    goal="Execute capabilities defined under the workspace node generate_plot",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

generate_image_prompts_agent = Agent(
    role="Generate Image Prompts",
    goal="Execute capabilities defined under the workspace node generate_image_prompts",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

create_images_agent = Agent(
    role="Create Images",
    goal="Execute capabilities defined under the workspace node create_images",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

create_gif_agent = Agent(
    role="Create Gif",
    goal="Execute capabilities defined under the workspace node create_gif",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

classify_content_agent = Agent(
    role="Classify Content",
    goal="Execute capabilities defined under the workspace node classify_content",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

process_general_agent = Agent(
    role="Process General",
    goal="Execute capabilities defined under the workspace node process_general",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

process_poem_agent = Agent(
    role="Process Poem",
    goal="Execute capabilities defined under the workspace node process_poem",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

process_news_agent = Agent(
    role="Process News",
    goal="Execute capabilities defined under the workspace node process_news",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

process_joke_agent = Agent(
    role="Process Joke",
    goal="Execute capabilities defined under the workspace node process_joke",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

text_to_speech_agent = Agent(
    role="Text To Speech",
    goal="Execute capabilities defined under the workspace node text_to_speech",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

categorize_agent = Agent(
    role="Categorize",
    goal="Execute capabilities defined under the workspace node categorize",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

handle_learning_resource_agent = Agent(
    role="Handle Learning Resource",
    goal="Execute capabilities defined under the workspace node handle_learning_resource",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

handle_resume_making_agent = Agent(
    role="Handle Resume Making",
    goal="Execute capabilities defined under the workspace node handle_resume_making",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

handle_interview_preparation_agent = Agent(
    role="Handle Interview Preparation",
    goal="Execute capabilities defined under the workspace node handle_interview_preparation",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

job_search_agent = Agent(
    role="Job Search",
    goal="Execute capabilities defined under the workspace node job_search",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

mock_interview_agent = Agent(
    role="Mock Interview",
    goal="Execute capabilities defined under the workspace node mock_interview",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

interview_topics_questions_agent = Agent(
    role="Interview Topics Questions",
    goal="Execute capabilities defined under the workspace node interview_topics_questions",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

tutorial_agent_agent = Agent(
    role="Tutorial Agent",
    goal="Execute capabilities defined under the workspace node tutorial_agent",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

ask_query_bot_agent = Agent(
    role="Ask Query Bot",
    goal="Execute capabilities defined under the workspace node ask_query_bot",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

calendar_analyzer_agent = Agent(
    role="Calendar Analyzer",
    goal="Execute capabilities defined under the workspace node calendar_analyzer",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

task_analyzer_agent = Agent(
    role="Task Analyzer",
    goal="Execute capabilities defined under the workspace node task_analyzer",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

plan_generator_agent = Agent(
    role="Plan Generator",
    goal="Execute capabilities defined under the workspace node plan_generator",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

notewriter_analyze_agent = Agent(
    role="Notewriter Analyze",
    goal="Execute capabilities defined under the workspace node notewriter_analyze",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

notewriter_generate_agent = Agent(
    role="Notewriter Generate",
    goal="Execute capabilities defined under the workspace node notewriter_generate",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

advisor_analyze_agent = Agent(
    role="Advisor Analyze",
    goal="Execute capabilities defined under the workspace node advisor_analyze",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

advisor_generate_agent = Agent(
    role="Advisor Generate",
    goal="Execute capabilities defined under the workspace node advisor_generate",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

coordinator_agent = Agent(
    role="Coordinator",
    goal="Execute capabilities defined under the workspace node coordinator",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

profile_analyzer_agent = Agent(
    role="Profile Analyzer",
    goal="Execute capabilities defined under the workspace node profile_analyzer",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

execute_agent = Agent(
    role="Execute",
    goal="Execute capabilities defined under the workspace node execute",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

calendar_analyzer_agent = Agent(
    role="Calendar Analyzer",
    goal="Execute capabilities defined under the workspace node calendar_analyzer",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

task_analyzer_agent = Agent(
    role="Task Analyzer",
    goal="Execute capabilities defined under the workspace node task_analyzer",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

plan_generator_agent = Agent(
    role="Plan Generator",
    goal="Execute capabilities defined under the workspace node plan_generator",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

notewriter_analyze_agent = Agent(
    role="Notewriter Analyze",
    goal="Execute capabilities defined under the workspace node notewriter_analyze",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

notewriter_generate_agent = Agent(
    role="Notewriter Generate",
    goal="Execute capabilities defined under the workspace node notewriter_generate",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

advisor_analyze_agent = Agent(
    role="Advisor Analyze",
    goal="Execute capabilities defined under the workspace node advisor_analyze",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

advisor_generate_agent = Agent(
    role="Advisor Generate",
    goal="Execute capabilities defined under the workspace node advisor_generate",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

convert_user_instruction_to_actions_agent = Agent(
    role="Convert User Instruction To Actions",
    goal="Execute capabilities defined under the workspace node convert_user_instruction_to_actions",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

get_initial_action_agent = Agent(
    role="Get Initial Action",
    goal="Execute capabilities defined under the workspace node get_initial_action",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

get_website_state_agent = Agent(
    role="Get Website State",
    goal="Execute capabilities defined under the workspace node get_website_state",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

generate_code_for_action_agent = Agent(
    role="Generate Code For Action",
    goal="Execute capabilities defined under the workspace node generate_code_for_action",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

validate_generated_action_agent = Agent(
    role="Validate Generated Action",
    goal="Execute capabilities defined under the workspace node validate_generated_action",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

handle_generation_error_agent = Agent(
    role="Handle Generation Error",
    goal="Execute capabilities defined under the workspace node handle_generation_error",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

post_process_script_agent = Agent(
    role="Post Process Script",
    goal="Execute capabilities defined under the workspace node post_process_script",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

execute_test_case_agent = Agent(
    role="Execute Test Case",
    goal="Execute capabilities defined under the workspace node execute_test_case",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

generate_test_report_agent = Agent(
    role="Generate Test Report",
    goal="Execute capabilities defined under the workspace node generate_test_report",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

categorize_agent = Agent(
    role="Categorize",
    goal="Execute capabilities defined under the workspace node categorize",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

analyze_sentiment_agent = Agent(
    role="Analyze Sentiment",
    goal="Execute capabilities defined under the workspace node analyze_sentiment",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

handle_technical_agent = Agent(
    role="Handle Technical",
    goal="Execute capabilities defined under the workspace node handle_technical",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

handle_billing_agent = Agent(
    role="Handle Billing",
    goal="Execute capabilities defined under the workspace node handle_billing",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

handle_general_agent = Agent(
    role="Handle General",
    goal="Execute capabilities defined under the workspace node handle_general",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

escalate_agent = Agent(
    role="Escalate",
    goal="Execute capabilities defined under the workspace node escalate",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

get_website_content_agent = Agent(
    role="Get Website Content",
    goal="Execute capabilities defined under the workspace node get_website_content",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

analyze_company_agent = Agent(
    role="Analyze Company",
    goal="Execute capabilities defined under the workspace node analyze_company",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

generate_concepts_agent = Agent(
    role="Generate Concepts",
    goal="Execute capabilities defined under the workspace node generate_concepts",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

select_templates_agent = Agent(
    role="Select Templates",
    goal="Execute capabilities defined under the workspace node select_templates",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

generate_text_agent = Agent(
    role="Generate Text",
    goal="Execute capabilities defined under the workspace node generate_text",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

create_url_agent = Agent(
    role="Create Url",
    goal="Execute capabilities defined under the workspace node create_url",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

tavily_search_agent = Agent(
    role="Tavily Search",
    goal="Execute capabilities defined under the workspace node tavily_search",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

schema_mapping_agent = Agent(
    role="Schema Mapping",
    goal="Execute capabilities defined under the workspace node schema_mapping",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

product_comparison_agent = Agent(
    role="Product Comparison",
    goal="Execute capabilities defined under the workspace node product_comparison",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

youtube_review_agent = Agent(
    role="Youtube Review",
    goal="Execute capabilities defined under the workspace node youtube_review",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

display_agent = Agent(
    role="Display",
    goal="Execute capabilities defined under the workspace node display",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

send_email_agent = Agent(
    role="Send Email",
    goal="Execute capabilities defined under the workspace node send_email",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

classify_input_agent = Agent(
    role="Classify Input",
    goal="Execute capabilities defined under the workspace node classify_input",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

discover_database_agent = Agent(
    role="Discover Database",
    goal="Execute capabilities defined under the workspace node discover_database",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

create_plan_agent = Agent(
    role="Create Plan",
    goal="Execute capabilities defined under the workspace node create_plan",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

execute_plan_agent = Agent(
    role="Execute Plan",
    goal="Execute capabilities defined under the workspace node execute_plan",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

generate_response_agent = Agent(
    role="Generate Response",
    goal="Execute capabilities defined under the workspace node generate_response",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

generate_newsapi_params_agent = Agent(
    role="Generate Newsapi Params",
    goal="Execute capabilities defined under the workspace node generate_newsapi_params",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

retrieve_articles_metadata_agent = Agent(
    role="Retrieve Articles Metadata",
    goal="Execute capabilities defined under the workspace node retrieve_articles_metadata",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

retrieve_articles_text_agent = Agent(
    role="Retrieve Articles Text",
    goal="Execute capabilities defined under the workspace node retrieve_articles_text",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

select_top_urls_agent = Agent(
    role="Select Top Urls",
    goal="Execute capabilities defined under the workspace node select_top_urls",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

summarize_articles_parallel_agent = Agent(
    role="Summarize Articles Parallel",
    goal="Execute capabilities defined under the workspace node summarize_articles_parallel",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

format_results_agent = Agent(
    role="Format Results",
    goal="Execute capabilities defined under the workspace node format_results",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

decision_making_agent = Agent(
    role="Decision Making",
    goal="Execute capabilities defined under the workspace node decision_making",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

planning_agent = Agent(
    role="Planning",
    goal="Execute capabilities defined under the workspace node planning",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

tools_agent = Agent(
    role="Tools",
    goal="Execute capabilities defined under the workspace node tools",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

agent_agent = Agent(
    role="Agent",
    goal="Execute capabilities defined under the workspace node agent",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

judge_agent = Agent(
    role="Judge",
    goal="Execute capabilities defined under the workspace node judge",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

CATEGORY_agent = Agent(
    role="Category",
    goal="Execute capabilities defined under the workspace node CATEGORY",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

SUMMARY_agent = Agent(
    role="Summary",
    goal="Execute capabilities defined under the workspace node SUMMARY",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

FACT_CHECKING_agent = Agent(
    role="Fact Checking",
    goal="Execute capabilities defined under the workspace node FACT_CHECKING",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

TONE_ANALYSIS_agent = Agent(
    role="Tone Analysis",
    goal="Execute capabilities defined under the workspace node TONE_ANALYSIS",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

QUOTE_EXTRACTION_agent = Agent(
    role="Quote Extraction",
    goal="Execute capabilities defined under the workspace node QUOTE_EXTRACTION",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

GRAMMAR_AND_BIAS_REVIEW_agent = Agent(
    role="Grammar And Bias Review",
    goal="Execute capabilities defined under the workspace node GRAMMAR_AND_BIAS_REVIEW",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

web_download_agent = Agent(
    role="Web Download",
    goal="Execute capabilities defined under the workspace node web_download",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

embeddings_ner_agent = Agent(
    role="Embeddings Ner",
    goal="Execute capabilities defined under the workspace node embeddings_ner",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

main_assistant_agent = Agent(
    role="Main Assistant",
    goal="Execute capabilities defined under the workspace node main_assistant",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

main_assistant_tools_agent = Agent(
    role="Main Assistant Tools",
    goal="Execute capabilities defined under the workspace node main_assistant_tools",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

underwriting_assistant_agent = Agent(
    role="Underwriting Assistant",
    goal="Execute capabilities defined under the workspace node underwriting_assistant",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

quote_assistant_agent = Agent(
    role="Quote Assistant",
    goal="Execute capabilities defined under the workspace node quote_assistant",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

quote_assistant_tools_agent = Agent(
    role="Quote Assistant Tools",
    goal="Execute capabilities defined under the workspace node quote_assistant_tools",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

entry_quote_assistant_agent = Agent(
    role="Entry Quote Assistant",
    goal="Execute capabilities defined under the workspace node entry_quote_assistant",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

retrieve_agent = Agent(
    role="Retrieve",
    goal="Execute capabilities defined under the workspace node retrieve",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

reasoning_agent = Agent(
    role="Reasoning",
    goal="Execute capabilities defined under the workspace node reasoning",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

classification_grading_agent = Agent(
    role="Classification Grading",
    goal="Execute capabilities defined under the workspace node classification_grading",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

update_state_agent = Agent(
    role="Update State",
    goal="Execute capabilities defined under the workspace node update_state",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

reroute_agent = Agent(
    role="Reroute",
    goal="Execute capabilities defined under the workspace node reroute",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

pass_tool_call_id_agent = Agent(
    role="Pass Tool Call Id",
    goal="Execute capabilities defined under the workspace node pass_tool_call_id",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

pass_final_classifications_agent = Agent(
    role="Pass Final Classifications",
    goal="Execute capabilities defined under the workspace node pass_final_classifications",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

create_tool_message_agent = Agent(
    role="Create Tool Message",
    goal="Execute capabilities defined under the workspace node create_tool_message",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

update_workflow_state_agent = Agent(
    role="Update Workflow State",
    goal="Execute capabilities defined under the workspace node update_workflow_state",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

ask_user_needs_agent = Agent(
    role="Ask User Needs",
    goal="Execute capabilities defined under the workspace node ask_user_needs",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

build_filters_agent = Agent(
    role="Build Filters",
    goal="Execute capabilities defined under the workspace node build_filters",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

search_listings_agent = Agent(
    role="Search Listings",
    goal="Execute capabilities defined under the workspace node search_listings",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

fetch_additional_info_agent = Agent(
    role="Fetch Additional Info",
    goal="Execute capabilities defined under the workspace node fetch_additional_info",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

irrelevant_agent = Agent(
    role="Irrelevant",
    goal="Execute capabilities defined under the workspace node irrelevant",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

classify_contract_agent = Agent(
    role="Classify Contract",
    goal="Execute capabilities defined under the workspace node classify_contract",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

retrieve_clauses_agent = Agent(
    role="Retrieve Clauses",
    goal="Execute capabilities defined under the workspace node retrieve_clauses",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

execute_step_clause_agent = Agent(
    role="Execute Step Clause",
    goal="Execute capabilities defined under the workspace node execute_step_clause",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

create_review_plan_agent = Agent(
    role="Create Review Plan",
    goal="Execute capabilities defined under the workspace node create_review_plan",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

execute_step_agent = Agent(
    role="Execute Step",
    goal="Execute capabilities defined under the workspace node execute_step",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

generate_final_report_agent = Agent(
    role="Generate Final Report",
    goal="Execute capabilities defined under the workspace node generate_final_report",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

search_agent = Agent(
    role="Search",
    goal="Execute capabilities defined under the workspace node search",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

summarize_agent = Agent(
    role="Summarize",
    goal="Execute capabilities defined under the workspace node summarize",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

publish_agent = Agent(
    role="Publish",
    goal="Execute capabilities defined under the workspace node publish",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

Keywords_agent = Agent(
    role="Keywords",
    goal="Execute capabilities defined under the workspace node Keywords",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

Structure_agent = Agent(
    role="Structure",
    goal="Execute capabilities defined under the workspace node Structure",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

Host question_agent = Agent(
    role="Host Question",
    goal="Execute capabilities defined under the workspace node Host question",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

Web research_agent = Agent(
    role="Web Research",
    goal="Execute capabilities defined under the workspace node Web research",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

Wiki research_agent = Agent(
    role="Wiki Research",
    goal="Execute capabilities defined under the workspace node Wiki research",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

Expert answer_agent = Agent(
    role="Expert Answer",
    goal="Execute capabilities defined under the workspace node Expert answer",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

Save podcast_agent = Agent(
    role="Save Podcast",
    goal="Execute capabilities defined under the workspace node Save podcast",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

Write script_agent = Agent(
    role="Write Script",
    goal="Execute capabilities defined under the workspace node Write script",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

Planing_agent = Agent(
    role="Planing",
    goal="Execute capabilities defined under the workspace node Planing",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

Start research_agent = Agent(
    role="Start Research",
    goal="Execute capabilities defined under the workspace node Start research",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

Create podcast_agent = Agent(
    role="Create Podcast",
    goal="Execute capabilities defined under the workspace node Create podcast",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

Write report_agent = Agent(
    role="Write Report",
    goal="Execute capabilities defined under the workspace node Write report",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

Write introduction_agent = Agent(
    role="Write Introduction",
    goal="Execute capabilities defined under the workspace node Write introduction",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

Write conclusion_agent = Agent(
    role="Write Conclusion",
    goal="Execute capabilities defined under the workspace node Write conclusion",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

Finalize podcast_agent = Agent(
    role="Finalize Podcast",
    goal="Execute capabilities defined under the workspace node Finalize podcast",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

requirements_gathering_agent = Agent(
    role="Requirements Gathering",
    goal="Execute capabilities defined under the workspace node requirements_gathering",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

generate_job_desc_agent = Agent(
    role="Generate Job Desc",
    goal="Execute capabilities defined under the workspace node generate_job_desc",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

linkedin_process_agent = Agent(
    role="Linkedin Process",
    goal="Execute capabilities defined under the workspace node linkedin_process",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

analyze_cv_agent = Agent(
    role="Analyze Cv",
    goal="Execute capabilities defined under the workspace node analyze_cv",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

prepare_interview_agent = Agent(
    role="Prepare Interview",
    goal="Execute capabilities defined under the workspace node prepare_interview",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

classification_node_agent = Agent(
    role="Classification Node",
    goal="Execute capabilities defined under the workspace node classification_node",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

entity_extraction_agent = Agent(
    role="Entity Extraction",
    goal="Execute capabilities defined under the workspace node entity_extraction",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

summarization_agent = Agent(
    role="Summarization",
    goal="Execute capabilities defined under the workspace node summarization",
    backstory="You are a specialized automation layer unit extracted from a opaque_blob pipeline. Authorized MCP Interfaces: []",
    tools=[ToQuoteAssistant],
    verbose=True,
    allow_delegation=False
)

# 6. Define Concrete Task Assignments linked back to Code Blobs
approach_analysis_task = Task(
    description="Execute processing code logic anchored at: blobs/approach_analysis.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=approach_analysis_agent
)

task_knowledge_retrieval_task = Task(
    description="Execute processing code logic anchored at: blobs/task_knowledge_retrieval.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=task_knowledge_retrieval_agent
)

customized_approach_generation_task = Task(
    description="Execute processing code logic anchored at: blobs/customized_approach_generation.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=customized_approach_generation_agent
)

melody_generator_task = Task(
    description="Execute processing code logic anchored at: blobs/melody_generator.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=melody_generator_agent
)

harmony_creator_task = Task(
    description="Execute processing code logic anchored at: blobs/harmony_creator.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=harmony_creator_agent
)

rhythm_analyzer_task = Task(
    description="Execute processing code logic anchored at: blobs/rhythm_analyzer.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=rhythm_analyzer_agent
)

style_adapter_task = Task(
    description="Execute processing code logic anchored at: blobs/style_adapter.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=style_adapter_agent
)

midi_converter_task = Task(
    description="Execute processing code logic anchored at: blobs/midi_converter.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=midi_converter_agent
)

triage_task = Task(
    description="Execute processing code logic anchored at: blobs/triage.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=triage_agent
)

response_agent_task = Task(
    description="Execute processing code logic anchored at: blobs/response_agent.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=response_agent_agent
)

triage_task = Task(
    description="Execute processing code logic anchored at: blobs/triage.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=triage_agent
)

response_agent_task = Task(
    description="Execute processing code logic anchored at: blobs/response_agent.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=response_agent_agent
)

code_execution_node_task = Task(
    description="Execute processing code logic anchored at: blobs/code_execution_node.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=code_execution_node_agent
)

code_update_node_task = Task(
    description="Execute processing code logic anchored at: blobs/code_update_node.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=code_update_node_agent
)

code_patching_node_task = Task(
    description="Execute processing code logic anchored at: blobs/code_patching_node.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=code_patching_node_agent
)

bug_report_node_task = Task(
    description="Execute processing code logic anchored at: blobs/bug_report_node.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=bug_report_node_agent
)

memory_search_node_task = Task(
    description="Execute processing code logic anchored at: blobs/memory_search_node.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=memory_search_node_agent
)

memory_filter_node_task = Task(
    description="Execute processing code logic anchored at: blobs/memory_filter_node.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=memory_filter_node_agent
)

memory_modification_node_task = Task(
    description="Execute processing code logic anchored at: blobs/memory_modification_node.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=memory_modification_node_agent
)

memory_generation_node_task = Task(
    description="Execute processing code logic anchored at: blobs/memory_generation_node.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=memory_generation_node_agent
)

input_city_task = Task(
    description="Execute processing code logic anchored at: blobs/input_city.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=input_city_agent
)

input_interests_task = Task(
    description="Execute processing code logic anchored at: blobs/input_interests.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=input_interests_agent
)

create_itinerary_task = Task(
    description="Execute processing code logic anchored at: blobs/create_itinerary.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=create_itinerary_agent
)

get_weather_task = Task(
    description="Execute processing code logic anchored at: blobs/get_weather.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=get_weather_agent
)

analyze_disaster_task = Task(
    description="Execute processing code logic anchored at: blobs/analyze_disaster.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=analyze_disaster_agent
)

assess_severity_task = Task(
    description="Execute processing code logic anchored at: blobs/assess_severity.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=assess_severity_agent
)

data_logging_task = Task(
    description="Execute processing code logic anchored at: blobs/data_logging.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=data_logging_agent
)

emergency_response_task = Task(
    description="Execute processing code logic anchored at: blobs/emergency_response.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=emergency_response_agent
)

civil_defense_response_task = Task(
    description="Execute processing code logic anchored at: blobs/civil_defense_response.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=civil_defense_response_agent
)

public_works_response_task = Task(
    description="Execute processing code logic anchored at: blobs/public_works_response.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=public_works_response_agent
)

get_human_verification_task = Task(
    description="Execute processing code logic anchored at: blobs/get_human_verification.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=get_human_verification_agent
)

send_email_alert_task = Task(
    description="Execute processing code logic anchored at: blobs/send_email_alert.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=send_email_alert_agent
)

handle_no_approval_task = Task(
    description="Execute processing code logic anchored at: blobs/handle_no_approval.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=handle_no_approval_agent
)

get_weather_task = Task(
    description="Execute processing code logic anchored at: blobs/get_weather.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=get_weather_agent
)

social_media_monitoring_task = Task(
    description="Execute processing code logic anchored at: blobs/social_media_monitoring.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=social_media_monitoring_agent
)

analyze_disaster_task = Task(
    description="Execute processing code logic anchored at: blobs/analyze_disaster.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=analyze_disaster_agent
)

assess_severity_task = Task(
    description="Execute processing code logic anchored at: blobs/assess_severity.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=assess_severity_agent
)

data_logging_task = Task(
    description="Execute processing code logic anchored at: blobs/data_logging.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=data_logging_agent
)

emergency_response_task = Task(
    description="Execute processing code logic anchored at: blobs/emergency_response.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=emergency_response_agent
)

civil_defense_response_task = Task(
    description="Execute processing code logic anchored at: blobs/civil_defense_response.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=civil_defense_response_agent
)

public_works_response_task = Task(
    description="Execute processing code logic anchored at: blobs/public_works_response.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=public_works_response_agent
)

get_human_verification_task = Task(
    description="Execute processing code logic anchored at: blobs/get_human_verification.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=get_human_verification_agent
)

send_email_alert_task = Task(
    description="Execute processing code logic anchored at: blobs/send_email_alert.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=send_email_alert_agent
)

handle_no_approval_task = Task(
    description="Execute processing code logic anchored at: blobs/handle_no_approval.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=handle_no_approval_agent
)

assistant_task = Task(
    description="Execute processing code logic anchored at: blobs/assistant.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=assistant_agent
)

tools_task = Task(
    description="Execute processing code logic anchored at: blobs/tools.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=tools_agent
)

generate_new_inputs_task = Task(
    description="Execute processing code logic anchored at: blobs/generate_new_inputs.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=generate_new_inputs_agent
)

static_test_task = Task(
    description="Execute processing code logic anchored at: blobs/static_test.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=static_test_agent
)

generate_node_descriptions_task = Task(
    description="Execute processing code logic anchored at: blobs/generate_node_descriptions.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=generate_node_descriptions_agent
)

generate_testers_task = Task(
    description="Execute processing code logic anchored at: blobs/generate_testers.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=generate_testers_agent
)

generate_test_cases_task = Task(
    description="Execute processing code logic anchored at: blobs/generate_test_cases.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=generate_test_cases_agent
)

run_test_cases_task = Task(
    description="Execute processing code logic anchored at: blobs/run_test_cases.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=run_test_cases_agent
)

analize_results_task = Task(
    description="Execute processing code logic anchored at: blobs/analize_results.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=analize_results_agent
)

assistant_task = Task(
    description="Execute processing code logic anchored at: blobs/assistant.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=assistant_agent
)

tools_task = Task(
    description="Execute processing code logic anchored at: blobs/tools.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=tools_agent
)

process_input_task = Task(
    description="Execute processing code logic anchored at: blobs/process_input.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=process_input_agent
)

planner_task = Task(
    description="Execute processing code logic anchored at: blobs/planner.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=planner_agent
)

researcher_task = Task(
    description="Execute processing code logic anchored at: blobs/researcher.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=researcher_agent
)

search_articles_task = Task(
    description="Execute processing code logic anchored at: blobs/search_articles.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=search_articles_agent
)

article_decisions_task = Task(
    description="Execute processing code logic anchored at: blobs/article_decisions.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=article_decisions_agent
)

download_articles_task = Task(
    description="Execute processing code logic anchored at: blobs/download_articles.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=download_articles_agent
)

paper_analyzer_task = Task(
    description="Execute processing code logic anchored at: blobs/paper_analyzer.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=paper_analyzer_agent
)

write_abstract_task = Task(
    description="Execute processing code logic anchored at: blobs/write_abstract.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=write_abstract_agent
)

write_introduction_task = Task(
    description="Execute processing code logic anchored at: blobs/write_introduction.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=write_introduction_agent
)

write_methods_task = Task(
    description="Execute processing code logic anchored at: blobs/write_methods.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=write_methods_agent
)

write_results_task = Task(
    description="Execute processing code logic anchored at: blobs/write_results.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=write_results_agent
)

write_conclusion_task = Task(
    description="Execute processing code logic anchored at: blobs/write_conclusion.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=write_conclusion_agent
)

write_references_task = Task(
    description="Execute processing code logic anchored at: blobs/write_references.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=write_references_agent
)

aggregate_paper_task = Task(
    description="Execute processing code logic anchored at: blobs/aggregate_paper.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=aggregate_paper_agent
)

critique_paper_task = Task(
    description="Execute processing code logic anchored at: blobs/critique_paper.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=critique_paper_agent
)

revise_paper_task = Task(
    description="Execute processing code logic anchored at: blobs/revise_paper.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=revise_paper_agent
)

final_draft_task = Task(
    description="Execute processing code logic anchored at: blobs/final_draft.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=final_draft_agent
)

task_generation_task = Task(
    description="Execute processing code logic anchored at: blobs/task_generation.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=task_generation_agent
)

task_dependencies_task = Task(
    description="Execute processing code logic anchored at: blobs/task_dependencies.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=task_dependencies_agent
)

task_scheduler_task = Task(
    description="Execute processing code logic anchored at: blobs/task_scheduler.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=task_scheduler_agent
)

task_allocator_task = Task(
    description="Execute processing code logic anchored at: blobs/task_allocator.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=task_allocator_agent
)

risk_assessor_task = Task(
    description="Execute processing code logic anchored at: blobs/risk_assessor.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=risk_assessor_agent
)

insight_generator_task = Task(
    description="Execute processing code logic anchored at: blobs/insight_generator.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=insight_generator_agent
)

create_project_plan_task = Task(
    description="Execute processing code logic anchored at: blobs/create_project_plan.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=create_project_plan_agent
)

requirements_gathering_task = Task(
    description="Execute processing code logic anchored at: blobs/requirements_gathering.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=requirements_gathering_agent
)

generate_job_desc_task = Task(
    description="Execute processing code logic anchored at: blobs/generate_job_desc.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=generate_job_desc_agent
)

linkedin_process_task = Task(
    description="Execute processing code logic anchored at: blobs/linkedin_process.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=linkedin_process_agent
)

analyze_cv_task = Task(
    description="Execute processing code logic anchored at: blobs/analyze_cv.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=analyze_cv_agent
)

prepare_interview_task = Task(
    description="Execute processing code logic anchored at: blobs/prepare_interview.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=prepare_interview_agent
)

check_relevance_task = Task(
    description="Execute processing code logic anchored at: blobs/check_relevance.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=check_relevance_agent
)

check_grammar_task = Task(
    description="Execute processing code logic anchored at: blobs/check_grammar.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=check_grammar_agent
)

analyze_structure_task = Task(
    description="Execute processing code logic anchored at: blobs/analyze_structure.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=analyze_structure_agent
)

evaluate_depth_task = Task(
    description="Execute processing code logic anchored at: blobs/evaluate_depth.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=evaluate_depth_agent
)

calculate_final_score_task = Task(
    description="Execute processing code logic anchored at: blobs/calculate_final_score.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=calculate_final_score_agent
)

generate_query_task = Task(
    description="Execute processing code logic anchored at: blobs/generate_query.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=generate_query_agent
)

search_web_task = Task(
    description="Execute processing code logic anchored at: blobs/search_web.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=search_web_agent
)

chunk_context_task = Task(
    description="Execute processing code logic anchored at: blobs/chunk_context.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=chunk_context_agent
)

context_validation_task = Task(
    description="Execute processing code logic anchored at: blobs/context_validation.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=context_validation_agent
)

generate_checkpoints_task = Task(
    description="Execute processing code logic anchored at: blobs/generate_checkpoints.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=generate_checkpoints_agent
)

generate_question_task = Task(
    description="Execute processing code logic anchored at: blobs/generate_question.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=generate_question_agent
)

next_checkpoint_task = Task(
    description="Execute processing code logic anchored at: blobs/next_checkpoint.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=next_checkpoint_agent
)

user_answer_task = Task(
    description="Execute processing code logic anchored at: blobs/user_answer.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=user_answer_agent
)

verify_answer_task = Task(
    description="Execute processing code logic anchored at: blobs/verify_answer.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=verify_answer_agent
)

teach_concept_task = Task(
    description="Execute processing code logic anchored at: blobs/teach_concept.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=teach_concept_agent
)

tour_introduction_task = Task(
    description="Execute processing code logic anchored at: blobs/tour_introduction.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=tour_introduction_agent
)

display_artwork_task = Task(
    description="Execute processing code logic anchored at: blobs/display_artwork.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=display_artwork_agent
)

get_next_artwork_task = Task(
    description="Execute processing code logic anchored at: blobs/get_next_artwork.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=get_next_artwork_agent
)

discuss_task = Task(
    description="Execute processing code logic anchored at: blobs/discuss.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=discuss_agent
)

conclude_tour_task = Task(
    description="Execute processing code logic anchored at: blobs/conclude_tour.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=conclude_tour_agent
)

character_introduction_task = Task(
    description="Execute processing code logic anchored at: blobs/character_introduction.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=character_introduction_agent
)

ask_question_task = Task(
    description="Execute processing code logic anchored at: blobs/ask_question.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=ask_question_agent
)

answer_question_task = Task(
    description="Execute processing code logic anchored at: blobs/answer_question.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=answer_question_agent
)

create_characters_task = Task(
    description="Execute processing code logic anchored at: blobs/create_characters.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=create_characters_agent
)

create_story_task = Task(
    description="Execute processing code logic anchored at: blobs/create_story.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=create_story_agent
)

narrartor_task = Task(
    description="Execute processing code logic anchored at: blobs/narrartor.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=narrartor_agent
)

sherlock_task = Task(
    description="Execute processing code logic anchored at: blobs/sherlock.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=sherlock_agent
)

guesser_task = Task(
    description="Execute processing code logic anchored at: blobs/guesser.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=guesser_agent
)

conversation_task = Task(
    description="Execute processing code logic anchored at: blobs/conversation.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=conversation_agent
)

summary_node_task = Task(
    description="Execute processing code logic anchored at: blobs/summary_node.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=summary_node_agent
)

research_node_task = Task(
    description="Execute processing code logic anchored at: blobs/research_node.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=research_node_agent
)

intent_matching_node_task = Task(
    description="Execute processing code logic anchored at: blobs/intent_matching_node.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=intent_matching_node_agent
)

instagram_task = Task(
    description="Execute processing code logic anchored at: blobs/instagram.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=instagram_agent
)

twitter_task = Task(
    description="Execute processing code logic anchored at: blobs/twitter.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=twitter_agent
)

linkedin_task = Task(
    description="Execute processing code logic anchored at: blobs/linkedin.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=linkedin_agent
)

blog_task = Task(
    description="Execute processing code logic anchored at: blobs/blog.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=blog_agent
)

combine_content_task = Task(
    description="Execute processing code logic anchored at: blobs/combine_content.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=combine_content_agent
)

generate_character_description_task = Task(
    description="Execute processing code logic anchored at: blobs/generate_character_description.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=generate_character_description_agent
)

generate_plot_task = Task(
    description="Execute processing code logic anchored at: blobs/generate_plot.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=generate_plot_agent
)

generate_image_prompts_task = Task(
    description="Execute processing code logic anchored at: blobs/generate_image_prompts.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=generate_image_prompts_agent
)

create_images_task = Task(
    description="Execute processing code logic anchored at: blobs/create_images.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=create_images_agent
)

create_gif_task = Task(
    description="Execute processing code logic anchored at: blobs/create_gif.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=create_gif_agent
)

classify_content_task = Task(
    description="Execute processing code logic anchored at: blobs/classify_content.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=classify_content_agent
)

process_general_task = Task(
    description="Execute processing code logic anchored at: blobs/process_general.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=process_general_agent
)

process_poem_task = Task(
    description="Execute processing code logic anchored at: blobs/process_poem.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=process_poem_agent
)

process_news_task = Task(
    description="Execute processing code logic anchored at: blobs/process_news.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=process_news_agent
)

process_joke_task = Task(
    description="Execute processing code logic anchored at: blobs/process_joke.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=process_joke_agent
)

text_to_speech_task = Task(
    description="Execute processing code logic anchored at: blobs/text_to_speech.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=text_to_speech_agent
)

categorize_task = Task(
    description="Execute processing code logic anchored at: blobs/categorize.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=categorize_agent
)

handle_learning_resource_task = Task(
    description="Execute processing code logic anchored at: blobs/handle_learning_resource.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=handle_learning_resource_agent
)

handle_resume_making_task = Task(
    description="Execute processing code logic anchored at: blobs/handle_resume_making.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=handle_resume_making_agent
)

handle_interview_preparation_task = Task(
    description="Execute processing code logic anchored at: blobs/handle_interview_preparation.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=handle_interview_preparation_agent
)

job_search_task = Task(
    description="Execute processing code logic anchored at: blobs/job_search.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=job_search_agent
)

mock_interview_task = Task(
    description="Execute processing code logic anchored at: blobs/mock_interview.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=mock_interview_agent
)

interview_topics_questions_task = Task(
    description="Execute processing code logic anchored at: blobs/interview_topics_questions.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=interview_topics_questions_agent
)

tutorial_agent_task = Task(
    description="Execute processing code logic anchored at: blobs/tutorial_agent.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=tutorial_agent_agent
)

ask_query_bot_task = Task(
    description="Execute processing code logic anchored at: blobs/ask_query_bot.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=ask_query_bot_agent
)

calendar_analyzer_task = Task(
    description="Execute processing code logic anchored at: blobs/calendar_analyzer.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=calendar_analyzer_agent
)

task_analyzer_task = Task(
    description="Execute processing code logic anchored at: blobs/task_analyzer.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=task_analyzer_agent
)

plan_generator_task = Task(
    description="Execute processing code logic anchored at: blobs/plan_generator.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=plan_generator_agent
)

notewriter_analyze_task = Task(
    description="Execute processing code logic anchored at: blobs/notewriter_analyze.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=notewriter_analyze_agent
)

notewriter_generate_task = Task(
    description="Execute processing code logic anchored at: blobs/notewriter_generate.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=notewriter_generate_agent
)

advisor_analyze_task = Task(
    description="Execute processing code logic anchored at: blobs/advisor_analyze.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=advisor_analyze_agent
)

advisor_generate_task = Task(
    description="Execute processing code logic anchored at: blobs/advisor_generate.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=advisor_generate_agent
)

coordinator_task = Task(
    description="Execute processing code logic anchored at: blobs/coordinator.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=coordinator_agent
)

profile_analyzer_task = Task(
    description="Execute processing code logic anchored at: blobs/profile_analyzer.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=profile_analyzer_agent
)

execute_task = Task(
    description="Execute processing code logic anchored at: blobs/execute.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=execute_agent
)

calendar_analyzer_task = Task(
    description="Execute processing code logic anchored at: blobs/calendar_analyzer.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=calendar_analyzer_agent
)

task_analyzer_task = Task(
    description="Execute processing code logic anchored at: blobs/task_analyzer.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=task_analyzer_agent
)

plan_generator_task = Task(
    description="Execute processing code logic anchored at: blobs/plan_generator.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=plan_generator_agent
)

notewriter_analyze_task = Task(
    description="Execute processing code logic anchored at: blobs/notewriter_analyze.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=notewriter_analyze_agent
)

notewriter_generate_task = Task(
    description="Execute processing code logic anchored at: blobs/notewriter_generate.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=notewriter_generate_agent
)

advisor_analyze_task = Task(
    description="Execute processing code logic anchored at: blobs/advisor_analyze.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=advisor_analyze_agent
)

advisor_generate_task = Task(
    description="Execute processing code logic anchored at: blobs/advisor_generate.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=advisor_generate_agent
)

convert_user_instruction_to_actions_task = Task(
    description="Execute processing code logic anchored at: blobs/convert_user_instruction_to_actions.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=convert_user_instruction_to_actions_agent
)

get_initial_action_task = Task(
    description="Execute processing code logic anchored at: blobs/get_initial_action.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=get_initial_action_agent
)

get_website_state_task = Task(
    description="Execute processing code logic anchored at: blobs/get_website_state.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=get_website_state_agent
)

generate_code_for_action_task = Task(
    description="Execute processing code logic anchored at: blobs/generate_code_for_action.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=generate_code_for_action_agent
)

validate_generated_action_task = Task(
    description="Execute processing code logic anchored at: blobs/validate_generated_action.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=validate_generated_action_agent
)

handle_generation_error_task = Task(
    description="Execute processing code logic anchored at: blobs/handle_generation_error.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=handle_generation_error_agent
)

post_process_script_task = Task(
    description="Execute processing code logic anchored at: blobs/post_process_script.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=post_process_script_agent
)

execute_test_case_task = Task(
    description="Execute processing code logic anchored at: blobs/execute_test_case.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=execute_test_case_agent
)

generate_test_report_task = Task(
    description="Execute processing code logic anchored at: blobs/generate_test_report.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=generate_test_report_agent
)

categorize_task = Task(
    description="Execute processing code logic anchored at: blobs/categorize.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=categorize_agent
)

analyze_sentiment_task = Task(
    description="Execute processing code logic anchored at: blobs/analyze_sentiment.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=analyze_sentiment_agent
)

handle_technical_task = Task(
    description="Execute processing code logic anchored at: blobs/handle_technical.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=handle_technical_agent
)

handle_billing_task = Task(
    description="Execute processing code logic anchored at: blobs/handle_billing.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=handle_billing_agent
)

handle_general_task = Task(
    description="Execute processing code logic anchored at: blobs/handle_general.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=handle_general_agent
)

escalate_task = Task(
    description="Execute processing code logic anchored at: blobs/escalate.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=escalate_agent
)

get_website_content_task = Task(
    description="Execute processing code logic anchored at: blobs/get_website_content.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=get_website_content_agent
)

analyze_company_task = Task(
    description="Execute processing code logic anchored at: blobs/analyze_company.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=analyze_company_agent
)

generate_concepts_task = Task(
    description="Execute processing code logic anchored at: blobs/generate_concepts.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=generate_concepts_agent
)

select_templates_task = Task(
    description="Execute processing code logic anchored at: blobs/select_templates.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=select_templates_agent
)

generate_text_task = Task(
    description="Execute processing code logic anchored at: blobs/generate_text.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=generate_text_agent
)

create_url_task = Task(
    description="Execute processing code logic anchored at: blobs/create_url.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=create_url_agent
)

tavily_search_task = Task(
    description="Execute processing code logic anchored at: blobs/tavily_search.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=tavily_search_agent
)

schema_mapping_task = Task(
    description="Execute processing code logic anchored at: blobs/schema_mapping.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=schema_mapping_agent
)

product_comparison_task = Task(
    description="Execute processing code logic anchored at: blobs/product_comparison.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=product_comparison_agent
)

youtube_review_task = Task(
    description="Execute processing code logic anchored at: blobs/youtube_review.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=youtube_review_agent
)

display_task = Task(
    description="Execute processing code logic anchored at: blobs/display.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=display_agent
)

send_email_task = Task(
    description="Execute processing code logic anchored at: blobs/send_email.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=send_email_agent
)

classify_input_task = Task(
    description="Execute processing code logic anchored at: blobs/classify_input.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=classify_input_agent
)

discover_database_task = Task(
    description="Execute processing code logic anchored at: blobs/discover_database.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=discover_database_agent
)

create_plan_task = Task(
    description="Execute processing code logic anchored at: blobs/create_plan.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=create_plan_agent
)

execute_plan_task = Task(
    description="Execute processing code logic anchored at: blobs/execute_plan.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=execute_plan_agent
)

generate_response_task = Task(
    description="Execute processing code logic anchored at: blobs/generate_response.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=generate_response_agent
)

generate_newsapi_params_task = Task(
    description="Execute processing code logic anchored at: blobs/generate_newsapi_params.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=generate_newsapi_params_agent
)

retrieve_articles_metadata_task = Task(
    description="Execute processing code logic anchored at: blobs/retrieve_articles_metadata.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=retrieve_articles_metadata_agent
)

retrieve_articles_text_task = Task(
    description="Execute processing code logic anchored at: blobs/retrieve_articles_text.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=retrieve_articles_text_agent
)

select_top_urls_task = Task(
    description="Execute processing code logic anchored at: blobs/select_top_urls.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=select_top_urls_agent
)

summarize_articles_parallel_task = Task(
    description="Execute processing code logic anchored at: blobs/summarize_articles_parallel.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=summarize_articles_parallel_agent
)

format_results_task = Task(
    description="Execute processing code logic anchored at: blobs/format_results.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=format_results_agent
)

decision_making_task = Task(
    description="Execute processing code logic anchored at: blobs/decision_making.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=decision_making_agent
)

planning_task = Task(
    description="Execute processing code logic anchored at: blobs/planning.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=planning_agent
)

tools_task = Task(
    description="Execute processing code logic anchored at: blobs/tools.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=tools_agent
)

agent_task = Task(
    description="Execute processing code logic anchored at: blobs/agent.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=agent_agent
)

judge_task = Task(
    description="Execute processing code logic anchored at: blobs/judge.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=judge_agent
)

CATEGORY_task = Task(
    description="Execute processing code logic anchored at: blobs/CATEGORY.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=CATEGORY_agent
)

SUMMARY_task = Task(
    description="Execute processing code logic anchored at: blobs/SUMMARY.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=SUMMARY_agent
)

FACT_CHECKING_task = Task(
    description="Execute processing code logic anchored at: blobs/FACT_CHECKING.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=FACT_CHECKING_agent
)

TONE_ANALYSIS_task = Task(
    description="Execute processing code logic anchored at: blobs/TONE_ANALYSIS.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=TONE_ANALYSIS_agent
)

QUOTE_EXTRACTION_task = Task(
    description="Execute processing code logic anchored at: blobs/QUOTE_EXTRACTION.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=QUOTE_EXTRACTION_agent
)

GRAMMAR_AND_BIAS_REVIEW_task = Task(
    description="Execute processing code logic anchored at: blobs/GRAMMAR_AND_BIAS_REVIEW.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=GRAMMAR_AND_BIAS_REVIEW_agent
)

web_download_task = Task(
    description="Execute processing code logic anchored at: blobs/web_download.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=web_download_agent
)

embeddings_ner_task = Task(
    description="Execute processing code logic anchored at: blobs/embeddings_ner.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=embeddings_ner_agent
)

main_assistant_task = Task(
    description="Execute processing code logic anchored at: blobs/main_assistant.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=main_assistant_agent
)

main_assistant_tools_task = Task(
    description="Execute processing code logic anchored at: blobs/main_assistant_tools.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=main_assistant_tools_agent
)

underwriting_assistant_task = Task(
    description="Execute processing code logic anchored at: blobs/underwriting_assistant.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=underwriting_assistant_agent
)

quote_assistant_task = Task(
    description="Execute processing code logic anchored at: blobs/quote_assistant.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=quote_assistant_agent
)

quote_assistant_tools_task = Task(
    description="Execute processing code logic anchored at: blobs/quote_assistant_tools.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=quote_assistant_tools_agent
)

entry_quote_assistant_task = Task(
    description="Execute processing code logic anchored at: blobs/entry_quote_assistant.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=entry_quote_assistant_agent
)

retrieve_task = Task(
    description="Execute processing code logic anchored at: blobs/retrieve.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=retrieve_agent
)

reasoning_task = Task(
    description="Execute processing code logic anchored at: blobs/reasoning.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=reasoning_agent
)

classification_grading_task = Task(
    description="Execute processing code logic anchored at: blobs/classification_grading.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=classification_grading_agent
)

update_state_task = Task(
    description="Execute processing code logic anchored at: blobs/update_state.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=update_state_agent
)

reroute_task = Task(
    description="Execute processing code logic anchored at: blobs/reroute.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=reroute_agent
)

pass_tool_call_id_task = Task(
    description="Execute processing code logic anchored at: blobs/pass_tool_call_id.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=pass_tool_call_id_agent
)

pass_final_classifications_task = Task(
    description="Execute processing code logic anchored at: blobs/pass_final_classifications.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=pass_final_classifications_agent
)

create_tool_message_task = Task(
    description="Execute processing code logic anchored at: blobs/create_tool_message.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=create_tool_message_agent
)

update_workflow_state_task = Task(
    description="Execute processing code logic anchored at: blobs/update_workflow_state.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=update_workflow_state_agent
)

ask_user_needs_task = Task(
    description="Execute processing code logic anchored at: blobs/ask_user_needs.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=ask_user_needs_agent
)

build_filters_task = Task(
    description="Execute processing code logic anchored at: blobs/build_filters.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=build_filters_agent
)

search_listings_task = Task(
    description="Execute processing code logic anchored at: blobs/search_listings.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=search_listings_agent
)

fetch_additional_info_task = Task(
    description="Execute processing code logic anchored at: blobs/fetch_additional_info.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=fetch_additional_info_agent
)

irrelevant_task = Task(
    description="Execute processing code logic anchored at: blobs/irrelevant.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=irrelevant_agent
)

classify_contract_task = Task(
    description="Execute processing code logic anchored at: blobs/classify_contract.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=classify_contract_agent
)

retrieve_clauses_task = Task(
    description="Execute processing code logic anchored at: blobs/retrieve_clauses.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=retrieve_clauses_agent
)

execute_step_clause_task = Task(
    description="Execute processing code logic anchored at: blobs/execute_step_clause.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=execute_step_clause_agent
)

create_review_plan_task = Task(
    description="Execute processing code logic anchored at: blobs/create_review_plan.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=create_review_plan_agent
)

execute_step_task = Task(
    description="Execute processing code logic anchored at: blobs/execute_step.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=execute_step_agent
)

generate_final_report_task = Task(
    description="Execute processing code logic anchored at: blobs/generate_final_report.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=generate_final_report_agent
)

search_task = Task(
    description="Execute processing code logic anchored at: blobs/search.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=search_agent
)

summarize_task = Task(
    description="Execute processing code logic anchored at: blobs/summarize.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=summarize_agent
)

publish_task = Task(
    description="Execute processing code logic anchored at: blobs/publish.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=publish_agent
)

Keywords_task = Task(
    description="Execute processing code logic anchored at: blobs/Keywords.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=Keywords_agent
)

Structure_task = Task(
    description="Execute processing code logic anchored at: blobs/Structure.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=Structure_agent
)

Host question_task = Task(
    description="Execute processing code logic anchored at: blobs/Host question.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=Host question_agent
)

Web research_task = Task(
    description="Execute processing code logic anchored at: blobs/Web research.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=Web research_agent
)

Wiki research_task = Task(
    description="Execute processing code logic anchored at: blobs/Wiki research.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=Wiki research_agent
)

Expert answer_task = Task(
    description="Execute processing code logic anchored at: blobs/Expert answer.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=Expert answer_agent
)

Save podcast_task = Task(
    description="Execute processing code logic anchored at: blobs/Save podcast.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=Save podcast_agent
)

Write script_task = Task(
    description="Execute processing code logic anchored at: blobs/Write script.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=Write script_agent
)

Planing_task = Task(
    description="Execute processing code logic anchored at: blobs/Planing.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=Planing_agent
)

Start research_task = Task(
    description="Execute processing code logic anchored at: blobs/Start research.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=Start research_agent
)

Create podcast_task = Task(
    description="Execute processing code logic anchored at: blobs/Create podcast.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=Create podcast_agent
)

Write report_task = Task(
    description="Execute processing code logic anchored at: blobs/Write report.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=Write report_agent
)

Write introduction_task = Task(
    description="Execute processing code logic anchored at: blobs/Write introduction.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=Write introduction_agent
)

Write conclusion_task = Task(
    description="Execute processing code logic anchored at: blobs/Write conclusion.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=Write conclusion_agent
)

Finalize podcast_task = Task(
    description="Execute processing code logic anchored at: blobs/Finalize podcast.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=Finalize podcast_agent
)

requirements_gathering_task = Task(
    description="Execute processing code logic anchored at: blobs/requirements_gathering.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=requirements_gathering_agent
)

generate_job_desc_task = Task(
    description="Execute processing code logic anchored at: blobs/generate_job_desc.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=generate_job_desc_agent
)

linkedin_process_task = Task(
    description="Execute processing code logic anchored at: blobs/linkedin_process.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=linkedin_process_agent
)

analyze_cv_task = Task(
    description="Execute processing code logic anchored at: blobs/analyze_cv.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=analyze_cv_agent
)

prepare_interview_task = Task(
    description="Execute processing code logic anchored at: blobs/prepare_interview.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=prepare_interview_agent
)

classification_node_task = Task(
    description="Execute processing code logic anchored at: blobs/classification_node.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=classification_node_agent
)

entity_extraction_task = Task(
    description="Execute processing code logic anchored at: blobs/entity_extraction.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=entity_extraction_agent
)

summarization_task = Task(
    description="Execute processing code logic anchored at: blobs/summarization.py. Authorized Connection Boundaries: []",
    expected_output="Successful completion state payload matching criteria for next sequence step.",
    agent=summarization_agent
)

# 7. Assemble the Unified Crew Workspace Execution Order
crew = Crew(
    agents=[approach_analysis_agent, task_knowledge_retrieval_agent, customized_approach_generation_agent, melody_generator_agent, harmony_creator_agent, rhythm_analyzer_agent, style_adapter_agent, midi_converter_agent, triage_agent, response_agent_agent, triage_agent, response_agent_agent, code_execution_node_agent, code_update_node_agent, code_patching_node_agent, bug_report_node_agent, memory_search_node_agent, memory_filter_node_agent, memory_modification_node_agent, memory_generation_node_agent, input_city_agent, input_interests_agent, create_itinerary_agent, get_weather_agent, analyze_disaster_agent, assess_severity_agent, data_logging_agent, emergency_response_agent, civil_defense_response_agent, public_works_response_agent, get_human_verification_agent, send_email_alert_agent, handle_no_approval_agent, get_weather_agent, social_media_monitoring_agent, analyze_disaster_agent, assess_severity_agent, data_logging_agent, emergency_response_agent, civil_defense_response_agent, public_works_response_agent, get_human_verification_agent, send_email_alert_agent, handle_no_approval_agent, assistant_agent, tools_agent, generate_new_inputs_agent, static_test_agent, generate_node_descriptions_agent, generate_testers_agent, generate_test_cases_agent, run_test_cases_agent, analize_results_agent, assistant_agent, tools_agent, process_input_agent, planner_agent, researcher_agent, search_articles_agent, article_decisions_agent, download_articles_agent, paper_analyzer_agent, write_abstract_agent, write_introduction_agent, write_methods_agent, write_results_agent, write_conclusion_agent, write_references_agent, aggregate_paper_agent, critique_paper_agent, revise_paper_agent, final_draft_agent, task_generation_agent, task_dependencies_agent, task_scheduler_agent, task_allocator_agent, risk_assessor_agent, insight_generator_agent, create_project_plan_agent, requirements_gathering_agent, generate_job_desc_agent, linkedin_process_agent, analyze_cv_agent, prepare_interview_agent, check_relevance_agent, check_grammar_agent, analyze_structure_agent, evaluate_depth_agent, calculate_final_score_agent, generate_query_agent, search_web_agent, chunk_context_agent, context_validation_agent, generate_checkpoints_agent, generate_question_agent, next_checkpoint_agent, user_answer_agent, verify_answer_agent, teach_concept_agent, tour_introduction_agent, display_artwork_agent, get_next_artwork_agent, discuss_agent, conclude_tour_agent, character_introduction_agent, ask_question_agent, answer_question_agent, create_characters_agent, create_story_agent, narrartor_agent, sherlock_agent, guesser_agent, conversation_agent, summary_node_agent, research_node_agent, intent_matching_node_agent, instagram_agent, twitter_agent, linkedin_agent, blog_agent, combine_content_agent, generate_character_description_agent, generate_plot_agent, generate_image_prompts_agent, create_images_agent, create_gif_agent, classify_content_agent, process_general_agent, process_poem_agent, process_news_agent, process_joke_agent, text_to_speech_agent, categorize_agent, handle_learning_resource_agent, handle_resume_making_agent, handle_interview_preparation_agent, job_search_agent, mock_interview_agent, interview_topics_questions_agent, tutorial_agent_agent, ask_query_bot_agent, calendar_analyzer_agent, task_analyzer_agent, plan_generator_agent, notewriter_analyze_agent, notewriter_generate_agent, advisor_analyze_agent, advisor_generate_agent, coordinator_agent, profile_analyzer_agent, execute_agent, calendar_analyzer_agent, task_analyzer_agent, plan_generator_agent, notewriter_analyze_agent, notewriter_generate_agent, advisor_analyze_agent, advisor_generate_agent, convert_user_instruction_to_actions_agent, get_initial_action_agent, get_website_state_agent, generate_code_for_action_agent, validate_generated_action_agent, handle_generation_error_agent, post_process_script_agent, execute_test_case_agent, generate_test_report_agent, categorize_agent, analyze_sentiment_agent, handle_technical_agent, handle_billing_agent, handle_general_agent, escalate_agent, get_website_content_agent, analyze_company_agent, generate_concepts_agent, select_templates_agent, generate_text_agent, create_url_agent, tavily_search_agent, schema_mapping_agent, product_comparison_agent, youtube_review_agent, display_agent, send_email_agent, classify_input_agent, discover_database_agent, create_plan_agent, execute_plan_agent, generate_response_agent, generate_newsapi_params_agent, retrieve_articles_metadata_agent, retrieve_articles_text_agent, select_top_urls_agent, summarize_articles_parallel_agent, format_results_agent, decision_making_agent, planning_agent, tools_agent, agent_agent, judge_agent, CATEGORY_agent, SUMMARY_agent, FACT_CHECKING_agent, TONE_ANALYSIS_agent, QUOTE_EXTRACTION_agent, GRAMMAR_AND_BIAS_REVIEW_agent, web_download_agent, embeddings_ner_agent, main_assistant_agent, main_assistant_tools_agent, underwriting_assistant_agent, quote_assistant_agent, quote_assistant_tools_agent, entry_quote_assistant_agent, retrieve_agent, reasoning_agent, classification_grading_agent, update_state_agent, reroute_agent, pass_tool_call_id_agent, pass_final_classifications_agent, create_tool_message_agent, update_workflow_state_agent, ask_user_needs_agent, build_filters_agent, search_listings_agent, fetch_additional_info_agent, irrelevant_agent, classify_contract_agent, retrieve_clauses_agent, execute_step_clause_agent, create_review_plan_agent, execute_step_agent, generate_final_report_agent, search_agent, summarize_agent, publish_agent, Keywords_agent, Structure_agent, Host question_agent, Web research_agent, Wiki research_agent, Expert answer_agent, Save podcast_agent, Write script_agent, Planing_agent, Start research_agent, Create podcast_agent, Write report_agent, Write introduction_agent, Write conclusion_agent, Finalize podcast_agent, requirements_gathering_agent, generate_job_desc_agent, linkedin_process_agent, analyze_cv_agent, prepare_interview_agent, classification_node_agent, entity_extraction_agent, summarization_agent],
    tasks=[approach_analysis_task, task_knowledge_retrieval_task, customized_approach_generation_task, melody_generator_task, harmony_creator_task, rhythm_analyzer_task, style_adapter_task, midi_converter_task, triage_task, response_agent_task, triage_task, response_agent_task, code_execution_node_task, code_update_node_task, code_patching_node_task, bug_report_node_task, memory_search_node_task, memory_filter_node_task, memory_modification_node_task, memory_generation_node_task, input_city_task, input_interests_task, create_itinerary_task, get_weather_task, analyze_disaster_task, assess_severity_task, data_logging_task, emergency_response_task, civil_defense_response_task, public_works_response_task, get_human_verification_task, send_email_alert_task, handle_no_approval_task, get_weather_task, social_media_monitoring_task, analyze_disaster_task, assess_severity_task, data_logging_task, emergency_response_task, civil_defense_response_task, public_works_response_task, get_human_verification_task, send_email_alert_task, handle_no_approval_task, assistant_task, tools_task, generate_new_inputs_task, static_test_task, generate_node_descriptions_task, generate_testers_task, generate_test_cases_task, run_test_cases_task, analize_results_task, assistant_task, tools_task, process_input_task, planner_task, researcher_task, search_articles_task, article_decisions_task, download_articles_task, paper_analyzer_task, write_abstract_task, write_introduction_task, write_methods_task, write_results_task, write_conclusion_task, write_references_task, aggregate_paper_task, critique_paper_task, revise_paper_task, final_draft_task, task_generation_task, task_dependencies_task, task_scheduler_task, task_allocator_task, risk_assessor_task, insight_generator_task, create_project_plan_task, requirements_gathering_task, generate_job_desc_task, linkedin_process_task, analyze_cv_task, prepare_interview_task, check_relevance_task, check_grammar_task, analyze_structure_task, evaluate_depth_task, calculate_final_score_task, generate_query_task, search_web_task, chunk_context_task, context_validation_task, generate_checkpoints_task, generate_question_task, next_checkpoint_task, user_answer_task, verify_answer_task, teach_concept_task, tour_introduction_task, display_artwork_task, get_next_artwork_task, discuss_task, conclude_tour_task, character_introduction_task, ask_question_task, answer_question_task, create_characters_task, create_story_task, narrartor_task, sherlock_task, guesser_task, conversation_task, summary_node_task, research_node_task, intent_matching_node_task, instagram_task, twitter_task, linkedin_task, blog_task, combine_content_task, generate_character_description_task, generate_plot_task, generate_image_prompts_task, create_images_task, create_gif_task, classify_content_task, process_general_task, process_poem_task, process_news_task, process_joke_task, text_to_speech_task, categorize_task, handle_learning_resource_task, handle_resume_making_task, handle_interview_preparation_task, job_search_task, mock_interview_task, interview_topics_questions_task, tutorial_agent_task, ask_query_bot_task, calendar_analyzer_task, task_analyzer_task, plan_generator_task, notewriter_analyze_task, notewriter_generate_task, advisor_analyze_task, advisor_generate_task, coordinator_task, profile_analyzer_task, execute_task, calendar_analyzer_task, task_analyzer_task, plan_generator_task, notewriter_analyze_task, notewriter_generate_task, advisor_analyze_task, advisor_generate_task, convert_user_instruction_to_actions_task, get_initial_action_task, get_website_state_task, generate_code_for_action_task, validate_generated_action_task, handle_generation_error_task, post_process_script_task, execute_test_case_task, generate_test_report_task, categorize_task, analyze_sentiment_task, handle_technical_task, handle_billing_task, handle_general_task, escalate_task, get_website_content_task, analyze_company_task, generate_concepts_task, select_templates_task, generate_text_task, create_url_task, tavily_search_task, schema_mapping_task, product_comparison_task, youtube_review_task, display_task, send_email_task, classify_input_task, discover_database_task, create_plan_task, execute_plan_task, generate_response_task, generate_newsapi_params_task, retrieve_articles_metadata_task, retrieve_articles_text_task, select_top_urls_task, summarize_articles_parallel_task, format_results_task, decision_making_task, planning_task, tools_task, agent_task, judge_task, CATEGORY_task, SUMMARY_task, FACT_CHECKING_task, TONE_ANALYSIS_task, QUOTE_EXTRACTION_task, GRAMMAR_AND_BIAS_REVIEW_task, web_download_task, embeddings_ner_task, main_assistant_task, main_assistant_tools_task, underwriting_assistant_task, quote_assistant_task, quote_assistant_tools_task, entry_quote_assistant_task, retrieve_task, reasoning_task, classification_grading_task, update_state_task, reroute_task, pass_tool_call_id_task, pass_final_classifications_task, create_tool_message_task, update_workflow_state_task, ask_user_needs_task, build_filters_task, search_listings_task, fetch_additional_info_task, irrelevant_task, classify_contract_task, retrieve_clauses_task, execute_step_clause_task, create_review_plan_task, execute_step_task, generate_final_report_task, search_task, summarize_task, publish_task, Keywords_task, Structure_task, Host question_task, Web research_task, Wiki research_task, Expert answer_task, Save podcast_task, Write script_task, Planing_task, Start research_task, Create podcast_task, Write report_task, Write introduction_task, Write conclusion_task, Finalize podcast_task, requirements_gathering_task, generate_job_desc_task, linkedin_process_task, analyze_cv_task, prepare_interview_task, classification_node_task, entity_extraction_task, summarization_task],
    process=Process.sequential,
    verbose=True
)

# 8. Execution and Localized Blob Verification Pipeline
if __name__ == "__main__":
    print("🚀 Running compiled SwarmHub execution pipeline validation...")
    print("⚠️ [Mode: Local Offline Execution] State-Machine verification pass ignited.\n")
    default_state = {"messages": [], "context": {}, "next_action": ""}
    state = default_state

    # Target framework execution state-machine routing configuration maps
    NODES_CONFIG = {
        "approach_analysis": {"import_path": "blobs.approach_analysis", "interfaces": [], "inline_f": "_inline_approach_analysis" if hasattr(sys.modules[__name__], "_inline_approach_analysis") else None},
        "task_knowledge_retrieval": {"import_path": "blobs.task_knowledge_retrieval", "interfaces": [], "inline_f": "_inline_task_knowledge_retrieval" if hasattr(sys.modules[__name__], "_inline_task_knowledge_retrieval") else None},
        "customized_approach_generation": {"import_path": "blobs.customized_approach_generation", "interfaces": [], "inline_f": "_inline_customized_approach_generation" if hasattr(sys.modules[__name__], "_inline_customized_approach_generation") else None},
        "melody_generator": {"import_path": "blobs.melody_generator", "interfaces": [], "inline_f": "_inline_melody_generator" if hasattr(sys.modules[__name__], "_inline_melody_generator") else None},
        "harmony_creator": {"import_path": "blobs.harmony_creator", "interfaces": [], "inline_f": "_inline_harmony_creator" if hasattr(sys.modules[__name__], "_inline_harmony_creator") else None},
        "rhythm_analyzer": {"import_path": "blobs.rhythm_analyzer", "interfaces": [], "inline_f": "_inline_rhythm_analyzer" if hasattr(sys.modules[__name__], "_inline_rhythm_analyzer") else None},
        "style_adapter": {"import_path": "blobs.style_adapter", "interfaces": [], "inline_f": "_inline_style_adapter" if hasattr(sys.modules[__name__], "_inline_style_adapter") else None},
        "midi_converter": {"import_path": "blobs.midi_converter", "interfaces": [], "inline_f": "_inline_midi_converter" if hasattr(sys.modules[__name__], "_inline_midi_converter") else None},
        "triage": {"import_path": "blobs.triage", "interfaces": [], "inline_f": "_inline_triage" if hasattr(sys.modules[__name__], "_inline_triage") else None},
        "response_agent": {"import_path": "blobs.response_agent", "interfaces": [], "inline_f": "_inline_response_agent" if hasattr(sys.modules[__name__], "_inline_response_agent") else None},
        "triage": {"import_path": "blobs.triage", "interfaces": [], "inline_f": "_inline_triage" if hasattr(sys.modules[__name__], "_inline_triage") else None},
        "response_agent": {"import_path": "blobs.response_agent", "interfaces": [], "inline_f": "_inline_response_agent" if hasattr(sys.modules[__name__], "_inline_response_agent") else None},
        "code_execution_node": {"import_path": "blobs.code_execution_node", "interfaces": [], "inline_f": "_inline_code_execution_node" if hasattr(sys.modules[__name__], "_inline_code_execution_node") else None},
        "code_update_node": {"import_path": "blobs.code_update_node", "interfaces": [], "inline_f": "_inline_code_update_node" if hasattr(sys.modules[__name__], "_inline_code_update_node") else None},
        "code_patching_node": {"import_path": "blobs.code_patching_node", "interfaces": [], "inline_f": "_inline_code_patching_node" if hasattr(sys.modules[__name__], "_inline_code_patching_node") else None},
        "bug_report_node": {"import_path": "blobs.bug_report_node", "interfaces": [], "inline_f": "_inline_bug_report_node" if hasattr(sys.modules[__name__], "_inline_bug_report_node") else None},
        "memory_search_node": {"import_path": "blobs.memory_search_node", "interfaces": [], "inline_f": "_inline_memory_search_node" if hasattr(sys.modules[__name__], "_inline_memory_search_node") else None},
        "memory_filter_node": {"import_path": "blobs.memory_filter_node", "interfaces": [], "inline_f": "_inline_memory_filter_node" if hasattr(sys.modules[__name__], "_inline_memory_filter_node") else None},
        "memory_modification_node": {"import_path": "blobs.memory_modification_node", "interfaces": [], "inline_f": "_inline_memory_modification_node" if hasattr(sys.modules[__name__], "_inline_memory_modification_node") else None},
        "memory_generation_node": {"import_path": "blobs.memory_generation_node", "interfaces": [], "inline_f": "_inline_memory_generation_node" if hasattr(sys.modules[__name__], "_inline_memory_generation_node") else None},
        "input_city": {"import_path": "blobs.input_city", "interfaces": [], "inline_f": "_inline_input_city" if hasattr(sys.modules[__name__], "_inline_input_city") else None},
        "input_interests": {"import_path": "blobs.input_interests", "interfaces": [], "inline_f": "_inline_input_interests" if hasattr(sys.modules[__name__], "_inline_input_interests") else None},
        "create_itinerary": {"import_path": "blobs.create_itinerary", "interfaces": [], "inline_f": "_inline_create_itinerary" if hasattr(sys.modules[__name__], "_inline_create_itinerary") else None},
        "get_weather": {"import_path": "blobs.get_weather", "interfaces": [], "inline_f": "_inline_get_weather" if hasattr(sys.modules[__name__], "_inline_get_weather") else None},
        "analyze_disaster": {"import_path": "blobs.analyze_disaster", "interfaces": [], "inline_f": "_inline_analyze_disaster" if hasattr(sys.modules[__name__], "_inline_analyze_disaster") else None},
        "assess_severity": {"import_path": "blobs.assess_severity", "interfaces": [], "inline_f": "_inline_assess_severity" if hasattr(sys.modules[__name__], "_inline_assess_severity") else None},
        "data_logging": {"import_path": "blobs.data_logging", "interfaces": [], "inline_f": "_inline_data_logging" if hasattr(sys.modules[__name__], "_inline_data_logging") else None},
        "emergency_response": {"import_path": "blobs.emergency_response", "interfaces": [], "inline_f": "_inline_emergency_response" if hasattr(sys.modules[__name__], "_inline_emergency_response") else None},
        "civil_defense_response": {"import_path": "blobs.civil_defense_response", "interfaces": [], "inline_f": "_inline_civil_defense_response" if hasattr(sys.modules[__name__], "_inline_civil_defense_response") else None},
        "public_works_response": {"import_path": "blobs.public_works_response", "interfaces": [], "inline_f": "_inline_public_works_response" if hasattr(sys.modules[__name__], "_inline_public_works_response") else None},
        "get_human_verification": {"import_path": "blobs.get_human_verification", "interfaces": [], "inline_f": "_inline_get_human_verification" if hasattr(sys.modules[__name__], "_inline_get_human_verification") else None},
        "send_email_alert": {"import_path": "blobs.send_email_alert", "interfaces": [], "inline_f": "_inline_send_email_alert" if hasattr(sys.modules[__name__], "_inline_send_email_alert") else None},
        "handle_no_approval": {"import_path": "blobs.handle_no_approval", "interfaces": [], "inline_f": "_inline_handle_no_approval" if hasattr(sys.modules[__name__], "_inline_handle_no_approval") else None},
        "get_weather": {"import_path": "blobs.get_weather", "interfaces": [], "inline_f": "_inline_get_weather" if hasattr(sys.modules[__name__], "_inline_get_weather") else None},
        "social_media_monitoring": {"import_path": "blobs.social_media_monitoring", "interfaces": [], "inline_f": "_inline_social_media_monitoring" if hasattr(sys.modules[__name__], "_inline_social_media_monitoring") else None},
        "analyze_disaster": {"import_path": "blobs.analyze_disaster", "interfaces": [], "inline_f": "_inline_analyze_disaster" if hasattr(sys.modules[__name__], "_inline_analyze_disaster") else None},
        "assess_severity": {"import_path": "blobs.assess_severity", "interfaces": [], "inline_f": "_inline_assess_severity" if hasattr(sys.modules[__name__], "_inline_assess_severity") else None},
        "data_logging": {"import_path": "blobs.data_logging", "interfaces": [], "inline_f": "_inline_data_logging" if hasattr(sys.modules[__name__], "_inline_data_logging") else None},
        "emergency_response": {"import_path": "blobs.emergency_response", "interfaces": [], "inline_f": "_inline_emergency_response" if hasattr(sys.modules[__name__], "_inline_emergency_response") else None},
        "civil_defense_response": {"import_path": "blobs.civil_defense_response", "interfaces": [], "inline_f": "_inline_civil_defense_response" if hasattr(sys.modules[__name__], "_inline_civil_defense_response") else None},
        "public_works_response": {"import_path": "blobs.public_works_response", "interfaces": [], "inline_f": "_inline_public_works_response" if hasattr(sys.modules[__name__], "_inline_public_works_response") else None},
        "get_human_verification": {"import_path": "blobs.get_human_verification", "interfaces": [], "inline_f": "_inline_get_human_verification" if hasattr(sys.modules[__name__], "_inline_get_human_verification") else None},
        "send_email_alert": {"import_path": "blobs.send_email_alert", "interfaces": [], "inline_f": "_inline_send_email_alert" if hasattr(sys.modules[__name__], "_inline_send_email_alert") else None},
        "handle_no_approval": {"import_path": "blobs.handle_no_approval", "interfaces": [], "inline_f": "_inline_handle_no_approval" if hasattr(sys.modules[__name__], "_inline_handle_no_approval") else None},
        "assistant": {"import_path": "blobs.assistant", "interfaces": [], "inline_f": "_inline_assistant" if hasattr(sys.modules[__name__], "_inline_assistant") else None},
        "tools": {"import_path": "blobs.tools", "interfaces": [], "inline_f": "_inline_tools" if hasattr(sys.modules[__name__], "_inline_tools") else None},
        "generate_new_inputs": {"import_path": "blobs.generate_new_inputs", "interfaces": [], "inline_f": "_inline_generate_new_inputs" if hasattr(sys.modules[__name__], "_inline_generate_new_inputs") else None},
        "static_test": {"import_path": "blobs.static_test", "interfaces": [], "inline_f": "_inline_static_test" if hasattr(sys.modules[__name__], "_inline_static_test") else None},
        "generate_node_descriptions": {"import_path": "blobs.generate_node_descriptions", "interfaces": [], "inline_f": "_inline_generate_node_descriptions" if hasattr(sys.modules[__name__], "_inline_generate_node_descriptions") else None},
        "generate_testers": {"import_path": "blobs.generate_testers", "interfaces": [], "inline_f": "_inline_generate_testers" if hasattr(sys.modules[__name__], "_inline_generate_testers") else None},
        "generate_test_cases": {"import_path": "blobs.generate_test_cases", "interfaces": [], "inline_f": "_inline_generate_test_cases" if hasattr(sys.modules[__name__], "_inline_generate_test_cases") else None},
        "run_test_cases": {"import_path": "blobs.run_test_cases", "interfaces": [], "inline_f": "_inline_run_test_cases" if hasattr(sys.modules[__name__], "_inline_run_test_cases") else None},
        "analize_results": {"import_path": "blobs.analize_results", "interfaces": [], "inline_f": "_inline_analize_results" if hasattr(sys.modules[__name__], "_inline_analize_results") else None},
        "assistant": {"import_path": "blobs.assistant", "interfaces": [], "inline_f": "_inline_assistant" if hasattr(sys.modules[__name__], "_inline_assistant") else None},
        "tools": {"import_path": "blobs.tools", "interfaces": [], "inline_f": "_inline_tools" if hasattr(sys.modules[__name__], "_inline_tools") else None},
        "process_input": {"import_path": "blobs.process_input", "interfaces": [], "inline_f": "_inline_process_input" if hasattr(sys.modules[__name__], "_inline_process_input") else None},
        "planner": {"import_path": "blobs.planner", "interfaces": [], "inline_f": "_inline_planner" if hasattr(sys.modules[__name__], "_inline_planner") else None},
        "researcher": {"import_path": "blobs.researcher", "interfaces": [], "inline_f": "_inline_researcher" if hasattr(sys.modules[__name__], "_inline_researcher") else None},
        "search_articles": {"import_path": "blobs.search_articles", "interfaces": [], "inline_f": "_inline_search_articles" if hasattr(sys.modules[__name__], "_inline_search_articles") else None},
        "article_decisions": {"import_path": "blobs.article_decisions", "interfaces": [], "inline_f": "_inline_article_decisions" if hasattr(sys.modules[__name__], "_inline_article_decisions") else None},
        "download_articles": {"import_path": "blobs.download_articles", "interfaces": [], "inline_f": "_inline_download_articles" if hasattr(sys.modules[__name__], "_inline_download_articles") else None},
        "paper_analyzer": {"import_path": "blobs.paper_analyzer", "interfaces": [], "inline_f": "_inline_paper_analyzer" if hasattr(sys.modules[__name__], "_inline_paper_analyzer") else None},
        "write_abstract": {"import_path": "blobs.write_abstract", "interfaces": [], "inline_f": "_inline_write_abstract" if hasattr(sys.modules[__name__], "_inline_write_abstract") else None},
        "write_introduction": {"import_path": "blobs.write_introduction", "interfaces": [], "inline_f": "_inline_write_introduction" if hasattr(sys.modules[__name__], "_inline_write_introduction") else None},
        "write_methods": {"import_path": "blobs.write_methods", "interfaces": [], "inline_f": "_inline_write_methods" if hasattr(sys.modules[__name__], "_inline_write_methods") else None},
        "write_results": {"import_path": "blobs.write_results", "interfaces": [], "inline_f": "_inline_write_results" if hasattr(sys.modules[__name__], "_inline_write_results") else None},
        "write_conclusion": {"import_path": "blobs.write_conclusion", "interfaces": [], "inline_f": "_inline_write_conclusion" if hasattr(sys.modules[__name__], "_inline_write_conclusion") else None},
        "write_references": {"import_path": "blobs.write_references", "interfaces": [], "inline_f": "_inline_write_references" if hasattr(sys.modules[__name__], "_inline_write_references") else None},
        "aggregate_paper": {"import_path": "blobs.aggregate_paper", "interfaces": [], "inline_f": "_inline_aggregate_paper" if hasattr(sys.modules[__name__], "_inline_aggregate_paper") else None},
        "critique_paper": {"import_path": "blobs.critique_paper", "interfaces": [], "inline_f": "_inline_critique_paper" if hasattr(sys.modules[__name__], "_inline_critique_paper") else None},
        "revise_paper": {"import_path": "blobs.revise_paper", "interfaces": [], "inline_f": "_inline_revise_paper" if hasattr(sys.modules[__name__], "_inline_revise_paper") else None},
        "final_draft": {"import_path": "blobs.final_draft", "interfaces": [], "inline_f": "_inline_final_draft" if hasattr(sys.modules[__name__], "_inline_final_draft") else None},
        "task_generation": {"import_path": "blobs.task_generation", "interfaces": [], "inline_f": "_inline_task_generation" if hasattr(sys.modules[__name__], "_inline_task_generation") else None},
        "task_dependencies": {"import_path": "blobs.task_dependencies", "interfaces": [], "inline_f": "_inline_task_dependencies" if hasattr(sys.modules[__name__], "_inline_task_dependencies") else None},
        "task_scheduler": {"import_path": "blobs.task_scheduler", "interfaces": [], "inline_f": "_inline_task_scheduler" if hasattr(sys.modules[__name__], "_inline_task_scheduler") else None},
        "task_allocator": {"import_path": "blobs.task_allocator", "interfaces": [], "inline_f": "_inline_task_allocator" if hasattr(sys.modules[__name__], "_inline_task_allocator") else None},
        "risk_assessor": {"import_path": "blobs.risk_assessor", "interfaces": [], "inline_f": "_inline_risk_assessor" if hasattr(sys.modules[__name__], "_inline_risk_assessor") else None},
        "insight_generator": {"import_path": "blobs.insight_generator", "interfaces": [], "inline_f": "_inline_insight_generator" if hasattr(sys.modules[__name__], "_inline_insight_generator") else None},
        "create_project_plan": {"import_path": "blobs.create_project_plan", "interfaces": [], "inline_f": "_inline_create_project_plan" if hasattr(sys.modules[__name__], "_inline_create_project_plan") else None},
        "requirements_gathering": {"import_path": "blobs.requirements_gathering", "interfaces": [], "inline_f": "_inline_requirements_gathering" if hasattr(sys.modules[__name__], "_inline_requirements_gathering") else None},
        "generate_job_desc": {"import_path": "blobs.generate_job_desc", "interfaces": [], "inline_f": "_inline_generate_job_desc" if hasattr(sys.modules[__name__], "_inline_generate_job_desc") else None},
        "linkedin_process": {"import_path": "blobs.linkedin_process", "interfaces": [], "inline_f": "_inline_linkedin_process" if hasattr(sys.modules[__name__], "_inline_linkedin_process") else None},
        "analyze_cv": {"import_path": "blobs.analyze_cv", "interfaces": [], "inline_f": "_inline_analyze_cv" if hasattr(sys.modules[__name__], "_inline_analyze_cv") else None},
        "prepare_interview": {"import_path": "blobs.prepare_interview", "interfaces": [], "inline_f": "_inline_prepare_interview" if hasattr(sys.modules[__name__], "_inline_prepare_interview") else None},
        "check_relevance": {"import_path": "blobs.check_relevance", "interfaces": [], "inline_f": "_inline_check_relevance" if hasattr(sys.modules[__name__], "_inline_check_relevance") else None},
        "check_grammar": {"import_path": "blobs.check_grammar", "interfaces": [], "inline_f": "_inline_check_grammar" if hasattr(sys.modules[__name__], "_inline_check_grammar") else None},
        "analyze_structure": {"import_path": "blobs.analyze_structure", "interfaces": [], "inline_f": "_inline_analyze_structure" if hasattr(sys.modules[__name__], "_inline_analyze_structure") else None},
        "evaluate_depth": {"import_path": "blobs.evaluate_depth", "interfaces": [], "inline_f": "_inline_evaluate_depth" if hasattr(sys.modules[__name__], "_inline_evaluate_depth") else None},
        "calculate_final_score": {"import_path": "blobs.calculate_final_score", "interfaces": [], "inline_f": "_inline_calculate_final_score" if hasattr(sys.modules[__name__], "_inline_calculate_final_score") else None},
        "generate_query": {"import_path": "blobs.generate_query", "interfaces": [], "inline_f": "_inline_generate_query" if hasattr(sys.modules[__name__], "_inline_generate_query") else None},
        "search_web": {"import_path": "blobs.search_web", "interfaces": [], "inline_f": "_inline_search_web" if hasattr(sys.modules[__name__], "_inline_search_web") else None},
        "chunk_context": {"import_path": "blobs.chunk_context", "interfaces": [], "inline_f": "_inline_chunk_context" if hasattr(sys.modules[__name__], "_inline_chunk_context") else None},
        "context_validation": {"import_path": "blobs.context_validation", "interfaces": [], "inline_f": "_inline_context_validation" if hasattr(sys.modules[__name__], "_inline_context_validation") else None},
        "generate_checkpoints": {"import_path": "blobs.generate_checkpoints", "interfaces": [], "inline_f": "_inline_generate_checkpoints" if hasattr(sys.modules[__name__], "_inline_generate_checkpoints") else None},
        "generate_question": {"import_path": "blobs.generate_question", "interfaces": [], "inline_f": "_inline_generate_question" if hasattr(sys.modules[__name__], "_inline_generate_question") else None},
        "next_checkpoint": {"import_path": "blobs.next_checkpoint", "interfaces": [], "inline_f": "_inline_next_checkpoint" if hasattr(sys.modules[__name__], "_inline_next_checkpoint") else None},
        "user_answer": {"import_path": "blobs.user_answer", "interfaces": [], "inline_f": "_inline_user_answer" if hasattr(sys.modules[__name__], "_inline_user_answer") else None},
        "verify_answer": {"import_path": "blobs.verify_answer", "interfaces": [], "inline_f": "_inline_verify_answer" if hasattr(sys.modules[__name__], "_inline_verify_answer") else None},
        "teach_concept": {"import_path": "blobs.teach_concept", "interfaces": [], "inline_f": "_inline_teach_concept" if hasattr(sys.modules[__name__], "_inline_teach_concept") else None},
        "tour_introduction": {"import_path": "blobs.tour_introduction", "interfaces": [], "inline_f": "_inline_tour_introduction" if hasattr(sys.modules[__name__], "_inline_tour_introduction") else None},
        "display_artwork": {"import_path": "blobs.display_artwork", "interfaces": [], "inline_f": "_inline_display_artwork" if hasattr(sys.modules[__name__], "_inline_display_artwork") else None},
        "get_next_artwork": {"import_path": "blobs.get_next_artwork", "interfaces": [], "inline_f": "_inline_get_next_artwork" if hasattr(sys.modules[__name__], "_inline_get_next_artwork") else None},
        "discuss": {"import_path": "blobs.discuss", "interfaces": [], "inline_f": "_inline_discuss" if hasattr(sys.modules[__name__], "_inline_discuss") else None},
        "conclude_tour": {"import_path": "blobs.conclude_tour", "interfaces": [], "inline_f": "_inline_conclude_tour" if hasattr(sys.modules[__name__], "_inline_conclude_tour") else None},
        "character_introduction": {"import_path": "blobs.character_introduction", "interfaces": [], "inline_f": "_inline_character_introduction" if hasattr(sys.modules[__name__], "_inline_character_introduction") else None},
        "ask_question": {"import_path": "blobs.ask_question", "interfaces": [], "inline_f": "_inline_ask_question" if hasattr(sys.modules[__name__], "_inline_ask_question") else None},
        "answer_question": {"import_path": "blobs.answer_question", "interfaces": [], "inline_f": "_inline_answer_question" if hasattr(sys.modules[__name__], "_inline_answer_question") else None},
        "create_characters": {"import_path": "blobs.create_characters", "interfaces": [], "inline_f": "_inline_create_characters" if hasattr(sys.modules[__name__], "_inline_create_characters") else None},
        "create_story": {"import_path": "blobs.create_story", "interfaces": [], "inline_f": "_inline_create_story" if hasattr(sys.modules[__name__], "_inline_create_story") else None},
        "narrartor": {"import_path": "blobs.narrartor", "interfaces": [], "inline_f": "_inline_narrartor" if hasattr(sys.modules[__name__], "_inline_narrartor") else None},
        "sherlock": {"import_path": "blobs.sherlock", "interfaces": [], "inline_f": "_inline_sherlock" if hasattr(sys.modules[__name__], "_inline_sherlock") else None},
        "guesser": {"import_path": "blobs.guesser", "interfaces": [], "inline_f": "_inline_guesser" if hasattr(sys.modules[__name__], "_inline_guesser") else None},
        "conversation": {"import_path": "blobs.conversation", "interfaces": [], "inline_f": "_inline_conversation" if hasattr(sys.modules[__name__], "_inline_conversation") else None},
        "summary_node": {"import_path": "blobs.summary_node", "interfaces": [], "inline_f": "_inline_summary_node" if hasattr(sys.modules[__name__], "_inline_summary_node") else None},
        "research_node": {"import_path": "blobs.research_node", "interfaces": [], "inline_f": "_inline_research_node" if hasattr(sys.modules[__name__], "_inline_research_node") else None},
        "intent_matching_node": {"import_path": "blobs.intent_matching_node", "interfaces": [], "inline_f": "_inline_intent_matching_node" if hasattr(sys.modules[__name__], "_inline_intent_matching_node") else None},
        "instagram": {"import_path": "blobs.instagram", "interfaces": [], "inline_f": "_inline_instagram" if hasattr(sys.modules[__name__], "_inline_instagram") else None},
        "twitter": {"import_path": "blobs.twitter", "interfaces": [], "inline_f": "_inline_twitter" if hasattr(sys.modules[__name__], "_inline_twitter") else None},
        "linkedin": {"import_path": "blobs.linkedin", "interfaces": [], "inline_f": "_inline_linkedin" if hasattr(sys.modules[__name__], "_inline_linkedin") else None},
        "blog": {"import_path": "blobs.blog", "interfaces": [], "inline_f": "_inline_blog" if hasattr(sys.modules[__name__], "_inline_blog") else None},
        "combine_content": {"import_path": "blobs.combine_content", "interfaces": [], "inline_f": "_inline_combine_content" if hasattr(sys.modules[__name__], "_inline_combine_content") else None},
        "generate_character_description": {"import_path": "blobs.generate_character_description", "interfaces": [], "inline_f": "_inline_generate_character_description" if hasattr(sys.modules[__name__], "_inline_generate_character_description") else None},
        "generate_plot": {"import_path": "blobs.generate_plot", "interfaces": [], "inline_f": "_inline_generate_plot" if hasattr(sys.modules[__name__], "_inline_generate_plot") else None},
        "generate_image_prompts": {"import_path": "blobs.generate_image_prompts", "interfaces": [], "inline_f": "_inline_generate_image_prompts" if hasattr(sys.modules[__name__], "_inline_generate_image_prompts") else None},
        "create_images": {"import_path": "blobs.create_images", "interfaces": [], "inline_f": "_inline_create_images" if hasattr(sys.modules[__name__], "_inline_create_images") else None},
        "create_gif": {"import_path": "blobs.create_gif", "interfaces": [], "inline_f": "_inline_create_gif" if hasattr(sys.modules[__name__], "_inline_create_gif") else None},
        "classify_content": {"import_path": "blobs.classify_content", "interfaces": [], "inline_f": "_inline_classify_content" if hasattr(sys.modules[__name__], "_inline_classify_content") else None},
        "process_general": {"import_path": "blobs.process_general", "interfaces": [], "inline_f": "_inline_process_general" if hasattr(sys.modules[__name__], "_inline_process_general") else None},
        "process_poem": {"import_path": "blobs.process_poem", "interfaces": [], "inline_f": "_inline_process_poem" if hasattr(sys.modules[__name__], "_inline_process_poem") else None},
        "process_news": {"import_path": "blobs.process_news", "interfaces": [], "inline_f": "_inline_process_news" if hasattr(sys.modules[__name__], "_inline_process_news") else None},
        "process_joke": {"import_path": "blobs.process_joke", "interfaces": [], "inline_f": "_inline_process_joke" if hasattr(sys.modules[__name__], "_inline_process_joke") else None},
        "text_to_speech": {"import_path": "blobs.text_to_speech", "interfaces": [], "inline_f": "_inline_text_to_speech" if hasattr(sys.modules[__name__], "_inline_text_to_speech") else None},
        "categorize": {"import_path": "blobs.categorize", "interfaces": [], "inline_f": "_inline_categorize" if hasattr(sys.modules[__name__], "_inline_categorize") else None},
        "handle_learning_resource": {"import_path": "blobs.handle_learning_resource", "interfaces": [], "inline_f": "_inline_handle_learning_resource" if hasattr(sys.modules[__name__], "_inline_handle_learning_resource") else None},
        "handle_resume_making": {"import_path": "blobs.handle_resume_making", "interfaces": [], "inline_f": "_inline_handle_resume_making" if hasattr(sys.modules[__name__], "_inline_handle_resume_making") else None},
        "handle_interview_preparation": {"import_path": "blobs.handle_interview_preparation", "interfaces": [], "inline_f": "_inline_handle_interview_preparation" if hasattr(sys.modules[__name__], "_inline_handle_interview_preparation") else None},
        "job_search": {"import_path": "blobs.job_search", "interfaces": [], "inline_f": "_inline_job_search" if hasattr(sys.modules[__name__], "_inline_job_search") else None},
        "mock_interview": {"import_path": "blobs.mock_interview", "interfaces": [], "inline_f": "_inline_mock_interview" if hasattr(sys.modules[__name__], "_inline_mock_interview") else None},
        "interview_topics_questions": {"import_path": "blobs.interview_topics_questions", "interfaces": [], "inline_f": "_inline_interview_topics_questions" if hasattr(sys.modules[__name__], "_inline_interview_topics_questions") else None},
        "tutorial_agent": {"import_path": "blobs.tutorial_agent", "interfaces": [], "inline_f": "_inline_tutorial_agent" if hasattr(sys.modules[__name__], "_inline_tutorial_agent") else None},
        "ask_query_bot": {"import_path": "blobs.ask_query_bot", "interfaces": [], "inline_f": "_inline_ask_query_bot" if hasattr(sys.modules[__name__], "_inline_ask_query_bot") else None},
        "calendar_analyzer": {"import_path": "blobs.calendar_analyzer", "interfaces": [], "inline_f": "_inline_calendar_analyzer" if hasattr(sys.modules[__name__], "_inline_calendar_analyzer") else None},
        "task_analyzer": {"import_path": "blobs.task_analyzer", "interfaces": [], "inline_f": "_inline_task_analyzer" if hasattr(sys.modules[__name__], "_inline_task_analyzer") else None},
        "plan_generator": {"import_path": "blobs.plan_generator", "interfaces": [], "inline_f": "_inline_plan_generator" if hasattr(sys.modules[__name__], "_inline_plan_generator") else None},
        "notewriter_analyze": {"import_path": "blobs.notewriter_analyze", "interfaces": [], "inline_f": "_inline_notewriter_analyze" if hasattr(sys.modules[__name__], "_inline_notewriter_analyze") else None},
        "notewriter_generate": {"import_path": "blobs.notewriter_generate", "interfaces": [], "inline_f": "_inline_notewriter_generate" if hasattr(sys.modules[__name__], "_inline_notewriter_generate") else None},
        "advisor_analyze": {"import_path": "blobs.advisor_analyze", "interfaces": [], "inline_f": "_inline_advisor_analyze" if hasattr(sys.modules[__name__], "_inline_advisor_analyze") else None},
        "advisor_generate": {"import_path": "blobs.advisor_generate", "interfaces": [], "inline_f": "_inline_advisor_generate" if hasattr(sys.modules[__name__], "_inline_advisor_generate") else None},
        "coordinator": {"import_path": "blobs.coordinator", "interfaces": [], "inline_f": "_inline_coordinator" if hasattr(sys.modules[__name__], "_inline_coordinator") else None},
        "profile_analyzer": {"import_path": "blobs.profile_analyzer", "interfaces": [], "inline_f": "_inline_profile_analyzer" if hasattr(sys.modules[__name__], "_inline_profile_analyzer") else None},
        "execute": {"import_path": "blobs.execute", "interfaces": [], "inline_f": "_inline_execute" if hasattr(sys.modules[__name__], "_inline_execute") else None},
        "calendar_analyzer": {"import_path": "blobs.calendar_analyzer", "interfaces": [], "inline_f": "_inline_calendar_analyzer" if hasattr(sys.modules[__name__], "_inline_calendar_analyzer") else None},
        "task_analyzer": {"import_path": "blobs.task_analyzer", "interfaces": [], "inline_f": "_inline_task_analyzer" if hasattr(sys.modules[__name__], "_inline_task_analyzer") else None},
        "plan_generator": {"import_path": "blobs.plan_generator", "interfaces": [], "inline_f": "_inline_plan_generator" if hasattr(sys.modules[__name__], "_inline_plan_generator") else None},
        "notewriter_analyze": {"import_path": "blobs.notewriter_analyze", "interfaces": [], "inline_f": "_inline_notewriter_analyze" if hasattr(sys.modules[__name__], "_inline_notewriter_analyze") else None},
        "notewriter_generate": {"import_path": "blobs.notewriter_generate", "interfaces": [], "inline_f": "_inline_notewriter_generate" if hasattr(sys.modules[__name__], "_inline_notewriter_generate") else None},
        "advisor_analyze": {"import_path": "blobs.advisor_analyze", "interfaces": [], "inline_f": "_inline_advisor_analyze" if hasattr(sys.modules[__name__], "_inline_advisor_analyze") else None},
        "advisor_generate": {"import_path": "blobs.advisor_generate", "interfaces": [], "inline_f": "_inline_advisor_generate" if hasattr(sys.modules[__name__], "_inline_advisor_generate") else None},
        "convert_user_instruction_to_actions": {"import_path": "blobs.convert_user_instruction_to_actions", "interfaces": [], "inline_f": "_inline_convert_user_instruction_to_actions" if hasattr(sys.modules[__name__], "_inline_convert_user_instruction_to_actions") else None},
        "get_initial_action": {"import_path": "blobs.get_initial_action", "interfaces": [], "inline_f": "_inline_get_initial_action" if hasattr(sys.modules[__name__], "_inline_get_initial_action") else None},
        "get_website_state": {"import_path": "blobs.get_website_state", "interfaces": [], "inline_f": "_inline_get_website_state" if hasattr(sys.modules[__name__], "_inline_get_website_state") else None},
        "generate_code_for_action": {"import_path": "blobs.generate_code_for_action", "interfaces": [], "inline_f": "_inline_generate_code_for_action" if hasattr(sys.modules[__name__], "_inline_generate_code_for_action") else None},
        "validate_generated_action": {"import_path": "blobs.validate_generated_action", "interfaces": [], "inline_f": "_inline_validate_generated_action" if hasattr(sys.modules[__name__], "_inline_validate_generated_action") else None},
        "handle_generation_error": {"import_path": "blobs.handle_generation_error", "interfaces": [], "inline_f": "_inline_handle_generation_error" if hasattr(sys.modules[__name__], "_inline_handle_generation_error") else None},
        "post_process_script": {"import_path": "blobs.post_process_script", "interfaces": [], "inline_f": "_inline_post_process_script" if hasattr(sys.modules[__name__], "_inline_post_process_script") else None},
        "execute_test_case": {"import_path": "blobs.execute_test_case", "interfaces": [], "inline_f": "_inline_execute_test_case" if hasattr(sys.modules[__name__], "_inline_execute_test_case") else None},
        "generate_test_report": {"import_path": "blobs.generate_test_report", "interfaces": [], "inline_f": "_inline_generate_test_report" if hasattr(sys.modules[__name__], "_inline_generate_test_report") else None},
        "categorize": {"import_path": "blobs.categorize", "interfaces": [], "inline_f": "_inline_categorize" if hasattr(sys.modules[__name__], "_inline_categorize") else None},
        "analyze_sentiment": {"import_path": "blobs.analyze_sentiment", "interfaces": [], "inline_f": "_inline_analyze_sentiment" if hasattr(sys.modules[__name__], "_inline_analyze_sentiment") else None},
        "handle_technical": {"import_path": "blobs.handle_technical", "interfaces": [], "inline_f": "_inline_handle_technical" if hasattr(sys.modules[__name__], "_inline_handle_technical") else None},
        "handle_billing": {"import_path": "blobs.handle_billing", "interfaces": [], "inline_f": "_inline_handle_billing" if hasattr(sys.modules[__name__], "_inline_handle_billing") else None},
        "handle_general": {"import_path": "blobs.handle_general", "interfaces": [], "inline_f": "_inline_handle_general" if hasattr(sys.modules[__name__], "_inline_handle_general") else None},
        "escalate": {"import_path": "blobs.escalate", "interfaces": [], "inline_f": "_inline_escalate" if hasattr(sys.modules[__name__], "_inline_escalate") else None},
        "get_website_content": {"import_path": "blobs.get_website_content", "interfaces": [], "inline_f": "_inline_get_website_content" if hasattr(sys.modules[__name__], "_inline_get_website_content") else None},
        "analyze_company": {"import_path": "blobs.analyze_company", "interfaces": [], "inline_f": "_inline_analyze_company" if hasattr(sys.modules[__name__], "_inline_analyze_company") else None},
        "generate_concepts": {"import_path": "blobs.generate_concepts", "interfaces": [], "inline_f": "_inline_generate_concepts" if hasattr(sys.modules[__name__], "_inline_generate_concepts") else None},
        "select_templates": {"import_path": "blobs.select_templates", "interfaces": [], "inline_f": "_inline_select_templates" if hasattr(sys.modules[__name__], "_inline_select_templates") else None},
        "generate_text": {"import_path": "blobs.generate_text", "interfaces": [], "inline_f": "_inline_generate_text" if hasattr(sys.modules[__name__], "_inline_generate_text") else None},
        "create_url": {"import_path": "blobs.create_url", "interfaces": [], "inline_f": "_inline_create_url" if hasattr(sys.modules[__name__], "_inline_create_url") else None},
        "tavily_search": {"import_path": "blobs.tavily_search", "interfaces": [], "inline_f": "_inline_tavily_search" if hasattr(sys.modules[__name__], "_inline_tavily_search") else None},
        "schema_mapping": {"import_path": "blobs.schema_mapping", "interfaces": [], "inline_f": "_inline_schema_mapping" if hasattr(sys.modules[__name__], "_inline_schema_mapping") else None},
        "product_comparison": {"import_path": "blobs.product_comparison", "interfaces": [], "inline_f": "_inline_product_comparison" if hasattr(sys.modules[__name__], "_inline_product_comparison") else None},
        "youtube_review": {"import_path": "blobs.youtube_review", "interfaces": [], "inline_f": "_inline_youtube_review" if hasattr(sys.modules[__name__], "_inline_youtube_review") else None},
        "display": {"import_path": "blobs.display", "interfaces": [], "inline_f": "_inline_display" if hasattr(sys.modules[__name__], "_inline_display") else None},
        "send_email": {"import_path": "blobs.send_email", "interfaces": [], "inline_f": "_inline_send_email" if hasattr(sys.modules[__name__], "_inline_send_email") else None},
        "classify_input": {"import_path": "blobs.classify_input", "interfaces": [], "inline_f": "_inline_classify_input" if hasattr(sys.modules[__name__], "_inline_classify_input") else None},
        "discover_database": {"import_path": "blobs.discover_database", "interfaces": [], "inline_f": "_inline_discover_database" if hasattr(sys.modules[__name__], "_inline_discover_database") else None},
        "create_plan": {"import_path": "blobs.create_plan", "interfaces": [], "inline_f": "_inline_create_plan" if hasattr(sys.modules[__name__], "_inline_create_plan") else None},
        "execute_plan": {"import_path": "blobs.execute_plan", "interfaces": [], "inline_f": "_inline_execute_plan" if hasattr(sys.modules[__name__], "_inline_execute_plan") else None},
        "generate_response": {"import_path": "blobs.generate_response", "interfaces": [], "inline_f": "_inline_generate_response" if hasattr(sys.modules[__name__], "_inline_generate_response") else None},
        "generate_newsapi_params": {"import_path": "blobs.generate_newsapi_params", "interfaces": [], "inline_f": "_inline_generate_newsapi_params" if hasattr(sys.modules[__name__], "_inline_generate_newsapi_params") else None},
        "retrieve_articles_metadata": {"import_path": "blobs.retrieve_articles_metadata", "interfaces": [], "inline_f": "_inline_retrieve_articles_metadata" if hasattr(sys.modules[__name__], "_inline_retrieve_articles_metadata") else None},
        "retrieve_articles_text": {"import_path": "blobs.retrieve_articles_text", "interfaces": [], "inline_f": "_inline_retrieve_articles_text" if hasattr(sys.modules[__name__], "_inline_retrieve_articles_text") else None},
        "select_top_urls": {"import_path": "blobs.select_top_urls", "interfaces": [], "inline_f": "_inline_select_top_urls" if hasattr(sys.modules[__name__], "_inline_select_top_urls") else None},
        "summarize_articles_parallel": {"import_path": "blobs.summarize_articles_parallel", "interfaces": [], "inline_f": "_inline_summarize_articles_parallel" if hasattr(sys.modules[__name__], "_inline_summarize_articles_parallel") else None},
        "format_results": {"import_path": "blobs.format_results", "interfaces": [], "inline_f": "_inline_format_results" if hasattr(sys.modules[__name__], "_inline_format_results") else None},
        "decision_making": {"import_path": "blobs.decision_making", "interfaces": [], "inline_f": "_inline_decision_making" if hasattr(sys.modules[__name__], "_inline_decision_making") else None},
        "planning": {"import_path": "blobs.planning", "interfaces": [], "inline_f": "_inline_planning" if hasattr(sys.modules[__name__], "_inline_planning") else None},
        "tools": {"import_path": "blobs.tools", "interfaces": [], "inline_f": "_inline_tools" if hasattr(sys.modules[__name__], "_inline_tools") else None},
        "agent": {"import_path": "blobs.agent", "interfaces": [], "inline_f": "_inline_agent" if hasattr(sys.modules[__name__], "_inline_agent") else None},
        "judge": {"import_path": "blobs.judge", "interfaces": [], "inline_f": "_inline_judge" if hasattr(sys.modules[__name__], "_inline_judge") else None},
        "CATEGORY": {"import_path": "blobs.CATEGORY", "interfaces": [], "inline_f": "_inline_CATEGORY" if hasattr(sys.modules[__name__], "_inline_CATEGORY") else None},
        "SUMMARY": {"import_path": "blobs.SUMMARY", "interfaces": [], "inline_f": "_inline_SUMMARY" if hasattr(sys.modules[__name__], "_inline_SUMMARY") else None},
        "FACT_CHECKING": {"import_path": "blobs.FACT_CHECKING", "interfaces": [], "inline_f": "_inline_FACT_CHECKING" if hasattr(sys.modules[__name__], "_inline_FACT_CHECKING") else None},
        "TONE_ANALYSIS": {"import_path": "blobs.TONE_ANALYSIS", "interfaces": [], "inline_f": "_inline_TONE_ANALYSIS" if hasattr(sys.modules[__name__], "_inline_TONE_ANALYSIS") else None},
        "QUOTE_EXTRACTION": {"import_path": "blobs.QUOTE_EXTRACTION", "interfaces": [], "inline_f": "_inline_QUOTE_EXTRACTION" if hasattr(sys.modules[__name__], "_inline_QUOTE_EXTRACTION") else None},
        "GRAMMAR_AND_BIAS_REVIEW": {"import_path": "blobs.GRAMMAR_AND_BIAS_REVIEW", "interfaces": [], "inline_f": "_inline_GRAMMAR_AND_BIAS_REVIEW" if hasattr(sys.modules[__name__], "_inline_GRAMMAR_AND_BIAS_REVIEW") else None},
        "web_download": {"import_path": "blobs.web_download", "interfaces": [], "inline_f": "_inline_web_download" if hasattr(sys.modules[__name__], "_inline_web_download") else None},
        "embeddings_ner": {"import_path": "blobs.embeddings_ner", "interfaces": [], "inline_f": "_inline_embeddings_ner" if hasattr(sys.modules[__name__], "_inline_embeddings_ner") else None},
        "main_assistant": {"import_path": "blobs.main_assistant", "interfaces": [], "inline_f": "_inline_main_assistant" if hasattr(sys.modules[__name__], "_inline_main_assistant") else None},
        "main_assistant_tools": {"import_path": "blobs.main_assistant_tools", "interfaces": [], "inline_f": "_inline_main_assistant_tools" if hasattr(sys.modules[__name__], "_inline_main_assistant_tools") else None},
        "underwriting_assistant": {"import_path": "blobs.underwriting_assistant", "interfaces": [], "inline_f": "_inline_underwriting_assistant" if hasattr(sys.modules[__name__], "_inline_underwriting_assistant") else None},
        "quote_assistant": {"import_path": "blobs.quote_assistant", "interfaces": [], "inline_f": "_inline_quote_assistant" if hasattr(sys.modules[__name__], "_inline_quote_assistant") else None},
        "quote_assistant_tools": {"import_path": "blobs.quote_assistant_tools", "interfaces": [], "inline_f": "_inline_quote_assistant_tools" if hasattr(sys.modules[__name__], "_inline_quote_assistant_tools") else None},
        "entry_quote_assistant": {"import_path": "blobs.entry_quote_assistant", "interfaces": [], "inline_f": "_inline_entry_quote_assistant" if hasattr(sys.modules[__name__], "_inline_entry_quote_assistant") else None},
        "retrieve": {"import_path": "blobs.retrieve", "interfaces": [], "inline_f": "_inline_retrieve" if hasattr(sys.modules[__name__], "_inline_retrieve") else None},
        "reasoning": {"import_path": "blobs.reasoning", "interfaces": [], "inline_f": "_inline_reasoning" if hasattr(sys.modules[__name__], "_inline_reasoning") else None},
        "classification_grading": {"import_path": "blobs.classification_grading", "interfaces": [], "inline_f": "_inline_classification_grading" if hasattr(sys.modules[__name__], "_inline_classification_grading") else None},
        "update_state": {"import_path": "blobs.update_state", "interfaces": [], "inline_f": "_inline_update_state" if hasattr(sys.modules[__name__], "_inline_update_state") else None},
        "reroute": {"import_path": "blobs.reroute", "interfaces": [], "inline_f": "_inline_reroute" if hasattr(sys.modules[__name__], "_inline_reroute") else None},
        "pass_tool_call_id": {"import_path": "blobs.pass_tool_call_id", "interfaces": [], "inline_f": "_inline_pass_tool_call_id" if hasattr(sys.modules[__name__], "_inline_pass_tool_call_id") else None},
        "pass_final_classifications": {"import_path": "blobs.pass_final_classifications", "interfaces": [], "inline_f": "_inline_pass_final_classifications" if hasattr(sys.modules[__name__], "_inline_pass_final_classifications") else None},
        "create_tool_message": {"import_path": "blobs.create_tool_message", "interfaces": [], "inline_f": "_inline_create_tool_message" if hasattr(sys.modules[__name__], "_inline_create_tool_message") else None},
        "update_workflow_state": {"import_path": "blobs.update_workflow_state", "interfaces": [], "inline_f": "_inline_update_workflow_state" if hasattr(sys.modules[__name__], "_inline_update_workflow_state") else None},
        "ask_user_needs": {"import_path": "blobs.ask_user_needs", "interfaces": [], "inline_f": "_inline_ask_user_needs" if hasattr(sys.modules[__name__], "_inline_ask_user_needs") else None},
        "build_filters": {"import_path": "blobs.build_filters", "interfaces": [], "inline_f": "_inline_build_filters" if hasattr(sys.modules[__name__], "_inline_build_filters") else None},
        "search_listings": {"import_path": "blobs.search_listings", "interfaces": [], "inline_f": "_inline_search_listings" if hasattr(sys.modules[__name__], "_inline_search_listings") else None},
        "fetch_additional_info": {"import_path": "blobs.fetch_additional_info", "interfaces": [], "inline_f": "_inline_fetch_additional_info" if hasattr(sys.modules[__name__], "_inline_fetch_additional_info") else None},
        "irrelevant": {"import_path": "blobs.irrelevant", "interfaces": [], "inline_f": "_inline_irrelevant" if hasattr(sys.modules[__name__], "_inline_irrelevant") else None},
        "classify_contract": {"import_path": "blobs.classify_contract", "interfaces": [], "inline_f": "_inline_classify_contract" if hasattr(sys.modules[__name__], "_inline_classify_contract") else None},
        "retrieve_clauses": {"import_path": "blobs.retrieve_clauses", "interfaces": [], "inline_f": "_inline_retrieve_clauses" if hasattr(sys.modules[__name__], "_inline_retrieve_clauses") else None},
        "execute_step_clause": {"import_path": "blobs.execute_step_clause", "interfaces": [], "inline_f": "_inline_execute_step_clause" if hasattr(sys.modules[__name__], "_inline_execute_step_clause") else None},
        "create_review_plan": {"import_path": "blobs.create_review_plan", "interfaces": [], "inline_f": "_inline_create_review_plan" if hasattr(sys.modules[__name__], "_inline_create_review_plan") else None},
        "execute_step": {"import_path": "blobs.execute_step", "interfaces": [], "inline_f": "_inline_execute_step" if hasattr(sys.modules[__name__], "_inline_execute_step") else None},
        "generate_final_report": {"import_path": "blobs.generate_final_report", "interfaces": [], "inline_f": "_inline_generate_final_report" if hasattr(sys.modules[__name__], "_inline_generate_final_report") else None},
        "search": {"import_path": "blobs.search", "interfaces": [], "inline_f": "_inline_search" if hasattr(sys.modules[__name__], "_inline_search") else None},
        "summarize": {"import_path": "blobs.summarize", "interfaces": [], "inline_f": "_inline_summarize" if hasattr(sys.modules[__name__], "_inline_summarize") else None},
        "publish": {"import_path": "blobs.publish", "interfaces": [], "inline_f": "_inline_publish" if hasattr(sys.modules[__name__], "_inline_publish") else None},
        "Keywords": {"import_path": "blobs.Keywords", "interfaces": [], "inline_f": "_inline_Keywords" if hasattr(sys.modules[__name__], "_inline_Keywords") else None},
        "Structure": {"import_path": "blobs.Structure", "interfaces": [], "inline_f": "_inline_Structure" if hasattr(sys.modules[__name__], "_inline_Structure") else None},
        "Host question": {"import_path": "blobs.Host question", "interfaces": [], "inline_f": "_inline_Host question" if hasattr(sys.modules[__name__], "_inline_Host question") else None},
        "Web research": {"import_path": "blobs.Web research", "interfaces": [], "inline_f": "_inline_Web research" if hasattr(sys.modules[__name__], "_inline_Web research") else None},
        "Wiki research": {"import_path": "blobs.Wiki research", "interfaces": [], "inline_f": "_inline_Wiki research" if hasattr(sys.modules[__name__], "_inline_Wiki research") else None},
        "Expert answer": {"import_path": "blobs.Expert answer", "interfaces": [], "inline_f": "_inline_Expert answer" if hasattr(sys.modules[__name__], "_inline_Expert answer") else None},
        "Save podcast": {"import_path": "blobs.Save podcast", "interfaces": [], "inline_f": "_inline_Save podcast" if hasattr(sys.modules[__name__], "_inline_Save podcast") else None},
        "Write script": {"import_path": "blobs.Write script", "interfaces": [], "inline_f": "_inline_Write script" if hasattr(sys.modules[__name__], "_inline_Write script") else None},
        "Planing": {"import_path": "blobs.Planing", "interfaces": [], "inline_f": "_inline_Planing" if hasattr(sys.modules[__name__], "_inline_Planing") else None},
        "Start research": {"import_path": "blobs.Start research", "interfaces": [], "inline_f": "_inline_Start research" if hasattr(sys.modules[__name__], "_inline_Start research") else None},
        "Create podcast": {"import_path": "blobs.Create podcast", "interfaces": [], "inline_f": "_inline_Create podcast" if hasattr(sys.modules[__name__], "_inline_Create podcast") else None},
        "Write report": {"import_path": "blobs.Write report", "interfaces": [], "inline_f": "_inline_Write report" if hasattr(sys.modules[__name__], "_inline_Write report") else None},
        "Write introduction": {"import_path": "blobs.Write introduction", "interfaces": [], "inline_f": "_inline_Write introduction" if hasattr(sys.modules[__name__], "_inline_Write introduction") else None},
        "Write conclusion": {"import_path": "blobs.Write conclusion", "interfaces": [], "inline_f": "_inline_Write conclusion" if hasattr(sys.modules[__name__], "_inline_Write conclusion") else None},
        "Finalize podcast": {"import_path": "blobs.Finalize podcast", "interfaces": [], "inline_f": "_inline_Finalize podcast" if hasattr(sys.modules[__name__], "_inline_Finalize podcast") else None},
        "requirements_gathering": {"import_path": "blobs.requirements_gathering", "interfaces": [], "inline_f": "_inline_requirements_gathering" if hasattr(sys.modules[__name__], "_inline_requirements_gathering") else None},
        "generate_job_desc": {"import_path": "blobs.generate_job_desc", "interfaces": [], "inline_f": "_inline_generate_job_desc" if hasattr(sys.modules[__name__], "_inline_generate_job_desc") else None},
        "linkedin_process": {"import_path": "blobs.linkedin_process", "interfaces": [], "inline_f": "_inline_linkedin_process" if hasattr(sys.modules[__name__], "_inline_linkedin_process") else None},
        "analyze_cv": {"import_path": "blobs.analyze_cv", "interfaces": [], "inline_f": "_inline_analyze_cv" if hasattr(sys.modules[__name__], "_inline_analyze_cv") else None},
        "prepare_interview": {"import_path": "blobs.prepare_interview", "interfaces": [], "inline_f": "_inline_prepare_interview" if hasattr(sys.modules[__name__], "_inline_prepare_interview") else None},
        "classification_node": {"import_path": "blobs.classification_node", "interfaces": [], "inline_f": "_inline_classification_node" if hasattr(sys.modules[__name__], "_inline_classification_node") else None},
        "entity_extraction": {"import_path": "blobs.entity_extraction", "interfaces": [], "inline_f": "_inline_entity_extraction" if hasattr(sys.modules[__name__], "_inline_entity_extraction") else None},
        "summarization": {"import_path": "blobs.summarization", "interfaces": [], "inline_f": "_inline_summarization" if hasattr(sys.modules[__name__], "_inline_summarization") else None},
    }

    ROUTING_TABLE = {
        "approach_analysis": {
            "TASK_KNOWLEDGE_RETRIEVAL": "task_knowledge_retrieval",
            "END": "END"
        },
        "task_knowledge_retrieval": {
            "CUSTOMIZED_APPROACH_GENERATION": "customized_approach_generation",
            "END": "END"
        },
        "customized_approach_generation": {
            "END": "END",
            "END": "END"
        },
        "melody_generator": {
            "HARMONY_CREATOR": "harmony_creator",
            "END": "END"
        },
        "harmony_creator": {
            "RHYTHM_ANALYZER": "rhythm_analyzer",
            "END": "END"
        },
        "rhythm_analyzer": {
            "STYLE_ADAPTER": "style_adapter",
            "END": "END"
        },
        "style_adapter": {
            "MIDI_CONVERTER": "midi_converter",
            "END": "END"
        },
        "midi_converter": {
            "END": "END",
            "END": "END"
        },
        "triage": {
            "END": "END"
        },
        "response_agent": {
            "END": "END"
        },
        "triage": {
            "END": "END"
        },
        "response_agent": {
            "END": "END"
        },
        "code_execution_node": {
            "END": "END"
        },
        "code_update_node": {
            "CODE_PATCHING_NODE": "code_patching_node",
            "END": "END"
        },
        "code_patching_node": {
            "CODE_EXECUTION_NODE": "code_execution_node",
            "END": "END"
        },
        "bug_report_node": {
            "MEMORY_SEARCH_NODE": "memory_search_node",
            "END": "END"
        },
        "memory_search_node": {
            "END": "END"
        },
        "memory_filter_node": {
            "END": "END"
        },
        "memory_modification_node": {
            "END": "END"
        },
        "memory_generation_node": {
            "CODE_UPDATE_NODE": "code_update_node",
            "END": "END"
        },
        "input_city": {
            "INPUT_INTERESTS": "input_interests",
            "END": "END"
        },
        "input_interests": {
            "CREATE_ITINERARY": "create_itinerary",
            "END": "END"
        },
        "create_itinerary": {
            "END": "END",
            "END": "END"
        },
        "get_weather": {
            "ANALYZE_DISASTER": "analyze_disaster",
            "SOCIAL_MEDIA_MONITORING": "social_media_monitoring",
            "END": "END"
        },
        "analyze_disaster": {
            "ASSESS_SEVERITY": "assess_severity",
            "ASSESS_SEVERITY": "assess_severity",
            "END": "END"
        },
        "assess_severity": {
            "DATA_LOGGING": "data_logging",
            "DATA_LOGGING": "data_logging",
            "END": "END"
        },
        "data_logging": {
            "END": "END"
        },
        "emergency_response": {
            "SEND_EMAIL_ALERT": "send_email_alert",
            "SEND_EMAIL_ALERT": "send_email_alert",
            "END": "END"
        },
        "civil_defense_response": {
            "GET_HUMAN_VERIFICATION": "get_human_verification",
            "GET_HUMAN_VERIFICATION": "get_human_verification",
            "END": "END"
        },
        "public_works_response": {
            "GET_HUMAN_VERIFICATION": "get_human_verification",
            "GET_HUMAN_VERIFICATION": "get_human_verification",
            "END": "END"
        },
        "get_human_verification": {
            "END": "END"
        },
        "send_email_alert": {
            "END": "END",
            "END": "END",
            "END": "END"
        },
        "handle_no_approval": {
            "END": "END",
            "END": "END",
            "END": "END"
        },
        "get_weather": {
            "ANALYZE_DISASTER": "analyze_disaster",
            "SOCIAL_MEDIA_MONITORING": "social_media_monitoring",
            "END": "END"
        },
        "social_media_monitoring": {
            "ANALYZE_DISASTER": "analyze_disaster",
            "END": "END"
        },
        "analyze_disaster": {
            "ASSESS_SEVERITY": "assess_severity",
            "ASSESS_SEVERITY": "assess_severity",
            "END": "END"
        },
        "assess_severity": {
            "DATA_LOGGING": "data_logging",
            "DATA_LOGGING": "data_logging",
            "END": "END"
        },
        "data_logging": {
            "END": "END"
        },
        "emergency_response": {
            "SEND_EMAIL_ALERT": "send_email_alert",
            "SEND_EMAIL_ALERT": "send_email_alert",
            "END": "END"
        },
        "civil_defense_response": {
            "GET_HUMAN_VERIFICATION": "get_human_verification",
            "GET_HUMAN_VERIFICATION": "get_human_verification",
            "END": "END"
        },
        "public_works_response": {
            "GET_HUMAN_VERIFICATION": "get_human_verification",
            "GET_HUMAN_VERIFICATION": "get_human_verification",
            "END": "END"
        },
        "get_human_verification": {
            "END": "END"
        },
        "send_email_alert": {
            "END": "END",
            "END": "END",
            "END": "END"
        },
        "handle_no_approval": {
            "END": "END",
            "END": "END",
            "END": "END"
        },
        "assistant": {
            "END": "END"
        },
        "tools": {
            "ASSISTANT": "assistant",
            "ASSISTANT": "assistant",
            "AGENT": "agent",
            "END": "END"
        },
        "generate_new_inputs": {
            "END": "END"
        },
        "static_test": {
            "GENERATE_NODE_DESCRIPTIONS": "generate_node_descriptions",
            "END": "END"
        },
        "generate_node_descriptions": {
            "GENERATE_TESTERS": "generate_testers",
            "END": "END"
        },
        "generate_testers": {
            "GENERATE_TEST_CASES": "generate_test_cases",
            "END": "END"
        },
        "generate_test_cases": {
            "END": "END"
        },
        "run_test_cases": {
            "ANALIZE_RESULTS": "analize_results",
            "END": "END"
        },
        "analize_results": {
            "END": "END"
        },
        "assistant": {
            "END": "END"
        },
        "tools": {
            "ASSISTANT": "assistant",
            "ASSISTANT": "assistant",
            "AGENT": "agent",
            "END": "END"
        },
        "process_input": {
            "PLANNER": "planner",
            "END": "END"
        },
        "planner": {
            "RESEARCHER": "researcher",
            "END": "END"
        },
        "researcher": {
            "SEARCH_ARTICLES": "search_articles",
            "END": "END"
        },
        "search_articles": {
            "ARTICLE_DECISIONS": "article_decisions",
            "END": "END"
        },
        "article_decisions": {
            "DOWNLOAD_ARTICLES": "download_articles",
            "END": "END"
        },
        "download_articles": {
            "PAPER_ANALYZER": "paper_analyzer",
            "END": "END"
        },
        "paper_analyzer": {
            "WRITE_ABSTRACT": "write_abstract",
            "WRITE_INTRODUCTION": "write_introduction",
            "WRITE_METHODS": "write_methods",
            "WRITE_RESULTS": "write_results",
            "WRITE_CONCLUSION": "write_conclusion",
            "WRITE_REFERENCES": "write_references",
            "END": "END"
        },
        "write_abstract": {
            "AGGREGATE_PAPER": "aggregate_paper",
            "END": "END"
        },
        "write_introduction": {
            "AGGREGATE_PAPER": "aggregate_paper",
            "END": "END"
        },
        "write_methods": {
            "AGGREGATE_PAPER": "aggregate_paper",
            "END": "END"
        },
        "write_results": {
            "AGGREGATE_PAPER": "aggregate_paper",
            "END": "END"
        },
        "write_conclusion": {
            "AGGREGATE_PAPER": "aggregate_paper",
            "END": "END"
        },
        "write_references": {
            "AGGREGATE_PAPER": "aggregate_paper",
            "END": "END"
        },
        "aggregate_paper": {
            "CRITIQUE_PAPER": "critique_paper",
            "END": "END"
        },
        "critique_paper": {
            "END": "END"
        },
        "revise_paper": {
            "CRITIQUE_PAPER": "critique_paper",
            "END": "END"
        },
        "final_draft": {
            "END": "END",
            "END": "END"
        },
        "task_generation": {
            "TASK_DEPENDENCIES": "task_dependencies",
            "END": "END"
        },
        "task_dependencies": {
            "TASK_SCHEDULER": "task_scheduler",
            "END": "END"
        },
        "task_scheduler": {
            "TASK_ALLOCATOR": "task_allocator",
            "END": "END"
        },
        "task_allocator": {
            "RISK_ASSESSOR": "risk_assessor",
            "END": "END"
        },
        "risk_assessor": {
            "END": "END"
        },
        "insight_generator": {
            "TASK_SCHEDULER": "task_scheduler",
            "END": "END"
        },
        "create_project_plan": {
            "END": "END",
            "END": "END"
        },
        "requirements_gathering": {
            "GENERATE_JOB_DESC": "generate_job_desc",
            "GENERATE_JOB_DESC": "generate_job_desc",
            "END": "END"
        },
        "generate_job_desc": {
            "END": "END"
        },
        "linkedin_process": {
            "ANALYZE_CV": "analyze_cv",
            "ANALYZE_CV": "analyze_cv",
            "END": "END"
        },
        "analyze_cv": {
            "END": "END"
        },
        "prepare_interview": {
            "END": "END",
            "END": "END",
            "END": "END"
        },
        "check_relevance": {
            "END": "END"
        },
        "check_grammar": {
            "END": "END"
        },
        "analyze_structure": {
            "END": "END"
        },
        "evaluate_depth": {
            "END": "END"
        },
        "calculate_final_score": {
            "END": "END",
            "END": "END"
        },
        "generate_query": {
            "SEARCH_WEB": "search_web",
            "END": "END"
        },
        "search_web": {
            "GENERATE_QUESTION": "generate_question",
            "END": "END"
        },
        "chunk_context": {
            "CONTEXT_VALIDATION": "context_validation",
            "END": "END"
        },
        "context_validation": {
            "END": "END"
        },
        "generate_checkpoints": {
            "END": "END"
        },
        "generate_question": {
            "USER_ANSWER": "user_answer",
            "END": "END"
        },
        "next_checkpoint": {
            "GENERATE_QUESTION": "generate_question",
            "END": "END"
        },
        "user_answer": {
            "VERIFY_ANSWER": "verify_answer",
            "END": "END"
        },
        "verify_answer": {
            "END": "END"
        },
        "teach_concept": {
            "END": "END"
        },
        "tour_introduction": {
            "DISPLAY_ARTWORK": "display_artwork",
            "END": "END"
        },
        "display_artwork": {
            "DISCUSS": "discuss",
            "END": "END"
        },
        "get_next_artwork": {
            "DISPLAY_ARTWORK": "display_artwork",
            "END": "END"
        },
        "discuss": {
            "END": "END"
        },
        "conclude_tour": {
            "END": "END",
            "END": "END"
        },
        "character_introduction": {
            "ASK_QUESTION": "ask_question",
            "END": "END"
        },
        "ask_question": {
            "HUMAN_DISCUSS": "human_discuss",
            "END": "END"
        },
        "answer_question": {
            "ASK_QUESTION": "ask_question",
            "END": "END"
        },
        "create_characters": {
            "CREATE_STORY": "create_story",
            "END": "END"
        },
        "create_story": {
            "NARRARTOR": "narrartor",
            "END": "END"
        },
        "narrartor": {
            "SHERLOCK": "sherlock",
            "END": "END"
        },
        "sherlock": {
            "END": "END"
        },
        "guesser": {
            "END": "END"
        },
        "conversation": {
            "SHERLOCK": "sherlock",
            "END": "END"
        },
        "summary_node": {
            "RESEARCH_NODE": "research_node",
            "END": "END"
        },
        "research_node": {
            "INTENT_MATCHING_NODE": "intent_matching_node",
            "END": "END"
        },
        "intent_matching_node": {
            "INSTAGRAM": "instagram",
            "TWITTER": "twitter",
            "LINKEDIN": "linkedin",
            "BLOG": "blog",
            "END": "END"
        },
        "instagram": {
            "COMBINE_CONTENT": "combine_content",
            "END": "END"
        },
        "twitter": {
            "COMBINE_CONTENT": "combine_content",
            "END": "END"
        },
        "linkedin": {
            "COMBINE_CONTENT": "combine_content",
            "END": "END"
        },
        "blog": {
            "COMBINE_CONTENT": "combine_content",
            "END": "END"
        },
        "combine_content": {
            "END": "END",
            "END": "END"
        },
        "generate_character_description": {
            "GENERATE_PLOT": "generate_plot",
            "END": "END"
        },
        "generate_plot": {
            "GENERATE_IMAGE_PROMPTS": "generate_image_prompts",
            "END": "END"
        },
        "generate_image_prompts": {
            "CREATE_IMAGES": "create_images",
            "END": "END"
        },
        "create_images": {
            "CREATE_GIF": "create_gif",
            "END": "END"
        },
        "create_gif": {
            "END": "END",
            "END": "END"
        },
        "classify_content": {
            "END": "END"
        },
        "process_general": {
            "TEXT_TO_SPEECH": "text_to_speech",
            "END": "END"
        },
        "process_poem": {
            "TEXT_TO_SPEECH": "text_to_speech",
            "END": "END"
        },
        "process_news": {
            "TEXT_TO_SPEECH": "text_to_speech",
            "END": "END"
        },
        "process_joke": {
            "TEXT_TO_SPEECH": "text_to_speech",
            "END": "END"
        },
        "text_to_speech": {
            "END": "END"
        },
        "categorize": {
            "ANALYZE_SENTIMENT": "analyze_sentiment",
            "END": "END"
        },
        "handle_learning_resource": {
            "END": "END"
        },
        "handle_resume_making": {
            "END": "END",
            "END": "END"
        },
        "handle_interview_preparation": {
            "END": "END"
        },
        "job_search": {
            "END": "END",
            "END": "END"
        },
        "mock_interview": {
            "END": "END",
            "END": "END"
        },
        "interview_topics_questions": {
            "END": "END",
            "END": "END"
        },
        "tutorial_agent": {
            "END": "END",
            "END": "END"
        },
        "ask_query_bot": {
            "END": "END",
            "END": "END"
        },
        "calendar_analyzer": {
            "TASK_ANALYZER": "task_analyzer",
            "TASK_ANALYZER": "task_analyzer",
            "END": "END"
        },
        "task_analyzer": {
            "PLAN_GENERATOR": "plan_generator",
            "PLAN_GENERATOR": "plan_generator",
            "END": "END"
        },
        "plan_generator": {
            "EXECUTE": "execute",
            "END": "END"
        },
        "notewriter_analyze": {
            "NOTEWRITER_GENERATE": "notewriter_generate",
            "NOTEWRITER_GENERATE": "notewriter_generate",
            "END": "END"
        },
        "notewriter_generate": {
            "END": "END",
            "EXECUTE": "execute",
            "END": "END"
        },
        "advisor_analyze": {
            "ADVISOR_GENERATE": "advisor_generate",
            "ADVISOR_GENERATE": "advisor_generate",
            "END": "END"
        },
        "advisor_generate": {
            "END": "END",
            "EXECUTE": "execute",
            "END": "END"
        },
        "coordinator": {
            "PROFILE_ANALYZER": "profile_analyzer",
            "END": "END"
        },
        "profile_analyzer": {
            "END": "END"
        },
        "execute": {
            "END": "END"
        },
        "calendar_analyzer": {
            "TASK_ANALYZER": "task_analyzer",
            "TASK_ANALYZER": "task_analyzer",
            "END": "END"
        },
        "task_analyzer": {
            "PLAN_GENERATOR": "plan_generator",
            "PLAN_GENERATOR": "plan_generator",
            "END": "END"
        },
        "plan_generator": {
            "EXECUTE": "execute",
            "END": "END"
        },
        "notewriter_analyze": {
            "NOTEWRITER_GENERATE": "notewriter_generate",
            "NOTEWRITER_GENERATE": "notewriter_generate",
            "END": "END"
        },
        "notewriter_generate": {
            "END": "END",
            "EXECUTE": "execute",
            "END": "END"
        },
        "advisor_analyze": {
            "ADVISOR_GENERATE": "advisor_generate",
            "ADVISOR_GENERATE": "advisor_generate",
            "END": "END"
        },
        "advisor_generate": {
            "END": "END",
            "EXECUTE": "execute",
            "END": "END"
        },
        "convert_user_instruction_to_actions": {
            "GET_INITIAL_ACTION": "get_initial_action",
            "END": "END"
        },
        "get_initial_action": {
            "GET_WEBSITE_STATE": "get_website_state",
            "END": "END"
        },
        "get_website_state": {
            "GENERATE_CODE_FOR_ACTION": "generate_code_for_action",
            "END": "END"
        },
        "generate_code_for_action": {
            "VALIDATE_GENERATED_ACTION": "validate_generated_action",
            "END": "END"
        },
        "validate_generated_action": {
            "END": "END"
        },
        "handle_generation_error": {
            "END": "END",
            "END": "END"
        },
        "post_process_script": {
            "EXECUTE_TEST_CASE": "execute_test_case",
            "END": "END"
        },
        "execute_test_case": {
            "GENERATE_TEST_REPORT": "generate_test_report",
            "END": "END"
        },
        "generate_test_report": {
            "END": "END",
            "END": "END"
        },
        "categorize": {
            "ANALYZE_SENTIMENT": "analyze_sentiment",
            "END": "END"
        },
        "analyze_sentiment": {
            "END": "END"
        },
        "handle_technical": {
            "END": "END",
            "END": "END"
        },
        "handle_billing": {
            "END": "END",
            "END": "END"
        },
        "handle_general": {
            "END": "END",
            "END": "END"
        },
        "escalate": {
            "END": "END",
            "END": "END"
        },
        "get_website_content": {
            "ANALYZE_COMPANY": "analyze_company",
            "END": "END"
        },
        "analyze_company": {
            "GENERATE_CONCEPTS": "generate_concepts",
            "END": "END"
        },
        "generate_concepts": {
            "SELECT_TEMPLATES": "select_templates",
            "END": "END"
        },
        "select_templates": {
            "GENERATE_TEXT": "generate_text",
            "END": "END"
        },
        "generate_text": {
            "CREATE_URL": "create_url",
            "END": "END"
        },
        "create_url": {
            "END": "END",
            "END": "END"
        },
        "tavily_search": {
            "SCHEMA_MAPPING": "schema_mapping",
            "END": "END"
        },
        "schema_mapping": {
            "PRODUCT_COMPARISON": "product_comparison",
            "END": "END"
        },
        "product_comparison": {
            "YOUTUBE_REVIEW": "youtube_review",
            "END": "END"
        },
        "youtube_review": {
            "DISPLAY": "display",
            "SEND_EMAIL": "send_email",
            "END": "END"
        },
        "display": {
            "END": "END",
            "END": "END"
        },
        "send_email": {
            "END": "END",
            "END": "END"
        },
        "classify_input": {
            "END": "END"
        },
        "discover_database": {
            "CREATE_PLAN": "create_plan",
            "END": "END"
        },
        "create_plan": {
            "END": "END"
        },
        "execute_plan": {
            "GENERATE_RESPONSE": "generate_response",
            "END": "END"
        },
        "generate_response": {
            "END": "END",
            "END": "END"
        },
        "generate_newsapi_params": {
            "RETRIEVE_ARTICLES_METADATA": "retrieve_articles_metadata",
            "END": "END"
        },
        "retrieve_articles_metadata": {
            "RETRIEVE_ARTICLES_TEXT": "retrieve_articles_text",
            "END": "END"
        },
        "retrieve_articles_text": {
            "END": "END"
        },
        "select_top_urls": {
            "SUMMARIZE_ARTICLES_PARALLEL": "summarize_articles_parallel",
            "END": "END"
        },
        "summarize_articles_parallel": {
            "END": "END"
        },
        "format_results": {
            "END": "END",
            "END": "END"
        },
        "decision_making": {
            "END": "END"
        },
        "planning": {
            "AGENT": "agent",
            "END": "END"
        },
        "tools": {
            "ASSISTANT": "assistant",
            "ASSISTANT": "assistant",
            "AGENT": "agent",
            "END": "END"
        },
        "agent": {
            "END": "END"
        },
        "judge": {
            "END": "END"
        },
        "CATEGORY": {
            "END": "END"
        },
        "SUMMARY": {
            "END": "END",
            "END": "END"
        },
        "FACT_CHECKING": {
            "END": "END",
            "END": "END"
        },
        "TONE_ANALYSIS": {
            "END": "END",
            "END": "END"
        },
        "QUOTE_EXTRACTION": {
            "END": "END",
            "END": "END"
        },
        "GRAMMAR_AND_BIAS_REVIEW": {
            "END": "END",
            "END": "END"
        },
        "web_download": {
            "END": "END"
        },
        "embeddings_ner": {
            "PREPARE_TOPIC": "prepare_topic",
            "END": "END"
        },
        "main_assistant": {
            "END": "END"
        },
        "main_assistant_tools": {
            "UPDATE_STATE": "update_state",
            "END": "END"
        },
        "underwriting_assistant": {
            "END": "END"
        },
        "quote_assistant": {
            "END": "END"
        },
        "quote_assistant_tools": {
            "QUOTE_ASSISTANT": "quote_assistant",
            "END": "END"
        },
        "entry_quote_assistant": {
            "QUOTE_ASSISTANT": "quote_assistant",
            "END": "END"
        },
        "retrieve": {
            "REASONING": "reasoning",
            "END": "END"
        },
        "reasoning": {
            "CLASSIFICATION_GRADING": "classification_grading",
            "END": "END"
        },
        "classification_grading": {
            "PASS_FINAL_CLASSIFICATIONS": "pass_final_classifications",
            "END": "END"
        },
        "update_state": {
            "MAIN_ASSISTANT": "main_assistant",
            "END": "END"
        },
        "reroute": {
            "MAIN_ASSISTANT": "main_assistant",
            "END": "END"
        },
        "pass_tool_call_id": {
            "RETRIEVE": "retrieve",
            "END": "END"
        },
        "pass_final_classifications": {
            "CREATE_TOOL_MESSAGE": "create_tool_message",
            "END": "END"
        },
        "create_tool_message": {
            "UNDERWRITING_ASSISTANT": "underwriting_assistant",
            "END": "END"
        },
        "update_workflow_state": {
            "ENTRY_QUOTE_ASSISTANT": "entry_quote_assistant",
            "END": "END"
        },
        "ask_user_needs": {
            "END": "END"
        },
        "build_filters": {
            "SEARCH_LISTINGS": "search_listings",
            "END": "END"
        },
        "search_listings": {
            "END": "END"
        },
        "fetch_additional_info": {
            "END": "END"
        },
        "irrelevant": {
            "END": "END",
            "END": "END"
        },
        "classify_contract": {
            "RETRIEVE_CLAUSES": "retrieve_clauses",
            "END": "END"
        },
        "retrieve_clauses": {
            "END": "END"
        },
        "execute_step_clause": {
            "CREATE_REVIEW_PLAN": "create_review_plan",
            "END": "END"
        },
        "create_review_plan": {
            "END": "END"
        },
        "execute_step": {
            "GENERATE_FINAL_REPORT": "generate_final_report",
            "END": "END"
        },
        "generate_final_report": {
            "END": "END",
            "END": "END"
        },
        "search": {
            "SUMMARIZE": "summarize",
            "END": "END"
        },
        "summarize": {
            "PUBLISH": "publish",
            "END": "END"
        },
        "publish": {
            "END": "END"
        },
        "Keywords": {
            "STRUCTURE": "Structure",
            "END": "END"
        },
        "Structure": {
            "END": "END",
            "END": "END"
        },
        "Host question": {
            "WEB RESEARCH": "Web research",
            "WIKI RESEARCH": "Wiki research",
            "END": "END"
        },
        "Web research": {
            "EXPERT ANSWER": "Expert answer",
            "END": "END"
        },
        "Wiki research": {
            "EXPERT ANSWER": "Expert answer",
            "END": "END"
        },
        "Expert answer": {
            "END": "END"
        },
        "Save podcast": {
            "WRITE SCRIPT": "Write script",
            "END": "END"
        },
        "Write script": {
            "END": "END",
            "END": "END"
        },
        "Planing": {
            "START RESEARCH": "Start research",
            "END": "END"
        },
        "Start research": {
            "END": "END"
        },
        "Create podcast": {
            "WRITE REPORT": "Write report",
            "WRITE INTRODUCTION": "Write introduction",
            "WRITE CONCLUSION": "Write conclusion",
            "END": "END"
        },
        "Write report": {
            "END": "END"
        },
        "Write introduction": {
            "END": "END"
        },
        "Write conclusion": {
            "END": "END"
        },
        "Finalize podcast": {
            "END": "END",
            "END": "END"
        },
        "requirements_gathering": {
            "GENERATE_JOB_DESC": "generate_job_desc",
            "GENERATE_JOB_DESC": "generate_job_desc",
            "END": "END"
        },
        "generate_job_desc": {
            "END": "END"
        },
        "linkedin_process": {
            "ANALYZE_CV": "analyze_cv",
            "ANALYZE_CV": "analyze_cv",
            "END": "END"
        },
        "analyze_cv": {
            "END": "END"
        },
        "prepare_interview": {
            "END": "END",
            "END": "END",
            "END": "END"
        },
        "classification_node": {
            "ENTITY_EXTRACTION": "entity_extraction",
            "END": "END"
        },
        "entity_extraction": {
            "SUMMARIZATION": "summarization",
            "END": "END"
        },
        "summarization": {
            "END": "END",
            "END": "END"
        },
    }

    current_node = "requirements_gathering"
    incoming_action = "INITIAL_ENTRY"
    while current_node and current_node != "END":
        cfg = NODES_CONFIG.get(current_node)
        if not cfg:
            break
        print(f"\n--- 🟢 Entering Runtime Task Node: {current_node} ---")
        print(f"    🔒 [Permissions] Authorized MCP Interfaces: {cfg['interfaces']}")
        
        span_id = f"span-{uuid.uuid4().hex[:8]}"
        contract_status = "VERIFIED"
        start_time = time.perf_counter()
        
        try:
            SharedContextContract(**state["context"])
        except Exception as contract_err:
            print(f"    ⚠️ [Contract Breakage] Incoming schema anomaly caught at entry of {current_node}: {contract_err}")
            contract_status = "FAILED_ENTRY"
        
        try:
            if cfg["inline_f"] and cfg["inline_f"] in globals():
                state = globals()[cfg["inline_f"]](state)
            else:
                module = importlib.import_module(cfg["import_path"])
                state = module.run(state)
            
            if contract_status == "VERIFIED":
                try:
                    SharedContextContract(**state["context"])
                except Exception as contract_err_exit:
                    print(f"    ❌ [Contract Breakage] Outgoing contract violation caught at exit of {current_node}: {contract_err_exit}")
                    contract_status = "FAILED_EXIT"
        except Exception as e:
            print(f"    ❌ Execution/Contract Fault inside {current_node}: {e}")
            contract_status = "CRASHED"
            break
        
        latency = round(time.perf_counter() - start_time, 4)
        action = state.get("next_action", "PROCEED").upper()
        if action.startswith("GOTO_"):
            action = action.replace("GOTO_", "", 1)
        
        # 📊 EMIT UNIFIED SWARMHUB TELEMETRY STRIP LOG
        telemetry_span = {
            "span_id": span_id,
            "thread_id": "test_1",
            "node_id": current_node,
            "latency_seconds": latency,
            "incoming_action": incoming_action,
            "outgoing_action": action,
            "contract_status": contract_status
        }
        print(f"📊 [Telemetry Span Generated]: {json.dumps(telemetry_span)}")
        
        incoming_action = action
        current_node = ROUTING_TABLE.get(current_node, {}).get(action, "END")

    print("\n🏁 Local CrewAI Task Blob Pipeline Successfully Executed!")
    print("Final Verified State Context Payload:", state["context"])