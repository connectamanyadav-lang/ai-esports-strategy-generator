import openai

openai.api_key = "YOUR_API_KEY"

def generate_strategy(game, map_name, playstyle):
    prompt = f"""
    You are a professional esports coach.

    Game: {game}
    Map: {map_name}
    Playstyle: {playstyle}

    Give a competitive strategy including:
    - Early game plan
    - Mid game positioning
    - End game tactics
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response['choices'][0]['message']['content']


if __name__ == "__main__":
    game = input("Enter game: ")
    map_name = input("Enter map: ")
    playstyle = input("Enter playstyle: ")

    strategy = generate_strategy(game, map_name, playstyle)
    print("\n🔥 Strategy:\n")
    print(strategy)
