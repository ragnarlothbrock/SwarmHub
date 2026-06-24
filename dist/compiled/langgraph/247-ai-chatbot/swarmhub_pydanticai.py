# ==========================================================================
# GENERATED AUTOMATICALLY BY SWARMHUB FOR AGENT SWARM: 247-ai-chatbot
# TARGET RUNTIME: PydanticAI (Memory Layer: in_memory | Thread: test_1)
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

from pydantic_ai import Agent, RunContext

# 1. Patch Runtime Environment Paths to discover localized Code Blobs
sys.path.insert(0, os.getcwd())

# 2. Initialize Global Runtime Configurations
# Target Model Provider Coordinate: openai:gpt-4o-mini

# 3. Define functional stubs for cross-compiled tools
def ToQuoteAssistant(ctx: RunContext[Any], *args, **kwargs) -> str:
    """Cross-compiled SwarmHub tool capability artifact: ToQuoteAssistant"""
    print("    🧰 [Tool Called] Executing workspace tool stub: ToQuoteAssistant")
    return "Tool execution fallback payload finished."

# 3.2 Initialize Registered Global MCP Capability Interface Targets
GLOBAL_INTERFACES_REGISTRY = {}

# 4. Define strict Data Contract Verification Model schemas
class SharedContextContract(BaseModel):
    pass

# 5. Define Autonomous PydanticAI Agents dynamically from Topology
approach_analysis_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: approach_analysis. Authorized MCP Interfaces: []",
)
approach_analysis_agent.tool_plain(ToQuoteAssistant)

task_knowledge_retrieval_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: task_knowledge_retrieval. Authorized MCP Interfaces: []",
)
task_knowledge_retrieval_agent.tool_plain(ToQuoteAssistant)

customized_approach_generation_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: customized_approach_generation. Authorized MCP Interfaces: []",
)
customized_approach_generation_agent.tool_plain(ToQuoteAssistant)

melody_generator_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: melody_generator. Authorized MCP Interfaces: []",
)
melody_generator_agent.tool_plain(ToQuoteAssistant)

harmony_creator_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: harmony_creator. Authorized MCP Interfaces: []",
)
harmony_creator_agent.tool_plain(ToQuoteAssistant)

rhythm_analyzer_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: rhythm_analyzer. Authorized MCP Interfaces: []",
)
rhythm_analyzer_agent.tool_plain(ToQuoteAssistant)

style_adapter_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: style_adapter. Authorized MCP Interfaces: []",
)
style_adapter_agent.tool_plain(ToQuoteAssistant)

midi_converter_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: midi_converter. Authorized MCP Interfaces: []",
)
midi_converter_agent.tool_plain(ToQuoteAssistant)

triage_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: triage. Authorized MCP Interfaces: []",
)
triage_agent.tool_plain(ToQuoteAssistant)

response_agent_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: response_agent. Authorized MCP Interfaces: []",
)
response_agent_agent.tool_plain(ToQuoteAssistant)

triage_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: triage. Authorized MCP Interfaces: []",
)
triage_agent.tool_plain(ToQuoteAssistant)

response_agent_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: response_agent. Authorized MCP Interfaces: []",
)
response_agent_agent.tool_plain(ToQuoteAssistant)

code_execution_node_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: code_execution_node. Authorized MCP Interfaces: []",
)
code_execution_node_agent.tool_plain(ToQuoteAssistant)

code_update_node_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: code_update_node. Authorized MCP Interfaces: []",
)
code_update_node_agent.tool_plain(ToQuoteAssistant)

code_patching_node_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: code_patching_node. Authorized MCP Interfaces: []",
)
code_patching_node_agent.tool_plain(ToQuoteAssistant)

bug_report_node_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: bug_report_node. Authorized MCP Interfaces: []",
)
bug_report_node_agent.tool_plain(ToQuoteAssistant)

memory_search_node_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: memory_search_node. Authorized MCP Interfaces: []",
)
memory_search_node_agent.tool_plain(ToQuoteAssistant)

memory_filter_node_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: memory_filter_node. Authorized MCP Interfaces: []",
)
memory_filter_node_agent.tool_plain(ToQuoteAssistant)

memory_modification_node_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: memory_modification_node. Authorized MCP Interfaces: []",
)
memory_modification_node_agent.tool_plain(ToQuoteAssistant)

memory_generation_node_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: memory_generation_node. Authorized MCP Interfaces: []",
)
memory_generation_node_agent.tool_plain(ToQuoteAssistant)

input_city_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: input_city. Authorized MCP Interfaces: []",
)
input_city_agent.tool_plain(ToQuoteAssistant)

input_interests_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: input_interests. Authorized MCP Interfaces: []",
)
input_interests_agent.tool_plain(ToQuoteAssistant)

create_itinerary_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: create_itinerary. Authorized MCP Interfaces: []",
)
create_itinerary_agent.tool_plain(ToQuoteAssistant)

get_weather_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: get_weather. Authorized MCP Interfaces: []",
)
get_weather_agent.tool_plain(ToQuoteAssistant)

analyze_disaster_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: analyze_disaster. Authorized MCP Interfaces: []",
)
analyze_disaster_agent.tool_plain(ToQuoteAssistant)

assess_severity_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: assess_severity. Authorized MCP Interfaces: []",
)
assess_severity_agent.tool_plain(ToQuoteAssistant)

data_logging_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: data_logging. Authorized MCP Interfaces: []",
)
data_logging_agent.tool_plain(ToQuoteAssistant)

emergency_response_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: emergency_response. Authorized MCP Interfaces: []",
)
emergency_response_agent.tool_plain(ToQuoteAssistant)

civil_defense_response_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: civil_defense_response. Authorized MCP Interfaces: []",
)
civil_defense_response_agent.tool_plain(ToQuoteAssistant)

public_works_response_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: public_works_response. Authorized MCP Interfaces: []",
)
public_works_response_agent.tool_plain(ToQuoteAssistant)

get_human_verification_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: get_human_verification. Authorized MCP Interfaces: []",
)
get_human_verification_agent.tool_plain(ToQuoteAssistant)

send_email_alert_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: send_email_alert. Authorized MCP Interfaces: []",
)
send_email_alert_agent.tool_plain(ToQuoteAssistant)

handle_no_approval_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: handle_no_approval. Authorized MCP Interfaces: []",
)
handle_no_approval_agent.tool_plain(ToQuoteAssistant)

get_weather_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: get_weather. Authorized MCP Interfaces: []",
)
get_weather_agent.tool_plain(ToQuoteAssistant)

social_media_monitoring_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: social_media_monitoring. Authorized MCP Interfaces: []",
)
social_media_monitoring_agent.tool_plain(ToQuoteAssistant)

analyze_disaster_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: analyze_disaster. Authorized MCP Interfaces: []",
)
analyze_disaster_agent.tool_plain(ToQuoteAssistant)

assess_severity_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: assess_severity. Authorized MCP Interfaces: []",
)
assess_severity_agent.tool_plain(ToQuoteAssistant)

data_logging_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: data_logging. Authorized MCP Interfaces: []",
)
data_logging_agent.tool_plain(ToQuoteAssistant)

emergency_response_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: emergency_response. Authorized MCP Interfaces: []",
)
emergency_response_agent.tool_plain(ToQuoteAssistant)

civil_defense_response_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: civil_defense_response. Authorized MCP Interfaces: []",
)
civil_defense_response_agent.tool_plain(ToQuoteAssistant)

public_works_response_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: public_works_response. Authorized MCP Interfaces: []",
)
public_works_response_agent.tool_plain(ToQuoteAssistant)

get_human_verification_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: get_human_verification. Authorized MCP Interfaces: []",
)
get_human_verification_agent.tool_plain(ToQuoteAssistant)

send_email_alert_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: send_email_alert. Authorized MCP Interfaces: []",
)
send_email_alert_agent.tool_plain(ToQuoteAssistant)

handle_no_approval_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: handle_no_approval. Authorized MCP Interfaces: []",
)
handle_no_approval_agent.tool_plain(ToQuoteAssistant)

assistant_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: assistant. Authorized MCP Interfaces: []",
)
assistant_agent.tool_plain(ToQuoteAssistant)

tools_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: tools. Authorized MCP Interfaces: []",
)
tools_agent.tool_plain(ToQuoteAssistant)

generate_new_inputs_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: generate_new_inputs. Authorized MCP Interfaces: []",
)
generate_new_inputs_agent.tool_plain(ToQuoteAssistant)

static_test_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: static_test. Authorized MCP Interfaces: []",
)
static_test_agent.tool_plain(ToQuoteAssistant)

generate_node_descriptions_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: generate_node_descriptions. Authorized MCP Interfaces: []",
)
generate_node_descriptions_agent.tool_plain(ToQuoteAssistant)

generate_testers_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: generate_testers. Authorized MCP Interfaces: []",
)
generate_testers_agent.tool_plain(ToQuoteAssistant)

generate_test_cases_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: generate_test_cases. Authorized MCP Interfaces: []",
)
generate_test_cases_agent.tool_plain(ToQuoteAssistant)

run_test_cases_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: run_test_cases. Authorized MCP Interfaces: []",
)
run_test_cases_agent.tool_plain(ToQuoteAssistant)

analize_results_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: analize_results. Authorized MCP Interfaces: []",
)
analize_results_agent.tool_plain(ToQuoteAssistant)

assistant_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: assistant. Authorized MCP Interfaces: []",
)
assistant_agent.tool_plain(ToQuoteAssistant)

tools_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: tools. Authorized MCP Interfaces: []",
)
tools_agent.tool_plain(ToQuoteAssistant)

process_input_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: process_input. Authorized MCP Interfaces: []",
)
process_input_agent.tool_plain(ToQuoteAssistant)

planner_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: planner. Authorized MCP Interfaces: []",
)
planner_agent.tool_plain(ToQuoteAssistant)

researcher_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: researcher. Authorized MCP Interfaces: []",
)
researcher_agent.tool_plain(ToQuoteAssistant)

search_articles_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: search_articles. Authorized MCP Interfaces: []",
)
search_articles_agent.tool_plain(ToQuoteAssistant)

article_decisions_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: article_decisions. Authorized MCP Interfaces: []",
)
article_decisions_agent.tool_plain(ToQuoteAssistant)

download_articles_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: download_articles. Authorized MCP Interfaces: []",
)
download_articles_agent.tool_plain(ToQuoteAssistant)

paper_analyzer_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: paper_analyzer. Authorized MCP Interfaces: []",
)
paper_analyzer_agent.tool_plain(ToQuoteAssistant)

write_abstract_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: write_abstract. Authorized MCP Interfaces: []",
)
write_abstract_agent.tool_plain(ToQuoteAssistant)

write_introduction_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: write_introduction. Authorized MCP Interfaces: []",
)
write_introduction_agent.tool_plain(ToQuoteAssistant)

write_methods_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: write_methods. Authorized MCP Interfaces: []",
)
write_methods_agent.tool_plain(ToQuoteAssistant)

write_results_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: write_results. Authorized MCP Interfaces: []",
)
write_results_agent.tool_plain(ToQuoteAssistant)

write_conclusion_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: write_conclusion. Authorized MCP Interfaces: []",
)
write_conclusion_agent.tool_plain(ToQuoteAssistant)

write_references_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: write_references. Authorized MCP Interfaces: []",
)
write_references_agent.tool_plain(ToQuoteAssistant)

aggregate_paper_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: aggregate_paper. Authorized MCP Interfaces: []",
)
aggregate_paper_agent.tool_plain(ToQuoteAssistant)

critique_paper_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: critique_paper. Authorized MCP Interfaces: []",
)
critique_paper_agent.tool_plain(ToQuoteAssistant)

revise_paper_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: revise_paper. Authorized MCP Interfaces: []",
)
revise_paper_agent.tool_plain(ToQuoteAssistant)

final_draft_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: final_draft. Authorized MCP Interfaces: []",
)
final_draft_agent.tool_plain(ToQuoteAssistant)

task_generation_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: task_generation. Authorized MCP Interfaces: []",
)
task_generation_agent.tool_plain(ToQuoteAssistant)

task_dependencies_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: task_dependencies. Authorized MCP Interfaces: []",
)
task_dependencies_agent.tool_plain(ToQuoteAssistant)

task_scheduler_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: task_scheduler. Authorized MCP Interfaces: []",
)
task_scheduler_agent.tool_plain(ToQuoteAssistant)

task_allocator_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: task_allocator. Authorized MCP Interfaces: []",
)
task_allocator_agent.tool_plain(ToQuoteAssistant)

risk_assessor_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: risk_assessor. Authorized MCP Interfaces: []",
)
risk_assessor_agent.tool_plain(ToQuoteAssistant)

insight_generator_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: insight_generator. Authorized MCP Interfaces: []",
)
insight_generator_agent.tool_plain(ToQuoteAssistant)

create_project_plan_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: create_project_plan. Authorized MCP Interfaces: []",
)
create_project_plan_agent.tool_plain(ToQuoteAssistant)

requirements_gathering_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: requirements_gathering. Authorized MCP Interfaces: []",
)
requirements_gathering_agent.tool_plain(ToQuoteAssistant)

generate_job_desc_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: generate_job_desc. Authorized MCP Interfaces: []",
)
generate_job_desc_agent.tool_plain(ToQuoteAssistant)

linkedin_process_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: linkedin_process. Authorized MCP Interfaces: []",
)
linkedin_process_agent.tool_plain(ToQuoteAssistant)

analyze_cv_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: analyze_cv. Authorized MCP Interfaces: []",
)
analyze_cv_agent.tool_plain(ToQuoteAssistant)

prepare_interview_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: prepare_interview. Authorized MCP Interfaces: []",
)
prepare_interview_agent.tool_plain(ToQuoteAssistant)

check_relevance_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: check_relevance. Authorized MCP Interfaces: []",
)
check_relevance_agent.tool_plain(ToQuoteAssistant)

check_grammar_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: check_grammar. Authorized MCP Interfaces: []",
)
check_grammar_agent.tool_plain(ToQuoteAssistant)

analyze_structure_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: analyze_structure. Authorized MCP Interfaces: []",
)
analyze_structure_agent.tool_plain(ToQuoteAssistant)

evaluate_depth_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: evaluate_depth. Authorized MCP Interfaces: []",
)
evaluate_depth_agent.tool_plain(ToQuoteAssistant)

calculate_final_score_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: calculate_final_score. Authorized MCP Interfaces: []",
)
calculate_final_score_agent.tool_plain(ToQuoteAssistant)

generate_query_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: generate_query. Authorized MCP Interfaces: []",
)
generate_query_agent.tool_plain(ToQuoteAssistant)

search_web_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: search_web. Authorized MCP Interfaces: []",
)
search_web_agent.tool_plain(ToQuoteAssistant)

chunk_context_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: chunk_context. Authorized MCP Interfaces: []",
)
chunk_context_agent.tool_plain(ToQuoteAssistant)

context_validation_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: context_validation. Authorized MCP Interfaces: []",
)
context_validation_agent.tool_plain(ToQuoteAssistant)

generate_checkpoints_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: generate_checkpoints. Authorized MCP Interfaces: []",
)
generate_checkpoints_agent.tool_plain(ToQuoteAssistant)

generate_question_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: generate_question. Authorized MCP Interfaces: []",
)
generate_question_agent.tool_plain(ToQuoteAssistant)

next_checkpoint_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: next_checkpoint. Authorized MCP Interfaces: []",
)
next_checkpoint_agent.tool_plain(ToQuoteAssistant)

user_answer_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: user_answer. Authorized MCP Interfaces: []",
)
user_answer_agent.tool_plain(ToQuoteAssistant)

verify_answer_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: verify_answer. Authorized MCP Interfaces: []",
)
verify_answer_agent.tool_plain(ToQuoteAssistant)

teach_concept_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: teach_concept. Authorized MCP Interfaces: []",
)
teach_concept_agent.tool_plain(ToQuoteAssistant)

tour_introduction_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: tour_introduction. Authorized MCP Interfaces: []",
)
tour_introduction_agent.tool_plain(ToQuoteAssistant)

display_artwork_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: display_artwork. Authorized MCP Interfaces: []",
)
display_artwork_agent.tool_plain(ToQuoteAssistant)

get_next_artwork_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: get_next_artwork. Authorized MCP Interfaces: []",
)
get_next_artwork_agent.tool_plain(ToQuoteAssistant)

discuss_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: discuss. Authorized MCP Interfaces: []",
)
discuss_agent.tool_plain(ToQuoteAssistant)

conclude_tour_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: conclude_tour. Authorized MCP Interfaces: []",
)
conclude_tour_agent.tool_plain(ToQuoteAssistant)

character_introduction_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: character_introduction. Authorized MCP Interfaces: []",
)
character_introduction_agent.tool_plain(ToQuoteAssistant)

ask_question_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: ask_question. Authorized MCP Interfaces: []",
)
ask_question_agent.tool_plain(ToQuoteAssistant)

answer_question_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: answer_question. Authorized MCP Interfaces: []",
)
answer_question_agent.tool_plain(ToQuoteAssistant)

create_characters_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: create_characters. Authorized MCP Interfaces: []",
)
create_characters_agent.tool_plain(ToQuoteAssistant)

create_story_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: create_story. Authorized MCP Interfaces: []",
)
create_story_agent.tool_plain(ToQuoteAssistant)

narrartor_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: narrartor. Authorized MCP Interfaces: []",
)
narrartor_agent.tool_plain(ToQuoteAssistant)

sherlock_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: sherlock. Authorized MCP Interfaces: []",
)
sherlock_agent.tool_plain(ToQuoteAssistant)

guesser_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: guesser. Authorized MCP Interfaces: []",
)
guesser_agent.tool_plain(ToQuoteAssistant)

conversation_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: conversation. Authorized MCP Interfaces: []",
)
conversation_agent.tool_plain(ToQuoteAssistant)

summary_node_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: summary_node. Authorized MCP Interfaces: []",
)
summary_node_agent.tool_plain(ToQuoteAssistant)

research_node_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: research_node. Authorized MCP Interfaces: []",
)
research_node_agent.tool_plain(ToQuoteAssistant)

intent_matching_node_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: intent_matching_node. Authorized MCP Interfaces: []",
)
intent_matching_node_agent.tool_plain(ToQuoteAssistant)

instagram_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: instagram. Authorized MCP Interfaces: []",
)
instagram_agent.tool_plain(ToQuoteAssistant)

twitter_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: twitter. Authorized MCP Interfaces: []",
)
twitter_agent.tool_plain(ToQuoteAssistant)

linkedin_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: linkedin. Authorized MCP Interfaces: []",
)
linkedin_agent.tool_plain(ToQuoteAssistant)

blog_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: blog. Authorized MCP Interfaces: []",
)
blog_agent.tool_plain(ToQuoteAssistant)

combine_content_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: combine_content. Authorized MCP Interfaces: []",
)
combine_content_agent.tool_plain(ToQuoteAssistant)

generate_character_description_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: generate_character_description. Authorized MCP Interfaces: []",
)
generate_character_description_agent.tool_plain(ToQuoteAssistant)

generate_plot_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: generate_plot. Authorized MCP Interfaces: []",
)
generate_plot_agent.tool_plain(ToQuoteAssistant)

generate_image_prompts_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: generate_image_prompts. Authorized MCP Interfaces: []",
)
generate_image_prompts_agent.tool_plain(ToQuoteAssistant)

create_images_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: create_images. Authorized MCP Interfaces: []",
)
create_images_agent.tool_plain(ToQuoteAssistant)

create_gif_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: create_gif. Authorized MCP Interfaces: []",
)
create_gif_agent.tool_plain(ToQuoteAssistant)

classify_content_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: classify_content. Authorized MCP Interfaces: []",
)
classify_content_agent.tool_plain(ToQuoteAssistant)

process_general_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: process_general. Authorized MCP Interfaces: []",
)
process_general_agent.tool_plain(ToQuoteAssistant)

process_poem_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: process_poem. Authorized MCP Interfaces: []",
)
process_poem_agent.tool_plain(ToQuoteAssistant)

process_news_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: process_news. Authorized MCP Interfaces: []",
)
process_news_agent.tool_plain(ToQuoteAssistant)

process_joke_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: process_joke. Authorized MCP Interfaces: []",
)
process_joke_agent.tool_plain(ToQuoteAssistant)

text_to_speech_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: text_to_speech. Authorized MCP Interfaces: []",
)
text_to_speech_agent.tool_plain(ToQuoteAssistant)

categorize_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: categorize. Authorized MCP Interfaces: []",
)
categorize_agent.tool_plain(ToQuoteAssistant)

handle_learning_resource_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: handle_learning_resource. Authorized MCP Interfaces: []",
)
handle_learning_resource_agent.tool_plain(ToQuoteAssistant)

handle_resume_making_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: handle_resume_making. Authorized MCP Interfaces: []",
)
handle_resume_making_agent.tool_plain(ToQuoteAssistant)

handle_interview_preparation_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: handle_interview_preparation. Authorized MCP Interfaces: []",
)
handle_interview_preparation_agent.tool_plain(ToQuoteAssistant)

job_search_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: job_search. Authorized MCP Interfaces: []",
)
job_search_agent.tool_plain(ToQuoteAssistant)

mock_interview_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: mock_interview. Authorized MCP Interfaces: []",
)
mock_interview_agent.tool_plain(ToQuoteAssistant)

interview_topics_questions_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: interview_topics_questions. Authorized MCP Interfaces: []",
)
interview_topics_questions_agent.tool_plain(ToQuoteAssistant)

tutorial_agent_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: tutorial_agent. Authorized MCP Interfaces: []",
)
tutorial_agent_agent.tool_plain(ToQuoteAssistant)

ask_query_bot_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: ask_query_bot. Authorized MCP Interfaces: []",
)
ask_query_bot_agent.tool_plain(ToQuoteAssistant)

calendar_analyzer_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: calendar_analyzer. Authorized MCP Interfaces: []",
)
calendar_analyzer_agent.tool_plain(ToQuoteAssistant)

task_analyzer_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: task_analyzer. Authorized MCP Interfaces: []",
)
task_analyzer_agent.tool_plain(ToQuoteAssistant)

plan_generator_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: plan_generator. Authorized MCP Interfaces: []",
)
plan_generator_agent.tool_plain(ToQuoteAssistant)

notewriter_analyze_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: notewriter_analyze. Authorized MCP Interfaces: []",
)
notewriter_analyze_agent.tool_plain(ToQuoteAssistant)

notewriter_generate_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: notewriter_generate. Authorized MCP Interfaces: []",
)
notewriter_generate_agent.tool_plain(ToQuoteAssistant)

advisor_analyze_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: advisor_analyze. Authorized MCP Interfaces: []",
)
advisor_analyze_agent.tool_plain(ToQuoteAssistant)

advisor_generate_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: advisor_generate. Authorized MCP Interfaces: []",
)
advisor_generate_agent.tool_plain(ToQuoteAssistant)

coordinator_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: coordinator. Authorized MCP Interfaces: []",
)
coordinator_agent.tool_plain(ToQuoteAssistant)

profile_analyzer_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: profile_analyzer. Authorized MCP Interfaces: []",
)
profile_analyzer_agent.tool_plain(ToQuoteAssistant)

execute_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: execute. Authorized MCP Interfaces: []",
)
execute_agent.tool_plain(ToQuoteAssistant)

calendar_analyzer_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: calendar_analyzer. Authorized MCP Interfaces: []",
)
calendar_analyzer_agent.tool_plain(ToQuoteAssistant)

task_analyzer_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: task_analyzer. Authorized MCP Interfaces: []",
)
task_analyzer_agent.tool_plain(ToQuoteAssistant)

plan_generator_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: plan_generator. Authorized MCP Interfaces: []",
)
plan_generator_agent.tool_plain(ToQuoteAssistant)

notewriter_analyze_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: notewriter_analyze. Authorized MCP Interfaces: []",
)
notewriter_analyze_agent.tool_plain(ToQuoteAssistant)

notewriter_generate_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: notewriter_generate. Authorized MCP Interfaces: []",
)
notewriter_generate_agent.tool_plain(ToQuoteAssistant)

advisor_analyze_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: advisor_analyze. Authorized MCP Interfaces: []",
)
advisor_analyze_agent.tool_plain(ToQuoteAssistant)

advisor_generate_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: advisor_generate. Authorized MCP Interfaces: []",
)
advisor_generate_agent.tool_plain(ToQuoteAssistant)

convert_user_instruction_to_actions_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: convert_user_instruction_to_actions. Authorized MCP Interfaces: []",
)
convert_user_instruction_to_actions_agent.tool_plain(ToQuoteAssistant)

get_initial_action_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: get_initial_action. Authorized MCP Interfaces: []",
)
get_initial_action_agent.tool_plain(ToQuoteAssistant)

get_website_state_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: get_website_state. Authorized MCP Interfaces: []",
)
get_website_state_agent.tool_plain(ToQuoteAssistant)

generate_code_for_action_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: generate_code_for_action. Authorized MCP Interfaces: []",
)
generate_code_for_action_agent.tool_plain(ToQuoteAssistant)

validate_generated_action_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: validate_generated_action. Authorized MCP Interfaces: []",
)
validate_generated_action_agent.tool_plain(ToQuoteAssistant)

handle_generation_error_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: handle_generation_error. Authorized MCP Interfaces: []",
)
handle_generation_error_agent.tool_plain(ToQuoteAssistant)

post_process_script_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: post_process_script. Authorized MCP Interfaces: []",
)
post_process_script_agent.tool_plain(ToQuoteAssistant)

execute_test_case_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: execute_test_case. Authorized MCP Interfaces: []",
)
execute_test_case_agent.tool_plain(ToQuoteAssistant)

generate_test_report_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: generate_test_report. Authorized MCP Interfaces: []",
)
generate_test_report_agent.tool_plain(ToQuoteAssistant)

categorize_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: categorize. Authorized MCP Interfaces: []",
)
categorize_agent.tool_plain(ToQuoteAssistant)

analyze_sentiment_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: analyze_sentiment. Authorized MCP Interfaces: []",
)
analyze_sentiment_agent.tool_plain(ToQuoteAssistant)

handle_technical_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: handle_technical. Authorized MCP Interfaces: []",
)
handle_technical_agent.tool_plain(ToQuoteAssistant)

handle_billing_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: handle_billing. Authorized MCP Interfaces: []",
)
handle_billing_agent.tool_plain(ToQuoteAssistant)

handle_general_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: handle_general. Authorized MCP Interfaces: []",
)
handle_general_agent.tool_plain(ToQuoteAssistant)

escalate_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: escalate. Authorized MCP Interfaces: []",
)
escalate_agent.tool_plain(ToQuoteAssistant)

get_website_content_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: get_website_content. Authorized MCP Interfaces: []",
)
get_website_content_agent.tool_plain(ToQuoteAssistant)

analyze_company_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: analyze_company. Authorized MCP Interfaces: []",
)
analyze_company_agent.tool_plain(ToQuoteAssistant)

generate_concepts_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: generate_concepts. Authorized MCP Interfaces: []",
)
generate_concepts_agent.tool_plain(ToQuoteAssistant)

select_templates_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: select_templates. Authorized MCP Interfaces: []",
)
select_templates_agent.tool_plain(ToQuoteAssistant)

generate_text_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: generate_text. Authorized MCP Interfaces: []",
)
generate_text_agent.tool_plain(ToQuoteAssistant)

create_url_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: create_url. Authorized MCP Interfaces: []",
)
create_url_agent.tool_plain(ToQuoteAssistant)

tavily_search_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: tavily_search. Authorized MCP Interfaces: []",
)
tavily_search_agent.tool_plain(ToQuoteAssistant)

schema_mapping_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: schema_mapping. Authorized MCP Interfaces: []",
)
schema_mapping_agent.tool_plain(ToQuoteAssistant)

product_comparison_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: product_comparison. Authorized MCP Interfaces: []",
)
product_comparison_agent.tool_plain(ToQuoteAssistant)

youtube_review_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: youtube_review. Authorized MCP Interfaces: []",
)
youtube_review_agent.tool_plain(ToQuoteAssistant)

display_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: display. Authorized MCP Interfaces: []",
)
display_agent.tool_plain(ToQuoteAssistant)

send_email_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: send_email. Authorized MCP Interfaces: []",
)
send_email_agent.tool_plain(ToQuoteAssistant)

classify_input_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: classify_input. Authorized MCP Interfaces: []",
)
classify_input_agent.tool_plain(ToQuoteAssistant)

discover_database_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: discover_database. Authorized MCP Interfaces: []",
)
discover_database_agent.tool_plain(ToQuoteAssistant)

create_plan_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: create_plan. Authorized MCP Interfaces: []",
)
create_plan_agent.tool_plain(ToQuoteAssistant)

execute_plan_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: execute_plan. Authorized MCP Interfaces: []",
)
execute_plan_agent.tool_plain(ToQuoteAssistant)

generate_response_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: generate_response. Authorized MCP Interfaces: []",
)
generate_response_agent.tool_plain(ToQuoteAssistant)

generate_newsapi_params_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: generate_newsapi_params. Authorized MCP Interfaces: []",
)
generate_newsapi_params_agent.tool_plain(ToQuoteAssistant)

retrieve_articles_metadata_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: retrieve_articles_metadata. Authorized MCP Interfaces: []",
)
retrieve_articles_metadata_agent.tool_plain(ToQuoteAssistant)

retrieve_articles_text_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: retrieve_articles_text. Authorized MCP Interfaces: []",
)
retrieve_articles_text_agent.tool_plain(ToQuoteAssistant)

select_top_urls_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: select_top_urls. Authorized MCP Interfaces: []",
)
select_top_urls_agent.tool_plain(ToQuoteAssistant)

summarize_articles_parallel_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: summarize_articles_parallel. Authorized MCP Interfaces: []",
)
summarize_articles_parallel_agent.tool_plain(ToQuoteAssistant)

format_results_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: format_results. Authorized MCP Interfaces: []",
)
format_results_agent.tool_plain(ToQuoteAssistant)

decision_making_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: decision_making. Authorized MCP Interfaces: []",
)
decision_making_agent.tool_plain(ToQuoteAssistant)

planning_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: planning. Authorized MCP Interfaces: []",
)
planning_agent.tool_plain(ToQuoteAssistant)

tools_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: tools. Authorized MCP Interfaces: []",
)
tools_agent.tool_plain(ToQuoteAssistant)

agent_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: agent. Authorized MCP Interfaces: []",
)
agent_agent.tool_plain(ToQuoteAssistant)

judge_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: judge. Authorized MCP Interfaces: []",
)
judge_agent.tool_plain(ToQuoteAssistant)

CATEGORY_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: CATEGORY. Authorized MCP Interfaces: []",
)
CATEGORY_agent.tool_plain(ToQuoteAssistant)

SUMMARY_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: SUMMARY. Authorized MCP Interfaces: []",
)
SUMMARY_agent.tool_plain(ToQuoteAssistant)

FACT_CHECKING_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: FACT_CHECKING. Authorized MCP Interfaces: []",
)
FACT_CHECKING_agent.tool_plain(ToQuoteAssistant)

TONE_ANALYSIS_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: TONE_ANALYSIS. Authorized MCP Interfaces: []",
)
TONE_ANALYSIS_agent.tool_plain(ToQuoteAssistant)

QUOTE_EXTRACTION_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: QUOTE_EXTRACTION. Authorized MCP Interfaces: []",
)
QUOTE_EXTRACTION_agent.tool_plain(ToQuoteAssistant)

GRAMMAR_AND_BIAS_REVIEW_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: GRAMMAR_AND_BIAS_REVIEW. Authorized MCP Interfaces: []",
)
GRAMMAR_AND_BIAS_REVIEW_agent.tool_plain(ToQuoteAssistant)

web_download_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: web_download. Authorized MCP Interfaces: []",
)
web_download_agent.tool_plain(ToQuoteAssistant)

embeddings_ner_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: embeddings_ner. Authorized MCP Interfaces: []",
)
embeddings_ner_agent.tool_plain(ToQuoteAssistant)

main_assistant_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: main_assistant. Authorized MCP Interfaces: []",
)
main_assistant_agent.tool_plain(ToQuoteAssistant)

main_assistant_tools_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: main_assistant_tools. Authorized MCP Interfaces: []",
)
main_assistant_tools_agent.tool_plain(ToQuoteAssistant)

underwriting_assistant_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: underwriting_assistant. Authorized MCP Interfaces: []",
)
underwriting_assistant_agent.tool_plain(ToQuoteAssistant)

quote_assistant_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: quote_assistant. Authorized MCP Interfaces: []",
)
quote_assistant_agent.tool_plain(ToQuoteAssistant)

quote_assistant_tools_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: quote_assistant_tools. Authorized MCP Interfaces: []",
)
quote_assistant_tools_agent.tool_plain(ToQuoteAssistant)

entry_quote_assistant_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: entry_quote_assistant. Authorized MCP Interfaces: []",
)
entry_quote_assistant_agent.tool_plain(ToQuoteAssistant)

retrieve_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: retrieve. Authorized MCP Interfaces: []",
)
retrieve_agent.tool_plain(ToQuoteAssistant)

reasoning_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: reasoning. Authorized MCP Interfaces: []",
)
reasoning_agent.tool_plain(ToQuoteAssistant)

classification_grading_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: classification_grading. Authorized MCP Interfaces: []",
)
classification_grading_agent.tool_plain(ToQuoteAssistant)

update_state_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: update_state. Authorized MCP Interfaces: []",
)
update_state_agent.tool_plain(ToQuoteAssistant)

reroute_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: reroute. Authorized MCP Interfaces: []",
)
reroute_agent.tool_plain(ToQuoteAssistant)

pass_tool_call_id_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: pass_tool_call_id. Authorized MCP Interfaces: []",
)
pass_tool_call_id_agent.tool_plain(ToQuoteAssistant)

pass_final_classifications_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: pass_final_classifications. Authorized MCP Interfaces: []",
)
pass_final_classifications_agent.tool_plain(ToQuoteAssistant)

create_tool_message_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: create_tool_message. Authorized MCP Interfaces: []",
)
create_tool_message_agent.tool_plain(ToQuoteAssistant)

update_workflow_state_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: update_workflow_state. Authorized MCP Interfaces: []",
)
update_workflow_state_agent.tool_plain(ToQuoteAssistant)

ask_user_needs_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: ask_user_needs. Authorized MCP Interfaces: []",
)
ask_user_needs_agent.tool_plain(ToQuoteAssistant)

build_filters_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: build_filters. Authorized MCP Interfaces: []",
)
build_filters_agent.tool_plain(ToQuoteAssistant)

search_listings_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: search_listings. Authorized MCP Interfaces: []",
)
search_listings_agent.tool_plain(ToQuoteAssistant)

fetch_additional_info_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: fetch_additional_info. Authorized MCP Interfaces: []",
)
fetch_additional_info_agent.tool_plain(ToQuoteAssistant)

irrelevant_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: irrelevant. Authorized MCP Interfaces: []",
)
irrelevant_agent.tool_plain(ToQuoteAssistant)

classify_contract_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: classify_contract. Authorized MCP Interfaces: []",
)
classify_contract_agent.tool_plain(ToQuoteAssistant)

retrieve_clauses_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: retrieve_clauses. Authorized MCP Interfaces: []",
)
retrieve_clauses_agent.tool_plain(ToQuoteAssistant)

execute_step_clause_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: execute_step_clause. Authorized MCP Interfaces: []",
)
execute_step_clause_agent.tool_plain(ToQuoteAssistant)

create_review_plan_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: create_review_plan. Authorized MCP Interfaces: []",
)
create_review_plan_agent.tool_plain(ToQuoteAssistant)

execute_step_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: execute_step. Authorized MCP Interfaces: []",
)
execute_step_agent.tool_plain(ToQuoteAssistant)

generate_final_report_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: generate_final_report. Authorized MCP Interfaces: []",
)
generate_final_report_agent.tool_plain(ToQuoteAssistant)

search_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: search. Authorized MCP Interfaces: []",
)
search_agent.tool_plain(ToQuoteAssistant)

summarize_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: summarize. Authorized MCP Interfaces: []",
)
summarize_agent.tool_plain(ToQuoteAssistant)

publish_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: publish. Authorized MCP Interfaces: []",
)
publish_agent.tool_plain(ToQuoteAssistant)

Keywords_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: Keywords. Authorized MCP Interfaces: []",
)
Keywords_agent.tool_plain(ToQuoteAssistant)

Structure_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: Structure. Authorized MCP Interfaces: []",
)
Structure_agent.tool_plain(ToQuoteAssistant)

Host question_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: Host question. Authorized MCP Interfaces: []",
)
Host question_agent.tool_plain(ToQuoteAssistant)

Web research_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: Web research. Authorized MCP Interfaces: []",
)
Web research_agent.tool_plain(ToQuoteAssistant)

Wiki research_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: Wiki research. Authorized MCP Interfaces: []",
)
Wiki research_agent.tool_plain(ToQuoteAssistant)

Expert answer_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: Expert answer. Authorized MCP Interfaces: []",
)
Expert answer_agent.tool_plain(ToQuoteAssistant)

Save podcast_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: Save podcast. Authorized MCP Interfaces: []",
)
Save podcast_agent.tool_plain(ToQuoteAssistant)

Write script_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: Write script. Authorized MCP Interfaces: []",
)
Write script_agent.tool_plain(ToQuoteAssistant)

Planing_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: Planing. Authorized MCP Interfaces: []",
)
Planing_agent.tool_plain(ToQuoteAssistant)

Start research_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: Start research. Authorized MCP Interfaces: []",
)
Start research_agent.tool_plain(ToQuoteAssistant)

Create podcast_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: Create podcast. Authorized MCP Interfaces: []",
)
Create podcast_agent.tool_plain(ToQuoteAssistant)

Write report_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: Write report. Authorized MCP Interfaces: []",
)
Write report_agent.tool_plain(ToQuoteAssistant)

Write introduction_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: Write introduction. Authorized MCP Interfaces: []",
)
Write introduction_agent.tool_plain(ToQuoteAssistant)

Write conclusion_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: Write conclusion. Authorized MCP Interfaces: []",
)
Write conclusion_agent.tool_plain(ToQuoteAssistant)

Finalize podcast_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: Finalize podcast. Authorized MCP Interfaces: []",
)
Finalize podcast_agent.tool_plain(ToQuoteAssistant)

requirements_gathering_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: requirements_gathering. Authorized MCP Interfaces: []",
)
requirements_gathering_agent.tool_plain(ToQuoteAssistant)

generate_job_desc_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: generate_job_desc. Authorized MCP Interfaces: []",
)
generate_job_desc_agent.tool_plain(ToQuoteAssistant)

linkedin_process_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: linkedin_process. Authorized MCP Interfaces: []",
)
linkedin_process_agent.tool_plain(ToQuoteAssistant)

analyze_cv_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: analyze_cv. Authorized MCP Interfaces: []",
)
analyze_cv_agent.tool_plain(ToQuoteAssistant)

prepare_interview_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: prepare_interview. Authorized MCP Interfaces: []",
)
prepare_interview_agent.tool_plain(ToQuoteAssistant)

classification_node_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: classification_node. Authorized MCP Interfaces: []",
)
classification_node_agent.tool_plain(ToQuoteAssistant)

entity_extraction_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: entity_extraction. Authorized MCP Interfaces: []",
)
entity_extraction_agent.tool_plain(ToQuoteAssistant)

summarization_agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="Extracted automatically via SwarmHub static AST source-slicing. Node context: summarization. Authorized MCP Interfaces: []",
)
summarization_agent.tool_plain(ToQuoteAssistant)

# 6. Assemble the State-Machine Execution Architecture Runtime Maps
if __name__ == "__main__":
    print("🚀 Running compiled SwarmHub execution pipeline validation...")
    print("⚠️ [Mode: Local Offline Execution] PydanticAI state-machine verification pass ignited.\n")
    initial_state_context = {}
    if "row" in locals() and row:
        state = json.loads(row[0])
    else:
        state = {
            "messages": [],
            "context": initial_state_context,
            "next_action": "PROCEED"
        }

    NODES_REGISTRY = {
        "approach_analysis": approach_analysis_agent,
        "task_knowledge_retrieval": task_knowledge_retrieval_agent,
        "customized_approach_generation": customized_approach_generation_agent,
        "melody_generator": melody_generator_agent,
        "harmony_creator": harmony_creator_agent,
        "rhythm_analyzer": rhythm_analyzer_agent,
        "style_adapter": style_adapter_agent,
        "midi_converter": midi_converter_agent,
        "triage": triage_agent,
        "response_agent": response_agent_agent,
        "triage": triage_agent,
        "response_agent": response_agent_agent,
        "code_execution_node": code_execution_node_agent,
        "code_update_node": code_update_node_agent,
        "code_patching_node": code_patching_node_agent,
        "bug_report_node": bug_report_node_agent,
        "memory_search_node": memory_search_node_agent,
        "memory_filter_node": memory_filter_node_agent,
        "memory_modification_node": memory_modification_node_agent,
        "memory_generation_node": memory_generation_node_agent,
        "input_city": input_city_agent,
        "input_interests": input_interests_agent,
        "create_itinerary": create_itinerary_agent,
        "get_weather": get_weather_agent,
        "analyze_disaster": analyze_disaster_agent,
        "assess_severity": assess_severity_agent,
        "data_logging": data_logging_agent,
        "emergency_response": emergency_response_agent,
        "civil_defense_response": civil_defense_response_agent,
        "public_works_response": public_works_response_agent,
        "get_human_verification": get_human_verification_agent,
        "send_email_alert": send_email_alert_agent,
        "handle_no_approval": handle_no_approval_agent,
        "get_weather": get_weather_agent,
        "social_media_monitoring": social_media_monitoring_agent,
        "analyze_disaster": analyze_disaster_agent,
        "assess_severity": assess_severity_agent,
        "data_logging": data_logging_agent,
        "emergency_response": emergency_response_agent,
        "civil_defense_response": civil_defense_response_agent,
        "public_works_response": public_works_response_agent,
        "get_human_verification": get_human_verification_agent,
        "send_email_alert": send_email_alert_agent,
        "handle_no_approval": handle_no_approval_agent,
        "assistant": assistant_agent,
        "tools": tools_agent,
        "generate_new_inputs": generate_new_inputs_agent,
        "static_test": static_test_agent,
        "generate_node_descriptions": generate_node_descriptions_agent,
        "generate_testers": generate_testers_agent,
        "generate_test_cases": generate_test_cases_agent,
        "run_test_cases": run_test_cases_agent,
        "analize_results": analize_results_agent,
        "assistant": assistant_agent,
        "tools": tools_agent,
        "process_input": process_input_agent,
        "planner": planner_agent,
        "researcher": researcher_agent,
        "search_articles": search_articles_agent,
        "article_decisions": article_decisions_agent,
        "download_articles": download_articles_agent,
        "paper_analyzer": paper_analyzer_agent,
        "write_abstract": write_abstract_agent,
        "write_introduction": write_introduction_agent,
        "write_methods": write_methods_agent,
        "write_results": write_results_agent,
        "write_conclusion": write_conclusion_agent,
        "write_references": write_references_agent,
        "aggregate_paper": aggregate_paper_agent,
        "critique_paper": critique_paper_agent,
        "revise_paper": revise_paper_agent,
        "final_draft": final_draft_agent,
        "task_generation": task_generation_agent,
        "task_dependencies": task_dependencies_agent,
        "task_scheduler": task_scheduler_agent,
        "task_allocator": task_allocator_agent,
        "risk_assessor": risk_assessor_agent,
        "insight_generator": insight_generator_agent,
        "create_project_plan": create_project_plan_agent,
        "requirements_gathering": requirements_gathering_agent,
        "generate_job_desc": generate_job_desc_agent,
        "linkedin_process": linkedin_process_agent,
        "analyze_cv": analyze_cv_agent,
        "prepare_interview": prepare_interview_agent,
        "check_relevance": check_relevance_agent,
        "check_grammar": check_grammar_agent,
        "analyze_structure": analyze_structure_agent,
        "evaluate_depth": evaluate_depth_agent,
        "calculate_final_score": calculate_final_score_agent,
        "generate_query": generate_query_agent,
        "search_web": search_web_agent,
        "chunk_context": chunk_context_agent,
        "context_validation": context_validation_agent,
        "generate_checkpoints": generate_checkpoints_agent,
        "generate_question": generate_question_agent,
        "next_checkpoint": next_checkpoint_agent,
        "user_answer": user_answer_agent,
        "verify_answer": verify_answer_agent,
        "teach_concept": teach_concept_agent,
        "tour_introduction": tour_introduction_agent,
        "display_artwork": display_artwork_agent,
        "get_next_artwork": get_next_artwork_agent,
        "discuss": discuss_agent,
        "conclude_tour": conclude_tour_agent,
        "character_introduction": character_introduction_agent,
        "ask_question": ask_question_agent,
        "answer_question": answer_question_agent,
        "create_characters": create_characters_agent,
        "create_story": create_story_agent,
        "narrartor": narrartor_agent,
        "sherlock": sherlock_agent,
        "guesser": guesser_agent,
        "conversation": conversation_agent,
        "summary_node": summary_node_agent,
        "research_node": research_node_agent,
        "intent_matching_node": intent_matching_node_agent,
        "instagram": instagram_agent,
        "twitter": twitter_agent,
        "linkedin": linkedin_agent,
        "blog": blog_agent,
        "combine_content": combine_content_agent,
        "generate_character_description": generate_character_description_agent,
        "generate_plot": generate_plot_agent,
        "generate_image_prompts": generate_image_prompts_agent,
        "create_images": create_images_agent,
        "create_gif": create_gif_agent,
        "classify_content": classify_content_agent,
        "process_general": process_general_agent,
        "process_poem": process_poem_agent,
        "process_news": process_news_agent,
        "process_joke": process_joke_agent,
        "text_to_speech": text_to_speech_agent,
        "categorize": categorize_agent,
        "handle_learning_resource": handle_learning_resource_agent,
        "handle_resume_making": handle_resume_making_agent,
        "handle_interview_preparation": handle_interview_preparation_agent,
        "job_search": job_search_agent,
        "mock_interview": mock_interview_agent,
        "interview_topics_questions": interview_topics_questions_agent,
        "tutorial_agent": tutorial_agent_agent,
        "ask_query_bot": ask_query_bot_agent,
        "calendar_analyzer": calendar_analyzer_agent,
        "task_analyzer": task_analyzer_agent,
        "plan_generator": plan_generator_agent,
        "notewriter_analyze": notewriter_analyze_agent,
        "notewriter_generate": notewriter_generate_agent,
        "advisor_analyze": advisor_analyze_agent,
        "advisor_generate": advisor_generate_agent,
        "coordinator": coordinator_agent,
        "profile_analyzer": profile_analyzer_agent,
        "execute": execute_agent,
        "calendar_analyzer": calendar_analyzer_agent,
        "task_analyzer": task_analyzer_agent,
        "plan_generator": plan_generator_agent,
        "notewriter_analyze": notewriter_analyze_agent,
        "notewriter_generate": notewriter_generate_agent,
        "advisor_analyze": advisor_analyze_agent,
        "advisor_generate": advisor_generate_agent,
        "convert_user_instruction_to_actions": convert_user_instruction_to_actions_agent,
        "get_initial_action": get_initial_action_agent,
        "get_website_state": get_website_state_agent,
        "generate_code_for_action": generate_code_for_action_agent,
        "validate_generated_action": validate_generated_action_agent,
        "handle_generation_error": handle_generation_error_agent,
        "post_process_script": post_process_script_agent,
        "execute_test_case": execute_test_case_agent,
        "generate_test_report": generate_test_report_agent,
        "categorize": categorize_agent,
        "analyze_sentiment": analyze_sentiment_agent,
        "handle_technical": handle_technical_agent,
        "handle_billing": handle_billing_agent,
        "handle_general": handle_general_agent,
        "escalate": escalate_agent,
        "get_website_content": get_website_content_agent,
        "analyze_company": analyze_company_agent,
        "generate_concepts": generate_concepts_agent,
        "select_templates": select_templates_agent,
        "generate_text": generate_text_agent,
        "create_url": create_url_agent,
        "tavily_search": tavily_search_agent,
        "schema_mapping": schema_mapping_agent,
        "product_comparison": product_comparison_agent,
        "youtube_review": youtube_review_agent,
        "display": display_agent,
        "send_email": send_email_agent,
        "classify_input": classify_input_agent,
        "discover_database": discover_database_agent,
        "create_plan": create_plan_agent,
        "execute_plan": execute_plan_agent,
        "generate_response": generate_response_agent,
        "generate_newsapi_params": generate_newsapi_params_agent,
        "retrieve_articles_metadata": retrieve_articles_metadata_agent,
        "retrieve_articles_text": retrieve_articles_text_agent,
        "select_top_urls": select_top_urls_agent,
        "summarize_articles_parallel": summarize_articles_parallel_agent,
        "format_results": format_results_agent,
        "decision_making": decision_making_agent,
        "planning": planning_agent,
        "tools": tools_agent,
        "agent": agent_agent,
        "judge": judge_agent,
        "CATEGORY": CATEGORY_agent,
        "SUMMARY": SUMMARY_agent,
        "FACT_CHECKING": FACT_CHECKING_agent,
        "TONE_ANALYSIS": TONE_ANALYSIS_agent,
        "QUOTE_EXTRACTION": QUOTE_EXTRACTION_agent,
        "GRAMMAR_AND_BIAS_REVIEW": GRAMMAR_AND_BIAS_REVIEW_agent,
        "web_download": web_download_agent,
        "embeddings_ner": embeddings_ner_agent,
        "main_assistant": main_assistant_agent,
        "main_assistant_tools": main_assistant_tools_agent,
        "underwriting_assistant": underwriting_assistant_agent,
        "quote_assistant": quote_assistant_agent,
        "quote_assistant_tools": quote_assistant_tools_agent,
        "entry_quote_assistant": entry_quote_assistant_agent,
        "retrieve": retrieve_agent,
        "reasoning": reasoning_agent,
        "classification_grading": classification_grading_agent,
        "update_state": update_state_agent,
        "reroute": reroute_agent,
        "pass_tool_call_id": pass_tool_call_id_agent,
        "pass_final_classifications": pass_final_classifications_agent,
        "create_tool_message": create_tool_message_agent,
        "update_workflow_state": update_workflow_state_agent,
        "ask_user_needs": ask_user_needs_agent,
        "build_filters": build_filters_agent,
        "search_listings": search_listings_agent,
        "fetch_additional_info": fetch_additional_info_agent,
        "irrelevant": irrelevant_agent,
        "classify_contract": classify_contract_agent,
        "retrieve_clauses": retrieve_clauses_agent,
        "execute_step_clause": execute_step_clause_agent,
        "create_review_plan": create_review_plan_agent,
        "execute_step": execute_step_agent,
        "generate_final_report": generate_final_report_agent,
        "search": search_agent,
        "summarize": summarize_agent,
        "publish": publish_agent,
        "Keywords": Keywords_agent,
        "Structure": Structure_agent,
        "Host question": Host question_agent,
        "Web research": Web research_agent,
        "Wiki research": Wiki research_agent,
        "Expert answer": Expert answer_agent,
        "Save podcast": Save podcast_agent,
        "Write script": Write script_agent,
        "Planing": Planing_agent,
        "Start research": Start research_agent,
        "Create podcast": Create podcast_agent,
        "Write report": Write report_agent,
        "Write introduction": Write introduction_agent,
        "Write conclusion": Write conclusion_agent,
        "Finalize podcast": Finalize podcast_agent,
        "requirements_gathering": requirements_gathering_agent,
        "generate_job_desc": generate_job_desc_agent,
        "linkedin_process": linkedin_process_agent,
        "analyze_cv": analyze_cv_agent,
        "prepare_interview": prepare_interview_agent,
        "classification_node": classification_node_agent,
        "entity_extraction": entity_extraction_agent,
        "summarization": summarization_agent,
    }
    NODES_PIPELINE_MAP = {
        "approach_analysis": importlib.import_module("blobs.approach_analysis").run,
        "task_knowledge_retrieval": importlib.import_module("blobs.task_knowledge_retrieval").run,
        "customized_approach_generation": importlib.import_module("blobs.customized_approach_generation").run,
        "melody_generator": importlib.import_module("blobs.melody_generator").run,
        "harmony_creator": importlib.import_module("blobs.harmony_creator").run,
        "rhythm_analyzer": importlib.import_module("blobs.rhythm_analyzer").run,
        "style_adapter": importlib.import_module("blobs.style_adapter").run,
        "midi_converter": importlib.import_module("blobs.midi_converter").run,
        "triage": importlib.import_module("blobs.triage").run,
        "response_agent": importlib.import_module("blobs.response_agent").run,
        "triage": importlib.import_module("blobs.triage").run,
        "response_agent": importlib.import_module("blobs.response_agent").run,
        "code_execution_node": importlib.import_module("blobs.code_execution_node").run,
        "code_update_node": importlib.import_module("blobs.code_update_node").run,
        "code_patching_node": importlib.import_module("blobs.code_patching_node").run,
        "bug_report_node": importlib.import_module("blobs.bug_report_node").run,
        "memory_search_node": importlib.import_module("blobs.memory_search_node").run,
        "memory_filter_node": importlib.import_module("blobs.memory_filter_node").run,
        "memory_modification_node": importlib.import_module("blobs.memory_modification_node").run,
        "memory_generation_node": importlib.import_module("blobs.memory_generation_node").run,
        "input_city": importlib.import_module("blobs.input_city").run,
        "input_interests": importlib.import_module("blobs.input_interests").run,
        "create_itinerary": importlib.import_module("blobs.create_itinerary").run,
        "get_weather": importlib.import_module("blobs.get_weather").run,
        "analyze_disaster": importlib.import_module("blobs.analyze_disaster").run,
        "assess_severity": importlib.import_module("blobs.assess_severity").run,
        "data_logging": importlib.import_module("blobs.data_logging").run,
        "emergency_response": importlib.import_module("blobs.emergency_response").run,
        "civil_defense_response": importlib.import_module("blobs.civil_defense_response").run,
        "public_works_response": importlib.import_module("blobs.public_works_response").run,
        "get_human_verification": importlib.import_module("blobs.get_human_verification").run,
        "send_email_alert": importlib.import_module("blobs.send_email_alert").run,
        "handle_no_approval": importlib.import_module("blobs.handle_no_approval").run,
        "get_weather": importlib.import_module("blobs.get_weather").run,
        "social_media_monitoring": importlib.import_module("blobs.social_media_monitoring").run,
        "analyze_disaster": importlib.import_module("blobs.analyze_disaster").run,
        "assess_severity": importlib.import_module("blobs.assess_severity").run,
        "data_logging": importlib.import_module("blobs.data_logging").run,
        "emergency_response": importlib.import_module("blobs.emergency_response").run,
        "civil_defense_response": importlib.import_module("blobs.civil_defense_response").run,
        "public_works_response": importlib.import_module("blobs.public_works_response").run,
        "get_human_verification": importlib.import_module("blobs.get_human_verification").run,
        "send_email_alert": importlib.import_module("blobs.send_email_alert").run,
        "handle_no_approval": importlib.import_module("blobs.handle_no_approval").run,
        "assistant": importlib.import_module("blobs.assistant").run,
        "tools": importlib.import_module("blobs.tools").run,
        "generate_new_inputs": importlib.import_module("blobs.generate_new_inputs").run,
        "static_test": importlib.import_module("blobs.static_test").run,
        "generate_node_descriptions": importlib.import_module("blobs.generate_node_descriptions").run,
        "generate_testers": importlib.import_module("blobs.generate_testers").run,
        "generate_test_cases": importlib.import_module("blobs.generate_test_cases").run,
        "run_test_cases": importlib.import_module("blobs.run_test_cases").run,
        "analize_results": importlib.import_module("blobs.analize_results").run,
        "assistant": importlib.import_module("blobs.assistant").run,
        "tools": importlib.import_module("blobs.tools").run,
        "process_input": importlib.import_module("blobs.process_input").run,
        "planner": importlib.import_module("blobs.planner").run,
        "researcher": importlib.import_module("blobs.researcher").run,
        "search_articles": importlib.import_module("blobs.search_articles").run,
        "article_decisions": importlib.import_module("blobs.article_decisions").run,
        "download_articles": importlib.import_module("blobs.download_articles").run,
        "paper_analyzer": importlib.import_module("blobs.paper_analyzer").run,
        "write_abstract": importlib.import_module("blobs.write_abstract").run,
        "write_introduction": importlib.import_module("blobs.write_introduction").run,
        "write_methods": importlib.import_module("blobs.write_methods").run,
        "write_results": importlib.import_module("blobs.write_results").run,
        "write_conclusion": importlib.import_module("blobs.write_conclusion").run,
        "write_references": importlib.import_module("blobs.write_references").run,
        "aggregate_paper": importlib.import_module("blobs.aggregate_paper").run,
        "critique_paper": importlib.import_module("blobs.critique_paper").run,
        "revise_paper": importlib.import_module("blobs.revise_paper").run,
        "final_draft": importlib.import_module("blobs.final_draft").run,
        "task_generation": importlib.import_module("blobs.task_generation").run,
        "task_dependencies": importlib.import_module("blobs.task_dependencies").run,
        "task_scheduler": importlib.import_module("blobs.task_scheduler").run,
        "task_allocator": importlib.import_module("blobs.task_allocator").run,
        "risk_assessor": importlib.import_module("blobs.risk_assessor").run,
        "insight_generator": importlib.import_module("blobs.insight_generator").run,
        "create_project_plan": importlib.import_module("blobs.create_project_plan").run,
        "requirements_gathering": importlib.import_module("blobs.requirements_gathering").run,
        "generate_job_desc": importlib.import_module("blobs.generate_job_desc").run,
        "linkedin_process": importlib.import_module("blobs.linkedin_process").run,
        "analyze_cv": importlib.import_module("blobs.analyze_cv").run,
        "prepare_interview": importlib.import_module("blobs.prepare_interview").run,
        "check_relevance": importlib.import_module("blobs.check_relevance").run,
        "check_grammar": importlib.import_module("blobs.check_grammar").run,
        "analyze_structure": importlib.import_module("blobs.analyze_structure").run,
        "evaluate_depth": importlib.import_module("blobs.evaluate_depth").run,
        "calculate_final_score": importlib.import_module("blobs.calculate_final_score").run,
        "generate_query": importlib.import_module("blobs.generate_query").run,
        "search_web": importlib.import_module("blobs.search_web").run,
        "chunk_context": importlib.import_module("blobs.chunk_context").run,
        "context_validation": importlib.import_module("blobs.context_validation").run,
        "generate_checkpoints": importlib.import_module("blobs.generate_checkpoints").run,
        "generate_question": importlib.import_module("blobs.generate_question").run,
        "next_checkpoint": importlib.import_module("blobs.next_checkpoint").run,
        "user_answer": importlib.import_module("blobs.user_answer").run,
        "verify_answer": importlib.import_module("blobs.verify_answer").run,
        "teach_concept": importlib.import_module("blobs.teach_concept").run,
        "tour_introduction": importlib.import_module("blobs.tour_introduction").run,
        "display_artwork": importlib.import_module("blobs.display_artwork").run,
        "get_next_artwork": importlib.import_module("blobs.get_next_artwork").run,
        "discuss": importlib.import_module("blobs.discuss").run,
        "conclude_tour": importlib.import_module("blobs.conclude_tour").run,
        "character_introduction": importlib.import_module("blobs.character_introduction").run,
        "ask_question": importlib.import_module("blobs.ask_question").run,
        "answer_question": importlib.import_module("blobs.answer_question").run,
        "create_characters": importlib.import_module("blobs.create_characters").run,
        "create_story": importlib.import_module("blobs.create_story").run,
        "narrartor": importlib.import_module("blobs.narrartor").run,
        "sherlock": importlib.import_module("blobs.sherlock").run,
        "guesser": importlib.import_module("blobs.guesser").run,
        "conversation": importlib.import_module("blobs.conversation").run,
        "summary_node": importlib.import_module("blobs.summary_node").run,
        "research_node": importlib.import_module("blobs.research_node").run,
        "intent_matching_node": importlib.import_module("blobs.intent_matching_node").run,
        "instagram": importlib.import_module("blobs.instagram").run,
        "twitter": importlib.import_module("blobs.twitter").run,
        "linkedin": importlib.import_module("blobs.linkedin").run,
        "blog": importlib.import_module("blobs.blog").run,
        "combine_content": importlib.import_module("blobs.combine_content").run,
        "generate_character_description": importlib.import_module("blobs.generate_character_description").run,
        "generate_plot": importlib.import_module("blobs.generate_plot").run,
        "generate_image_prompts": importlib.import_module("blobs.generate_image_prompts").run,
        "create_images": importlib.import_module("blobs.create_images").run,
        "create_gif": importlib.import_module("blobs.create_gif").run,
        "classify_content": importlib.import_module("blobs.classify_content").run,
        "process_general": importlib.import_module("blobs.process_general").run,
        "process_poem": importlib.import_module("blobs.process_poem").run,
        "process_news": importlib.import_module("blobs.process_news").run,
        "process_joke": importlib.import_module("blobs.process_joke").run,
        "text_to_speech": importlib.import_module("blobs.text_to_speech").run,
        "categorize": importlib.import_module("blobs.categorize").run,
        "handle_learning_resource": importlib.import_module("blobs.handle_learning_resource").run,
        "handle_resume_making": importlib.import_module("blobs.handle_resume_making").run,
        "handle_interview_preparation": importlib.import_module("blobs.handle_interview_preparation").run,
        "job_search": importlib.import_module("blobs.job_search").run,
        "mock_interview": importlib.import_module("blobs.mock_interview").run,
        "interview_topics_questions": importlib.import_module("blobs.interview_topics_questions").run,
        "tutorial_agent": importlib.import_module("blobs.tutorial_agent").run,
        "ask_query_bot": importlib.import_module("blobs.ask_query_bot").run,
        "calendar_analyzer": importlib.import_module("blobs.calendar_analyzer").run,
        "task_analyzer": importlib.import_module("blobs.task_analyzer").run,
        "plan_generator": importlib.import_module("blobs.plan_generator").run,
        "notewriter_analyze": importlib.import_module("blobs.notewriter_analyze").run,
        "notewriter_generate": importlib.import_module("blobs.notewriter_generate").run,
        "advisor_analyze": importlib.import_module("blobs.advisor_analyze").run,
        "advisor_generate": importlib.import_module("blobs.advisor_generate").run,
        "coordinator": importlib.import_module("blobs.coordinator").run,
        "profile_analyzer": importlib.import_module("blobs.profile_analyzer").run,
        "execute": importlib.import_module("blobs.execute").run,
        "calendar_analyzer": importlib.import_module("blobs.calendar_analyzer").run,
        "task_analyzer": importlib.import_module("blobs.task_analyzer").run,
        "plan_generator": importlib.import_module("blobs.plan_generator").run,
        "notewriter_analyze": importlib.import_module("blobs.notewriter_analyze").run,
        "notewriter_generate": importlib.import_module("blobs.notewriter_generate").run,
        "advisor_analyze": importlib.import_module("blobs.advisor_analyze").run,
        "advisor_generate": importlib.import_module("blobs.advisor_generate").run,
        "convert_user_instruction_to_actions": importlib.import_module("blobs.convert_user_instruction_to_actions").run,
        "get_initial_action": importlib.import_module("blobs.get_initial_action").run,
        "get_website_state": importlib.import_module("blobs.get_website_state").run,
        "generate_code_for_action": importlib.import_module("blobs.generate_code_for_action").run,
        "validate_generated_action": importlib.import_module("blobs.validate_generated_action").run,
        "handle_generation_error": importlib.import_module("blobs.handle_generation_error").run,
        "post_process_script": importlib.import_module("blobs.post_process_script").run,
        "execute_test_case": importlib.import_module("blobs.execute_test_case").run,
        "generate_test_report": importlib.import_module("blobs.generate_test_report").run,
        "categorize": importlib.import_module("blobs.categorize").run,
        "analyze_sentiment": importlib.import_module("blobs.analyze_sentiment").run,
        "handle_technical": importlib.import_module("blobs.handle_technical").run,
        "handle_billing": importlib.import_module("blobs.handle_billing").run,
        "handle_general": importlib.import_module("blobs.handle_general").run,
        "escalate": importlib.import_module("blobs.escalate").run,
        "get_website_content": importlib.import_module("blobs.get_website_content").run,
        "analyze_company": importlib.import_module("blobs.analyze_company").run,
        "generate_concepts": importlib.import_module("blobs.generate_concepts").run,
        "select_templates": importlib.import_module("blobs.select_templates").run,
        "generate_text": importlib.import_module("blobs.generate_text").run,
        "create_url": importlib.import_module("blobs.create_url").run,
        "tavily_search": importlib.import_module("blobs.tavily_search").run,
        "schema_mapping": importlib.import_module("blobs.schema_mapping").run,
        "product_comparison": importlib.import_module("blobs.product_comparison").run,
        "youtube_review": importlib.import_module("blobs.youtube_review").run,
        "display": importlib.import_module("blobs.display").run,
        "send_email": importlib.import_module("blobs.send_email").run,
        "classify_input": importlib.import_module("blobs.classify_input").run,
        "discover_database": importlib.import_module("blobs.discover_database").run,
        "create_plan": importlib.import_module("blobs.create_plan").run,
        "execute_plan": importlib.import_module("blobs.execute_plan").run,
        "generate_response": importlib.import_module("blobs.generate_response").run,
        "generate_newsapi_params": importlib.import_module("blobs.generate_newsapi_params").run,
        "retrieve_articles_metadata": importlib.import_module("blobs.retrieve_articles_metadata").run,
        "retrieve_articles_text": importlib.import_module("blobs.retrieve_articles_text").run,
        "select_top_urls": importlib.import_module("blobs.select_top_urls").run,
        "summarize_articles_parallel": importlib.import_module("blobs.summarize_articles_parallel").run,
        "format_results": importlib.import_module("blobs.format_results").run,
        "decision_making": importlib.import_module("blobs.decision_making").run,
        "planning": importlib.import_module("blobs.planning").run,
        "tools": importlib.import_module("blobs.tools").run,
        "agent": importlib.import_module("blobs.agent").run,
        "judge": importlib.import_module("blobs.judge").run,
        "CATEGORY": importlib.import_module("blobs.CATEGORY").run,
        "SUMMARY": importlib.import_module("blobs.SUMMARY").run,
        "FACT_CHECKING": importlib.import_module("blobs.FACT_CHECKING").run,
        "TONE_ANALYSIS": importlib.import_module("blobs.TONE_ANALYSIS").run,
        "QUOTE_EXTRACTION": importlib.import_module("blobs.QUOTE_EXTRACTION").run,
        "GRAMMAR_AND_BIAS_REVIEW": importlib.import_module("blobs.GRAMMAR_AND_BIAS_REVIEW").run,
        "web_download": importlib.import_module("blobs.web_download").run,
        "embeddings_ner": importlib.import_module("blobs.embeddings_ner").run,
        "main_assistant": importlib.import_module("blobs.main_assistant").run,
        "main_assistant_tools": importlib.import_module("blobs.main_assistant_tools").run,
        "underwriting_assistant": importlib.import_module("blobs.underwriting_assistant").run,
        "quote_assistant": importlib.import_module("blobs.quote_assistant").run,
        "quote_assistant_tools": importlib.import_module("blobs.quote_assistant_tools").run,
        "entry_quote_assistant": importlib.import_module("blobs.entry_quote_assistant").run,
        "retrieve": importlib.import_module("blobs.retrieve").run,
        "reasoning": importlib.import_module("blobs.reasoning").run,
        "classification_grading": importlib.import_module("blobs.classification_grading").run,
        "update_state": importlib.import_module("blobs.update_state").run,
        "reroute": importlib.import_module("blobs.reroute").run,
        "pass_tool_call_id": importlib.import_module("blobs.pass_tool_call_id").run,
        "pass_final_classifications": importlib.import_module("blobs.pass_final_classifications").run,
        "create_tool_message": importlib.import_module("blobs.create_tool_message").run,
        "update_workflow_state": importlib.import_module("blobs.update_workflow_state").run,
        "ask_user_needs": importlib.import_module("blobs.ask_user_needs").run,
        "build_filters": importlib.import_module("blobs.build_filters").run,
        "search_listings": importlib.import_module("blobs.search_listings").run,
        "fetch_additional_info": importlib.import_module("blobs.fetch_additional_info").run,
        "irrelevant": importlib.import_module("blobs.irrelevant").run,
        "classify_contract": importlib.import_module("blobs.classify_contract").run,
        "retrieve_clauses": importlib.import_module("blobs.retrieve_clauses").run,
        "execute_step_clause": importlib.import_module("blobs.execute_step_clause").run,
        "create_review_plan": importlib.import_module("blobs.create_review_plan").run,
        "execute_step": importlib.import_module("blobs.execute_step").run,
        "generate_final_report": importlib.import_module("blobs.generate_final_report").run,
        "search": importlib.import_module("blobs.search").run,
        "summarize": importlib.import_module("blobs.summarize").run,
        "publish": importlib.import_module("blobs.publish").run,
        "Keywords": importlib.import_module("blobs.Keywords").run,
        "Structure": importlib.import_module("blobs.Structure").run,
        "Host question": importlib.import_module("blobs.Host question").run,
        "Web research": importlib.import_module("blobs.Web research").run,
        "Wiki research": importlib.import_module("blobs.Wiki research").run,
        "Expert answer": importlib.import_module("blobs.Expert answer").run,
        "Save podcast": importlib.import_module("blobs.Save podcast").run,
        "Write script": importlib.import_module("blobs.Write script").run,
        "Planing": importlib.import_module("blobs.Planing").run,
        "Start research": importlib.import_module("blobs.Start research").run,
        "Create podcast": importlib.import_module("blobs.Create podcast").run,
        "Write report": importlib.import_module("blobs.Write report").run,
        "Write introduction": importlib.import_module("blobs.Write introduction").run,
        "Write conclusion": importlib.import_module("blobs.Write conclusion").run,
        "Finalize podcast": importlib.import_module("blobs.Finalize podcast").run,
        "requirements_gathering": importlib.import_module("blobs.requirements_gathering").run,
        "generate_job_desc": importlib.import_module("blobs.generate_job_desc").run,
        "linkedin_process": importlib.import_module("blobs.linkedin_process").run,
        "analyze_cv": importlib.import_module("blobs.analyze_cv").run,
        "prepare_interview": importlib.import_module("blobs.prepare_interview").run,
        "classification_node": importlib.import_module("blobs.classification_node").run,
        "entity_extraction": importlib.import_module("blobs.entity_extraction").run,
        "summarization": importlib.import_module("blobs.summarization").run,
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
        agent_instance = NODES_REGISTRY.get(current_node)
        node_executor = NODES_PIPELINE_MAP.get(current_node)
        if not agent_instance or not node_executor:
            break
        print(f"\n--- 🟢 Entering PydanticAI Core Node: {current_node} ---")
        
        span_id = f"span-{uuid.uuid4().hex[:8]}"
        contract_status = "VERIFIED"
        start_time = time.perf_counter()
        
        try:
            SharedContextContract(**state["context"])
        except Exception as contract_err:
            print(f"    ⚠️ [Contract Breakage] Incoming schema anomaly caught at entry of {current_node}: {contract_err}")
            contract_status = "FAILED_ENTRY"
        
        try:
            # Execute the node context mutation pass through the runtime executor hook
            state = node_executor(state)
            
            if contract_status == "VERIFIED":
                try:
                    SharedContextContract(**state["context"])
                except Exception as contract_err_exit:
                    print(f"    ❌ [Contract Breakage] Outgoing contract violation caught at exit of {current_node}: {contract_err_exit}")
                    contract_status = "FAILED_EXIT"
        except Exception as e:
            print(f"    ❌ Execution/Contract Fault inside node [{current_node}]: {e}")
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

    print("\n🏁 PydanticAI Task Step Loop Pipeline Successfully Executed!")
    print("Final Verified State Context Payload:", state["context"])