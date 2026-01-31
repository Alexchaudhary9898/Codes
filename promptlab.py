def generate_response(prompt, temperature=0.5):

    """Generate a response from Gemini API with a specified temperature."""

    try:

        # Initialize the client with API key from config module

        client = genai.Client(api_key=config.GEMINI_API_KEY)

        

        # Create the content structure

        contents = [

            types.Content(

                role="user",

                parts=[types.Part.from_text(text=prompt)],

            ),

        ]

        

        # Configure generation parameters

        generate_content_config = types.GenerateContentConfig(

            temperature=temperature,

            response_mime_type="text/plain",

        )

        

        # Generate content (non-streaming version for simplicity)

        response = client.models.generate_content(

            model="gemini-2.0-flash",

            contents=contents,

            config=generate_content_config,

        )

        

        # Extract and return the response text

        return response.text

    except Exception as e:

        return f"Error generating response: {str(e)}"