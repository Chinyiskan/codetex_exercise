Aquí tienes un archivo README.md para tu programa de "Fortune Cookie":

### README.md

```markdown
# Fortune Cookie Emulator

This simple Python program emulates a fortune cookie by providing random fortunes when executed. Each run of the program will output one of eight possible fortunes.

## How It Works

The program uses the `random` module to generate a random number between 1 and 8. Based on the generated number, it prints a corresponding fortune message.

## Usage

1. Make sure you have Python installed on your system.

2. Copy the code below into a Python file (e.g., `fortune_cookie.py`):

    ```python
    import random

    # This simple program emulates a fortune cookie🍪
    def fortune_cookie():
        cookie = random.randint(1, 8)

        if cookie == 1:
            print("Don't pursue happiness – create it.")
        elif cookie == 2:
            print("All things are difficult before they are easy.")
        elif cookie == 3:
            print("The early bird gets the worm, but the second mouse gets the cheese.")
        elif cookie == 4:
            print("Someone in your life needs a letter from you.")
        elif cookie == 5:
            print("Don't just think. Act!")
        elif cookie == 6:
            print("Your heart will skip a beat.")
        elif cookie == 7:
            print("The fortune you search for is in another cookie.")
        elif cookie == 8:
            print("Help! I'm being held prisoner in a Chinese bakery!")

    fortune_cookie()
    fortune_cookie()
    fortune_cookie()
    ```

3. Run the script using Python:

    ```sh
    python fortune_cookie.py
    ```

4. The program will print three random fortunes to the console.

## Example Output

```
The early bird gets the worm, but the second mouse gets the cheese.
Your heart will skip a beat.
Help! I'm being held prisoner in a Chinese bakery!
```

## Customization

You can easily customize the fortunes by modifying the messages within the `fortune_cookie` function. Simply replace the existing strings with your own messages.

## License

This project is open source and available under the MIT License.

Enjoy your fortune cookies! 🍪
```