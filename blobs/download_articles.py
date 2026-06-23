def run(state):
    print("DOWNLOAD PAPERS")
    last_message = state["messages"][-1]

    try:
        # Handle different types of content
        if isinstance(last_message.content, str):
            urls = ast.literal_eval(last_message.content)
        else:
            urls = last_message.content

        filenames = []
        for url in urls:
            try:
                response = requests.get(url)
                response.raise_for_status()

                # Create a papers directory if it doesn't exist
                if not os.path.exists('data'):
                    os.makedirs('data')

                # Generate a filename from the URL
                filename = f"data/{url.split('/')[-1]}"
                if not filename.endswith('.pdf'):
                    filename += '.pdf'

                # Save the PDF
                with open(filename, 'wb') as f:
                    f.write(response.content)

                filenames.append({"paper" : filename})
                print(f"Successfully downloaded: {filename}")

            except Exception as e:
                print(f"Error downloading {url}: {str(e)}")
                continue

        # Return AIMessage instead of raw strings
        return {
            "papers": [
                AIMessage(
                    content=filenames,
                    response_metadata={'finish_reason': 'stop'}
                )
            ]
        }

    except Exception as e:
        # Return error as AIMessage
        return {
            "messages": [
                AIMessage(
                    content=f"Error processing downloads: {str(e)}",
                    response_metadata={'finish_reason': 'error'}
                )
            ]
        }