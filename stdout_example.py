#!/usr/bin/env python3
"""
Console Output and Animation Demo

A comprehensive demonstration of using sys.stdout.write() and sys.stdout.flush()
for real-time console output, animations, and progress indicators.

This module showcases various techniques for creating dynamic console interfaces
including loading animations, progress bars, real-time updates, and threaded
animations.

Key Concepts:
- sys.stdout.write(): Writes text without automatic newline
- sys.stdout.flush(): Forces immediate output display
- \r: Carriage return (moves cursor to start of line)
- \b: Backspace (moves cursor back one character)
- \033[A/B: ANSI escape codes for cursor movement

Author: AI Assistant
License: MIT
Version: 1.0.0
"""

import sys
import time
import threading
from typing import List, Callable, Optional


class ConsoleAnimator:
    """Utility class for creating console animations and effects."""
    
    @staticmethod
    def write_with_flush(text: str) -> None:
        """Write text to stdout and immediately flush the buffer."""
        sys.stdout.write(text)
        sys.stdout.flush()
    
    @staticmethod
    def clear_line() -> None:
        """Clear the current line by overwriting with spaces."""
        sys.stdout.write('\r' + ' ' * 80 + '\r')
        sys.stdout.flush()
    
    @staticmethod
    def move_cursor_up(lines: int) -> None:
        """Move cursor up by specified number of lines."""
        sys.stdout.write(f'\033[{lines}A')
        sys.stdout.flush()
    
    @staticmethod
    def move_cursor_down(lines: int) -> None:
        """Move cursor down by specified number of lines."""
        sys.stdout.write(f'\033[{lines}B')
        sys.stdout.flush()


def demo_basic_write() -> None:
    """
    Demonstrate basic sys.stdout.write() vs print() differences.
    
    Shows how print() automatically adds newlines while sys.stdout.write()
    does not, requiring manual newline management.
    """
    print("\n=== Basic Write Demo ===")
    
    # Method 1: Using print() - adds newline automatically
    print("Line 1 with print")
    print("Line 2 with print")
    
    # Method 2: Using sys.stdout.write() - no automatic newline
    ConsoleAnimator.write_with_flush("Line 1 with stdout.write")
    ConsoleAnimator.write_with_flush("Line 2 with stdout.write")  # Same line!
    
    # Add newline manually
    ConsoleAnimator.write_with_flush("\n")
    print("Now we're on a new line")


def demo_flush_importance() -> None:
    """
    Demonstrate why sys.stdout.flush() is crucial for real-time output.
    
    Shows the difference between buffered output (without flush) and
    immediate output (with flush) during processing loops.
    """
    print("\n=== Flush Importance Demo ===")
    
    print("Without flush (may not show immediately):")
    for i in range(5):
        sys.stdout.write(f"Processing {i}... ")
        time.sleep(0.5)  # Simulate work
        # Without flush, output might be buffered and not show immediately
    
    print("\n\nWith flush (shows immediately):")
    for i in range(5):
        ConsoleAnimator.write_with_flush(f"Processing {i}... ")
        time.sleep(0.5)  # Simulate work
    
    print("\nDone!")


def demo_carriage_return() -> None:
    """
    Demonstrate using \r for overwriting lines in place.
    
    Shows how carriage return can be used to create countdown timers
    and other dynamic single-line updates.
    """
    print("\n=== Carriage Return Demo ===")
    
    print("Counting down with carriage return:")
    for i in range(10, 0, -1):
        ConsoleAnimator.write_with_flush(f"\rCountdown: {i}")
        time.sleep(0.5)
    
    ConsoleAnimator.write_with_flush("\rCountdown: Blast off!     \n")


def demo_loading_animation() -> None:
    """
    Create a simple loading animation using spinning characters.
    
    Demonstrates how to create engaging loading indicators
    using Unicode braille characters for smooth animation.
    """
    print("\n=== Loading Animation Demo ===")
    
    animation_chars: List[str] = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    
    print("Loading with animation:")
    for i in range(20):  # Run for 20 iterations
        char = animation_chars[i % len(animation_chars)]
        ConsoleAnimator.write_with_flush(f"\r{char} Loading... {i+1}/20")
        time.sleep(0.1)
    
    ConsoleAnimator.write_with_flush("\r✅ Loading complete!     \n")


def demo_progress_bar() -> None:
    """
    Create a visual progress bar with percentage and count.
    
    Shows how to create professional-looking progress indicators
    with filled blocks, percentages, and current/total counts.
    """
    print("\n=== Progress Bar Demo ===")
    
    total: int = 50
    bar_width: int = 30
    
    print("Processing with progress bar:")
    for i in range(total + 1):
        # Calculate progress percentage
        progress = i / total
        filled_width = int(bar_width * progress)
        
        # Create progress bar
        bar = "█" * filled_width + "░" * (bar_width - filled_width)
        percentage = int(progress * 100)
        
        # Display progress
        ConsoleAnimator.write_with_flush(
            f"\rProgress: [{bar}] {percentage}% ({i}/{total})"
        )
        time.sleep(0.05)
    
    print("\n✅ Processing complete!")


def demo_multi_line_output() -> None:
    """
    Demonstrate multi-line output with cursor control.
    
    Shows how to update multiple lines simultaneously using
    ANSI escape codes for cursor movement.
    """
    print("\n=== Multi-line Output Demo ===")
    
    print("Initial state:")
    print("Line 1: Ready")
    print("Line 2: Ready")
    print("Line 3: Ready")
    
    time.sleep(1)
    
    # Move cursor up 3 lines and update
    ConsoleAnimator.move_cursor_up(3)
    ConsoleAnimator.write_with_flush("\rLine 1: Processing...")
    time.sleep(0.5)
    
    ConsoleAnimator.move_cursor_down(1)
    ConsoleAnimator.write_with_flush("\rLine 2: Processing...")
    time.sleep(0.5)
    
    ConsoleAnimator.move_cursor_down(1)
    ConsoleAnimator.write_with_flush("\rLine 3: Processing...")
    time.sleep(0.5)
    
    # Move to bottom and add completion message
    ConsoleAnimator.move_cursor_down(1)
    print("\r✅ All lines processed!")


def demo_backspace() -> None:
    """
    Demonstrate using backspace for character-by-character effects.
    
    Shows how to create typing and deleting effects using
    backspace characters for dynamic text manipulation.
    """
    print("\n=== Backspace Demo ===")
    
    message: str = "Hello, World!"
    print("Typing effect:")
    
    # Type out message character by character
    for char in message:
        ConsoleAnimator.write_with_flush(char)
        time.sleep(0.1)
    
    print("\n")
    
    # Delete message character by character
    print("Deleting effect:")
    for i in range(len(message), 0, -1):
        ConsoleAnimator.write_with_flush("\b \b")  # Backspace, space, backspace
        time.sleep(0.1)
    
    print("Done!")


def demo_threaded_animation() -> None:
    """
    Demonstrate animation in a separate thread.
    
    Shows how to run animations concurrently with main processing
    using threading, with proper cleanup and synchronization.
    """
    print("\n=== Threaded Animation Demo ===")
    
    def animate(stop_event: threading.Event) -> None:
        """Animation function running in separate thread."""
        chars: List[str] = ["|", "/", "-", "\\"]
        i: int = 0
        while not stop_event.is_set():
            ConsoleAnimator.write_with_flush(f"\r{chars[i]} Working...")
            i = (i + 1) % len(chars)
            time.sleep(0.2)
    
    # Create stop event
    stop_event = threading.Event()
    
    # Start animation thread
    animation_thread = threading.Thread(target=animate, args=(stop_event,))
    animation_thread.daemon = True
    animation_thread.start()
    
    # Simulate main work
    print("Starting work...")
    time.sleep(3)  # Simulate 3 seconds of work
    
    # Stop animation
    stop_event.set()
    animation_thread.join()
    
    # Clear animation line
    ConsoleAnimator.clear_line()
    print("✅ Work complete!")


def demo_advanced_loading() -> None:
    """
    Advanced loading animation with multiple styles.
    
    Demonstrates different animation styles and how to
    create more sophisticated loading indicators.
    """
    print("\n=== Advanced Loading Demo ===")
    
    # Different animation styles
    animations = {
        "dots": ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"],
        "spinner": ["|", "/", "-", "\\"],
        "bars": ["▌", "▀", "▐", "▄"],
        "circles": ["◐", "◓", "◑", "◒"]
    }
    
    for style_name, chars in animations.items():
        print(f"\n{style_name.title()} animation:")
        for i in range(10):
            char = chars[i % len(chars)]
            ConsoleAnimator.write_with_flush(f"\r{char} {style_name} loading...")
            time.sleep(0.2)
        ConsoleAnimator.write_with_flush(f"\r✅ {style_name.title()} complete!     \n")


def demo_error_handling() -> None:
    """
    Demonstrate proper error handling in console animations.
    
    Shows how to gracefully handle errors and clean up
    console state when animations are interrupted.
    """
    print("\n=== Error Handling Demo ===")
    
    try:
        print("Starting risky operation...")
        for i in range(5):
            ConsoleAnimator.write_with_flush(f"\rProcessing step {i+1}/5...")
            time.sleep(0.5)
            
            # Simulate potential error
            if i == 2:
                raise RuntimeError("Simulated error during processing")
        
        ConsoleAnimator.write_with_flush("\r✅ Operation completed successfully!\n")
        
    except Exception as e:
        # Clean up console state
        ConsoleAnimator.clear_line()
        print(f"❌ Error occurred: {e}")
        print("Console state cleaned up properly.")


def main() -> None:
    """
    Run all demonstration functions.
    
    Executes all demo functions in sequence to showcase
    the various console output and animation techniques.
    """
    print("Console Output and Animation Demo")
    print("=" * 50)
    print("Demonstrating sys.stdout.write() and sys.stdout.flush() techniques")
    print("=" * 50)
    
    # Run all demos
    demos = [
        demo_basic_write,
        demo_flush_importance,
        demo_carriage_return,
        demo_loading_animation,
        demo_progress_bar,
        demo_multi_line_output,
        demo_backspace,
        demo_threaded_animation,
        demo_advanced_loading,
        demo_error_handling
    ]
    
    for demo in demos:
        try:
            demo()
        except KeyboardInterrupt:
            print("\n\n⚠️  Demo interrupted by user.")
            break
        except Exception as e:
            print(f"\n❌ Error in {demo.__name__}: {e}")
            continue
    
    print("\n" + "=" * 50)
    print("All demos completed!")
    print("=" * 50)


if __name__ == "__main__":
    main() 