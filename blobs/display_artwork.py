def run(state):
    """
    Render the widgets
    """
    state['footer'].value = html_widget_value(state['artwork_description'] + "\n\n## Comment on the artwork.")
    state['header'].value = html_widget_value(state['artwork'])
    state['image'].value = image_widget_value(state['artwork_url'])

    return state