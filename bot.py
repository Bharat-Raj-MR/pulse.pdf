import requests
from datetime import date

def get_weather(city="Thiruvananthapuram"):
    """Fetch today's weather as a one-line text summary."""
    url = f"https://wttr.in/{city}?format=3"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text.strip()  # Removes any trailing whitespace/newlines
    except Exception as e:
        return f"Weather unavailable ({e})"

def get_quote():
    """Fetch a random motivational quote from ZenQuotes."""
    url = "https://zenquotes.io/api/random"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        quote = data[0]["q"]   # 'q' stands for the quote text
        author = data[0]["a"]  # 'a' stands for the author
        return f'"{quote}" - {author}'
    except Exception as e:
        return f"Quote unavailable ({e})"

def build_summary():
    """Assemble the full daily summary from all data sources."""
    today = date.today().strftime("%A, %B %d, %Y")
    weather = get_weather()
    quote = get_quote()
    
    summary = f"""
=========================================
PULSE Daily Summary
{today}
=========================================
WEATHER:
{weather}

TODAY'S QUOTE:
{quote}
=========================================
"""
    return summary

def run():
    """Main entry point orchestrating the build, print, and save steps."""
    summary = build_summary()
    
    # This prints the summary into your terminal (or GitHub Actions log)
    print(summary)
    
    # This saves the summary as a text file artifact
    with open("daily_summary.txt", "w", encoding="utf-8") as f:
        f.write(summary)
    print("Pulse ran successfully. Summary artifact written.")

if __name__ == "__main__":
    run()
