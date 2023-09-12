import time

def calculate_typing_speed(correct_words, elapsed_time):
    words_per_minute = (correct_words / elapsed_time) * 60
    return words_per_minute

def main():
    input_text = input("Type the following sentence:\n"
                       "The quick brown fox jumps over the lazy dog\n")
    
    reference_text = "The quick brown fox jumps over the lazy dog"
    
    correct_words = 0
    input_words = input_text.split()
    reference_words = reference_text.split()
    
    for input_word, reference_word in zip(input_words, reference_words):
        if input_word == reference_word:
            correct_words += 1
    
    elapsed_time = time.time() - start_time
    typing_speed = calculate_typing_speed(correct_words, elapsed_time)
    
    print(f"Your typing speed: {typing_speed:.2f} WPM")

if __name__ == "__main__":
    start_time = time.time()
    main()
