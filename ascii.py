import pyfiglet
import os

def generate_ascii_art(text, font="standard"):
    """
    Generate ASCII art from text using the specified font.
    
    Args:
        text (str): The text to convert to ASCII art
        font (str): The font to use (default: "standard")
    
    Returns:
        str: The ASCII art representation of the text
    """
    try:
        ascii_art = pyfiglet.figlet_format(text, font=font)
        return ascii_art
    except Exception as e:
        print(f"Error generating ASCII art: {e}")
        return None

def save_to_file(content, filename="save.txt"):
    """
    Save content to a file.
    
    Args:
        content (str): The content to save
        filename (str): The name of the file to save to
    
    Returns:
        bool: True if saving was successful, False otherwise
    """
    try:
        with open(filename, 'w') as file:
            file.write(content)
        print(f"ASCII art saved to {filename}")
        return True
    except Exception as e:
        print(f"Error saving to file: {e}")
        return False

def list_available_fonts():
    """List all available fonts in pyfiglet."""
    return pyfiglet.FigletFont.getFonts()

def main():
    print("ASCII Art Generator")
    print("-----------------")
    
    # Get user input
    text = input("Enter text to convert to ASCII art: ")
    
    # Ask if user wants to see available fonts
    see_fonts = input("Do you want to see available fonts? (y/n): ").lower()
    if see_fonts == 'y':
        fonts = list_available_fonts()
        print("Available fonts:")
        for i, font in enumerate(fonts):
            print(f"{i+1}. {font}")
        
        # Let user select a font
        try:
            font_index = int(input(f"Enter font number (1-{len(fonts)}): ")) - 1
            if 0 <= font_index < len(fonts):
                selected_font = fonts[font_index]
            else:
                print("Invalid selection, using default font.")
                selected_font = "standard"
        except ValueError:
            print("Invalid input, using default font.")
            selected_font = "standard"
    else:
        selected_font = "standard"
    
    # Generate ASCII art
    art = generate_ascii_art(text, selected_font)
    
    if art:
        # Display the ASCII art
        print("\nYour ASCII Art:")
        print(art)
        
        # Save to file
        save_to_file(art)

if __name__ == "__main__":
    # Check if pyfiglet is installed, if not prompt user to install it
    try:
        import pyfiglet
    except ImportError:
        print("The pyfiglet module is required but not installed.")
        install = input("Do you want to install it now? (y/n): ").lower()
        if install == 'y':
            import subprocess
            subprocess.call(["pip", "install", "pyfiglet"])
            print("pyfiglet installed successfully!")
            import pyfiglet
        else:
            print("Cannot continue without pyfiglet. Exiting.")
            exit(1)
    
    main()
