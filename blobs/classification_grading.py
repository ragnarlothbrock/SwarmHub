def run(state):
    """
    Grade each category based on how well it matches the business description.
    """
    print("\n=== CLASSIFICATION GRADING START ===")
    
    # Extract core data
    description = rag_state["description"]
    rationale = rag_state["rationale"]
    categories = rationale.categories
    
    print(f"Processing {len(categories)} categories for grading...")
    
    try:
        # Format categories into a single string
        cat_and_rat = "\n\n".join([
            f"Category: {cat.category}\n"
            f"Description: {cat.cat_description}\n"
            f"Code: {cat.code}\n"
            f"Rationale: {cat.rationalization}\n"
            for cat in categories
        ])
        
        graded_categories = classification_grading_runnable.invoke({
            "description": description,
            "cat_and_rat": cat_and_rat
        })
        
        print(f"\nCompleted grading {len(graded_categories.description_grades)} categories")
        
    except Exception as e:
        print(f"Error during classification grading: {str(e)}")
        raise
    
    print("=== CLASSIFICATION GRADING END ===\n")
    return {"graded_categories": graded_categories.description_grades}